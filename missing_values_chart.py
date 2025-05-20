import pandas as pd
import matplotlib.pyplot as plt

# Đọc file CSV (giả sử tên là 'vietnam_weather.csv')
df = pd.read_csv('Data/weather.csv')

missing_counts = df.isnull().sum()

# Lọc ra các cột thực sự có missing values
missing_counts = missing_counts[missing_counts > 0]

if not missing_counts.empty:
    missing_counts.sort_values().plot(kind='barh', color='skyblue')
    plt.xlabel('Số lượng giá trị thiếu')
    plt.title('Biểu đồ các giá trị thiếu theo cột')
    plt.tight_layout()
    plt.show()
else:
    print("Không có giá trị thiếu trong DataFrame.")
