import numpy as np
import pandas as pd
data_df = pd.read_csv('./data/auto-mpg.csv', header = 0, engine = 'python')

print('데이터셋 크기: ', data_df.shape)
print (data_df.head())

data_df = data_df.drop(['car_name', 'origin', 'horsepower'], axis = 1, inplace = False)
print (data_df.head())

print('데이터셋 크기: ', data_df.shape)

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

Y = data_df['mpg']
X = data_df.drop(['mpg'], axis = 1, inplace = False)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.3, random_state = 0)

lr = LinearRegression()

lr.fit(X_train,Y_train)

Y_predict = lr.predict(X_test)

mse = mean_squared_error(Y_test, Y_predict) # 자동차 연비에 끼치는 피처의 영향 분석
rmse = np.sqrt(mse)
print('MSE : {0:.3f}, RMSE : {1:.3f}'.format(mse, rmse))
print('R^2(Variance score) : {0:.3f}'.format(r2_score(Y_test, Y_predict)))

print('Y 절편 값: ', np.round(lr.intercept_, 2))
print('회귀 계수 값: ', np.round(lr.coef_, 2))

coef = pd.Series(data = np.round(lr.coef_, 2), index = X.columns)
print (coef.sort_values(ascending = False))

import matplotlib.pyplot as plt
import seaborn as sns

fig, axs = plt.subplots(figsize = (16, 16), ncols = 3, nrows = 2)
x_features = ['model_year', 'acceleration', 'displacement', 'weight', 'cylinders']
plot_color = ['r', 'b', 'y', 'g', 'r']
for i, feature in enumerate(x_features):
     row = int(i/3)
     col = i%3
     sns.regplot(x = feature, y = 'mpg', data = data_df, ax = axs[row][col], color = plot_color[i])

plt.show()


temp = []
print("연비를 예측하고 싶은 차의 정보를 입력해주세요.")
temp.append(int(input("cylinders : ")))
temp.append(int(input("displacement : ")))
temp.append(int(input("weight : ")))
temp.append(int(input("acceleration : ")))
temp.append(int(input("model_year : ")))

mpg_predict = lr.predict([temp])

print("이 자동차의 예상 연비(MPG)는 %.2f입니다." %mpg_predict)

