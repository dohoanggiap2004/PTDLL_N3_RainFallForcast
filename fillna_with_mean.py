import pandas as pd

data = pd.read_csv("Data/data_encode.csv")

def fillna_with_mean(col_name):
    mean_value = data[col_name].mean()
    data[col_name] = data[col_name].fillna(mean_value)

fillna_with_mean("cloud")
