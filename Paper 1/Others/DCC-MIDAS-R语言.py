import math

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.interpolate as sci
import scipy.optimize as sco
import seaborn as sns
import tushare as ts
from arch import arch_model
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import acf, adfuller, pacf

#全局设置----------------------------------------------------------------------------------------------------------------
plt.rcParams['font.sans-serif'] = ['Palatino Linotype']
plt.rcParams['font.size'] = 12
plt.rcParams['axes.unicode_minus'] = False

pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)

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

def decomposing(timeseries):
    decomposition=seasonal_decompose(timeseries)
    trend= decomposition.trend
    seasonal=decomposition.seasonal
    residual= decomposition.resid

    plt.figure(figsize=(16,12))
    plt.subplot(412)
    plt.plot(trend,label='Trend')
    plt.subplot(413)
    plt.plot(seasonal,label='Seasonarity')
    plt.subplot(414)
    plt.plot(residual,label='Error')
    plt.show()

labels=["600519.sh", "600887.sh", "600008.sh", "000002.sz"]
# labels=['600519.sh',"600887.sh","600008.sh"]
number=len(labels)
portfolio=pd.DataFrame()

for i in range(len(labels)):
    portfolio.insert(i, labels[i], get_close(labels[i],'2018-01-01','2023-12-31')['close'])
portfolio = portfolio.dropna()
data = np.log(portfolio / portfolio.shift(1))
data.drop(data.index[0], inplace=True)

data.to_excel(r'C:\Users\徐浩然\Desktop\DCC-GARCH DATA.xlsx',sheet_name='data')


# decomposing()

# result = adfuller(data.iloc[:,0])
# print('ADF Statistic:', result[0])
# print('p-value:', result[1])
# print('Critical Values:', result[4])

# plot_acf(data.iloc[:,0], lags=20)
# plot_pacf(data.iloc[:,0], lags=20)
# 计算 ACF 和 PACF
# ts=data.iloc[:,0]
# lag_acf = acf(ts, nlags=20)
# lag_pacf = pacf(ts, nlags=20)
#
# # 绘制 ACF 和 PACF 的图像
# plt.subplot(121)
# plt.stem(lag_acf)
# plt.axhline(y=0, linestyle='--', color='gray')
# plt.axhline(y=-1.96/np.sqrt(len(ts)), linestyle='--', color='gray')
# plt.axhline(y=1.96/np.sqrt(len(ts)), linestyle='--', color='gray')
# plt.title('Autocorrelation Function')
#
# plt.subplot(122)
# plt.stem(lag_pacf)
# plt.axhline(y=0, linestyle='--', color='gray')
# plt.axhline(y=-1.96/np.sqrt(len(ts)), linestyle='--', color='gray')
# plt.axhline(y=1.96/np.sqrt(len(ts)), linestyle='--', color='gray')
# plt.title('Partial Autocorrelation Function')
#
# plt.tight_layout()
# plt.show()

corrmatrix=data.corr()
corr = corrmatrix.iloc[0][1]
print(corr)
# 去Rstudio中操作

# 从Rstudio中返回
L=pd.read_excel(r'C:\Users\徐浩然\Desktop\DCC-GARCH.xlsx',sheet_name='SCor',index_col=0,parse_dates=[0])
S=pd.read_excel(r'C:\Users\徐浩然\Desktop\DCC-GARCH.xlsx',sheet_name='LCor',index_col=0,parse_dates=[0])
v1=pd.read_excel(r'C:\Users\徐浩然\Desktop\DCC-GARCH.xlsx',sheet_name='v1',index_col=0,parse_dates=[0])
v2=pd.read_excel(r'C:\Users\徐浩然\Desktop\DCC-GARCH.xlsx',sheet_name='v2',index_col=0,parse_dates=[0])

S.drop(S.index[:1000], inplace=True)
L.drop(L.index[:1000], inplace=True)

v1.drop(v1.index[:1000], inplace=True)
v2.drop(v2.index[:1000], inplace=True)



plt.figure(figsize=(10,6))
plt.axhline(y=corr,color='black',linestyle='--')
plt.plot(L)
plt.plot(S)
plt.figure(figsize=(10,6))
plt.plot(v1)
plt.figure(figsize=(10,6))
plt.plot(v2)
plt.tight_layout()
plt.show()

