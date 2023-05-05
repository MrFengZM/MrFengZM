import requests
import json
from pykeyboard import PyKeyboard
from pymouse import PyMouse
import os,time

import pandas.io.clipboard as cb
import _thread

# 初始化鼠标对象
m = PyMouse()

# 初始化键盘对象
k = PyKeyboard()

# 移动鼠标到(x, y)绝对地址
# m.move(160, 970)
m.click(160, 970) # 点击底部如流
time.sleep(1)


m.click(160, 20)
time.sleep(1)
k.tap_key(k.backspace_key)
time.sleep(1)
cb.copy("冯明儿阿")
print(cb.paste())
myos.paste()
time.sleep(1)
m.click(160, 180)
os.startfile("../slnm/jietu")
myos.select_all()
time.sleep(1)
myos.copy()
m.click(160, 970)
time.sleep(1)
m.click(360, 870)
time.sleep(1)
myos.paste()
m.click(1460, 920)
