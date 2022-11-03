import numpy as np
import pandas as pd
#피처 이름 파일 읽어오기
feature_name_df = pd.read_csv('./data/UCI_HAR_Dataset/UCI_HAR_Dataset/features.txt', sep = '\s+', header = None, names = ['index','feature_name'], engine = 'python')

print (feature_name_df.head())
print (feature_name_df.shape) # 561,2

feature_name = feature_name_df.iloc[:, 1].values.tolist()

X_train = pd.read_csv('./data/UCI_HAR_Dataset/UCI_HAR_Dataset/train/X_train.txt', delim_whitespace=True, header=None, engine = 'python')
X_train.columns = feature_name
X_test = pd.read_csv('./data/UCI_HAR_Dataset/UCI_HAR_Dataset/test/X_test.txt', delim_whitespace=True, header=None, engine = 'python')
Y_train = pd.read_csv('./data/UCI_HAR_Dataset/UCI_HAR_Dataset/train/y_train.txt', delim_whitespace=True, header=None, names = ['action'], engine = 'python')
Y_test = pd.read_csv('./data/UCI_HAR_Dataset/UCI_HAR_Dataset/test/y_test.txt' , delim_whitespace=True, header=None, names = ['action'], engine = 'python')

