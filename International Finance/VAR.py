import math

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.interpolate as sci
import scipy.optimize as sco
import seaborn as sns
import tushare as ts

#全局设置----------------------------------------------------------------------------------------------------------------
plt.rcParams['font.sans-serif'] = ['Palatino Linotype']
plt.rcParams['font.size'] = 12
plt.rcParams['axes.unicode_minus'] = False
# plt.style.use('seaborn-ticks')

pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)



df1 = pd.read_excel(r'C:\Users\徐浩然\Desktop\汇率货币.xls', sheet_name='汇货',index_col=0,)
df2 = pd.read_excel(r'C:\Users\徐浩然\Desktop\汇率货币.xls', sheet_name='货汇',index_col=0)
plt.figure(figsize=(8,4))
plt.plot(df1['汇货'],label='Impulse')
plt.plot(df1['95% CI(UL)'],label='95% CI(UL)')
plt.plot(df1['95% CI(LL)'],label='95% CI(LL)')

plt.xticks(np.arange(0,11,1))
plt.axhline(y=0 ,c='black',ls="--",lw=1)

plt.legend(frameon=False)
plt.tight_layout()

plt.savefig(r'C:/Users/徐浩然/Desktop/汇货.png',dpi=400)

plt.figure(figsize=(8,4))
plt.plot(df2['货汇'],label='Impulse')
plt.plot(df2['95% CI(UL)'],label='95% CI(UL)')
plt.plot(df2['95% CI(LL)'],label='95% CI(LL)')
plt.xticks(np.arange(0,11,1))
plt.axhline(y=0 ,c='black',ls="--",lw=1)
plt.legend(frameon=False)
plt.tight_layout()
plt.savefig(r'C:/Users/徐浩然/Desktop/货汇.png',dpi=400)

plt.show()