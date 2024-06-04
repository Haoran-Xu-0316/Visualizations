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
plt.rcParams['axes.unicode_minus'] = True
plt.rcParams['lines.linewidth'] = 1
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)

l=['CSI 300 - Gold','CSI 300 - Oil','CSI 300 - Bitcoin','CSI 300 - GBond','Gold - Oil','Gold - Bitcoin','Gold - Bond','WTI - Bitcoin','WTI - Bond','Bitcoin - Bond']
S=pd.read_excel(r'C:\Users\徐浩然\Desktop\DCC-data-China\Varanice&Covariance-EPU.xlsx', sheet_name='Short-Cor',index_col=0,parse_dates=[0])
L=pd.read_excel(r'C:\Users\徐浩然\Desktop\DCC-data-China\Varanice&Covariance-EPU.xlsx', sheet_name='Long-Cor',index_col=0,parse_dates=[0])

ls=['S&P 500 - Gold','S&P 500 - Oil','S&P 500 - Bitcoin','S&P 500 - GBond','Gold - Oil','Gold - Bitcoin','Gold - Bond','WTI - Bitcoin','WTI - Bond','Bitcoin - Bond']
Ss=pd.read_excel(r'C:\Users\徐浩然\Desktop\DCC-data-US\Varanice&Covariance-EPU.xlsx', sheet_name='Short-Cor',index_col=0,parse_dates=[0])
Ls=pd.read_excel(r'C:\Users\徐浩然\Desktop\DCC-data-US\Varanice&Covariance-EPU.xlsx', sheet_name='Long-Cor',index_col=0,parse_dates=[0])

b=pd.read_excel(r'C:\Users\徐浩然\Desktop\DCC-data-China\Varanice&Covariance-Baseline.xlsx', sheet_name='Short-Cor',index_col=0,parse_dates=[0])
bs=pd.read_excel(r'C:\Users\徐浩然\Desktop\DCC-data-US\Varanice&Covariance-Baseline.xlsx', sheet_name='Short-Cor',index_col=0,parse_dates=[0])

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



Ms=Ss.mean()
Gold_ms=Ms[0]
WTI_ms=Ms[1]
BTC_ms=Ms[2]
Bond_ms=Ms[3]
Bonds = corrmatrix.iloc[1][2]
Golds = corrmatrix.iloc[1][3]
WTIs = corrmatrix.iloc[1][4]
BTCs = corrmatrix.iloc[1][5]

lw=1.5
plt.subplots(figsize=(18,9))
C_fill='#BDC3CD'
C_s='#243248'
C_l='#B74949'
Cbs='darkgrey'
bls='--'

plt.subplot(241)
plt.plot(b.iloc[:, 3],color=Cbs,ls=bls)
plt.plot(S.iloc[:, 3],label=l[3],color=C_s)
plt.plot(L.iloc[:, 3],linewidth=lw,color=C_l)

plt.legend(frameon=False,loc='lower right',handlelength=0,prop={'style':'italic','weight':'bold'})
legend_handle = plt.gca().get_legend().legendHandles[0]
legend_handle.set_visible(False)
plt.xlim(time)
plt.axhline(y=Bond,color='black',linestyle='--')
plt.axhline(y=0,color='black',linestyle='-',linewidth=1.5)
plt.axhline(y=Bond_m,color='black',linestyle=':')
plt.fill_between(pd.date_range(start='2019-9', end='2020-08', freq='M'), -0.3,0.4, color=C_fill, alpha=1, linewidth=0)
plt.margins(x=0,y=0)

plt.subplot(245)
plt.plot(bs.iloc[:, 3],color=Cbs,ls=bls)
plt.plot(Ss.iloc[:, 3],label=ls[3],color=C_s)
plt.plot(Ls.iloc[:, 3],linewidth=lw,color=C_l)

plt.legend(frameon=False,loc='lower right',handlelength=0,prop={'style':'italic','weight':'bold'})
legend_handle = plt.gca().get_legend().legendHandles[0]
legend_handle.set_visible(False)
plt.xlim(time)
plt.axhline(y=Bonds,color='black',linestyle='--')
plt.axhline(y=0,color='black',linestyle='-',linewidth=1.5)
plt.axhline(y=Bond_ms,color='black',linestyle=':')
plt.fill_between(pd.date_range(start='2019-9', end='2020-08', freq='M'), -0.6,0.5, color=C_fill, alpha=1, linewidth=0)
plt.margins(x=0,y=0)






plt.subplot(242)
plt.plot(b.iloc[:, 0],color=Cbs,ls=bls)
plt.plot(S.iloc[:, 0],label=l[0],color=C_s)
plt.plot(L.iloc[:, 0],linewidth=lw,color=C_l)

plt.legend(frameon=False,loc='lower right',handlelength=0,prop={'style':'italic','weight':'bold'})
legend_handle = plt.gca().get_legend().legendHandles[0]
legend_handle.set_visible(False)
plt.xlim(time)
plt.axhline(y=Gold,color='black',linestyle='--')
plt.axhline(y=0,color='black',linestyle='-',linewidth=1.5)
plt.axhline(y=Gold_m,color='black',linestyle=':')
plt.fill_between(pd.date_range(start='2019-9', end='2020-08', freq='M'), -0.30,0.30, color=C_fill, alpha=1, linewidth=0)
plt.margins(x=0,y=0)

