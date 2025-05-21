import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Đọc file CSV
df = pd.read_csv('Data/weather.csv')

# Gom nhóm cột 'cloud' thành các khoảng (bins)
# Ví dụ: 0-30% là Low, 30-70% là Medium, 70-100% là High
bins = [0, 30, 70, 100]  # Các khoảng mây che phủ
labels = ['Low', 'Medium', 'High']  # Nhãn cho các khoảng
df['cloud_category'] = pd.cut(df['cloud'], bins=bins, labels=labels, include_lowest=True)

# Tính giá trị trung bình lượng mưa theo nhóm mây che phủ và sắp xếp giảm dần
rain_by_cloud = df.groupby('cloud_category')['rain'].mean().sort_values(ascending=False)

# In kết quả trung bình để kiểm tra
print("Trung bình lượng mưa theo mức độ mây che phủ (sắp xếp giảm dần):")
print(rain_by_cloud)

# Vẽ biểu đồ boxplot
plt.figure(figsize=(8, 6))
sns.boxplot(x='cloud_category', y='rain', data=df, order=rain_by_cloud.index)
plt.title('Boxplot of Rainfall by Cloud Cover')
plt.xlabel('Cloud Cover')
plt.ylabel('Rainfall (mm)')
plt.show()