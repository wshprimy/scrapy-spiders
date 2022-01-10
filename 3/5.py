import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
df = pd.read_csv("BeijingPM20100101_20151231.csv")

columns = ['PM_Dongsi', 'PM_Dongsihuan', 'PM_Nongzhanguan', 'PM_US Post']
# 计算每一行四个pm2.5监测点的平均值
meanpm = round(df[columns].mean(axis=1), 1)
# 创建一个四个监测点名称到平均值的映射
fill = {}.fromkeys(columns, meanpm)
# 使用映射，将四个监测点的平均值替换某些监测点的空值
df.fillna(value=fill, inplace=True)
df.to_csv('./after.csv', index=False, encoding='utf-8')

avg = df.groupby(['year', 'month']).agg({'PM_Dongsi': np.mean})

plt.legend()
plt.title('北京2010-2015各年份PM2.5指数月均值折线图', fontsize=20)
plt.xlabel('月', loc='right', fontsize=16)
plt.ylabel('PM2.5指数月均值', loc='top', fontsize=16)
for i, year in enumerate(range(2010, 2016)):
    plt.plot(list(range(1,13)), avg.loc[year]['PM_Dongsi'].to_list(), label=year)

plt.legend()
plt.show()