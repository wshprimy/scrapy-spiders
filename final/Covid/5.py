import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']

df = pd.read_csv('./covid-final.csv')
notCountry = ['World', 'Asia', 'Europe', 'European Union', 'Africa', 'North America', 'South America', 'Oceania', 'High income', 'Upper middle income', 'Low income', 'Lower middle income']
df = df.loc[df['country'].isin(notCountry) == False] # 将非国家/地区（即为地区集合体）的数据删除
df_20211220 = df[df['time'] == '2021-12-20'] # 获得2021-12-20的数据
# 按照country分组后取max，实际上为了更方便的调用sort_values，以及调用head获取前10名数据
dict = df_20211220.groupby('country')['total_cases_per_million'].max().sort_values(ascending=False).head(10)

plt.figure(figsize=(16, 8))
plt.title('国家每百万人口累计确诊人数前十名国家/地区（2021.12.20）')
plt.xlabel('国家')
plt.ylabel('国家每百万人口累计确诊人数')
plt.bar(dict.index, dict.values)
for i, j in zip(dict.index, dict.values):
    plt.text(i, j, format(j, ''), ha='center', va='bottom', fontsize=12, color='black', alpha=0.7)

plt.savefig('./png/5.png', dpi=500)