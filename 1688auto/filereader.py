
import numpy as np
import pandas as pd

class FileReader:

    def read_data(self):
        pass


class DataFrameReader(FileReader):
    def __init__(self, path, sheet, cols):
        self.path = path
        self.sheet = sheet
        self.cols = cols

    def read_data(self):
        df = pd.read_excel(self.path, sheet_name=self.sheet)
        array = np.array(df)
        data_list = array[:, self.cols].tolist()

        return data_list