plt.subplot(246)
plt.plot(bs.iloc[:, 0],color=Cbs,ls=bls)
plt.plot(Ss.iloc[:, 0],label=ls[0],color=C_s)
plt.plot(Ls.iloc[:, 0],linewidth=lw,color=C_l)

plt.legend(frameon=False,loc='lower right',handlelength=0,prop={'style':'italic','weight':'bold'})
legend_handle = plt.gca().get_legend().legendHandles[0]
legend_handle.set_visible(False)
plt.xlim(time)
plt.axhline(y=Golds,color='black',linestyle='--')
plt.axhline(y=0,color='black',linestyle='-',linewidth=1.5)
plt.axhline(y=Gold_ms,color='black',linestyle=':')
plt.fill_between(pd.date_range(start='2019-9', end='2020-08', freq='M'), -0.60,0.40, color=C_fill, alpha=1, linewidth=0)
plt.margins(x=0,y=0)






plt.subplot(243)
plt.plot(b.iloc[:, 1],color=Cbs,ls=bls)
plt.plot(S.iloc[:, 1],label=l[1],color=C_s)
plt.plot(L.iloc[:, 1],linewidth=lw,color=C_l)

plt.legend(frameon=False,loc='lower right',handlelength=0,prop={'style':'italic','weight':'bold'})
legend_handle = plt.gca().get_legend().legendHandles[0]
legend_handle.set_visible(False)
plt.xlim(time)
plt.axhline(y=WTI,color='black',linestyle='--')
plt.axhline(y=0,color='black',linestyle='-',linewidth=1.5)
plt.axhline(y=WTI_m,color='black',linestyle=':')
plt.fill_between(pd.date_range(start='2019-9', end='2020-08', freq='M'), -0.3,0.60, color=C_fill, alpha=1, linewidth=0)
plt.margins(x=0,y=0)

plt.subplot(247)
plt.plot(bs.iloc[:, 1],color=Cbs,ls=bls)
plt.plot(Ss.iloc[:, 1],label=ls[1],color=C_s)
plt.plot(Ls.iloc[:, 1],linewidth=lw,color=C_l)

plt.legend(frameon=False,loc='lower right',handlelength=0,prop={'style':'italic','weight':'bold'})
legend_handle = plt.gca().get_legend().legendHandles[0]
legend_handle.set_visible(False)
plt.xlim(time)
plt.axhline(y=WTIs,color='black',linestyle='--')
plt.axhline(y=0,color='black',linestyle='-',linewidth=1.5)
plt.axhline(y=WTI_ms,color='black',linestyle=':')
plt.fill_between(pd.date_range(start='2019-9', end='2020-08', freq='M'), -0.1,0.60, color=C_fill, alpha=1, linewidth=0)
plt.margins(x=0,y=0)







plt.subplot(244)
plt.plot(b.iloc[:, 2],color=Cbs,ls=bls)
plt.plot(S.iloc[:, 2],label=l[2],color=C_s)
plt.plot(L.iloc[:, 2],linewidth=lw,color=C_l)

plt.legend(frameon=False,loc='lower right',handlelength=0,prop={'style':'italic','weight':'bold'})
legend_handle = plt.gca().get_legend().legendHandles[0]
legend_handle.set_visible(False)
plt.xlim(time)
plt.axhline(y=BTC,color='black',linestyle='--')
plt.axhline(y=0,color='black',linestyle='-',linewidth=1.5)
plt.axhline(y=BTC_m,color='black',linestyle=':')
plt.fill_between(pd.date_range(start='2019-9', end='2020-08', freq='M'), -0.3,0.30, color=C_fill, alpha=1, linewidth=0)
plt.margins(x=0,y=0)

plt.subplot(248)
plt.plot(bs.iloc[:, 2],color=Cbs,ls=bls)
plt.plot(Ss.iloc[:, 2],label=ls[2],color=C_s)
plt.plot(Ls.iloc[:, 2],linewidth=lw,color=C_l)

plt.legend(frameon=False,loc='lower right',handlelength=0,prop={'style':'italic','weight':'bold'})
legend_handle = plt.gca().get_legend().legendHandles[0]
legend_handle.set_visible(False)
plt.xlim(time)
plt.axhline(y=BTCs,color='black',linestyle='--')
plt.axhline(y=0,color='black',linestyle='-',linewidth=1.5)
plt.axhline(y=BTC_ms,color='black',linestyle=':')
plt.fill_between(pd.date_range(start='2019-9', end='2020-08', freq='M'), -0.4,0.60, color=C_fill, alpha=1, linewidth=0)
plt.margins(x=0,y=0)


plt.tight_layout()
plt.savefig(r'C:/Users/徐浩然/Desktop/Figure 2-U/DCC-EPU.pdf',dpi=2000)
plt.show()
