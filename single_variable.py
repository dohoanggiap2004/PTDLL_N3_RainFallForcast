import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Đọc file CSV
df = pd.read_csv('Data/data_encode.csv')

# Chuyển đổi cột 'date' thành kiểu datetime để trích xuất thông tin nếu cần
# df['date'] = pd.to_datetime(df['date'])

# Lấy danh sách các cột số (numeric) để so sánh với 'rain'
numeric_columns = df.select_dtypes(include=['int64', 'float64']).columns
numeric_columns = [col for col in numeric_columns if col != 'rain']  # Loại bỏ 'rain' khỏi danh sách

# Tạo figure với nhiều subplot
n_cols = len(numeric_columns)
fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(15, 10))  # 2 hàng, 3 cột
axes = axes.flatten()  # Làm phẳng mảng axes để dễ lặp

# Vẽ biểu đồ scatter cho từng cột số so với 'rain'
for idx, col in enumerate(numeric_columns):
    sns.scatterplot(data=df, x=col, y='rain', ax=axes[idx])
    axes[idx].set_title(f'Relationship between {col} and Rainfall (rain)')
    axes[idx].set_xlabel(col)
    axes[idx].set_ylabel('Rainfall (mm)')

# Loại bỏ các subplot thừa (nếu có)
for idx in range(len(numeric_columns), len(axes)):
    fig.delaxes(axes[idx])

# Điều chỉnh layout
plt.tight_layout()
plt.show()
