import pandas as pd

df = pd.read_csv('Data/weather_filled.csv')
df_numeric = df.select_dtypes(include=['number'])
print(df_numeric.describe().to_string())