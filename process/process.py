import multiprocessing
import os
import time


def dingding(nuber):
    os.startfile("D:\\DingDing\\DingtalkLauncher.exe")
    for i in range(1,nuber):
        print(i)
        time.sleep(1)
def weixin():
    os.startfile("D:\\weixin\\WeChat\\WeChat.exe")
    for i in range(1,4):
        print(i)
        time.sleep(1)
if __name__ =="__main__":
    wenxin_process=multiprocessing.Process(target=weixin)
    dingding_process=multiprocessing.Process(target=dingding,kwargs={"nuber":5})
    time.sleep(2)
    wenxin_process.start()
    dingding_process.start()
