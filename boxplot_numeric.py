import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('Data/weather_filled.csv')

# Vẽ boxplot
plt.figure(figsize=(10, 6))
sns.boxplot(data=df)
plt.xticks(rotation=45)
plt.title('Boxplot của các cột định lượng')
plt.ylabel('Giá trị')
plt.tight_layout()

# Mở canvas để hiển thị biểu đồ
plt.show()