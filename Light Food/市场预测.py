
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap

rc = {'font.sans-serif': 'Microsoft YaHei',  'axes.unicode_minus': False,"mathtext.fontset": 'stix'}
sns.set(context='notebook', rc=rc,style='ticks')
plt.rcParams['font.size'] = 12
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
clist=['#EAF6DE','#B3D0AB',"#77A67E",'#527D5D','#19422A']
df = pd.read_excel(r'C:\Users\徐浩然\Desktop\苏州人口.xlsx', sheet_name='汇总')
plt.figure(figsize=(10,6))
plt.plot(df['年'],df['真实值'],label='真实值',color='#527D5D',marker='v')
plt.plot(df['年'],df['灰色预测拟合值'],label='灰色预测拟合值',color='#F8CECC',linestyle="--",marker='*')
plt.plot(df['年'],df['时间序列拟合值'],label='时间序列拟合值',color='#DAE8FC',linestyle="-.",marker='p')
plt.plot(df['年'],df['时间序列预测值'],label='时间序列预测值',color="#6C8EBF",linestyle="-",marker='P')
plt.plot(df['年'],df['灰色预测预测值'],label='灰色预测预测值',color='#FF6666',marker='d')
plt.plot(df['年'],df['w'],color='black',linestyle='--',linewidth=1)
plt.plot(df['年'],df['e'],color='black',linestyle='--',linewidth=1)
plt.plot(df['年'],df['f'],color='black',linestyle='--',linewidth=1)
plt.plot(df['年'],df['g'],color='black',linestyle='--',linewidth=1)

plt.legend(frameon=False)
plt.savefig(r'C:/Users/徐浩然/Desktop/轻食Figure/预测',dpi=400)

plt.show()
# "#6C8EBF",'#FFBE99','#D5E8D4','#FF9999'
