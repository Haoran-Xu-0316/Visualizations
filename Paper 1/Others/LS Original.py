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

# S=pd.read_excel(r'C:\Users\徐浩然\Desktop\DCC-data\DCC-CPU.xlsx', sheet_name='Short-Cor',index_col=0,parse_dates=[0])
# L=pd.read_excel(r'C:\Users\徐浩然\Desktop\DCC-data\DCC-CPU.xlsx', sheet_name='Long-Cor',index_col=0,parse_dates=[0])

# S=pd.read_excel(r'C:\Users\徐浩然\Desktop\DCC-data\DCC-EPU.xlsx', sheet_name='Short-Cor',index_col=0,parse_dates=[0])
# L=pd.read_excel(r'C:\Users\徐浩然\Desktop\DCC-data\DCC-EPU.xlsx', sheet_name='Long-Cor',index_col=0,parse_dates=[0])
#
# S=pd.read_excel(r'C:\Users\徐浩然\Desktop\DCC-data\DCC-EMU.xlsx', sheet_name='Short-Cor',index_col=0,parse_dates=[0])
# L=pd.read_excel(r'C:\Users\徐浩然\Desktop\DCC-data\DCC-EMU.xlsx', sheet_name='Long-Cor',index_col=0,parse_dates=[0])
#
S=pd.read_excel(r'C:\Users\徐浩然\Desktop\DCC-data\DCC-TPU.xlsx', sheet_name='Short-Cor',index_col=0,parse_dates=[0])
L=pd.read_excel(r'C:\Users\徐浩然\Desktop\DCC-data\DCC-TPU.xlsx', sheet_name='Long-Cor',index_col=0,parse_dates=[0])

# S=pd.read_excel(r'C:\Users\徐浩然\Desktop\DCC-data\DCC-GPR.xlsx', sheet_name='Short-Cor',index_col=0,parse_dates=[0])
# L=pd.read_excel(r'C:\Users\徐浩然\Desktop\DCC-data\DCC-GPR.xlsx', sheet_name='Long-Cor',index_col=0,parse_dates=[0])

plt.subplots(figsize=(12,14))

plt.subplot(521)
plt.plot(S.iloc[:, 0],label=l[0])
plt.plot(L.iloc[:, 0])
plt.legend(frameon=False)

plt.subplot(522)
plt.plot(S.iloc[:, 1],label=l[1])
plt.plot(L.iloc[:, 1])
plt.legend(frameon=False)

plt.subplot(523)
plt.plot(S.iloc[:, 2],label=l[2])
plt.plot(L.iloc[:, 2])
plt.legend(frameon=False)

plt.subplot(524)
plt.plot(S.iloc[:, 3],label=l[3])
plt.plot(L.iloc[:, 3])
plt.legend(frameon=False)

plt.subplot(525)
plt.plot(S.iloc[:, 4],label=l[4])
plt.plot(L.iloc[:, 4])
plt.legend(frameon=False)

plt.subplot(526)
plt.plot(S.iloc[:, 5],label=l[5])
plt.plot(L.iloc[:, 5])
plt.legend(frameon=False)

plt.subplot(527)
plt.plot(S.iloc[:, 6],label=l[6])
plt.plot(L.iloc[:, 6])
plt.legend(frameon=False)

plt.subplot(528)
plt.plot(S.iloc[:, 7],label=l[7])
plt.plot(L.iloc[:, 7])
plt.legend(frameon=False)

plt.subplot(529)
plt.plot(S.iloc[:, 8],label=l[8])
plt.plot(L.iloc[:, 8])
plt.legend(frameon=False)

plt.subplot(5,2,10)
plt.plot(S.iloc[:, 9],label=l[9])
plt.plot(L.iloc[:, 9])
plt.legend(frameon=False)
plt.tight_layout()



# plt.savefig(r'C:/Users/徐浩然/Desktop/DCC-CPU.png',dpi=400)
# plt.savefig(r'C:/Users/徐浩然/Desktop/DCC-EPU.png',dpi=400)
# plt.savefig(r'C:/Users/徐浩然/Desktop/DCC-EMU.png',dpi=400)
# plt.savefig(r'C:/Users/徐浩然/Desktop/DCC-TPU.png',dpi=400)
# plt.savefig(r'C:/Users/徐浩然/Desktop/DCC-GPR.png',dpi=400)


plt.show()
