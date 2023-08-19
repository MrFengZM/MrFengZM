from selenium import webdriver
import time
from selenium.webdriver.common import by
import math
import datetime
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import _thread
from pymouse import PyMouse
from pykeyboard import PyKeyboard
from pymouse import PyMouse
import os,time
import pandas.io.clipboard as cb
import _thread

import time

import numpy as np
from PIL import ImageGrab

class myos(PyMouse, PyKeyboard):

    def __init__(self,):
        super().__init__()

    def ccontrol(self):
        self.press_key(self.control_key)
        time.sleep(2)
        self.release_key(self.control_key)

    def paste(self):
        _thread.start_new_thread(self.ccontrol, ())
        time.sleep(1)
        self.tap_key("v")
        time.sleep(2)

    def select_all(self):
        _thread.start_new_thread(self.ccontrol, ())
        time.sleep(1)
        self.tap_key("a")
        time.sleep(2)

    def copy(self):
        _thread.start_new_thread(self.ccontrol, ())
        time.sleep(1)
        self.tap_key("c")
        time.sleep(2)
    @staticmethod
    def now_time():
       now_time=datetime.datetime.now().strftime("%H%M")
       return  int(now_time)

if __name__ == "__main__":
    myos = myos()
    while True:
        print(myos.now_time())
        if (myos.now_time() > 400 and myos.now_time()< 430)\
                or (myos.now_time()> 1930 and myos.now_time() < 2200):
            time.sleep(3)
            os.startfile("C:\\Users\\冯智明\\Desktop\\考勤打卡.lnk")
            myos.move(975,20)
            time.sleep(2)
            myos.click(975,20)
            time.sleep(5)
            myos.move(800,550)
            time.sleep(3)
            myos.move(800,540)
            # myos.click(800,550)
            time.sleep(3)
            # myos.click(800,550)

            # _thread.start_new_thread(Run.run,("17620039144","812812fzm"))
            # _thread.start_new_thread(Run.run, ("15836285767", "021120hyd"))
            time.sleep(3600*7)
        time.sleep(30)

