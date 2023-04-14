from selenium import webdriver
import time
from selenium.webdriver.common import by
import math
import datetime
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class SiHai(object):

    def __init__(self,phone=None,password=None):
        self.__driver = webdriver.Chrome()
        self.phone = phone
        self.password = password

    @property
    def driver(self):
        return self.__driver

    @driver.setter
    def driver(self,driver):
        self.__driver = driver

    @staticmethod
    def now_time():
        return int(datetime.datetime.now().strftime("%H%M"))

    def sihai_sign(self):
        time.sleep(3)
        self.driver.get("https://sihai.baidu.com/sign-in")
        # self.driver.refresh()
        # time.sleep(1)
        self.driver.find_element(by.By.XPATH,'//*[@id="app"]/section/section/div[1]/section[1]').click()
        # self.driver.find_element(by.By.XPATH, '// *[ @ id = "app"] / section / section / div[3] / div / img').click()

class Run:

    @staticmethod
    def run(phone=None,password=None):
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
                break




if __name__ == "__main__":
    phone = "15836285767"
    # phone = "17620039144"
    password="021120hyd"
    # password = "fengzhiming631"

    while True:
        print(SiHai.now_time())
        if SiHai.now_time() > 400 and SiHai.now_time() < 430:
            Run.run(phone= phone,password=password)
            time.sleep(2000)
        elif SiHai.now_time()>1930 and SiHai.now_time()<2000:
            Run.run()
            time.sleep(2000)
        time.sleep(30)


