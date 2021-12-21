import pandas as pd

pd.set_option('display.unicode.east_asian_width', True)
data = pd.read_csv('./BeijingPM20100101_20151231.csv', encoding='utf-8')
# 数据抽取及存储
data2015 = data.loc[data['year']==2015].drop(columns=['No'])
data2015.to_csv('./BeijingPM2015.csv', index=False, encoding='utf-8')

data = pd.read_csv('./BeijingPM2015.csv', encoding='utf-8')
print('--------------------')
print('存在的空值列：')
# 找出存在空值的列
print(data.isnull().any())

print('--------------------')
print('列对应的空值数量：')
# 找出对应列空值数量
print(data.isnull().sum(axis=0))

print('--------------------')
columns = ['PM_Dongsi', 'PM_Dongsihuan', 'PM_Nongzhanguan', 'PM_US Post']
# 计算每一行四个pm2.5监测点的平均值
meanpm = round(data[columns].mean(axis=1), 1)
# 创建一个四个监测点名称到平均值的映射
fill = {}.fromkeys(columns, meanpm)
# 使用映射，将四个监测点的平均值替换某些监测点的空值
data.fillna(value=fill, inplace=True)

# 其他数据使用上一行的非空值填充
data.fillna(method='ffill', inplace=True)
print(data)

print('--------------------')
print('空值处理后存在的空值列：')
print(data.isnull().any())

print('--------------------')
print('空值处理后列对应的空值数量：')
print(data.isnull().sum(axis=0))
print('--------------------')

data.to_csv('./BeijingPM2015_cleaned.csv', index=False, encoding='utf-8')