from __future__ import division

import arch
import matplotlib.pyplot as plt
import numpy
import numpy as np
import pandas as pd
import tushare as ts
from arch.univariate import GARCH, ConstantMean

#全局设置----------------------------------------------------------------------------------------------------------------
plt.rcParams['font.sans-serif'] = ['Palatino Linotype']
plt.rcParams['font.size'] = 12
plt.rcParams['axes.unicode_minus'] = False
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
#获取数据--------------------------------------------------------------------------------------------------------------
ts.set_token('376ad9d1b8258927f4d4a8042e236755a89debdf118e62fb08edf641')
pro = ts.pro_api()

def get_close(ticker, start_date, end_date):
    df = pro.daily(ts_code=ticker,
                   start_date=start_date,
                   end_date=end_date)
    df = df.set_index('trade_date').sort_index()
    df_close = df[['close']]
    df_close=df_close.fillna(axis=0,method='ffill')
    return df_close
labels=['600104.sh',"600887.sh"]
s1=get_close('600104.sh','2020-01-01','2022-12-31')['close']
s2=get_close('600007.sh','2020-01-01','2022-12-31')['close']
rets1 = 100*np.log(s1 / s1.shift(1)).dropna()
rets2 = 100*np.log(s2 / s2.shift(1)).dropna()
rets1.to_excel(r'C:\Users\徐浩然\Desktop\3.xlsx',sheet_name='1')
rets2.to_excel(r'C:\Users\徐浩然\Desktop\4.xlsx',sheet_name='2')
# print(rets1,rets2)

# 建立GARCH(1,1)模型
garch_s1 = arch.arch_model(rets1, vol='Garch', p=1, o=0, q=1, dist='Normal')
garch_s2 = arch.arch_model(rets2, vol='Garch', p=1, o=0, q=1, dist='Normal')

# 拟合模型
res_s1 = garch_s1.fit()
res_s2 = garch_s2.fit()
s1_vol = res_s1.conditional_volatility
s2_vol = res_s2.conditional_volatility

s1_vol.to_excel(r'C:\Users\徐浩然\Desktop\1.xlsx',sheet_name='1')
s1_vol=pd.read_excel(r'C:\Users\徐浩然\Desktop\1.xlsx', sheet_name='1',index_col=0,parse_dates=[0])
s2_vol.to_excel(r'C:\Users\徐浩然\Desktop\2.xlsx',sheet_name='2')
s2_vol=pd.read_excel(r'C:\Users\徐浩然\Desktop\2.xlsx', sheet_name='2',index_col=0,parse_dates=[0])

print(res_s2.param_cov)
s1_std = np.sqrt(s1_vol)
s2_std = np.sqrt(s2_vol)
matrix1 = np.diag(np.ravel(s1_std))
matrix2 = np.diag(np.ravel(s2_std))
