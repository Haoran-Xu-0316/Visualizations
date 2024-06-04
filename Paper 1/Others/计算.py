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

Bond=pd.read_excel(r'C:\Users\徐浩然\Desktop\DCC-data\Portfolio return.xlsx', sheet_name='Bond',index_col=0,parse_dates=[0])
Oil=pd.read_excel(r'C:\Users\徐浩然\Desktop\DCC-data\Portfolio return.xlsx', sheet_name='Oil',index_col=0,parse_dates=[0])
BTC=pd.read_excel(r'C:\Users\徐浩然\Desktop\DCC-data\Portfolio return.xlsx', sheet_name='BTC',index_col=0,parse_dates=[0])
Gold=pd.read_excel(r'C:\Users\徐浩然\Desktop\DCC-data\Portfolio return.xlsx', sheet_name='Gold',index_col=0,parse_dates=[0])
stock=pd.read_excel(r'C:\Users\徐浩然\Desktop\DCC-data\Hedging Assets\hedging assets.xlsx', sheet_name='All-log',index_col=0,parse_dates=[0])
stock=stock['CSI 300']

sVaR = np.percentile(stock, (1 - 0.95) * 100)
sES = stock[stock <= sVaR].mean()


def VaR_Daily(a):
    VaR=np.percentile(a,(1-0.95)*100)
    VaR=(sVaR-VaR)/sVaR
    return VaR
def ES_Daily(a):
    VaR=np.percentile(a,(1-0.95)*100)
    ES=a[a<=VaR].mean()
    ES = (sES - ES) / sES
    return ES
bondvar=[]
goldvar=[]
btcvar=[]
oilvar=[]
bondes=[]
goldes=[]
oiles=[]
btces=[]



for i in range(5):
    bondvar.append(VaR_Daily(Bond.iloc[:, i]))
for i in range(5):
    bondes.append(ES_Daily(Bond.iloc[:, i]))

for i in range(5):
    goldvar.append(VaR_Daily(Gold.iloc[:, i]))
for i in range(5):
    goldes.append(ES_Daily(Gold.iloc[:, i]))

for i in range(5):
    oilvar.append(VaR_Daily(Oil.iloc[:, i]))
for i in range(5):
    oiles.append(ES_Daily(Oil.iloc[:, i]))

for i in range(5):
    btcvar.append(VaR_Daily(BTC.iloc[:, i]))
for i in range(5):
    btces.append(ES_Daily(BTC.iloc[:, i]))

print(bondvar)
print(bondes)

print(goldvar)
print(goldes)

print(oilvar)
print(oiles)

print(btcvar)
print(btces)