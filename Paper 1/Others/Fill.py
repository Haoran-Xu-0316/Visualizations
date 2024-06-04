import math
from datetime import datetime

import matplotlib.dates as dates
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import proplot
import scipy.interpolate as sci
import scipy.optimize as sco
import seaborn as sns

# plt.rcParams['font.sans-serif']=['Microsoft YaHei']
plt.rcParams['font.sans-serif'] = ['Palatino Linotype']
# plt.rcParams["font.weight"] = "bold"
plt.rcParams['font.size'] = 12
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['lines.linewidth'] = 1
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
df=pd.read_excel(r'C:\Users\徐浩然\Desktop\DCC-data-China\Macro Uncertainty\macro uncertainty.xlsx', sheet_name='Sheet2',index_col=0,parse_dates=[0])
# print(df)


print('----------------------------------')
df=df.fillna(df.interpolate())
# print(df)
df.to_excel(r'C:\Users\徐浩然\Desktop\datasss.xlsx')