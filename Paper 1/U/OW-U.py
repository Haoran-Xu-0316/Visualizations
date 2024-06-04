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

time=pd.Timestamp('2014-07-31'), pd.Timestamp('2023-07-28')
Bond=pd.read_excel(r'C:\Users\徐浩然\Desktop\DCC-data-China\OW.xlsx', sheet_name='Bond',index_col=0,parse_dates=[0])
Oil=pd.read_excel(r'C:\Users\徐浩然\Desktop\DCC-data-China\OW.xlsx', sheet_name='Oil',index_col=0,parse_dates=[0])
BTC=pd.read_excel(r'C:\Users\徐浩然\Desktop\DCC-data-China\OW.xlsx', sheet_name='BTC',index_col=0,parse_dates=[0])
Gold=pd.read_excel(r'C:\Users\徐浩然\Desktop\DCC-data-China\OW.xlsx', sheet_name='Gold',index_col=0,parse_dates=[0])


Bonds=pd.read_excel(r'C:\Users\徐浩然\Desktop\DCC-data-US\OW.xlsx', sheet_name='Bond',index_col=0,parse_dates=[0])
Oils=pd.read_excel(r'C:\Users\徐浩然\Desktop\DCC-data-US\OW.xlsx', sheet_name='Oil',index_col=0,parse_dates=[0])
BTCs=pd.read_excel(r'C:\Users\徐浩然\Desktop\DCC-data-US\OW.xlsx', sheet_name='BTC',index_col=0,parse_dates=[0])
Golds=pd.read_excel(r'C:\Users\徐浩然\Desktop\DCC-data-US\OW.xlsx', sheet_name='Gold',index_col=0,parse_dates=[0])

HA=pd.read_excel(r'C:\Users\徐浩然\Desktop\DCC-data-China\Hedging Assets\hedging assets.xlsx', sheet_name='All-log',index_col=0,parse_dates=[0])
C=['#FFDDB7','#9C3434','dimgrey','#E3A085','#334666']
Cbs='darkgrey'
bls='--'
#
plt.subplots(figsize=(18,9))
#
plt.subplot(241)
plt.plot(Bond.iloc[:, 5],label='BL',color=Cbs,ls=bls)
plt.plot(Bond.iloc[:, 1],label='EMV',color=C[0])
plt.plot(Bond.iloc[:, 3],label='GPR',color=C[3])
plt.plot(Bond.iloc[:, 4],label='CPU',color=C[2])
plt.plot(Bond.iloc[:, 2],label='EPU',color=C[1])
plt.plot(Bond.iloc[:, 0],label='TPU',color=C[4])
sl=plt.legend(labels=['CSI 300 - GBond'],frameon=False,loc='lower right',handlelength=0,prop={'style':'italic','weight':'bold'})
plt.legend(frameon=False,loc='lower left',labelspacing=0.15)
plt.gca().add_artist(sl)
plt.xlim(time)
plt.yticks([0.6, 0.7, 0.8, 0.9, 1.0])
# plt.axhline(y=0,color='black',linestyle='-',linewidth=2)

plt.subplot(245)
plt.plot(Bonds.iloc[:, 5],label='BL',color=Cbs,ls=bls)
plt.plot(Bonds.iloc[:, 1],label='EMV',color=C[0])
plt.plot(Bonds.iloc[:, 3],label='GPR',color=C[3])
plt.plot(Bonds.iloc[:, 4],label='CPU',color=C[2])
plt.plot(Bonds.iloc[:, 2],label='EPU',color=C[1])
plt.plot(Bonds.iloc[:, 0],label='TPU',color=C[4])
sl=plt.legend(labels=['S&P 500 - GBond'],frameon=False,loc='lower right',handlelength=0,prop={'style':'italic','weight':'bold'})
plt.legend(frameon=False,loc='lower left',labelspacing=0.15)
plt.gca().add_artist(sl)
plt.xlim(time)
# plt.axhline(y=0,color='black',linestyle='-',linewidth=2)







#
plt.subplot(242)
plt.plot(Gold.iloc[:, 5],label='BL',color=Cbs,ls=bls)
plt.plot(Gold.iloc[:, 1],label='EMV',color=C[0])
plt.plot(Gold.iloc[:, 3],label='GPR',color=C[3])
plt.plot(Gold.iloc[:, 4],label='CPU',color=C[2])
plt.plot(Gold.iloc[:, 2],label='EPU',color=C[1])
plt.plot(Gold.iloc[:, 0],label='TPU',color=C[4])
sl=plt.legend(labels=['CSI 300 - Gold'],frameon=False,loc='upper right',handlelength=0,prop={'style':'italic','weight':'bold'})
plt.legend(frameon=False,loc='lower left',labelspacing=0.15)
plt.gca().add_artist(sl)
plt.xlim(time)
# plt.axhline(y=0,color='black',linestyle='-',linewidth=2)

