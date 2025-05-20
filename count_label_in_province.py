import pandas as pd

df = pd.read_csv('Data/weather.csv')

# Đếm số lượng từng nhãn trong cột 'wind_d'
label_counts = df['province'].value_counts()

print('Số các giá trị duy nhất của cột province')
print(label_counts)
