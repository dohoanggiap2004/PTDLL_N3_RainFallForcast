import pandas as pd

df = pd.read_csv('Data/weather.csv')
# Xác định và ánh xạ tất cả các cột phân loại (kiểu object) thành số
for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].astype('category').cat.codes

# Ghi kết quả ra file mới
df.to_csv('Data/data_encode.csv', index=False)
print(df.head(10).to_string())

