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


df=pd.read_excel(r'C:\Users\徐浩然\Desktop\DCC-data\Hedging Assets\hedging assets.xlsx', sheet_name='All',index_col=0,parse_dates=[0])
log=pd.read_excel(r'C:\Users\徐浩然\Desktop\DCC-data\Hedging Assets\hedging assets.xlsx', sheet_name='All-log',index_col=0,parse_dates=[0])
#
#
plt.subplots(figsize=(8,8))
#
plt.subplot(511)
plt.plot(log.iloc[:, 0],label='CSI 300')

plt.legend(frameon=False,loc='lower right',handlelength=0)


plt.xlim(pd.Timestamp('2012-09-03'), pd.Timestamp('2023-06-02'))
# plt.xlim(pd.Timestamp('2013-11-08'), pd.Timestamp('2023-04-03'))
# plt.axhline(y=WTI,color='black',linestyle='--')
# plt.axhline(y=0,color='black',linestyle='-',linewidth=2)
# plt.fill_between(pd.date_range(start='2019-06', end='2020-09', freq='M'), -0.45,0.30, color='#B3D0AB', alpha=0.4, linewidth=0)
# plt.margins(x=0,y=0)
# # plt.yticks(np.arange(-0.45,0.20,0.10))
#
plt.subplot(512)
plt.plot(log.iloc[:, 3],label='Bond')

plt.xlim(pd.Timestamp('2012-09-03'), pd.Timestamp('2023-06-02'))

plt.legend(frameon=False,loc='lower right',handlelength=0)


# plt.xlim(pd.Timestamp('2013-11-08'), pd.Timestamp('2023-04-03'))
# plt.axhline(y=BTC,color='black',linestyle='--')
# plt.axhline(y=0,color='black',linestyle='-',linewidth=2)
# plt.fill_between(pd.date_range(start='2019-06', end='2020-09', freq='M'), -0.45,0.30, color='#B3D0AB', alpha=0.4, linewidth=0)
# plt.margins(x=0,y=0)
#
plt.subplot(513)
plt.plot(log.iloc[:, 4],label='Gold')

plt.xlim(pd.Timestamp('2012-09-03'), pd.Timestamp('2023-06-02'))

plt.legend(frameon=False,loc='lower right',handlelength=0)



# plt.xlim(pd.Timestamp('2013-11-08'), pd.Timestamp('2023-04-03'))
# plt.axhline(y=Bond,color='black',linestyle='--')
# plt.axhline(y=0,color='black',linestyle='-',linewidth=2)
# plt.fill_between(pd.date_range(start='2019-06', end='2020-09', freq='M'), -0.45,0.20, color='#B3D0AB', alpha=0.4, linewidth=0)
# plt.margins(x=0,y=0)
#
plt.subplot(514)
plt.plot(log.iloc[:, 5],label='WTI')

plt.xlim(pd.Timestamp('2012-09-03'), pd.Timestamp('2023-06-02'))

plt.legend(frameon=False,loc='lower right',handlelength=0)


# plt.xlim(pd.Timestamp('2013-11-08'), pd.Timestamp('2023-04-03'))
# plt.axhline(y=Gold,color='black',linestyle='--')
# plt.axhline(y=0,color='black',linestyle='-',linewidth=2)
# plt.text(0.5,0.5,'hh')
# plt.fill_between(pd.date_range(start='2019-06', end='2020-09', freq='M'), -0.45,0.30, color='#B3D0AB', alpha=0.4, linewidth=0)
# plt.margins(x=0,y=0)
#
#
plt.subplot(515)
plt.plot(log.iloc[:, 6],label='Bitcoin')
plt.xlim(pd.Timestamp('2012-09-03'), pd.Timestamp('2023-06-02'))
plt.legend(frameon=False,loc='lower right',handlelength=0)

# plt.xlim(pd.Timestamp('2013-11-08'), pd.Timestamp('2023-04-03'))
# plt.axhline(y=Gold,color='black',linestyle='--')
# plt.axhline(y=0,color='black',linestyle='-',linewidth=2)
# plt.text(0.5,0.5,'hh')
# plt.fill_between(pd.date_range(start='2019-06', end='2020-09', freq='M'), -0.45,0.30, color='#B3D0AB', alpha=0.4, linewidth=0)
# plt.margins(x=0,y=0)


plt.tight_layout()
#


plt.savefig(r'C:/Users/徐浩然/Desktop/log.png',dpi=400)


print(log)
plt.show()
