import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Đọc dữ liệu từ tệp CSV (trong thực tế, sẽ đọc trực tiếp từ tệp)
# Để minh họa, giả sử dữ liệu đã được tải vào DataFrame
# df = pd.read_csv('weather.csv')

# Tải dữ liệu mẫu (vì không thể tải trực tiếp CSV ở đây, đây là minh họa)
data = pd.read_csv('Data/weather.csv')

# Chuyển cột 'rain' thành dạng số, ép các lỗi thành NaN
data['rain'] = pd.to_numeric(data['rain'], errors='coerce')

# Trích xuất năm từ cột 'date'
data['Year'] = pd.to_datetime(data['date']).dt.year

# Nhóm dữ liệu theo 'Year' và tính trung bình của cột 'rain'
rainfall_by_year = data.groupby('Year')['rain'].mean().reset_index()

# Tạo biểu đồ cột bằng seaborn
plt.figure(figsize=(10, 6))
sns.barplot(x='Year', y='rain', data=rainfall_by_year, palette='YlGn')

# Tùy chỉnh biểu đồ
plt.title('Sự thay đổi lượng mưa trung bình theo từng năm', fontsize=14)
plt.xlabel('Năm', fontsize=12)
plt.ylabel('Lượng mưa trung bình (mm)', fontsize=12)
plt.xticks(rotation=45)
plt.grid(True, axis='y', linestyle='--', alpha=0.7)
plt.show()