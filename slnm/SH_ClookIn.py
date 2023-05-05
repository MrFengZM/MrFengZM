import requests
import json
from pykeyboard import PyKeyboard
from pymouse import PyMouse
import os,time,_thread

import pandas.io.clipboard as cb

class myos(PyMouse,PyKeyboard):

    def __init__(self):
        super().__init__()

    def ccontrol(self):
        self.press_key(self.control_key)
        time.sleep(2)
        self.release_key(self.control_key)

    def paste(self):
        _thread.start_new_thread(self.ccontrol,())
        time.sleep(1)
        self.tap_key("v")
        time.sleep(2)

    def select_all(self):
        _thread.start_new_thread(self.ccontrol,())
        time.sleep(1)
        self.tap_key("a")
        time.sleep(2)

    def copy(self):
        _thread.start_new_thread(self.ccontrol,())
        time.sleep(1)
        self.tap_key("c")
        time.sleep(2)




