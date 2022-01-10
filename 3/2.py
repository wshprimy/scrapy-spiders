import matplotlib.pyplot as plt

label = ['生活日用', '文教娱乐', '服饰美容', '交通出行', '饮食', '运动健康', '通讯物流', '住房缴费', '其他消费']
money = [51686.39, 10325.60, 7927.91, 5407.22, 5304.16, 980.11, 801.55, 770.00, 16041.03]

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.title('2018年支付宝年支出情况', fontsize=20)
explode = [0] * len(money)
for i in range(len(money)):
    if money[i] < 1000:
        explode[i] = 0.5
    elif money[i] < 5000:
        explode[i] = 0.1
    else:
        explode[i] = 0
plt.pie(money, labels=label, autopct='%.1f%%', explode=explode, radius=0.75)
plt.show()