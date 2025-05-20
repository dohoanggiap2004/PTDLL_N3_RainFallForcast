import pandas as pd

# Đọc dữ liệu từ file CSV
df = pd.read_csv('Data/data_encode.csv')

# Kiểm tra trung bình của cột 'cloud' (bỏ qua NaN)
mean_cloud = df['cloud'].mean()

# Điền giá trị thiếu bằng trung bình
df['cloud'].fillna(mean_cloud, inplace=True)

# Lưu lại file sau khi xử lý
df.to_csv('weather_filled_after.csv', index=False)

print("Hoàn thành điền giá trị thiếu cho cột 'cloud'.")
