# 目录操作
# os模块是python内置的与操作系统功能和文件系统相关的模块，该模块中的语句的执行结果通常与操作系统有关，在不同操作系统运行得到的结果也不一样
# os模块与os.path模块用于对目录或文件进行操作、
import os


def test_notepad():
    '''打开记事本'''
    os.system("notepad.exe")


def test_calc():
    '''# 打开计算器'''
    os.system("calc.exe")

def test_staertfile():
    '''打开系统文件'''
    os.startfile("C:\\Program Files (x86)\\baidu\\infoflow\\iLauncher.exe")

def test_getcwd():
    '''获取当前目录'''
    print(os.getcwd())

def test_listdir():
    '''获取指定目录下的文件和目录信息'''
    lst= os.listdir('../新建文件夹')
    print(lst)

def test_mkdir(path="d:\\HAH"):
    '''创建目录'''
    os.mkdir(path)

def test_makedirs():
    '''创建多级目录'''
    os.makedirs("HAH\\ee\\ww")

def test_rmdir():
    '''删除目录'''
    os.rmdir("D:\\HAH")

def test_removedirs():
    """删除多级目录"""
    os.removedirs("HAH\\ee\\ww")

def test_chdir():
    '''设置os工作目录'''
    test_mkdir()
    os.chdir("D:\\HAH")
    os.chdir("D:\MrFengZM\新建文件夹")
    print(os.getcwd())
    test_rmdir()

def test_chdir():
    PLATFORM_NAME = 'platform_name'

    desired_caps = {
        ('%s' % PLATFORM_NAME): 'Android',  # 被测手机是安卓
        'platform_version': '9',  # 手机安卓版本
        'device_name': 'android666',  # 设备名，安卓手机可以随意填写
        'app_package': 'com.alibaba.wireless',  # 启动APP Package名称
        'app_activity': 'launch.LauncherActivity',  # 启动Activity名称
        # 'unicodeKeyboard': True,  # 使用自带输入法，输入中文时填True
        'reset_keyboard': True,  # 执行完程序恢复原来输入法
        'no_reset': True,  # 不要重置App，如果为False的话，执行完脚本后，app的数据会清空，比如你原本登录了，执行完脚本后就退出登录了
        'new_command_timeout': 6000,
        'automation_name': 'UiAutomator2',
        "skip_server_installation": True
    }
    print(desired_caps)