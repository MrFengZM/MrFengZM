import numpy as np

import auto1688
import threading
import pandas
import numpy
from enum import Enum
from datetime import datetime
import time
from filereader import DataFrameReader


class file_info(Enum):
    PATH = "C:\\Users\\admin\\Downloads\\SPU_2024_08_20_09_02_24.xlsx"
    SHEET = "Sheet1"
    COL = 1


class MyThread(threading.Thread):
    def __init__(self, port, version, name):
        super().__init__()
        self.port = port
        self.version = version
        self.name = name
        self.commodity_list = DataFrameReader(file_info.PATH.value, file_info.SHEET.value,
                                              file_info.COL.value).read_data()

    def run(self) -> None:
        while True:
            try:
                print('{} is running >> {}'.format(threading.current_thread().name,datetime.now().strftime("%Y-%m-%d "
                                                                                                           "%H:%M:%S")))
                auto1688.main(self.commodity_list, self.port, self.version, self.name)
            except Exception as a:
                print('{}-{}-{}'.format(self.name,self.version,self.port),"Error:运行设备异常", a)
                continue


if __name__ == "__main__":

    MyThread('4723', '9', '8SUKKBYDZTS8N7B6').start()
    MyThread('4724', '12', 'VAUBB24423011293').start()
