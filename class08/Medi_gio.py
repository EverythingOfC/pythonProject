import pandas as pd
pd.set_option('mode.chained_assignment', None)
import numpy as np
pd.set_option('display.max_columns',50)
data = pd.read_csv('./data/공공보건의료기관현황.csv', index_col = 0,
                          encoding = ' CP949', engine = 'python')
print (data.head()) #작업 확인용 출력

addr = pd.DataFrame(data['주소'].apply(lambda v: v.split()[:2]).tolist(), columns = ('시도', '군구'))
print (addr.head()) #작업 확인용 출력

print (addr['시도'].unique())  # 해당 칼럼의 값을 중복을 제거하고 출력함.
print(addr[addr['시도'] == '창원시'])
addr.iloc[27] = ['경상남도', '창원시']
addr.iloc[31] = ['경상남도', '창원시']

addr.iloc[27] = ['경상남도', '경산시']

print(addr[addr['시도'] == '천안시'])

addr.iloc[209] = ['충청남도','천안시']
addr.iloc[210] = ['충청남도','천안시']


addr_aliases = {'경기':'경기도', '경남':'경상남도', '경북':'경상북도',
                    '충북':'충청북도', '서울시':'서울특별시', '부산특별시':
                    '부산광역시', '대전시':'대전광역시', '충남':'충청남도',
                    '전남':'전라남도', '전북':'전라북도'}
addr['시도'] = addr['시도'].apply(lambda v : addr_aliases.get(v,v)) # v값이 없을 경우에는 원래 값을 가져오게 하기 위해서 v,v로 쓷나.

print(addr['시도'].unique())

addr.iloc[75] = ['제주특별자치도', '제주시']

addr['시도군구'] = addr.apply(lambda r: r['시도'] + " " + r['군구'], axis = 1)
print (addr.head())   #작업 확인용 출력

addr['count'] = 0

addr_group = pd.DataFrame(addr.groupby(['시도', '군구', '시도군구'], as_index = False).count())
addr_group = addr_group.set_index('시도군구')
print (addr_group.head() )#작업 확인용 출력

population = pd.read_excel('./data/행정구역_시군구_별__성별_인구수.xlsx')
print(population.head()) #작업 확인용 출력

population = population.rename(columns = {'행정구역(시군구)별(1)': '시도', '행정구역(시군구)별(2)': '군구'})
print (population.head()) #작업 확인용 출력

for element in range(0,len(population)):
    population['군구'][element] = population['군구'][element].strip()

population['시도군구'] = population.apply(lambda r: r['시도'] + ' ' + r['군구'], axis = 1)
print (population.head())    #작업

population = population[population.군구 != '소계']

population = population.set_index("시도군구")

# print(population.head()) #작업 확인용 출력

addr_population_merge = pd.merge(addr_group,population, how ='inner',
                                                left_index = True, right_index = True)

print(addr_population_merge.head())

local_MC_Population = addr_population_merge[['시도_x', '군구_x','count', '총인구수 (명)']]
print(local_MC_Population.head()) #작업 확인용 출력

local_MC_Population = local_MC_Population.rename(columns = {'시도_x':'시도', '군구_x': '군구','총인구수 (명)': '인구수'})
MC_count = local_MC_Population['count']

print('\n\n\n')
local_MC_Population['MC_ratio'] = MC_count.div(local_MC_Population['인구수'], axis = 0)*100000 # 인구수의 비율
print(local_MC_Population.head()) #작업 확인용 출력

from matplotlib import pyplot as plt
from matplotlib import rcParams, style
style.use('ggplot')

from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname = "c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family = font_name)

MC_ratio = local_MC_Population[['count']]
MC_ratio = MC_ratio.sort_values('count', ascending = False)
plt.rcParams["figure.figsize"] = (25, 5)
MC_ratio.plot(kind = 'bar', rot = 90)
plt.show()

