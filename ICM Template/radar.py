from math import pi

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap

plt.rcParams['font.sans-serif'] = ['Arial']
plt.rcParams['font.size'] = 12
plt.rcParams['axes.unicode_minus'] = False
plt.style.use('seaborn-ticks')
# dataframe全显示
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)

c1list=[(16/255,70/255,128/255),(49/255,124/255,183/255),(109/255,173/255,209/255),(182/255,215/255,232/255),(233/255,241/255,244/255),(251/255,227/255,213/255),(246/255,178/255,147/255),(220/255,109/255,87/255),(183/255,34/255,48/255),(109/255,1/255,31/255)]
c2list=[(40/255,86/255,119/255),(177/255,193/255,204/255),(214/255,156/255,147/255),(229/255,207/255,194/255),(141/255,164/255,147/255)]
c3list=[(40/255,86/255,119/255),(177/255,193/255,204/255),(214/255,156/255,147/255),(229/255,207/255,194/255),(141/255,164/255,147/255),(59/255,72/255,47/255)]

C1 = LinearSegmentedColormap.from_list('Blues',c1list,N=256)
C2 = LinearSegmentedColormap.from_list('Blues',c2list,N=256)
C3 = LinearSegmentedColormap.from_list('Blues',c3list,N=256)

# 设置数据
df = pd.DataFrame({
    'group': ['GDP','Forest Resources',
'Water Resources',
'Mineral Resources',
'Natural Population Growth',
'Social Welfare Levels',
'Exhaust Emissions',
'Wastewater Discharge',
'Natural Disasters',
'Biodiversity',
'Eco-protected Area Ratio'
],
    'C3': [0.5052, 15, 30, 4,45,38, 15, 30, 4,45,23],
    'P1': [0.1193, 10, 9, 34,63,38, 15, 30, 4,45,34],
    'P2': [0.0179, 39, 23, 24,23,38, 15, 30, 4,45,23],
    'P3': [0.0567, 31, 33, 14,34,38, 40, 30, 4,45,34],
    'P4': [0.0605, 15, 32, 14,22,38, 15, 30, 4,45,34],
    'P5': [0.0202, 25, 62, 24,42,38, 15, 30, 4,45,12],
    'P6': [0.1125, 15, 30, 4, 45,38, 15, 30, 4,45,12],
    'P7': [0.0563, 10, 9, 34, 63,38, 15, 30, 4,45,12],
    'P8': [0.0318, 39, 23, 24, 23,38, 15, 30, 4,45,12],
    'P9': [0.0143, 70, 33, 14, 34,38, 50, 30, 4,45,12],
    'P10': [0.0048, 31, 33, 14, 34,38, 15, 30, 4,45,12],

})

# 目标数量
categories = list(df)[1:]
N = len(categories)

# 角度
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]

# 初始化
ax = plt.subplot(111, polar=True)

# 设置第一处
ax.set_theta_offset(pi / 2)
ax.set_theta_direction(-1)

# 添加背景信息
plt.xticks(angles[:-1], categories)
ax.set_rlabel_position(0)
plt.yticks([0.2, 0.4, 0.6], ["0.2", "0.4", "0.6"], color="grey", size=7)
plt.ylim(0, 0.6)

# 添加数据图

# 第一个
values = df.loc[0].drop('group').values.flatten().tolist()
values += values[:1]
ax.plot(angles, values, linewidth=2, linestyle='solid', label="group A",color=(40/255,86/255,119/255))
ax.fill(angles, values,color=(123/255,154/255,171/255), alpha=0.8)


# 添加图例
# plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))
plt.tight_layout()
plt.savefig(r'C:/Users/徐浩然/Desktop/美赛Figure_Template\189022000.png',dpi=400)
# 显示
plt.show()