import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']

df = pd.read_csv('./covid-final.csv')
notCountry = ['World', 'Asia', 'Europe', 'European Union', 'Africa', 'North America', 'South America', 'Oceania', 'High income', 'Upper middle income', 'Low income', 'Lower middle income']
df = df.loc[df['country'].isin(notCountry) == False] # 将非国家/地区（即为地区集合体）的数据删除
# 按照country分组后求和，为了获得15日内新增确诊人数最多的国家，排序后取前十名
dict = df.groupby('country')['new_cases'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(16, 8))
plt.title('新增确诊人数（2021.12.05-2021.12.20）')
plt.xlabel('日期')
plt.ylabel('新增确诊人数')
for country in dict.index.tolist():
    x = df.loc[df['country'] == country]['time']
    y = df.loc[df['country'] == country]['new_cases']
    plt.plot(x, y)
    for i, j in zip(x, y):
        plt.text(i, j, format(j, ''), ha='center', va='bottom', fontsize=6, color='black', alpha=0.7)

plt.legend(dict.index.tolist(), loc='upper left', fontsize=12)
plt.savefig('./png/2.png', dpi=500)