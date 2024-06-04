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

plt.rcParams["font.weight"] = "bold"

plt.rcParams['font.size'] = 14
plt.rcParams['axes.unicode_minus'] = False
# plt.style.use('seaborn-ticks')
# plt.rcParams['lines.linewidth'] = 1

pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)

df=pd.read_excel(r'C:\Users\徐浩然\Desktop\股债指数.xlsx', sheet_name='差分',index_col=0,parse_dates=[0])
dff=pd.read_excel(r'C:\Users\徐浩然\Desktop\股债指数.xlsx', sheet_name='原始',index_col=0,parse_dates=[0])
C='darkslategrey'
# ----------------------------------------------------------------------------------------------------------------------
plt.subplots(figsize=(14, 8))
plt.subplot(311)
df1 = df['SSE Green Bond Index']
plt.plot(df1,color=C,label='SHGBI')
plt.legend(frameon=False,loc='upper right')
plt.xlim(pd.Timestamp('2017-01-01'), pd.Timestamp('2023-01-01'))

plt.subplot(312)

df2 = df['SSE Conglomerates Index']
plt.plot(df2,color=C,label='SHCI')
plt.legend(frameon=False,loc='upper right')
plt.xlim(pd.Timestamp('2017-01-01'), pd.Timestamp('2023-01-01'))

plt.subplot(313)

df3 = df['SSE Government Bond Index']
plt.plot(df3,color=C,label='SHBI')
plt.legend(frameon=False,loc='upper right')
plt.xlim(pd.Timestamp('2017-01-01'), pd.Timestamp('2023-01-01'))

plt.tight_layout()
plt.savefig(r'C:/Users/徐浩然/Desktop/a.png',dpi=400)
# plt.show()
# ----------------------------------------------------------------------------------------------------------------------
plt.subplots(figsize=(14, 8))
plt.subplot(311)
dff1 = dff['SSE Green Bond Index']
plt.plot(dff1,color=C,label='SHGCI')
plt.legend(frameon=False,loc='upper left')
plt.xlim(pd.Timestamp('2017-01-01'), pd.Timestamp('2023-01-01'))


plt.subplot(312)

dff2 = dff['SSE Conglomerates Index']
plt.plot(dff2,color=C,label='SHCI')
plt.legend(frameon=False,loc='upper left')
plt.xlim(pd.Timestamp('2017-01-01'), pd.Timestamp('2023-01-01'))


plt.subplot(313)
dff3 = dff['SSE Government Bond Index']
plt.plot(dff3,color=C,label='SHBI')
plt.legend(frameon=False,loc='upper left')
plt.xlim(pd.Timestamp('2017-01-01'), pd.Timestamp('2023-01-01'))

plt.tight_layout()
plt.savefig(r'C:/Users/徐浩然/Desktop/b.png',dpi=400)
plt.show()