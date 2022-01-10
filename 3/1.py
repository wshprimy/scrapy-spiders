import matplotlib.pyplot as plt

year = [1953, 1964, 1982, 1990, 2000, 2010, 2020]
height = [58260, 69458, 100818, 113368, 126583, 133972, 141178]

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.title('历次普查全国人口\nNational Population from Population Censuses', fontsize=20)
plt.xlabel('年份\nyears', loc='right', fontsize=16)
plt.ylabel('万人 10000 persons', loc='top', fontsize=16)
plt.bar(year, height, width=2.0, color='b', alpha=0.7, align='center')
plt.xticks(ticks=year)
for i, j in zip(year, height):
    plt.text(i, j, format(j, ''), ha='center', va='bottom', fontsize=12, color='b', alpha=0.7)
plt.show()