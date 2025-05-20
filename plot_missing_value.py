import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('Data/weather.csv')
# Tính số lượng giá trị khuyết cho từng cột
missing_data = data.isnull().sum()
# Vẽ đồ thị cột
plt.figure(figsize=(10, 5))
missing_data.plot(kind='bar')
plt.title('Số lượng giá trị khuyết trong tập dữ liệu')
plt.xlabel('Tên cột')
plt.ylabel('Số lượng giá trị khuyết')
plt.show()