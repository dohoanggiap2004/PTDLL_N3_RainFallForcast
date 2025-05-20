import pandas as pd
import numpy as np

# Đọc dữ liệu từ tệp CSV
data = pd.read_csv('Data/weather.csv')

# Tạo một danh sách các chỉ số ngẫu nhiên để làm khuyết dữ liệu
np.random.seed(42)  # Đặt seed để kết quả có thể tái lập
missing_indices = np.random.choice(data.index, size=10000, replace=False)

# Đặt giá trị cột 'cloud' tại các chỉ số được chọn thành NaN
data.loc[missing_indices, 'cloud'] = np.nan

# Lưu dữ liệu đã chỉnh sửa vào một tệp CSV mới
data.to_csv('weather_missing_cloud.csv', index=False)