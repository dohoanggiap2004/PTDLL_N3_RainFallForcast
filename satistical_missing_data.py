from multiprocessing.reduction import duplicate
from statistics import LinearRegression

import numpy as np
import pandas as pd
data=pd.read_csv("Data/data_encode.csv")
#print(data.head(10))
def statistical_missing_data():
    missing_data=data.isnull().sum()
    duplicate_data=data.duplicated().sum()
    print("so lieu thieu trong moi cot:")
    print(missing_data)
    print("\nSo lieu trung lap")
    print(duplicate_data)
statistical_missing_data()