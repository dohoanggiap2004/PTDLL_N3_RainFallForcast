import pandas as pd

df = pd.read_csv('Data/weather.csv')

# Đếm số lượng từng nhãn trong cột 'wind_d'
label_counts = df['wind_d'].value_counts()

print('Số các giá trị duy nhất của cột wind_d')
print(label_counts)
