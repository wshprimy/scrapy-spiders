import pandas as pd

pd.set_option('display.unicode.east_asian_width', True)
data = pd.read_csv('./loupan.csv', encoding='utf-8-sig')

print('--------------------')
print('总价最贵的房子为：')
totalmax_id = data.loc[:, '总价'].idxmax()
print(data.loc[totalmax_id])

print('--------------------')
print('总价最便宜的房子为：')
totalmin_id = data.loc[:, '总价'].idxmin()
print(data.loc[totalmin_id])

print('--------------------')
print('总价的中位数：')
totalmin_id = data.loc[:, '总价'].idxmin()
print('{:.4f}'.format(data.loc[:, '总价'].median()))

print('--------------------')
print('均价最贵的房子为：')
totalmax_id = data.loc[:, '均价'].idxmax()
print(data.loc[totalmax_id])

print('--------------------')
print('均价最便宜的房子为：')
totalmin_id = data.loc[:, '均价'].idxmin()
print(data.loc[totalmin_id])

print('--------------------')
print('单价的中位数：')
totalmin_id = data.loc[:, '均价'].idxmin()
print('{:.4f}'.format(data.loc[:, '均价'].median()))

print('--------------------')
print('总价在均值三倍标准差以外的异常值：')
down = data['总价'].mean() - 3 * data['总价'].std()
up = data['总价'].mean() + 3 * data['总价'].std()
print(data.loc[(data['总价'] < down) | (data['总价'] > up)])

print('--------------------')
print('均价在箱型图原则下（k = 1.5）的异常值：')
k = 1.5
q1 = data['均价'].quantile(q=0.25)
q3 = data['均价'].quantile(q=0.75)
down = q1 - k * (q3 - q1)
up = q3 + k * (q3 - q1)
print(data.loc[(data['均价'] < down) | (data['均价'] > up)])

print('--------------------')
print('均价离散化处理：')
avgs = [0, 20000, 40000, 60000, 80000, 100000, 120000, 140000, 160000, 180000]
cuts = pd.cut(data['均价'], avgs)
calc = pd.value_counts(cuts).to_frame()
total = calc.iloc[:, 0].sum()
calc['百分比'] = 100 * calc.iloc[:, 0] / total
calc.sort_index(axis=0, ascending=True, inplace=True)
print(calc)
print('--------------------')