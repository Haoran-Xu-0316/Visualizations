import math
from datetime import datetime

import matplotlib.dates as dates
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.interpolate as sci
import scipy.optimize as sco
import seaborn as sns
import tushare as ts

#全局设置-----------------------------------------------------------------------------------------------------------------
# plt.rcParams['font.sans-serif']=['Microsoft YaHei']
plt.rcParams['font.sans-serif'] = ['Palatino Linotype']
# plt.rcParams["font.weight"] = "bold"
plt.rcParams['font.size'] = 12
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['lines.linewidth'] = 1
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)

l=['CSI 300 - Gold','CSI 300 - Oil','CSI 300 - Bitcoin','CSI 300 - Bond','Gold - Oil','Gold - Bitcoin','Gold - Bond','WTI - Bitcoin','WTI - Bond','Bitcoin - Bond']

S=pd.read_excel(r'C:\Users\徐浩然\Desktop\DCC-data-China\Varanice&Covariance-TPU.xlsx', sheet_name='Short-Cor',index_col=0,parse_dates=[0])
L=pd.read_excel(r'C:\Users\徐浩然\Desktop\DCC-data-China\Varanice&Covariance-TPU.xlsx', sheet_name='Long-Cor',index_col=0,parse_dates=[0])
time=pd.Timestamp('2014-07-31'), pd.Timestamp('2023-07-28')
HA=pd.read_excel(r'C:\Users\徐浩然\Desktop\DCC-data-China\Hedging Assets\hedging assets.xlsx', sheet_name='All-log',index_col=0,parse_dates=[0])
corrmatrix=HA.corr()
print(corrmatrix)
M=S.mean()
print(M)
Gold_m=M[0]
WTI_m=M[1]
BTC_m=M[2]
Bond_m=M[3]
Bond = corrmatrix.iloc[0][2]
Gold= corrmatrix.iloc[0][3]
WTI = corrmatrix.iloc[0][4]
BTC = corrmatrix.iloc[0][5]
print(Bond_m,Gold_m,WTI_m,BTC_m)
lw=1.5
plt.subplots(figsize=(12,8))
C_fill='#BDC3CD'
C_s='#243248'
C_l='#B74949'
plt.subplot(221)
plt.plot(S.iloc[:, 3],label=l[3],color=C_s)
plt.plot(L.iloc[:, 3],linewidth=lw,color=C_l)
plt.legend(frameon=False,loc='lower right',handlelength=0,prop={'style':'italic','weight':'bold'})
plt.xlim(time)
plt.axhline(y=Bond,color='black',linestyle='--')
plt.axhline(y=0,color='black',linestyle='-',linewidth=2)
plt.axhline(y=Bond_m,color='black',linestyle=':')
plt.fill_between(pd.date_range(start='2019-9', end='2020-08',freq='M'), -0.3,0.4, color=C_fill, alpha=0.4, linewidth=0)
plt.margins(x=0,y=0)

plt.subplot(222)
plt.plot(S.iloc[:, 0],label=l[0],color=C_s)
plt.plot(L.iloc[:, 0],linewidth=lw,color=C_l)
plt.legend(frameon=False,loc='lower right',handlelength=0,prop={'style':'italic','weight':'bold'})
plt.xlim(time)
plt.axhline(y=Gold,color='black',linestyle='--')
plt.axhline(y=0,color='black',linestyle='-',linewidth=2)
plt.axhline(y=Gold_m,color='black',linestyle=':')
plt.fill_between(pd.date_range(start='2019-9', end='2020-08', freq='M'), -0.30,0.30, color=C_fill, alpha=0.4, linewidth=0)
plt.margins(x=0,y=0)
# plt.yticks(np.arange(-0.45,0.20,0.10))

plt.subplot(223)
plt.plot(S.iloc[:, 1],label=l[1],color=C_s)
plt.plot(L.iloc[:, 1],linewidth=lw,color=C_l)
plt.legend(frameon=False,loc='lower right',handlelength=0,prop={'style':'italic','weight':'bold'})
plt.xlim(time)
plt.axhline(y=WTI,color='black',linestyle='--')
plt.axhline(y=0,color='black',linestyle='-',linewidth=2)
plt.axhline(y=WTI_m,color='black',linestyle=':')
plt.fill_between(pd.date_range(start='2019-9', end='2020-08', freq='M'), -0.3,0.6, color=C_fill, alpha=0.4, linewidth=0)
plt.margins(x=0,y=0)

plt.subplot(224)
plt.plot(S.iloc[:, 2],label=l[2],color=C_s)
plt.plot(L.iloc[:, 2],linewidth=lw,color=C_l)
plt.legend(frameon=False,loc='lower right',handlelength=0,prop={'style':'italic','weight':'bold'})
plt.xlim(time)
plt.axhline(y=BTC,color='black',linestyle='--')
plt.axhline(y=0,color='black',linestyle='-',linewidth=2)
plt.axhline(y=BTC_m,color='black',linestyle=':')
plt.fill_between(pd.date_range(start='2019-9', end='2020-08', freq='M'), -0.3,0.30, color=C_fill, alpha=0.4, linewidth=0)


plt.margins(x=0,y=0)
plt.tight_layout()
plt.savefig(r'C:/Users/徐浩然/Desktop/Figure 2-China/DCC-TPU.png',dpi=800)
plt.show()