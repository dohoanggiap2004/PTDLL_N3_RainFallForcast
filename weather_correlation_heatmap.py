import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Đọc dữ liệu từ tệp CSV (trong thực tế, sẽ đọc trực tiếp từ tệp)
# Để minh họa, giả sử dữ liệu đã được tải vào DataFrame
# df = pd.read_csv('weather.csv')

# Tải dữ liệu mẫu (vì không thể tải trực tiếp CSV ở đây, đây là minh họa)
data = pd.read_csv('Data/data_encode.csv')

# Chuyển các cột số thành dạng số, ép các lỗi thành NaN
numeric_columns = ['max', 'min', 'wind', 'rain', 'humidi', 'cloud', 'pressure']
for column in numeric_columns:
    data[column] = pd.to_numeric(data[column], errors='coerce')

# Tính ma trận tương quan
correlation_matrix = data[numeric_columns].corr()

# Vẽ heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1, center=0, square=True, fmt='.2f')

# Tùy chỉnh biểu đồ
plt.title('Ma trận tương quan giữa các biến số thời tiết', fontsize=14)
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)
plt.show()