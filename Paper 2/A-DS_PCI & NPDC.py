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
from scipy.stats import skew, kurtosis

#全局设置-----------------------------------------------------------------------------------------------------------------
plt.rcParams['font.sans-serif'] = ['Palatino Linotype']
# plt.rcParams["font.weight"] = "bold"
# plt.rcParams['font.style']='italic'
plt.rcParams['font.size'] = 12.5
fs=12.5
plt.rcParams['axes.unicode_minus'] = True
plt.rcParams['lines.linewidth'] = 0.3
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
ll=['EUA',	'SZA',	'HBA', 'PCM', 'CEI', 'GBI']

l = []

for i in range(len(ll)):
    if i + 1 <= len(ll):
        for j in range(i + 1, len(ll)):
            l.append(f"{ll[i]} - {ll[j]}")

#-----------------------------------------------------------------------------------------------------------------------
pcit=pd.read_excel(r'C:\Users\徐浩然\Desktop\P2 Results\All_pci.xlsx', sheet_name='Total',index_col=0,parse_dates=[0])
pci13=pd.read_excel(r'C:\Users\徐浩然\Desktop\P2 Results\All_pci.xlsx', sheet_name='1-3',index_col=0,parse_dates=[0])
pci36=pd.read_excel(r'C:\Users\徐浩然\Desktop\P2 Results\All_pci.xlsx', sheet_name='3-6',index_col=0,parse_dates=[0])
pci6=pd.read_excel(r'C:\Users\徐浩然\Desktop\P2 Results\All_pci.xlsx', sheet_name='6',index_col=0,parse_dates=[0])
d=pd.read_excel(r'C:\Users\徐浩然\Desktop\P2 Results\All_to.xlsx', sheet_name='to',parse_dates=[0])

#-----------------------------------------------------------------------------------------------------------------------
P_pcit=pd.read_excel(r'C:\Users\徐浩然\Desktop\P2 Results\Positive_pci.xlsx', sheet_name='Total',index_col=0,parse_dates=[0])
P_pci13=pd.read_excel(r'C:\Users\徐浩然\Desktop\P2 Results\Positive_pci.xlsx', sheet_name='1-3',index_col=0,parse_dates=[0])
P_pci36=pd.read_excel(r'C:\Users\徐浩然\Desktop\P2 Results\Positive_pci.xlsx', sheet_name='3-6',index_col=0,parse_dates=[0])
P_pci6=pd.read_excel(r'C:\Users\徐浩然\Desktop\P2 Results\Positive_pci.xlsx', sheet_name='6',index_col=0,parse_dates=[0])

#-----------------------------------------------------------------------------------------------------------------------
N_pcit=pd.read_excel(r'C:\Users\徐浩然\Desktop\P2 Results\Negative_pci.xlsx', sheet_name='Total',index_col=0,parse_dates=[0])
N_pci13=pd.read_excel(r'C:\Users\徐浩然\Desktop\P2 Results\Negative_pci.xlsx', sheet_name='1-3',index_col=0,parse_dates=[0])
N_pci36=pd.read_excel(r'C:\Users\徐浩然\Desktop\P2 Results\Negative_pci.xlsx', sheet_name='3-6',index_col=0,parse_dates=[0])
N_pci6=pd.read_excel(r'C:\Users\徐浩然\Desktop\P2 Results\Negative_pci.xlsx', sheet_name='6',index_col=0,parse_dates=[0])

#-----------------------------------------------------------------------------------------------------------------------



ddf = pd.DataFrame()
# pci
for i in range(math.comb(len(ll), 2)):
    #
    apcit=(N_pcit.iloc[:, i] - P_pcit.iloc[:, i]) / pcit.iloc[:, i]
    apci13=(N_pci13.iloc[:, i] - P_pci13.iloc[:, i]) / pci13.iloc[:, i]
    apci36=(N_pci36.iloc[:, i] - P_pci36.iloc[:, i]) / pci36.iloc[:, i]
    apci6=(N_pci6.iloc[:, i] - P_pci6.iloc[:, i]) / pci6.iloc[:, i]


    df = pd.concat([apcit, apci13, apci36, apci6], axis=1)
    df.columns = ['Total', '1-5', '5-22', '22-inf']  # 设置列名

    ddf=pd.concat([ddf, df], axis=1)
# print(df)
ddf.to_csv(r'C:\Users\徐浩然\Desktop\pci_summary_data.csv')


