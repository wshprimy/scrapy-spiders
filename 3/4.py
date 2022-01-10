import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
df = pd.read_excel('八年级期末考试成绩表.xlsx')
courses = ['地理分数', '历史分数', '政治分数', '生物分数', '物理分数', '英语分数']

plt.suptitle('八年级期末考试成绩分布直方图', fontsize=24)
for i, course in enumerate(courses):
    plt.subplot(2, 3, i + 1)
    plt.title(f'{course}分布直方图', fontsize=20)
    plt.xlabel(course, loc='right', fontsize=16)
    plt.ylabel('学生人数', loc='top', fontsize=16)
    score = df[course]
    limit = 120 if course == '英语分数' else 100
    bin = [i for i in range(0, limit + 10, 10)]
    plt.hist(score, bins=bin, alpha=0.7, edgecolor='black')

plt.show()