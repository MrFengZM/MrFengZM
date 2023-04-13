from selenium import webdriver
import time
from selenium.webdriver.common import by
import math
import datetime
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains



class SiHai():

    def __init__(self,phone=None,password=None):
        self.__driver=webdriver.Chrome()
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

    def sihai_login(self):
        self.driver.get("https://sihai.baidu.com/login?returnUrl=https%3A%2F%2Fsihai.baidu.com%2Fmobile")
        time.sleep(2)
        print(111)
        self.driver.find_element(by.By.XPATH, '//*[@id="TANGRAM__PSP_11__userName"]').send_keys(self.phone)
        time.sleep(2)
        self.driver.find_element(by.By.XPATH,'//*[@id="TANGRAM__PSP_11__password"]').send_keys(self.password)
        time.sleep(2)
        self.driver.find_element(by.By.XPATH,'// *[ @ id = "TANGRAM__PSP_11__submit"]').click()


    def sihai_sign(self):
        self.sihai_login()
        time.sleep(5)
        self.driver.get("https://sihai.baidu.com/sign-in")
        time.sleep(3)
        self.driver.find_element(by.By.XPATH,'//*[@id="app"]/section/section/div[1]/section[1]')
        # self.driver.find_element(by.By.XPATH, '// *[ @ id = "app"] / section / section / div[3] / div / img').click()

    def run(self):
        while True:
            try:
                self.sihai_sign()
            except Exception as error_log:
                print(error_log)
                time.sleep(3)
            else:
                print("成功")
                break


if __name__ == "__main__":
    sh = SiHai("17620039144","fengzhiming631")
    while True:
        time.sleep(60)
        print(SiHai.now_time())
        if sh.now_time()>400 and sh.now_time()<430:
            sh.run()
            time.sleep(2000)
        elif sh.now_time()>730 and sh.now_time()<800:
            sh.run()
            time.sleep(2000)


