from math import pi

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['font.size'] = 12
plt.rcParams['axes.unicode_minus'] = False
# dataframe全显示
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)

df2 = pd.DataFrame({
    'group': ['口味不好',
'产品温度',
'产品变质',
'缺少配送',
'配送延迟',
'食材安全',
'产品种类少',
'评价不真实'],
    '口味不好': [66, 15, 30, 4,45,38, 15, 30],
    '产品温度': [55, 10, 9, 34,63,38, 15, 30],
    '产品变质': [30, 39, 23, 24,23,38, 15, 30],
    '缺少配送': [38, 31, 33, 14,34,38, 40, 30],
    '配送延迟': [31, 15, 32, 14,22,38, 15, 30],
    '食材安全': [22, 25, 62, 24,42,38, 15, 30],
    '产品种类少': [56, 15, 30, 4, 45,38, 15, 30],
    '评价不真实': [46, 10, 9, 34, 63,38, 15, 30],


})
fig=plt.figure(figsize=(12,6))
categories = list(df2)[1:]
N = len(categories)

angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]

ax = plt.subplot(121, polar=True)

ax.set_theta_offset(pi / 2)
ax.set_theta_direction(-1)
clist=['#EAF6DE','#B3D0AB',"#77A67E",'#527D5D','#19422A']

plt.xticks(angles[:-1], categories)
ax.set_rlabel_position(0)
plt.yticks([0,20,40,60,80], ['0','20','40','60','80'], size=7)
plt.ylim(0, 80)

values = df2.loc[0].drop('group').values.flatten().tolist()
values += values[:1]
ax.plot(angles, values, linewidth=2, linestyle='solid', label="18-24岁",color='#6C8EBF')
ax.fill(angles, values,color="#A9C4EB", alpha=0.5)
ax.tick_params(axis='x', which='major', pad=20)




df3 = pd.DataFrame({
    'group': ['口味不好',
'产品温度',
'产品变质',
'缺少配送',
'配送延迟',
'食材安全',
'产品种类少',
'评价不真实'],
    '口味不好': [23, 15, 30, 4,45,38, 15, 30],
    '产品温度': [26, 10, 9, 34,63,38, 15, 30],
    '产品变质': [27, 39, 23, 24,23,38, 15, 30],
    '缺少配送': [29, 31, 33, 14,34,38, 40, 30],
    '配送延迟': [24, 15, 32, 14,22,38, 15, 30],
    '食材安全': [20, 25, 62, 24,42,38, 15, 30],
    '产品种类少': [26, 15, 30, 4, 45,38, 15, 30],
    '评价不真实': [23, 10, 9, 34, 63,38, 15, 30],
})

values = df3.loc[0].drop('group').values.flatten().tolist()
values += values[:1]
ax.plot(angles, values, linewidth=2, linestyle='solid', label="25-30岁",color='#B85450')
ax.fill(angles, values,color="#F8CECC", alpha=0.5)

df4 = pd.DataFrame({
    'group': ['口味不好',
'产品温度',
'产品变质',
'缺少配送',
'配送延迟',
'食材安全',
'产品种类少',
'评价不真实'],
    '口味不好': [20, 15, 30, 4,45,38, 15, 30],
    '产品温度': [26, 10, 9, 34,63,38, 15, 30],
    '产品变质': [25, 39, 23, 24,23,38, 15, 30],
    '缺少配送': [15, 31, 33, 14,34,38, 40, 30],
    '配送延迟': [17, 15, 32, 14,22,38, 15, 30],
    '食材安全': [17, 25, 62, 24,42,38, 15, 30],
    '产品种类少': [24, 15, 30, 4, 45,38, 15, 30],
    '评价不真实': [23, 10, 9, 34, 63,38, 15, 30],


})
values = df4.loc[0].drop('group').values.flatten().tolist()
values += values[:1]
ax.plot(angles, values, linewidth=2, linestyle='solid', label="31-40岁",color='#527D5D')
ax.fill(angles, values,color="#D5E8D4", alpha=0.5)


#-------------------------------------------------------------------------------------------------------------------

df0 = pd.DataFrame({
    'group': ['口味不好',
'产品温度',
'产品变质',
'缺少配送',
'配送延迟',
'食材安全',
'产品种类少',
'评价不真实'],
    '口味不好': [174, 15, 30, 4,45,38, 15, 30],
    '产品温度': [171, 10, 9, 34,63,38, 15, 30],
    '产品变质': [155, 39, 23, 24,23,38, 15, 30],
    '缺少配送': [152, 31, 33, 14,34,38, 40, 30],
    '配送延迟': [124, 15, 32, 14,22,38, 15, 30],
    '食材安全': [102, 25, 62, 24,42,38, 15, 30],
    '产品种类少': [174, 15, 30, 4, 45,38, 15, 30],
    '评价不真实': [150, 10, 9, 34, 63,38, 15, 30],


})
categories = list(df0)[1:]
N = len(categories)

angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]

ax0 = plt.subplot(122, polar=True)

ax0.set_theta_offset(pi / 2)
ax0.set_theta_direction(-1)
clist=['#EAF6DE','#B3D0AB',"#77A67E",'#527D5D','#19422A']

plt.xticks(angles[:-1], categories)
ax0.set_rlabel_position(0)
plt.yticks([0,50,100,150,200], ['0','50','100','150','200'], size=7)
plt.ylim(0, 200)

values = df0.loc[0].drop('group').values.flatten().tolist()
values += values[:1]
ax0.plot(angles, values, linewidth=2, linestyle='solid', label="总体",color='#19422A')
ax0.fill(angles, values,color="#77A67E", alpha=0.2)
ax0.tick_params(axis='x', which='major', pad=20)

fig.legend(loc='upper center',ncol=4,frameon=False)
plt.tight_layout()
plt.savefig(r'C:/Users/徐浩然/Desktop/轻食Figure/1&2.png',dpi=400)
plt.show()