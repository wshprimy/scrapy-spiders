import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']

df = pd.read_csv('./covid-final.csv')
gdptop10 = ['United States', 'China', 'Japan', 'Germany', 'United Kingdom', 'India', 'France', 'Italy', 'Canada', 'South Korea']
df = df.loc[df['country'].isin(gdptop10) == True] # 选择gdp前10的国家
df_20211220 = df[df['time'] == '2021-12-20'] # 获得2021-12-20的数据
# 按照country分组后取max，实际上为了更方便的得到dict
dict = df_20211220.groupby('country')['total_cases'].max()

dict.plot.box(showmeans=True, title='GDP前十名国家累计确诊人数（2021.12.20）') # 绘制箱型图
print('平均值 = {}'.format(dict.values.mean()))
plt.ylabel('累计确诊人数')
plt.grid(linestyle='-.')
plt.savefig('./png/8.png', dpi=500)