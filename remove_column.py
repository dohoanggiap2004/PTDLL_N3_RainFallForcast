import pandas as pd
df = pd.read_csv('Data/weather.csv')

def remove_weather_columns(df):
    columns_to_drop = ['province', 'wind_d', 'date']
    df.drop(columns=columns_to_drop, inplace=True)
    print(f'Đã xoá các cột không cần thiết: {columns_to_drop}')
    return df
df = remove_weather_columns(df)
df.to_csv('Data/data_remove.csv', index=False)
print(df.head(10).to_string())
