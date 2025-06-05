import pandas as pd
import numpy as np
import statsmodels.api as sm
from joblib import dump, load

# Đọc dữ liệu
data = pd.read_csv('Data/data_encode.csv')

# Kiểm tra và xử lý NaN hoặc giá trị vô hạn trong dữ liệu
# Thay thế các giá trị vô hạn bằng NaN và loại bỏ các dòng có NaN
data_clean = data.replace([np.inf, -np.inf], np.nan).dropna()


X = data_clean.drop('rain', axis=1)
Y = data_clean['rain']

X = sm.add_constant(X)

model = sm.OLS(Y, X).fit()

print(model.summary())

dump(model, 'linear_regression_model.joblib')
model = load('linear_regression_model.joblib')
