import pandas as pd
import seaborn as sns

pd.set_option('display.max_columns',20)
pd.set_option('display.max_rows',200)

df = sns.load_dataset('titanic')

df = df.loc[:,['age','sex','class','fare','survived']]

grouped = df.groupby(['class'])


grouped_filter = grouped.filter(lambda x: len(x)>=200) # 데이터개수가 200개 이상인 그룹을 필터링
print(grouped_filter.head())



