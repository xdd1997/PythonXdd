
# edit by xdd
# 2020-07-03
# 参考链接：https://zyk.mingrisoft.com/Develop/view/id/2570/type/7/cid/49.html

import xlrd
import pandas as pd
import matplotlib.pyplot as plt


plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文

plt.rcParams['axes.unicode_minus'] = False  # 显示负号

# 读取的时候，索引列变为chn_name,这样画图时候X轴自动为索引

df = pd.read_excel('mrbook.xlsx', index_col='月份')

df.index.name = '月份'  # x轴的label为月份’。

print(df)

plt.rc('font', family='SimHei', size=13)

plt.figure()

df['销量'].plot(kind='bar')

plt.ylabel('销量')

plt.title('销售情况对比')

p = df['rate']

p.plot(color='black', secondary_y=True, style='--o', linewidth=2)  # style--表示虚线，-表示实线

plt.ylabel('增长速度')

x = [0, 1, 2, 3, 4, 5]  # x轴默认对应的数值是从0开始

for a, b in zip(x, p):

    plt.text(a, b +0.02, '%.2f' % b, ha='center', va='bottom', fontsize=12, color='red')

plt.show()