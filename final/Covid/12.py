import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model

plt.rcParams['font.sans-serif'] = ['SimHei']

df = pd.read_csv('./covid-final.csv')
x = df.loc[df['country']=='World']['time']
y = df.loc[df['country']=='World']['total_cases']
x = [i for i in range(5, 21)]
y = y.values[0:16]

plt.figure(figsize=(24, 8))
plt.title('世界累计确诊人数（2021.12.05-2021.12.20）')
plt.xlabel('日期（2021.12）')
plt.ylabel('世界累计确诊人数')
plt.plot(x, y)
plt.scatter(x, y)
for i, j in zip(x, y):
    plt.text(i, j, format(j, ''), ha='center', va='bottom', fontsize=10, color='black', alpha=0.7)

model = linear_model.LinearRegression()
x = np.array([i for i in range(5, 16)]).reshape(-1, 1)
y = y[0:11]
model.fit(x, y) # 使用前10天的数据拟合曲线
x = np.array([i for i in range(16, 21)]).reshape(-1, 1)
y = model.predict(x) # 预测后5天的结果

x = [i for i in range(16, 21)]
plt.scatter(x, y, color='b')
for i, j in zip(x, y):
    plt.text(i, j, format(j, ''), ha='center', va='top', fontsize=10, color='black', alpha=0.7)

plt.savefig('./png/12.png', dpi=500)