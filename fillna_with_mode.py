from multiprocessing.reduction import duplicate
from statistics import LinearRegression

import numpy as np
import pandas as pd
data=pd.read_csv("Data/data_encode.csv")

def fillna_with_mode(col_name):
    mode_value=data[col_name].mode().iloc[0]
    data[col_name].fillna(mode_value,inplace=True)
fillna_with_mode("cloud")