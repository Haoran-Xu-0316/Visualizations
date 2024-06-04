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

l=['CSI 300 - Gold','CSI 300 - WTI','CSI 300 - Bitcoin','CSI 300 - Bond','Gold - WTI','Gold - Bitcoin','Gold - Bond','WTI - Bitcoin','WTI - Bond','Bitcoin - Bond']

Bond=pd.read_excel(r'C:\Users\徐浩然\Desktop\DCC-data\OW.xlsx', sheet_name='Bond',index_col=0,parse_dates=[0])
Oil=pd.read_excel(r'C:\Users\徐浩然\Desktop\DCC-data\OW.xlsx', sheet_name='Oil',index_col=0,parse_dates=[0])
BTC=pd.read_excel(r'C:\Users\徐浩然\Desktop\DCC-data\OW.xlsx', sheet_name='BTC',index_col=0,parse_dates=[0])
Gold=pd.read_excel(r'C:\Users\徐浩然\Desktop\DCC-data\OW.xlsx', sheet_name='Gold',index_col=0,parse_dates=[0])

HA=pd.read_excel(r'C:\Users\徐浩然\Desktop\DCC-data\Hedging Assets\hedging assets.xlsx', sheet_name='All-log',index_col=0,parse_dates=[0])
#
#
plt.subplots(figsize=(12,8))
#
plt.subplot(221)
plt.plot(Bond.iloc[:, 0],label='TPU')
plt.plot(Bond.iloc[:, 1],label='EMU')
plt.plot(Bond.iloc[:, 2],label='EPU')
plt.plot(Bond.iloc[:, 3],label='GPR')
plt.plot(Bond.iloc[:, 4],label='CPU')
sl=plt.legend(labels=['Bond'],frameon=False,loc='lower left',handlelength=0)
plt.legend(frameon=False,loc='lower right',labelspacing=0.15)
plt.gca().add_artist(sl)
plt.xlim(pd.Timestamp('2013-11-08'), pd.Timestamp('2023-03-27'))
# plt.axhline(y=WTI,color='black',linestyle='--')
# plt.axhline(y=0,color='black',linestyle='-',linewidth=2)
# plt.fill_between(pd.date_range(start='2019-06', end='2020-09', freq='M'), -0.45,0.30, color='#B3D0AB', alpha=0.4, linewidth=0)
# plt.margins(x=0,y=0)
# # plt.yticks(np.arange(-0.45,0.20,0.10))
#
plt.subplot(222)
plt.plot(Gold.iloc[:, 0],label='TPU')
plt.plot(Gold.iloc[:, 1],label='EMU')
plt.plot(Gold.iloc[:, 2],label='EPU')
plt.plot(Gold.iloc[:, 3],label='GPR')
plt.plot(Gold.iloc[:, 4],label='CPU')
sl=plt.legend(labels=['Gold'],frameon=False,loc='lower left',handlelength=0)
plt.legend(frameon=False,loc='lower right',labelspacing=0.15)
plt.gca().add_artist(sl)
plt.xlim(pd.Timestamp('2013-11-08'), pd.Timestamp('2023-03-27'))
# plt.axhline(y=BTC,color='black',linestyle='--')
# plt.axhline(y=0,color='black',linestyle='-',linewidth=2)
# plt.fill_between(pd.date_range(start='2019-06', end='2020-09', freq='M'), -0.45,0.30, color='#B3D0AB', alpha=0.4, linewidth=0)
# plt.margins(x=0,y=0)
#
plt.subplot(223)
plt.plot(Oil.iloc[:, 0],label='TPU')
plt.plot(Oil.iloc[:, 1],label='EMU')
plt.plot(Oil.iloc[:, 2],label='EPU')
plt.plot(Oil.iloc[:, 3],label='GPR')
plt.plot(Oil.iloc[:, 4],label='CPU')
plt.xlim(pd.Timestamp('2013-11-08'), pd.Timestamp('2023-03-27'))
sl=plt.legend(labels=['Oil'],frameon=False,loc='lower left',handlelength=0)
plt.legend(frameon=False,loc='lower right',labelspacing=0.15)
plt.gca().add_artist(sl)

#23/29/35

# plt.axes([0.08, 0.14, 0.22, 0.2])
# plt.plot(Oil.iloc[:, 35],label='TPU')
# plt.plot(Oil.iloc[:, 36],label='EMU')
# plt.plot(Oil.iloc[:, 37],label='EPU')
# plt.plot(Oil.iloc[:, 38],label='GPR')
# plt.plot(Oil.iloc[:, 39],label='CPU')
# plt.xlim(pd.Timestamp('2013-11-08'), pd.Timestamp('2023-03-27'))
# plt.tick_params(labelsize=6)     #调整坐标轴数字大小
# plt.legend()                 #plt.legend( prop = {'size':17})   图例字体大小
# plt.xlim(pd.Timestamp('2013-11-08'), pd.Timestamp('2023-04-03'))
# plt.axhline(y=Bond,color='black',linestyle='--')
# plt.axhline(y=0,color='black',linestyle='-',linewidth=2)
# plt.fill_between(pd.date_range(start='2019-06', end='2020-09', freq='M'), -0.45,0.20, color='#B3D0AB', alpha=0.4, linewidth=0)
# plt.margins(x=0,y=0)
#
plt.subplot(224)
plt.plot(BTC.iloc[:, 0],label='TPU')
plt.plot(BTC.iloc[:, 1],label='EMU')
plt.plot(BTC.iloc[:, 2],label='EPU')
plt.plot(BTC.iloc[:, 3],label='GPR')
plt.plot(BTC.iloc[:, 4],label='CPU')
plt.xlim(pd.Timestamp('2013-11-08'), pd.Timestamp('2023-03-27'))
sl=plt.legend(labels=['Bitcoin'],frameon=False,loc='lower left',handlelength=0)
plt.legend(frameon=False,loc='lower right',labelspacing=0.15)
plt.gca().add_artist(sl)
# plt.xlim(pd.Timestamp('2013-11-08'), pd.Timestamp('2023-04-03'))
# plt.axhline(y=Gold,color='black',linestyle='--')
# plt.axhline(y=0,color='black',linestyle='-',linewidth=2)
# plt.text(0.5,0.5,'hh')
# plt.fill_between(pd.date_range(start='2019-06', end='2020-09', freq='M'), -0.45,0.30, color='#B3D0AB', alpha=0.4, linewidth=0)
# plt.margins(x=0,y=0)
#
#
#
plt.tight_layout()
#


plt.savefig(r'C:/Users/徐浩然/Desktop/OW.png',dpi=400)

print(Bond.iloc[:, 23])
plt.show()
