import sys
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import time
try:
    df = pd.read_csv('Data/data_encode.csv')
except FileNotFoundError:
    print("File 'Data/data_encode.csv' không tìm thấy. Vui lòng kiểm tra đường dẫn!")
    sys.exit(1)
X = df[['province', 'max', 'min', 'wind', 'wind_d', 'humidi', 'cloud', 'pressure', 'date']]
y = df['rain']
X = X.fillna(X.mean())
y = y.fillna(y.mean())
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
n_estimators_value = 10
model = RandomForestRegressor(n_estimators=n_estimators_value, random_state=42, n_jobs=1)  # n_jobs=1 để giảm tải CPU

start_time = time.time()
model.fit(X_train, y_train)
training_time = time.time() - start_time
print(f"Thời gian huấn luyện: {training_time:.2f} giây")
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f'Mean Absolute Error: {mae}')
print(f'Mean Squared Error: {mse}')
print(f'R Square (Test): {r2}')
print(f'R Square (Train): {model.score(X_train, y_train)}')

