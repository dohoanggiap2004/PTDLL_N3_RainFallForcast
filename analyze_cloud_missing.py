import pandas as pd

data = pd.read_csv('Data/weather.csv')
# Tính giá trị trung bình của cột 'cloud'
cloud_mean = data['cloud'].mean()
# Đếm số lượng giá trị khuyết trong cột 'cloud'
missing_count = data['cloud'].isna().sum()
# In kết quả
print(f"Giá trị trung bình của cột 'cloud': {cloud_mean:.2f}")
print(f"Số lượng giá trị khuyết trong cột 'cloud': {missing_count}")