import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']

df = pd.read_csv('./covid-final.csv')
notCountry = ['World', 'Asia', 'Europe', 'European Union', 'Africa', 'North America', 'South America', 'Oceania', 'High income', 'Upper middle income', 'Low income', 'Lower middle income']
df = df.loc[df['country'].isin(notCountry) == False] # 将非国家/地区（即为地区集合体）的数据删除
df_20211220 = df[df['time'] == '2021-12-20'] # 获得2021-12-20的数据
# 按照country分组后取max，实际上为了更方便的调用sort_values，以及调用head获取前20名数据
dict = df_20211220.groupby('country')['total_cases'].max().sort_values(ascending=False).head(20)
list = dict.index.tolist()
# 选择前20名的数据
df_final = df_20211220.loc[df['country'].isin(list) == True].groupby('country')['total_cases'].max()
# 将其他数据求和
df_other = df_20211220.loc[df['country'].isin(list) == False].groupby('country')['total_cases'].max().sum()
# 将求和后的数据加入前20名的数据集中
df_final = df_final.append(pd.Series(df_other, index=['Others']))
# 将加入Others的数据集排序
df_final.sort_values(ascending=False, inplace=True)

plt.figure(figsize=(10, 10))
plt.title('国家累计确诊人数比例图（2021.12.20）')
# 绘制饼状图
plt.pie(df_final, labels=df_final.index, autopct='%.1f%%')
plt.savefig('./png/4.png', dpi=500)