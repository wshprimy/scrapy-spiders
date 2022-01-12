import pandas as pd
import matplotlib.pyplot as plt
from pyecharts.charts import Map
from pyecharts import options as opts

plt.rcParams['font.sans-serif'] = ['SimHei']

df = pd.read_csv('./covid-final.csv')
notCountry = ['World', 'Asia', 'Europe', 'European Union', 'Africa', 'North America', 'South America', 'Oceania', 'High income', 'Upper middle income', 'Low income', 'Lower middle income']
df = df.loc[df['country'].isin(notCountry) == False] # 将非国家/地区（即为地区集合体）的数据删除
df_20211220 = df[df['time'] == '2021-12-20'] # 获得2021-12-20的数据
# 按照country分组后取max，实际上为了更方便的得到dict
dict = df_20211220.groupby('country')['vaccinated'].max()

map = Map(init_opts=opts.InitOpts(width='100%', height='1200px'))
map.add(
    '累计疫苗接种人数',
    [list(i) for i in zip(dict.index, dict.values)],
    'world'
)
map.set_global_opts(
    title_opts=opts.TitleOpts(title='国家累计疫苗接种人数热力图'), # 图表标题
    visualmap_opts=opts.VisualMapOpts(max_=max(dict.values)) # 热⼒图数值区间
)
map.set_series_opts(
    label_opts=opts.LabelOpts(is_show=True) # 热力图图例
)
map.render('./png/6-1.html')