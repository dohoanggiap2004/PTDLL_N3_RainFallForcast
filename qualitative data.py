import pandas as pd
import matplotlib.pyplot as plt

# Đọc file CSV
df = pd.read_csv('Data/weather.csv')

# Đếm số lượng các giá trị trong các cột
province_counts = df['province'].value_counts()
wind_d_counts = df['wind_d'].value_counts()

# Tính tổng số bản ghi
total_records = len(df)

# Tính tỉ lệ phần trăm cho từng cột
province_percentages = (province_counts / total_records * 100).round(2)
wind_d_percentages = (wind_d_counts / total_records * 100).round(2)

# Danh sách mã màu đa dạng (hex codes) để tránh trùng lặp
color_palette = [
    '#FF6F61', '#6B5B95', '#88B04B', '#F7CAC9', '#92A8D1', '#955251', '#B565A7',
    '#009B77', '#DD4124', '#D65076', '#45B8AC', '#EFC050', '#5B5EA6', '#9B2335',
    '#DFCFBE', '#55B4B0', '#E15D44', '#7FCDCD', '#BC243C', '#C3447A', '#98B4D4',
    '#FF9800', '#78909C', '#4CAF50', '#F06292', '#FFD54F', '#4DB6AC', '#A1887F'
]

# Đảm bảo số lượng màu đủ cho province và wind_d
num_provinces = len(province_percentages)
num_wind_d = len(wind_d_percentages)

# Lấy danh sách màu cho province
province_colors = color_palette[:num_provinces]
print("Colors for Province chart:")
for label, color in zip(province_percentages.index, province_colors):
    print(f"{label}: {color}")

# Tạo biểu đồ hình tròn cho province
plt.figure(figsize=(10, 8))  # Tăng kích thước biểu đồ để có thêm không gian
plt.pie(province_percentages, autopct='%1.1f%%', startangle=90, colors=province_colors)
plt.title('Distribution of Province (province)')
# Thêm % vào legend và điều chỉnh để hiển thị hết
legend_labels = [f"{label} - {percent:.2f}%" for label, percent in zip(province_percentages.index, province_percentages)]
plt.legend(
    legend_labels,
    title="Province",
    loc="center left",
    bbox_to_anchor=(0.8, 0, 0.5, 1),  # Đặt legend bên ngoài biểu đồ
    fontsize=8,  # Giảm kích thước chữ để hiển thị nhiều mục hơn
    ncol=2  # Chia legend thành 2 cột để tiết kiệm không gian
)
plt.axis('equal')
plt.show()

# Lấy danh sách màu cho wind_d
wind_d_colors = color_palette[:num_wind_d]
print("\nColors for Wind Direction chart:")
for label, color in zip(wind_d_percentages.index, wind_d_colors):
    print(f"{label}: {color}")

# Tạo biểu đồ hình tròn cho wind_d
plt.figure(figsize=(10, 8))  # Tăng kích thước biểu đồ
plt.pie(wind_d_percentages, autopct='%1.1f%%', startangle=90, colors=wind_d_colors)
plt.title('Distribution of Wind Direction (wind_d)')
# Thêm % vào legend và điều chỉnh để hiển thị hết
legend_labels = [f"{label} - {percent:.2f}%" for label, percent in zip(wind_d_percentages.index, wind_d_percentages)]
plt.legend(
    legend_labels,
    title="Wind Direction",
    loc="center left",
    bbox_to_anchor=(0.9, 0, 0.5, 1),  # Đặt legend bên ngoài biểu đồ
    fontsize=8,  # Giảm kích thước chữ
    ncol=2  # Chia legend thành 2 cột
)
plt.axis('equal')
plt.show()