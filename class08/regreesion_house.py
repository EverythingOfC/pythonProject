import numpy as np
import pandas as pd
from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score



pd.set_option('display.max_columns',20)

boston = load_boston()# 보스턴 주택 가격 데이터를 활용하기 위해서 대입

print(type(boston)) # sklearn.utils.Bunch 형

boston_df = pd.DataFrame(boston.data, columns = boston.feature_names) # 독립변수의 이름 리스트
print (boston_df.head()) # 5x13

boston_df['PRICE'] = boston.target # 종속변수의 값
print (boston_df.head()) # 5x14
print(boston_df.shape)

Y = boston_df['PRICE'] # 종속변수
X = boston_df.drop(['PRICE'], axis = 1,inplace=False)

# 훈련용 데이터와 평가용 데이터 분할하기
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.3, random_state = 156)


lr = LinearRegression() # 회귀분석 모델 생성

lr.fit(X_train, Y_train) # 모델 훈련

Y_predict = lr.predict(X_test) # 평가 데이터에 대한 예측 수행 ( y의 결과값 도출 )

mse = mean_squared_error(Y_test, Y_predict) # 오차 계산(평가 지표)
rmse = np.sqrt(mse)

print('MSE : {0:.3f}, RMSE : {1:.3f}'.format(mse, rmse))
print('R^2(Variance score) : {0:.3f}'.format(r2_score(Y_test, Y_predict)))

print('Y 절편 값: ', lr.intercept_)
print('회귀 계수 값: ', np.round(lr.coef_, 1))

coef = pd.Series(data = np.round(lr.coef_, 2), index = X.columns) # 회귀 계수값과 피쳐를 시리즈 객체로 묶어서 반환
print (coef.sort_values(ascending = False)) # 회귀 분석값을 내림차순으로 출력



import matplotlib.pyplot as plt
import seaborn as sns

fig, axs = plt.subplots(figsize = (16, 16), ncols = 3, nrows = 5)

x_features = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT']

for i, feature in enumerate(x_features): # 13개의 피처를 돌려서
   row = int(i/3)
   col = i%3
   sns.regplot(x = feature, y = 'PRICE', data = boston_df, ax = axs[row][col])

plt.show()
