from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver import ActionChains
import sys
import time
from thefuzz import fuzz
from selenium.webdriver.common.by import By
import pandas as pd
import threading
from datetime import datetime

# import TouchAction
# 初始化参数
# PLATFORM_NAME = 'platform_name'
#
# desired_caps = {
#     ('%s' % PLATFORM_NAME): 'Android',  # 被测手机是安卓
#     'platform_version': '9',  # 手机安卓版本
#     'device_name': 'android666',  # 设备名，安卓手机可以随意填写
#     'app_package': 'com.alibaba.wireless',  # 启动APP Package名称
#     'app_activity': 'launch.LauncherActivity',  # 启动Activity名称
#     # 'unicodeKeyboard': True,  # 使用自带输入法，输入中文时填True
#     'reset_keyboard': True,  # 执行完程序恢复原来输入法
#     'no_reset': True,  # 不要重置App，如果为False的话，执行完脚本后，app的数据会清空，比如你原本登录了，执行完脚本后就退出登录了
#     'new_command_timeout': 6000,
#     'automation_name': 'UiAutomator2',
#     "skip_server_installation":True
# }

class Auto_1688(threading.Thread):

    def __init__(self, platform_name, platform_version, device_name, app_package, app_activity, new_command_timeout,
                 automation_name='UiAutomator2', skip_server_installation=True, reset_keyboard=True, no_reset=True,
                 port="4723"):
        super().__init__()
        self.platformName = platform_name
        self.platformVersion = platform_version
        self.deviceName = device_name
        self.appPackage = app_package
        self.appActivity = app_activity
        self.resetKeyboard = reset_keyboard
        self.noReset = no_reset
        self.newCommandTimeout = new_command_timeout
        self.automationName = automation_name
        self.skipServerInstallation = skip_server_installation
        self.port=port
        self.desired_caps = {
            'platformName': self.platformName,  # 被测手机是安卓
            'platformVersion': self.platformVersion,  # 手机安卓版本
            'deviceName': self.deviceName,  # 设备名，安卓手机可以随意填写
            'appPackage': self.appPackage,  # 启动APP Package名称
            'appActivity': self.appActivity,  # 启动Activity名称
            # 'unicodeKeyboard':self.reset_keyboard,  # 使用自带输入法，输入中文时填True
            'resetKeyboard': self.resetKeyboard,  # 执行完程序恢复原来输入法
            'noReset': self.noReset,  # 不要重置App，如果为False的话，执行完脚本后，app的数据会清空，比如你原本登录了，执行完脚本后就退出登录了
            'newCommandTimeout': self.newCommandTimeout,
            'automationName': self.automationName,
            "skipServerInstallation": self.skipServerInstallation
        }

        self.driver = webdriver.Remote(f'http://localhost:{self.port}/wd/hub', self.desired_caps)
        time.sleep(3)

    @staticmethod
    def date_time():
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def like_commodity(self, commodity="yry"):
        """匹配商品名称"""
        element_list = []
        time.sleep(1)
        elements = self.driver.find_elements(by=By.CLASS_NAME, value="android.widget.TextView")
        # print('获取所有元素', elements)
        for element in elements:
            try:
                a = element.text
            except Exception as a:
                print(self.date_time(), "{}-{}-{}找不到元素文本".format(self.deviceName, self.platformVersion, self.port), a)
                continue
            if fuzz.partial_ratio(str(element.text), commodity) == 100:
                print(self.date_time(),"{}-{}-{}匹配成功！".format(self.deviceName,self.platformVersion,self.port), element.text)
                element_list.append(element)
        return element_list

    def search_clink(self):
        """点击搜索框搜索商品"""
        time.sleep(3)
        self.driver.tap(positions=[(400, 380)], duration=500)
        # time.sleep(3)
        # self.driver.find_element(by=By.ID,value="com.alibaba.wireless:id/content").click()
        print(self.date_time(),"{}-{}-{}点击搜索框成功".format(self.deviceName,self.platformVersion,self.port))
        # self.driver.implicitly_wait(10)

    def search_commodity(self, commodity="yry"):
        time.sleep(1)
        print(self.date_time(),'{}-{}-{}'.format(self.deviceName,self.platformVersion,self.port),commodity)
        self.driver.find_element(by=By.ID, value="com.alibaba.wireless:id/et_search_input_edit").send_keys(commodity)
        self.driver.implicitly_wait(10)
        time.sleep(3)
        self.driver.find_element(by=By.ID, value="com.alibaba.wireless:id/btn_search_input_search").click()

    def return_commodity(self):
        self.driver.find_element(by=By.ID, value="com.alibaba.wireless:id/v5_common_return").click()
        time.sleep(1)
        self.driver.implicitly_wait(10)
        self.driver.find_element(by=By.ID, value="com.alibaba.wireless:id/et_search_input_edit").clear()
        # self.driver.implicitly_wait(10)

    def __slide(self, node, start, end, slide=1):
        """滑动屏幕"""
        if slide == 1:
            """横向滑动"""
            self.driver.swipe(start_x=start, start_y=node, end_x=end, end_y=node, duration=300)
        else:
            """竖向滑动"""
            self.driver.swipe(start_x=node, start_y=start, end_x=node, end_y=end, duration=300)

    @staticmethod
    def x_view(type, phone_size=None) -> int:
        """滑动详情图"""
        if phone_size is None:
            phone_size = {'width': 1080, 'height': 2201}
        node = round(phone_size.get("height") * 0.602)
        start = round(phone_size.get("width") * 0.833)
        end = round(phone_size.get("width") * 0.185)
        if type == 0:
            return node
        elif type == 1:
            return start
        else:
            return end

    @staticmethod
    def y_view(xy, type=None, phone_size=None) -> int:
        """滑动详情图"""
        if phone_size is None:
            phone_size = {'width': 1080, 'height': 2201}
        if type is None:
            type = 1
        if type == 0:
            """返回滑动参数"""
            node = round(phone_size.get("width") * 0.037)
            start = round(phone_size.get("height") * 0.855)
            end = round(phone_size.get("height") * 0.186)
        elif type == 1:
            node = round(phone_size.get("width") * 0.21296)
            start = round(phone_size.get("height") * 0.86642)
            end = round(phone_size.get("height") * 0.50159)

        if xy == 0:
            return node
        elif xy == 1:
            return start
        else:
            return end

    def view_commodity_old(self, element, is_car=0):
        """浏览商品 适用于旧版本"""
        time.sleep(1)
        element.click()
        phone_size = self.driver.get_window_size()
        self.driver.implicitly_wait(10)
        """滑动横向坐标"""
        self.__slide(self.x_view(0), self.x_view(1), self.x_view(2))
        self.driver.implicitly_wait(10)
        for i in range(5):
            time.sleep(1)
            """连续滑动竖向坐标"""
            self.__slide(self.y_view(0), self.y_view(1), self.y_view(2), 2)
            self.driver.implicitly_wait(10)
        time.sleep(2)
        if is_car == 0:
            try:
                time.sleep(1)
                self.driver.find_element(by=By.ID, value="com.alibaba.wireless:id/v5_common_return").click()
            except Exception as a:
                print(self.date_time(),"{}-{}-{}执行返回商品列表失败".format(self.deviceName,self.platformVersion,self.port), a)
                self.driver.tap(positions=[(540, 300)], duration=500)
                time.sleep(2)
                self.driver.implicitly_wait(10)

                self.driver.find_element(by=By.ID, value="com.alibaba.wireless:id/v5_common_return").click()
                time.sleep(1)
        else:
            self.driver.find_element(by=By.ID, value="com.alibaba.wireless:id/action_title").click()
            self.driver.implicitly_wait(10)
            time.sleep(1)
            self.driver.find_element(by=By.ID, value="com.alibaba.wireless:id/purchase_sku_increase").click()
            self.driver.implicitly_wait(10)
            time.sleep(1)
            self.driver.find_element(by=By.ID, value="com.alibaba.wireless:id/sku_confirm").click()
            self.driver.implicitly_wait(10)
            time.sleep(1)
            self.driver.find_element(by=By.ID, value="com.alibaba.wireless:id/v5_common_return").click()  # 返回商品列表
            self.driver.implicitly_wait(10)
            print(self.date_time(),'{}-{}-{}执行加购成功!!!'.format(self.deviceName,self.platformVersion,self.port))
            time.sleep(1)

    def view_commodity(self, element_list, is_car=0):
        """浏览商品 适用于新版本"""
        for element in element_list:
            try:
                element.click()
            except Exception as e:
                print(self.date_time(),"{}-{}-{}找不到要点击的商品".format(self.deviceName,self.platformVersion,self.port),e)
                continue
            try:
                self.driver.find_element(by=By.ID, value="com.alibaba.wireless:id/play_icon").click()
            except Exception as e:
                print(self.date_time(),"{}-{}-{}找不到视频".format(self.deviceName,self.platformVersion,self.port),e)
            else:
                time.sleep(10)  # 播放视频10s

            els = self.driver.find_elements(by=By.CLASS_NAME, value="android.widget.TextView")
            for el in els:
                try:
                    print(el.text)
                except Exception as a:
                    print(self.date_time(),a, "找不到元素文本")
                    continue
                if fuzz.partial_ratio(str(el.text), "图片") == 100:
                    el.click()
                    break
            try:
                text = self.driver.find_element(by=By.ID, value="com.alibaba.wireless:id/tv_index").text.split("/")
            except Exception as a:
                print(self.date_time(),a, '获取图片数量失败')
                text = 4
            for i in range(int(len(text)) - 1):
                self.driver.swipe(start_x=960, start_y=515, end_x=100, end_y=515)
                self.driver.implicitly_wait(10)
                time.sleep(2)
            for i in range(10):
                self.driver.swipe(start_x=20, start_y=1660, end_x=20, end_y=640)
            self.driver.implicitly_wait(10)
            time.sleep(1)
            if is_car == 1:
                print(self.date_time(),"开始执行加购行为")
                self.driver.find_element(by=By.ID, value="com.alibaba.wireless:id/action_title").click()  # 点击加购
                self.driver.implicitly_wait(10)
                self.driver.find_element(by=By.ID,
                                         value="com.alibaba.wireless:id/purchase_sku_increase").click()  # 选择加号
                self.driver.implicitly_wait(10)
                self.driver.find_element(by=By.ID, value="com.alibaba.wireless:id/sku_confirm").click()  # 确认
                self.driver.implicitly_wait(10)
                print(self.date_time(),"加购完成")
                self.driver.find_element(by=By.ID, value="com.alibaba.wireless:id/od_title_bar_back_btn").click()


            else:
                print(self.date_time(),"跳过加购,返回搜索页")
                self.driver.find_element(by=By.ID, value="com.alibaba.wireless:id/od_title_bar_back_btn").click()

    def down_glide(self):
        self.__slide(self.y_view(0), self.y_view(1), self.y_view(2), 2)


