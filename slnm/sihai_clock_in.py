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


class SiHai(object):

    def __init__(self,phone=None,password=None):
        self.__driver = webdriver.Chrome()
        self.phone = phone
        self.password = password
        self.moise = PyMouse()
        self.mk = myos()

    @property
    def driver(self):
        return self.__driver

    @driver.setter
    def driver(self,driver):
        self.__driver = driver

    @staticmethod
    def now_time():
        return int(datetime.datetime.now().strftime("%H%M"))

    @staticmethod
    def now_date():
        return int(datetime.datetime.now().strftime("%Y%m%d%H%M"))

    def sihai_sign(self):
        global jt_name
        time.sleep(3)
        self.driver.get("https://sihai.baidu.com/sign-in")
        # self.driver.refresh()
        # time.sleep(1)
        self.driver.find_element(by.By.XPATH,'//*[@id="app"]/section/section/div[1]/section[1]').click()
        time.sleep(1)
        # self.driver.find_element(by.By.XPATH, '// *[ @ id = "app"] / section / section / div[3] / div / img').click()
        print("打卡成功")
        time.sleep(1)

        jt_name = self.now_date()
        self.driver.save_screenshot(f".\\jietu\\{jt_name}.png")
        time.sleep(3)

    def send_png(self,keystr):
        cb.copy(keystr)  # 复制关键字
        time.sleep(1)
        self.mk.click(160, 970)  # 点击底部如流
        time.sleep(1)
        self.mk.click(160, 20)  # 点击搜索框
        time.sleep(1)
        self.mk.tap_key(self.mk.backspace_key)  # 清空搜索框
        time.sleep(1)
        print(cb.paste())
        time.sleep(1)
        self.mk.paste()  # 粘贴关键字
        time.sleep(1)
        self.mk.click(160, 180)  # 点击进入聊天框
        time.sleep(1)
        os.startfile(".\\jietu")  # 打开截图目录
        time.sleep(1)
        self.mk.select_all()  # 全选
        self.mk.copy()  # 复制图片
        self.mk.click(160, 970)
        time.sleep(2)
        self.mk.click(360, 870)
        self.mk.paste()  # 粘贴png
        self.mk.click(1460, 920)  # 点击发送
        time.sleep(3)
        os.remove(f"D:\\MrFengZM\\slnm\\jietu\\{jt_name}.png")  # 删除截图





class Run:

    @staticmethod
    def run(phone,password):
        sh = SiHai(phone,password)
        while True:
            try:
                sh.driver.get("https://sihai.baidu.com")
                time.sleep(1)
                sh.driver.find_element(by.By.XPATH, '//*[@id="TANGRAM__PSP_11__userName"]').click()
                sh.driver.find_element(by.By.XPATH, '//*[@id="TANGRAM__PSP_11__userName"]').send_keys(sh.phone)
                time.sleep(1)
                sh.driver.find_element(by.By.XPATH, '//*[@id="TANGRAM__PSP_11__password"]').click()

                sh.driver.find_element(by.By.XPATH,'//*[@id="TANGRAM__PSP_11__password"]').send_keys(sh.password)
                time.sleep(1)
                sh.driver.find_element(by.By.XPATH,'// *[ @ id = "TANGRAM__PSP_11__submit"]').click()
                time.sleep(3)

                sh.sihai_sign()
            except Exception as error_log:
                print(error_log)
                time.sleep(3)
            else:
                sh.send_png("外包同学群（摩都夜测）")
                # sh.send_png("冯明儿阿")
                break


if __name__ == "__main__":
    while True:
        print(SiHai.now_time())
        if (SiHai.now_time() > 100 and SiHai.now_time() < 430)\
                or (SiHai.now_time() > 1930 and SiHai.now_time() < 2000):
            _thread.start_new_thread(Run.run,("17620039144","812812fzm"))
            # _thread.start_new_thread(Run.run, ("15836285767", "021120hyd"))
            time.sleep(3600*7)
        time.sleep(300)