
import math

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.interpolate as sci
import scipy.optimize as sco
import seaborn as sns
import tushare as ts
from arch import arch_model
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import acf, adfuller, pacf

#全局设置----------------------------------------------------------------------------------------------------------------
# plt.rcParams['font.sans-serif']=['Microsoft YaHei']
plt.rcParams['font.sans-serif'] = ['Palatino Linotype']

plt.rcParams['font.size'] = 14
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['lines.linewidth'] = 1
plt.rcParams["font.weight"] = "bold"
C='darkslategrey'
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
df=pd.read_excel(r'C:\Users\徐浩然\Desktop\Cor.xlsx',sheet_name='GPR',index_col=0,parse_dates=[0])
# df=pd.read_excel(r'C:\Users\徐浩然\Desktop\Cor.xlsx',sheet_name='GPR',index_col=0,parse_dates=[0])
# df=pd.read_excel(r'C:\Users\徐浩然\Desktop\Cor.xlsx',sheet_name='GPR',index_col=0,parse_dates=[0])

low=pd.read_excel(r'C:\Users\徐浩然\Desktop\宏观指数.xlsx', sheet_name='原始',index_col=0,parse_dates=[0])
low = low.drop(low.index[:37])
r=pd.read_excel(r'C:\Users\徐浩然\Desktop\股债指数.xlsx',sheet_name='差分',index_col=0,parse_dates=[0])
corrmatrix=r.corr()
print(corrmatrix)

corr1 = corrmatrix.iloc[0][1]
corr2= corrmatrix.iloc[0][2]
corr3 = corrmatrix.iloc[1][2]
print(corr1,corr2,corr3)
alpha=0.8


# print(df)
plt.subplots(figsize=(17, 5))
plt.subplot(131)
plt.plot(df['s1[, 2]'],color=C,label='SHGBI-SHCI',alpha=alpha)
plt.plot(df['l1[, 2]'],color='firebrick')
plt.legend(frameon=False,loc='upper right',handlelength=0)
plt.xlim(pd.Timestamp('2018-01-01'), pd.Timestamp('2023-01-01'))
plt.axhline(y=corr1,color='black',linestyle='--')
plt.axhline(y=0,color='black',linestyle='-',linewidth=2)

plt.fill_between(pd.date_range(start='2019-06', end='2020-09', freq='M'), -0.45,0.30, color='#B3D0AB', alpha=0.4, linewidth=0)
plt.margins(x=0,y=0)
plt.yticks(np.arange(-0.45,0.30,0.10))




plt.subplot(132)
plt.plot(df['s2[, 2]'],color=C,label='SHGBI-SHBI',alpha=alpha)
plt.plot(df['l2[, 2]'],color='firebrick')
plt.legend(frameon=False,loc='upper right',handlelength=0)
plt.xlim(pd.Timestamp('2018-01-01'), pd.Timestamp('2023-01-01'))
plt.axhline(y=corr2,color='black',linestyle='--')
plt.axhline(y=0,color='black',linestyle='-',linewidth=2)

plt.fill_between(pd.date_range(start='2019-10', end='2020-08', freq='M'), 0.0,0.85, color='#B3D0AB', alpha=0.4, linewidth=0)
plt.margins(x=0,y=0)
plt.yticks(np.arange(0.0,0.85,0.10))




plt.subplot(133)
plt.plot(df['s3[, 2]'],color=C,label='SHCI-SHBI',alpha=alpha)
plt.plot(df['l3[, 2]'],color='firebrick')
plt.legend(frameon=False,loc='upper right',handlelength=0)
plt.xlim(pd.Timestamp('2018-01-01'), pd.Timestamp('2023-01-01'))
plt.axhline(y=corr3,color='black',linestyle='--')
plt.axhline(y=0,color='black',linestyle='-',linewidth=2)
plt.fill_between(pd.date_range(start='2019-09', end='2020-9', freq='M'), -0.35,0.20, color='#B3D0AB', alpha=0.4, linewidth=0)
plt.margins(x=0,y=0)
plt.yticks(np.arange(-0.35,0.20,0.10))




plt.tight_layout()
plt.savefig(r'C:/Users/徐浩然/Desktop/d.png',dpi=400)

plt.show()

# plt.subplots(figsize=(15, 5))
#
# plt.subplot(131)
# plt.plot(df['v1[, 2]'],color='black',label='SHGBI')
# plt.legend(frameon=False,loc='upper right',handlelength=0)
# plt.xlim(pd.Timestamp('2018-01-01'), pd.Timestamp('2023-01-01'))
#
# plt.subplot(132)
# plt.plot(df['v2[, 2]'],color='black',label='SHCI')
# plt.legend(frameon=False,loc='upper right',handlelength=0)
# plt.xlim(pd.Timestamp('2018-01-01'), pd.Timestamp('2023-01-01'))
#
# plt.subplot(133)
# plt.plot(df['v3[, 2]'],color='black',label='SHBI')
# plt.legend(frameon=False,loc='upper right',handlelength=0)
# plt.xlim(pd.Timestamp('2018-01-01'), pd.Timestamp('2023-01-01'))
#
# plt.tight_layout()
# plt.savefig(r'C:/Users/徐浩然/Desktop/c.png',dpi=400)
#
# plt.show()



#
# fig,ax=plt.subplots(figsize=(12, 8),ncols=1,nrows=3)
# # plt.subplot(312)
# dfff1 = low['GPR']
# ax[0].plot(df['s1[, 2]'],color='black',label='SHGBI-SHCI')
# ax[0].plot(df['l1[, 2]'],color='red')
# bx=ax[0].twinx()
# bx.plot(dfff1,color='darkgreen',label='GPR')
# # #
# dfff1 = low['EPU']
# ax[1].plot(df['s2[, 2]'],color='black',label='SHGBI-SHCI')
# ax[1].plot(df['l2[, 2]'],color='red')
# cx=ax[1].twinx()
# cx.plot(dfff1,color='darkgreen',label='GPR')
# #
# dfff1 = low['CPU']
# ax[2].plot(df['s3[, 2]'],color='black',label='SHGBI-SHCI')
# ax[2].plot(df['l3[, 2]'],color='red')
# dx=ax[2].twinx()
# dx.plot(dfff1,color='darkgreen',label='GPR')


