import pandas as pd

# Đọc dữ liệu thời tiết
dataFrame = pd.read_csv('Data/weather.csv')

#  đếm các giá trị duy nhất trong một cột
def categories_counts(label_name):
    print('----------------------------------------------------')
    print(f'Số các giá trị duy nhất của cột "{label_name}":')
    print(dataFrame[label_name].value_counts())

categories_counts('province')
categories_counts('wind_d')
categories_counts('date')
