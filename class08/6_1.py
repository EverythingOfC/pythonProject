import pandas as pd
import seaborn as sns

pd.set_option('display.max_columns',20)
pd.set_option('display.max_rows',200)

df = sns.load_dataset('titanic')

df = df.loc[:,['age','sex','class','fare','survived']]

grouped = df.groupby(['class'])


def min_max(x):
    return x.max() - x.min()

agg_minmax = grouped.agg({'fare':['min','max'],'age':'mean'})
print(agg_minmax.head())
print('\n')



