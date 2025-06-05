import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
data=pd.read_csv("Data/weather.csv")
rain_mean = data.groupby('province')['rain'].mean().sort_values(ascending=False)

plt.figure(figsize=(10,6))
sns.barplot(x=rain_mean.index, y=rain_mean.values)
plt.title('Trung bình lượng mưa theo tỉnh')
plt.xlabel('Tỉnh')
plt.ylabel('Lượng mưa trung bình')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
print(data['rain'].unique())
print(data['rain'].describe())
