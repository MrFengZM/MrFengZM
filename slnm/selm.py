from selenium import webdriver
import time
from selenium.webdriver.common import by
import math
from selenium.webdriver.common.keys import Keys
class Selenium_chrome:

    def __init__(self):
        self.c_driver = webdriver.Chrome()

    def open_chrome_url(self,url):
        '''打开url'''
        self.c_driver.get(url)

    def maximize_window(self):
        '''窗口最大化'''
        self.c_driver.maximize_window()

    def driver_refresh(self):
        '''浏览器刷新'''
        self.c_driver.refresh()

    def get_current_url(self):
        '''获取当前url'''
        url=self.c_driver.current_url
        print(url)
        return url

    def get_ccurrent_title(self):
        '''获取当前title'''
        title = self.c_driver.title
        print(title)
        return title

    def screenshot(self):
        '''网页ui截图'''
        self.c_driver.save_screenshot()

    def find_id(self,id):
        '''id定位'''
        element=self.c_driver.find_element(by.By.ID,id)
        return element

    def find_nime(self,name):
        '''name定位'''
        element=self.c_driver.find_element(by.By.NAME,name)
        return element

    def find_class_nime(self,class_name):
        '''class_name定位'''
        element=self.c_driver.find_element(by.By.CLASS_NAME,class_name)
        return element

    def find_(self,xpath):
        '''xpath定位'''
        element=self.c_driver.find_element(by.By.XPATH,xpath)
        return element


if __name__ == "__main__":
    s=Selenium_chrome()
    mobileNo="17620039144"
    note_code= 666666
    url = "https://m-qa-3.stg.fuyunhealth.com/#/login"
    s.open_chrome_url(url)
    s.maximize_window()
    time.sleep(1)
    for i in range(0,len(mobileNo)):
        #  键入手机号
        mobileNo = int(mobileNo)
        s.c_driver.find_element(by.By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div/div[2]/input').send_keys(Keys.HOME,mobileNo%10)
        mobileNo = math.floor(mobileNo/10)
    time.sleep(1)
    s.c_driver.find_element(by.By.XPATH,'//*[@id="root"]/div/div/div[3]/div[1]/img').click() # 勾选协议
    time.sleep(1)
    s.c_driver.find_element(by.By.XPATH,'//*[@id="root"]/div/div/div[4]/a/span').click() # 获取验证码
    time.sleep(1)
    s.c_driver.find_element(by.By.XPATH,'//*[@id="root"]/div/div/div[3]/div/div/div[1]/input').send_keys(note_code) # 键入验证码
    time.sleep(1)
    s.c_driver.find_element(by.By.CSS_SELECTOR,'#root > div > div > div.confirm_btn > a').click() # 登录
    time.sleep(50)

