from appium import webdriver
import pandas
import time
from appium.webdriver.common.touch_action import TouchAction
# from selenium.webdriver.common.by import By
# from selenium.webdriver import ActionChains
# import sys
#初始化参数
PLATFORM_NAME = 'platform_name'
desired_caps = {
    ('%s' % PLATFORM_NAME): 'Android',  # 被测手机是安卓
    'platform_version': '14',  # 手机安卓版本
    'device_name': 'android666',  # 设备名，安卓手机可以随意填写
    'app_package': 'com.alibaba.wireless',  # 启动APP Package名称
    'app_activity': 'launch.LauncherActivity',  # 启动Activity名称
    'unicodeKeyboard': True,  # 使用自带输入法，输入中文时填True
    'reset_keyboard': True,  # 执行完程序恢复原来输入法
    'no_reset': True,  # 不要重置App，如果为False的话，执行完脚本后，app的数据会清空，比如你原本登录了，执行完脚本后就退出登录了
    'new_command_timeout': 6000,
    'automation_name': 'UiAutomator2'
}
# 连接Appium Server，初始化自动化环境
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
def pan_duan_dian_ming(shop_name):     #判断页面是否存在店名，是则返回1 否则返回2
    text_vlaue = driver.find_elements_by_class_name("android.widget.TextView")
    for i in text_vlaue:
        if i.text == f"{shop_name}":
            return 1
    return 2
def shua(select_name,shop_name):
    TouchAction(driver).tap(x=278, y=377).perform()  #点击输入框
    time.sleep(1)
    el3 = driver.find_element_by_id("com.alibaba.wireless:id/et_search_input_edit")
    el3.send_keys(f"{select_name}") #输入标签名
    TouchAction(driver).tap(x=975, y=152).perform()  #点击搜索
    type = pan_duan_dian_ming(shop_name)
    oo = 0
    while type == 2:
        oo = oo + 1
        time.sleep(1)
        print(f"第{oo}次滑动")
        driver.swipe(1, 2300, 1, 1200, 1000)  #滑动
        type=pan_duan_dian_ming(shop_name)  #再次判断是否存在店名
        text_vlaue = driver.find_elements_by_class_name("android.widget.TextView")
        for i in text_vlaue:
            if i.text == "没有更多数据了" and type == 2:
                print(f"未搜到:{select_name}，next one")
                driver.press_keycode(4)
                time.sleep(1)
                driver.press_keycode(4)
                return
        if oo == 10:
            print (f"到底了~ 未搜到:{select_name}，next one")
            driver.press_keycode(4)
            time.sleep(1)
            driver.press_keycode(4)
            return
    driver.find_element_by_xpath(f"// *[ @ class ='android.widget.TextView'][ @ text ='{shop_name}']").click()
    time.sleep(1)
    driver.swipe(300, 1600, 300, 800, 1000)
    time.sleep(1)
    driver.swipe(300, 1600, 300, 800, 1000)
    el1 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView")
    el1.click() #点夹菜购物车
    time.sleep(1)
    print("加购成功！")
    el2 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.ScrollView/android.widget.LinearLayout/android.widget.ListView/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.ImageButton[2]")
    el2.click()
    el2.click()
    el2.click()
    el4 = driver.find_element_by_id("com.alibaba.wireless:id/sku_confirm")
    el4.click()
    driver.press_keycode(4)
    driver.press_keycode(4)
    driver.press_keycode(4)

op = 0
df = pandas.read_excel('E:\\1688excel\\1688.xlsx') # 读取Excel表格
shop_name = "上海慕江熙贸易商行(个人独资)"
for po in range(len(df.index.values)-1):
    select_name = df.iloc[op, 0]
    op = op + 1
    print(f"当前搜索第{po + 1}个商品,名称为（{select_name}）")

    shua(select_name,shop_name)
