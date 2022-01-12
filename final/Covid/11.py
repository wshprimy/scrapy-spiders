import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']

df = pd.read_csv('./covid-final.csv')
notCountry = ['World', 'Asia', 'Europe', 'European Union', 'Africa', 'North America', 'South America', 'Oceania', 'High income', 'Upper middle income', 'Low income', 'Lower middle income']
df = df.loc[df['country'].isin(notCountry) == False] # 将非国家/地区（即为地区集合体）的数据删除
# 按照country分组后取max能够获得最大值，累计量则最大值为最后一天（2021.12.20）的值

df_1 = df.groupby('country')['total_cases'].max().sort_index()
df_2 = df.groupby('country')['vaccinated'].max().sort_index()
df_3 = df.groupby('country')['vaccinated_fully_rate'].max().sort_index()

df_1 = (df_1 - df_1.min()) / (df_1.max() - df_1.min())
df_2 = (df_2 - df_2.min()) / (df_2.max() - df_2.min())
total = (1 - df_1) * 0.2 + df_2 * 0.4 + df_3 * 0.4
dict = total.sort_values(ascending=False).head(10)

plt.figure(figsize=(24, 8))
plt.title('应对新冠疫情最好的前十名国家/地区（2021.12.20）')
plt.xlabel('国家/地区')
plt.ylabel('得分函数')
plt.bar(dict.index, dict.values)
for i, j in zip(dict.index, dict.values):
    plt.text(i, j, format(j, ''), ha='center', va='bottom', fontsize=12, color='black', alpha=0.7)

plt.savefig('./png/11.png', dpi=500)