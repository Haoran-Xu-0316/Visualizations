import math
# import proplot
from datetime import datetime

import matplotlib.dates as dates
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.interpolate as sci
import scipy.optimize as sco
import seaborn as sns

#全局设置-----------------------------------------------------------------------------------------------------------------
# plt.rcParams['font.sans-serif']=['Microsoft YaHei']
plt.rcParams['font.sans-serif'] = ['Palatino Linotype']
# plt.rcParams["font.weight"] = "bold"
plt.rcParams['font.size'] = 12
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['lines.linewidth'] = 1
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)

NIC12=pd.read_excel(r'C:\Users\徐浩然\Desktop\Paper4 Figdata\ARMA_GARCH.xlsx', sheet_name='HE',index_col=0,parse_dates=[0])
NIC13=pd.read_excel(r'C:\Users\徐浩然\Desktop\Paper4 Figdata\ARMA_GARCH.xlsx', sheet_name='DB',index_col=0,parse_dates=[0])
NIC14=pd.read_excel(r'C:\Users\徐浩然\Desktop\Paper4 Figdata\ARMA_GARCH.xlsx', sheet_name='FF',index_col=0,parse_dates=[0])
NIC23=pd.read_excel(r'C:\Users\徐浩然\Desktop\Paper4 Figdata\ARMA_GARCH.xlsx', sheet_name='II',index_col=0,parse_dates=[0])

NIC12.set_index('newsx', inplace=True)
NIC13.set_index('newsx', inplace=True)
NIC14.set_index('newsx', inplace=True)
NIC23.set_index('newsx', inplace=True)

plt.subplots(figsize=(10,10))

print(NIC14)

plt.subplot(221)
plt.plot(NIC12['newsy'])

plt.subplot(222)
plt.plot(NIC13['newsy'])

plt.subplot(223)
plt.plot(NIC14['newsy'])


plt.subplot(224)
plt.plot(NIC23['newsy'])


plt.tight_layout()
plt.show()
