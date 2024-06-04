import math
from datetime import datetime

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.interpolate as sci
import scipy.optimize as sco
import seaborn as sns
import tushare as ts

#全局设置-----------------------------------------------------------------------------------------------------------------
plt.rcParams['font.sans-serif'] = ['Palatino Linotype']
plt.rcParams['font.size'] = 12
plt.rcParams['axes.unicode_minus'] = False
# plt.style.use('seaborn-ticks')

pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
plt.subplots(figsize=(10, 8))
# 绿色债券指数-------------------------------------------------------------------------------------------------------------
df1 = pd.read_excel(r'C:\Users\徐浩然\Desktop\930951perf.xlsx', sheet_name='930951perf',index_col=0,parse_dates=[0])
plt.subplot(321)
plt.plot(df1['收盘Close'],color='darkgreen',label='930951')
# plt.savefig(r'C:/Users/徐浩然/Desktop/ggg.png',dpi=400)
plt.legend(frameon=False,loc='upper left')
ret1 = np.log(df1['收盘Close'] / df1['收盘Close'].shift(1))
plt.subplot(322)

plt.plot(ret1,color='darkgreen',label='930951 Return')
# plt.savefig(r'C:/Users/徐浩然/Desktop/gg.png',dpi=400)
plt.legend(frameon=False,loc='upper right')
# 沪深300指数-------------------------------------------------------------------------------------------------------------
df2 = pd.read_excel(r'C:\Users\徐浩然\Desktop\000300perf.xlsx', sheet_name='000300perf',index_col=0,parse_dates=[0])
plt.subplot(323)

plt.plot(df2['收盘Close'],color='darkgreen',label='000300')
# plt.savefig(r'C:/Users/徐浩然/Desktop/300-.png',dpi=400)
plt.legend(frameon=False,loc='upper left')
ret2 = np.log(df2['收盘Close'] / df2['收盘Close'].shift(1))
plt.subplot(324)

plt.plot(ret2,color='darkgreen',label='000300 Return')
plt.legend(frameon=False,loc='upper right')


# plt.savefig(r'C:/Users/徐浩然/Desktop/300.png',dpi=400)
#纯债-----------------------------------------------------------------------
# df3 = pd.read_excel(r'C:\Users\徐浩然\Desktop\930609perf.xlsx', sheet_name='930609perf',index_col=0,parse_dates=[0])
df3 = pd.read_excel(r'C:\Users\徐浩然\Desktop\中证50债券指数 (H11016).xlsx', sheet_name='H11016perf',index_col=0,parse_dates=[0])

plt.subplot(325)

plt.plot(df3['收盘Close'],color='darkgreen',label='H11016')
# plt.savefig(r'C:/Users/徐浩然/Desktop/b-.png',dpi=400)
plt.legend(frameon=False,loc='upper left')
ret3 = np.log(df3['收盘Close'] / df3['收盘Close'].shift(1))
plt.subplot(326)

plt.plot(ret3,color='darkgreen',label='H11016 Return')
plt.legend(frameon=False,loc='upper right')
plt.tight_layout()

plt.savefig(r'C:/Users/徐浩然/Desktop/b.png',dpi=400)
plt.show()