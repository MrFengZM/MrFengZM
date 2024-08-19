import numpy as np

import auto1688

import pandas
import numpy
from enum import Enum

from filereader import DataFrameReader


class file_info(Enum):
    PATH = "C:\\Users\\admin\\Downloads\\SPU_2024_08_19_01_38_39.xlsx"
    SHEET = "Sheet1"
    COL = 1


if __name__ == "__main__":

    commodity_list = DataFrameReader(file_info.PATH.value, file_info.SHEET.value, file_info.COL.value).read_data()
    while True:
        try:
            auto1688.main(commodity_list)
        except Exception as a:
            continue