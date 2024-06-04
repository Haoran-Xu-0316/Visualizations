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
plt.subplots(figsize=(11, 6))
# 绿色债券指数-------------------------------------------------------------------------------------------------------------
df1 = pd.read_excel(r'C:\Users\徐浩然\Desktop\汇率货币.xls', sheet_name='Sheet0',index_col=0,parse_dates=[0])
plt.subplot(221)
plt.plot(df1['汇率'],color='darkgreen',label='Exchange Rate')
# plt.savefig(r'C:/Users/徐浩然/Desktop/ggg.png',dpi=400)
plt.legend(frameon=False,loc='upper left')
ret1 = np.log(df1['汇率'] / df1['汇率'].shift(1))
plt.subplot(222)
plt.plot(ret1,color='darkgreen',label='ER Volatility')
plt.legend(frameon=False,loc='lower right')
# 沪深300指数-------------------------------------------------------------------------------------------------------------
plt.subplot(223)

plt.plot(df1['货币供应'],color='darkgreen',label='Money Supply')
# plt.savefig(r'C:/Users/徐浩然/Desktop/300-.png',dpi=400)
plt.legend(frameon=False,loc='upper left')
ret2 = np.log(df1['货币供应'] / df1['货币供应'].shift(1))
plt.subplot(224)

plt.plot(ret2,color='darkgreen',label='MS Volatilty')
plt.legend(frameon=False,loc='lower right')



plt.tight_layout()
plt.savefig(r'C:/Users/徐浩然/Desktop/b.png',dpi=400)
plt.show()