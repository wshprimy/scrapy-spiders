import re
import pandas as pd

def delsign(x): # 去除所有单元格的','
    if type(x) == str:
        x = x.replace(',', '')
    return x

def delmillion(x): # 将所有单元格的million转换为原数值乘1000000
    if type(x) == str and re.search('million', x):
        x = x.replace(' million', '')
        x = int(float(x) * 1000000)
    return x

def delbillion(x): # 将所有单元格的billion转换为原数值乘1000000000
    if type(x) == str and re.search('billion', x):
        x = x.replace(' billion', '')
        x = int(float(x) * 1000000000)
    return x

def percentage(x): # 去除所有单元格的百分号
    if type(x) == str and re.search('%', x):
        x = x.replace('%', '')
        x = float(x) / 100.0
    return x
    
pd.set_option('display.unicode.east_asian_width', True)
df = pd.read_csv('./covid.csv', encoding='utf-8-sig')

df = df.applymap(delsign) # 去除所有单元格的','
df = df.applymap(delmillion) # 将所有单元格的million转换为原数值乘1000000
df = df.applymap(delbillion) # 将所有单元格的billion转换为原数值乘1000000000
df = df.applymap(percentage) # 去除所有单元格的百分号

# 将没有新增、累计、累计占国家人口数据的国家填充为0
df['new_cases'].fillna(value=0, inplace=True)
df['total_cases'].fillna(value=0, inplace=True)
df['total_cases_per_million'].fillna(value=0, inplace=True)

df.to_csv('./covid-final.csv', index=False, encoding='utf-8-sig')