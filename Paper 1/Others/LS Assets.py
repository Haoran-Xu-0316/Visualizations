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
plt.rcParams['font.size'] = 10
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['lines.linewidth'] = 0.5
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)

l=['CSI 300 - Gold','CSI 300 - WTI','CSI 300 - Bitcoin','CSI 300 - Bond','Gold - WTI','Gold - Bitcoin','Gold - Bond','WTI - Bitcoin','WTI - Bond','Bitcoin - Bond']

S1=pd.read_excel(r'C:\Users\徐浩然\Desktop\DCC-data\Varanice&Covariance-CPU.xlsx', sheet_name='Short-Cor',index_col=0,parse_dates=[0])
S2=pd.read_excel(r'C:\Users\徐浩然\Desktop\DCC-data\Varanice&Covariance-EPU.xlsx', sheet_name='Short-Cor',index_col=0,parse_dates=[0])
S3=pd.read_excel(r'C:\Users\徐浩然\Desktop\DCC-data\Varanice&Covariance-EMU.xlsx', sheet_name='Short-Cor',index_col=0,parse_dates=[0])
S4=pd.read_excel(r'C:\Users\徐浩然\Desktop\DCC-data\Varanice&Covariance-TPU.xlsx', sheet_name='Short-Cor',index_col=0,parse_dates=[0])
S5=pd.read_excel(r'C:\Users\徐浩然\Desktop\DCC-data\Varanice&Covariance-GPR.xlsx', sheet_name='Short-Cor',index_col=0,parse_dates=[0])

L1=pd.read_excel(r'C:\Users\徐浩然\Desktop\DCC-data\Varanice&Covariance-CPU.xlsx', sheet_name='Long-Cor',index_col=0,parse_dates=[0])
L2=pd.read_excel(r'C:\Users\徐浩然\Desktop\DCC-data\Varanice&Covariance-EPU.xlsx', sheet_name='Long-Cor',index_col=0,parse_dates=[0])
L3=pd.read_excel(r'C:\Users\徐浩然\Desktop\DCC-data\Varanice&Covariance-EMU.xlsx', sheet_name='Long-Cor',index_col=0,parse_dates=[0])
L4=pd.read_excel(r'C:\Users\徐浩然\Desktop\DCC-data\Varanice&Covariance-TPU.xlsx', sheet_name='Long-Cor',index_col=0,parse_dates=[0])
L5=pd.read_excel(r'C:\Users\徐浩然\Desktop\DCC-data\Varanice&Covariance-GPR.xlsx', sheet_name='Long-Cor',index_col=0,parse_dates=[0])

plt.subplots(figsize=(12,4))
n=5


plt.subplot(121)

plt.plot(S1.iloc[:, n],label='CPU')
plt.plot(S2.iloc[:, n],label='EPU')
plt.plot(S3.iloc[:, n],label='EMU')
plt.plot(S4.iloc[:, n],label='TPU')
plt.plot(S5.iloc[:, n],label='GPR')

plt.legend(frameon=False)

plt.subplot(122)

plt.plot(L1.iloc[:, n],label='CPU')
plt.plot(L2.iloc[:, n],label='EPU')
plt.plot(L3.iloc[:, n],label='EMU')
plt.plot(L4.iloc[:, n],label='TPU')
plt.plot(L5.iloc[:, n],label='GPR')

plt.legend(frameon=False)
plt.tight_layout()

plt.tight_layout()


# plt.savefig(r'C:/Users/徐浩然/Desktop/DCC-stock.png',dpi=400)
# plt.savefig(r'C:/Users/徐浩然/Desktop/DCC-gold.png',dpi=400)
# plt.savefig(r'C:/Users/徐浩然/Desktop/DCC-bitcoin.png',dpi=400)
# plt.savefig(r'C:/Users/徐浩然/Desktop/DCC-oil.png',dpi=400)
# plt.savefig(r'C:/Users/徐浩然/Desktop/DCC-bond.png',dpi=400)


plt.show()
