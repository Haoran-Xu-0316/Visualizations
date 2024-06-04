import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap

pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)

plt.rcParams['font.sans-serif']=['Microsoft YaHei']
plt.rcParams['font.size'] = 12
plt.rcParams['axes.unicode_minus'] = False

clist=['#EAF6DE','#B3D0AB',"#77A67E",'#527D5D','#19422A']
# clist=['#F1F5C9','#CEDEA2','#98B574','#678B4A','#435C28']
CC = LinearSegmentedColormap.from_list('Blues',clist,N=256)
C='#527D5D'
df = pd.read_excel(r'C:\Users\徐浩然\Desktop\时间序列.xlsx', sheet_name='Sheet1',index_col=0)
print(df)
plt.figure(figsize=(12,8))

plt.subplot(2,2,1)
plt.plot(df['95%置信区间上界'],color='#6C8EBF',label='95%置信区间上界')
plt.plot(df['95%置信区间下界'],color='#B85450',label='95%置信区间下界')
plt.bar(x=np.arange(1,16,1),height=df['最终差分数据自相关图(ACF)'],color='#19422A',alpha=0.7,label='自相关系数')
plt.xticks(np.arange(1,16,1))
plt.xlim(0,16)
plt.yticks(np.arange(-0.5,0.8,0.2))
plt.legend(frameon=False,ncol=3,fontsize=9,loc='upper center',columnspacing=1)
plt.subplot(2,2,2)
plt.plot(df['95%置信区间上界'],color='#6C8EBF',label='95%置信区间上界')
plt.plot(df['95%置信区间下界'],color='#B85450',label='95%置信区间下界')
plt.bar(x=np.arange(1,16,1),height=df['最终差分数据偏自相关图(PACF)'],color='#19422A',alpha=0.7,label='偏自相关系数')
plt.xticks(np.arange(1,16,1))
plt.xlim(0,16)
plt.yticks(np.arange(-0.5,0.8,0.2))
plt.legend(frameon=False,ncol=3,fontsize=9,loc='upper center',columnspacing=1)
plt.subplot(2,2,3)
plt.plot(df['95%置信区间上界'],color='#6C8EBF',label='95%置信区间上界')
plt.plot(df['95%置信区间下界'],color='#B85450',label='95%置信区间下界')
plt.bar(x=np.arange(1,16,1),height=df['模型残差自相关图(ACF)'],color='#19422A',alpha=0.7,label='自相关系数')
plt.xticks(np.arange(1,16,1))
plt.xlim(0,16)
plt.yticks(np.arange(-0.5,0.8,0.2))
plt.legend(frameon=False,ncol=3,fontsize=9,loc='upper center',columnspacing=1)
plt.subplot(2,2,4)
plt.plot(df['95%置信区间上界'],color='#6C8EBF',label='95%置信区间上界')
plt.plot(df['95%置信区间下界'],color='#B85450',label='95%置信区间下界')
plt.bar(x=np.arange(1,16,1),height=df['模型残差偏自相关图(PACF)'],color='#19422A',alpha=0.7,label='偏自相关系数')
plt.xticks(np.arange(1,16,1))
plt.xlim(0,16)
plt.yticks(np.arange(-0.5,0.8,0.2))
plt.legend(frameon=False,ncol=3,fontsize=9,loc='upper center',columnspacing=1)
plt.savefig(r'C:/Users/徐浩然/Desktop/轻食Figure/时间序列.png',dpi=400)

plt.show()