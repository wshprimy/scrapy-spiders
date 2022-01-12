import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']

df = pd.read_csv('./covid-final.csv')
x = df.loc[df['country']=='World']['time']
y = df.loc[df['country']=='World']['new_cases']

plt.figure(figsize=(16, 8))
plt.title('世界新增确诊人数（2021.12.05-2021.12.20）')
plt.xlabel('日期')
plt.ylabel('世界新增确诊人数')
plt.plot(x, y)
plt.scatter(x, y)
for i, j in zip(x, y):
    plt.text(i, j, format(j, ''), ha='center', va='bottom', fontsize=12, color='black', alpha=0.7)
plt.savefig('./png/1-1.png', dpi=500)