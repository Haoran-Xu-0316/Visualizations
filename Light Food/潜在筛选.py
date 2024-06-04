import geopandas
import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import statsmodels
from matplotlib import font_manager
from matplotlib.colors import LinearSegmentedColormap

# my_font=font_manager.FontProperties(fname="C:\Windows\Fonts\simsun.ttc")

plt.rcParams['font.size'] = 12
plt.rcParams['axes.unicode_minus'] = False
# plt.rcParams['sans.serif'] = ['SimSun']

rc = {'font.sans-serif': 'Microsoft YaHei',
      'axes.unicode_minus': False,"mathtext.fontset": 'stix'}
sns.set(style='ticks' ,rc=rc)
ticklabels_style = {
    "fontname": "Times New Roman",
}

# plt.style.use('seaborn-ticks')
# dataframe全显示
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)

# clist=['#EAF6DE','#B3D0AB',"#77A67E",'#527D5D','#19422A']
# # clist=['#F1F5C9','#CEDEA2','#98B574','#678B4A','#435C28']
# C = LinearSegmentedColormap.from_list('Blues',clist,N=256)

#B3D0AB
#19422A
df1 = pd.read_excel(r'C:\Users\徐浩然\Desktop\潜在用户特征信息（排除低意愿）.xlsx', sheet_name='Sheet1')
df2 = pd.read_excel(r'C:\Users\徐浩然\Desktop\既有用户基础特征+目标变量.xlsx', sheet_name='Sheet1')
plt.figure(figsize=(10,6))


plt.plot(range(len(df2['Q13（愿意为轻食支付的消费金额）'])),df2['Q13（愿意为轻食支付的消费金额）'],color='#B3D0AB',label='真实值')
plt.plot(range(len(df2['既有预测'])),df2['既有预测'],color='#19422A',label='预测值')

plt.xticks(range(0,1101,100))
plt.yticks(range(0,10,1))
plt.legend(frameon=False)
plt.savefig(r'C:/Users/徐浩然/Desktop/轻食Figure/多元1.png',dpi=400)

plt.figure(figsize=(10,6))

plt.plot(range(len(df1['潜在预测'])),df1['潜在预测'],color='#19422A',label='预测值')
plt.yticks(np.arange(5,7,0.2))
plt.legend(frameon=False,loc='lower left')
plt.fill_between(range(len(df1['潜在预测'])),5.666,6.097,color='#B3D0AB',alpha=0.4,linewidth=0)
plt.savefig(r'C:/Users/徐浩然/Desktop/轻食Figure/多元2.png',dpi=400)

plt.show()