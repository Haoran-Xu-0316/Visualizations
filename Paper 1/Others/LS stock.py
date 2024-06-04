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
plt.rcParams['lines.linewidth'] = 1
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)

l=['CSI 300 - Gold','CSI 300 - WTI','CSI 300 - Bitcoin','CSI 300 - Bond','Gold - WTI','Gold - Bitcoin','Gold - Bond','WTI - Bitcoin','WTI - Bond','Bitcoin - Bond']

S1=pd.read_excel(r'C:\Users\徐浩然\Desktop\DCC-data\DCC-CPU.xlsx', sheet_name='Short-Cor',index_col=0,parse_dates=[0])
S2=pd.read_excel(r'C:\Users\徐浩然\Desktop\DCC-data\DCC-EPU.xlsx', sheet_name='Short-Cor',index_col=0,parse_dates=[0])
S3=pd.read_excel(r'C:\Users\徐浩然\Desktop\DCC-data\DCC-EMU.xlsx', sheet_name='Short-Cor',index_col=0,parse_dates=[0])
S4=pd.read_excel(r'C:\Users\徐浩然\Desktop\DCC-data\DCC-TPU.xlsx', sheet_name='Short-Cor',index_col=0,parse_dates=[0])
S5=pd.read_excel(r'C:\Users\徐浩然\Desktop\DCC-data\DCC-GPR.xlsx', sheet_name='Short-Cor',index_col=0,parse_dates=[0])

L1=pd.read_excel(r'C:\Users\徐浩然\Desktop\DCC-data\DCC-CPU.xlsx', sheet_name='Long-Cor',index_col=0,parse_dates=[0])
L2=pd.read_excel(r'C:\Users\徐浩然\Desktop\DCC-data\DCC-EPU.xlsx', sheet_name='Long-Cor',index_col=0,parse_dates=[0])
L3=pd.read_excel(r'C:\Users\徐浩然\Desktop\DCC-data\DCC-EMU.xlsx', sheet_name='Long-Cor',index_col=0,parse_dates=[0])
L4=pd.read_excel(r'C:\Users\徐浩然\Desktop\DCC-data\DCC-TPU.xlsx', sheet_name='Long-Cor',index_col=0,parse_dates=[0])
L5=pd.read_excel(r'C:\Users\徐浩然\Desktop\DCC-data\DCC-GPR.xlsx', sheet_name='Long-Cor',index_col=0,parse_dates=[0])

plt.subplots(figsize=(6,12))

plt.subplot(511)

# plt.plot(L1.iloc[:, 0])
plt.plot(S1.iloc[:, 0])
# plt.plot(L1.iloc[:, 1])
plt.plot(S1.iloc[:, 1])
# plt.plot(L1.iloc[:, 2])
plt.plot(S1.iloc[:, 2])
# plt.plot(L1.iloc[:, 3])
plt.plot(S1.iloc[:, 3])
plt.legend(frameon=False)


plt.subplot(512)
# plt.plot(L2.iloc[:, 0])
plt.plot(S2.iloc[:, 0])
# plt.plot(L2.iloc[:, 1])
plt.plot(S2.iloc[:, 1])
# plt.plot(L2.iloc[:, 2])
plt.plot(S2.iloc[:, 2])
# plt.plot(L2.iloc[:, 3])
plt.plot(S2.iloc[:, 3])
plt.legend(frameon=False)

plt.subplot(513)
# plt.plot(L3.iloc[:, 0])
plt.plot(S3.iloc[:, 0])
# plt.plot(L3.iloc[:, 1])
plt.plot(S3.iloc[:, 1])
# plt.plot(L3.iloc[:, 2])
plt.plot(S3.iloc[:, 2])
# plt.plot(L3.iloc[:, 3])
plt.plot(S3.iloc[:, 3])
plt.legend(frameon=False)

plt.subplot(514)

# plt.plot(L4.iloc[:, 0])
plt.plot(S4.iloc[:, 0])
# plt.plot(L4.iloc[:, 1])
plt.plot(S4.iloc[:, 1])
# plt.plot(L4.iloc[:, 2])
plt.plot(S4.iloc[:, 2])
# plt.plot(L4.iloc[:, 3])
plt.plot(S4.iloc[:, 3])
plt.legend(frameon=False)

plt.subplot(515)

# plt.plot(L5.iloc[:, 0])
plt.plot(S5.iloc[:, 0])
# plt.plot(L5.iloc[:, 1])
plt.plot(S5.iloc[:, 1])
# plt.plot(L5.iloc[:, 2])
plt.plot(S5.iloc[:, 2])
# plt.plot(L5.iloc[:, 3])
plt.plot(S5.iloc[:, 3])
plt.legend(frameon=False)

# plt.savefig(r'C:/Users/徐浩然/Desktop/DCC-CPU.png',dpi=400)
# plt.savefig(r'C:/Users/徐浩然/Desktop/DCC-EPU.png',dpi=400)
# plt.savefig(r'C:/Users/徐浩然/Desktop/DCC-EMU.png',dpi=400)
# plt.savefig(r'C:/Users/徐浩然/Desktop/DCC-TPU.png',dpi=400)
# plt.savefig(r'C:/Users/徐浩然/Desktop/DCC-GPR.png',dpi=400)


plt.show()