plt.subplot(246)
plt.plot(Golds.iloc[:, 5],label='BL',color=Cbs,ls=bls)
plt.plot(Golds.iloc[:, 1],label='EMV',color=C[0])
plt.plot(Golds.iloc[:, 3],label='GPR',color=C[3])
plt.plot(Golds.iloc[:, 4],label='CPU',color=C[2])
plt.plot(Golds.iloc[:, 2],label='EPU',color=C[1])
plt.plot(Golds.iloc[:, 0],label='TPU',color=C[4])
sl=plt.legend(labels=['S&P 500 - Gold'],frameon=False,loc='lower left',handlelength=0,prop={'style':'italic','weight':'bold'})
plt.legend(frameon=False,loc='upper left',labelspacing=0.15)
plt.gca().add_artist(sl)
plt.xlim(time)
# plt.axhline(y=0,color='black',linestyle='-',linewidth=2)








#
plt.subplot(243)
plt.plot(Oil.iloc[:, 5],label='BL',color=Cbs,ls=bls)
plt.plot(Oil.iloc[:, 1],label='EMV',color=C[0])
plt.plot(Oil.iloc[:, 3],label='GPR',color=C[3])
plt.plot(Oil.iloc[:, 4],label='CPU',color=C[2])
plt.plot(Oil.iloc[:, 2],label='EPU',color=C[1])
plt.plot(Oil.iloc[:, 0],label='TPU',color=C[4])
sl=plt.legend(labels=['CSI 300 - Oil'],frameon=False,loc='upper left',handlelength=0,prop={'style':'italic','weight':'bold'})
plt.legend(frameon=False,loc='upper right',labelspacing=0.15)
plt.gca().add_artist(sl)
plt.xlim(time)
# plt.axhline(y=0,color='black',linestyle='-',linewidth=2)

plt.subplot(247)
plt.plot(Oils.iloc[:, 5],label='BL',color=Cbs,ls=bls)
plt.plot(Oils.iloc[:, 1],label='EMV',color=C[0])
plt.plot(Oils.iloc[:, 3],label='GPR',color=C[3])
plt.plot(Oils.iloc[:, 4],label='CPU',color=C[2])
plt.plot(Oils.iloc[:, 2],label='EPU',color=C[1])
plt.plot(Oils.iloc[:, 0],label='TPU',color=C[4])
sl=plt.legend(labels=['S&P 500 - Oil'],frameon=False,loc='upper right',handlelength=0,prop={'style':'italic','weight':'bold'})
plt.legend(frameon=False,loc='upper left',labelspacing=0.15)
plt.gca().add_artist(sl)
plt.xlim(time)
# plt.axhline(y=0,color='black',linestyle='-',linewidth=2)








#
plt.subplot(244)
plt.plot(BTC.iloc[:, 5],label='BL',color=Cbs,ls=bls)
plt.plot(BTC.iloc[:, 1],label='EMV',color=C[0])
plt.plot(BTC.iloc[:, 3],label='GPR',color=C[3])
plt.plot(BTC.iloc[:, 4],label='CPU',color=C[2])
plt.plot(BTC.iloc[:, 2],label='EPU',color=C[1])
plt.plot(BTC.iloc[:, 0],label='TPU',color=C[4])
sl=plt.legend(labels=['CSI 300 - Bitcoin'],frameon=False,loc='upper left',handlelength=0,prop={'style':'italic','weight':'bold'})
plt.legend(frameon=False,loc='upper right',labelspacing=0.15)
plt.gca().add_artist(sl)
plt.xlim(time)
# plt.axhline(y=0,color='black',linestyle='-',linewidth=2)

plt.subplot(248)
plt.plot(BTCs.iloc[:, 5],label='BL',color=Cbs,ls=bls)
plt.plot(BTCs.iloc[:, 1],label='EMV',color=C[0])
plt.plot(BTCs.iloc[:, 3],label='GPR',color=C[3])
plt.plot(BTCs.iloc[:, 4],label='CPU',color=C[2])
plt.plot(BTCs.iloc[:, 2],label='EPU',color=C[1])
plt.plot(BTCs.iloc[:, 0],label='TPU',color=C[4])
sl=plt.legend(labels=['S&P 500 - Bitcoin'],frameon=False,loc='upper left',handlelength=0,prop={'style':'italic','weight':'bold'})
plt.legend(frameon=False,loc='upper right',labelspacing=0.15)
plt.gca().add_artist(sl)
plt.xlim(time)
# plt.axhline(y=0,color='black',linestyle='-',linewidth=2)


#
plt.tight_layout()
plt.savefig(r'C:/Users/徐浩然/Desktop/Figure 2-U/OW.pdf',dpi=2000)
plt.show()
