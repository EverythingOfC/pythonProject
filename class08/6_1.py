import pandas as pd
import seaborn as sns

pd.set_option('display.max_columns',20)
pd.set_option('display.max_rows',200)

df = sns.load_dataset('titanic')

df = df.loc[:,['age','sex','class','fare','survived']]

grouped = df.groupby(['class'])

grouped_filter = grouped.filter(lambda x: len(x)>=200) # 데이터개수가 200개 이상인 그룹을 필터링
print(grouped_filter.head())
print('\n')

grouped_filter = grouped.filter(lambda x: x.age.mean() < 30)
print(grouped_filter.tail())
print('\n')

print(grouped.apply(lambda x: x.describe()))

def z_score(x):
    return (x-x.mean()) / x.std()  # 데이터가 평균으로부터 얼마나 떨어져있는지를 확인한다.

age_z_score = grouped.age.apply(z_score) # z_score함수에 grouped.age값을 대입한다.

print(age_z_score.head());


age_filter = grouped.apply(lambda x:x.age.mean() < 30)

for x in age_filter.index:
    if age_filter[x] == True:
        age_filter_df = grouped.get_group(x) # grouped의 행 인덱스 x값에 해당하는 그룹을 시리즈 객체로 출력한다.
        print(age_filter_df.head())
        print(type(age_filter_df))