def main(commodity, port="4723", version="9", name='android666'):
    dv = Auto_1688('Android', f'{version}', f'{name}', 'com.alibaba.wireless', 'launch.LauncherActivity', 6000,
                   port=port)
    print('{} is running success >> {}'.format(threading.current_thread().name,datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    """点击搜索框"""
    for i in range(3):
        try:
            dv.search_clink()
            time.sleep(1)
        except Exception as e:
            print(Auto_1688.date_time(),'{}-{}-{}'.format(name,version,port),"点击搜索框失败",e)
            continue
        else:
            break

    print(Auto_1688.date_time(),'{}-{}-{}'.format(name,version,port),"遍历商品")
    for cdy in commodity:
        """搜索商品"""
        # time.sleep(1)
        dv.search_commodity(cdy)

        """匹配商品名称"""
        time.sleep(2)
        try:
            for i in range(10):
                elements = dv.like_commodity("中山市宜润元电子商务商行")
                if not elements:
                    print(Auto_1688.date_time(),'{}-{}-{}'.format(name,version,port),"此页面没有匹配到商品，继续滑动")
                    time.sleep(0.5)
                    dv.down_glide()
                    time.sleep(0.5)
                    dv.down_glide()
                else:
                    print(Auto_1688.date_time(),'{}-{}-{}'.format(name,version,port),f"成功匹配到{len(elements)}个商品,执行浏览加购业务")
                    for element in elements:
                        time.sleep(2)
                        dv.view_commodity_old(element, 1)
                    break
        except Exception as a:
            print(Auto_1688.date_time(),'{}-{}-{}'.format(name,version,port),a, cdy, "{匹配商品异常}")
        try:
            time.sleep(2)
            dv.return_commodity()
            time.sleep(1)
        except Exception as a:
            print(Auto_1688.date_time(),'{}-{}-{}'.format(name,version,port),"执行清除失败，开始重启app")
            dv = Auto_1688('Android', '9', 'android666', 'com.alibaba.wireless', 'launch.LauncherActivity', 6000,
                           port=port)
            """点击搜索框"""
            for i in range(3):
                try:
                    dv.search_clink()
                    time.sleep(1)
                except Exception as e:
                    print(Auto_1688.date_time(),'{}-{}-{}'.format(name,version,port),e, "点击搜索框失败")
                    continue
                else:
                    break
