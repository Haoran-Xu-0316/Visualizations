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

# 全局设置-----------------------------------------------------------------------------------------------------------------
plt.rcParams['font.sans-serif'] = ['Palatino Linotype']
# plt.rcParams["font.weight"] = "bold"
# plt.rcParams['font.style']='italic'
plt.rcParams['font.size'] = 12
fs = 12
plt.rcParams['axes.unicode_minus'] = True
plt.rcParams['lines.linewidth'] = 0.4
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
ll = ['EUA', 'SZA', 'HBA', 'PCM', 'CEI', 'GBI']

l = []

for i in range(len(ll)):
    if i + 1 <= len(ll):
        for j in range(i + 1, len(ll)):
            l.append(f"{ll[i]} - {ll[j]}")

# -----------------------------------------------------------------------------------------------------------------------

net = pd.read_excel(r'C:\Users\徐浩然\Desktop\P2 Results\All_net.xlsx', sheet_name='net', index_col=0, parse_dates=[0])
# d = pd.read_excel(r'C:\Users\徐浩然\Desktop\P2 Results\All_to.xlsx', sheet_name='to', parse_dates=[0])

# -----------------------------------------------------------------------------------------------------------------------

P_net = pd.read_excel(r'C:\Users\徐浩然\Desktop\P2 Results\Positive_net.xlsx', sheet_name='net', index_col=0,
                      parse_dates=[0])

# -----------------------------------------------------------------------------------------------------------------------

N_net = pd.read_excel(r'C:\Users\徐浩然\Desktop\P2 Results\Negative_net.xlsx', sheet_name='net', index_col=0,
                      parse_dates=[0])

# -----------------------------------------------------------------------------------------------------------------------


ddf = pd.DataFrame()
# net
for i in range(len(ll)):
    #
    anett = (N_net.iloc[:, i] - P_net.iloc[:, i]) / net.iloc[:, i]
    anet13 = (N_net.iloc[:, i + len(ll)] - P_net.iloc[:, i + len(ll)]) / net.iloc[:, i + len(ll)]
    anet36 = (N_net.iloc[:, i + len(ll) * 2] - P_net.iloc[:, i + len(ll) * 2]) / net.iloc[:, i + len(ll) * 2]
    anet6 = (N_net.iloc[:, i + len(ll) * 3] - P_net.iloc[:, i + len(ll) * 3]) / net.iloc[:, i + len(ll) * 3]

    df = pd.concat([anett, anet13, anet36, anet6], axis=1)
    df.columns = ['Total', '1-5', '5-22', '22-inf']  # 设置列名

    ddf = pd.concat([ddf, df], axis=1)
# print(df)
ddf.to_csv(r'C:\Users\徐浩然\Desktop\net_summary_data.csv')