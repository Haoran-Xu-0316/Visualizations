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
#API获取数据--------------------------------------------------------------------------------------------------------------
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

# labels=['600021.SH','600028.SH', '601857.SH', '601688.SH',]#无贵州茅台
# labels=['600028.SH', '601857.SH', '600023.SH','600021.SH']#选的
labels=['600028.SH', '601857.SH', '601688.SH','600021.SH']#选的

number=len(labels)
portfolio=pd.DataFrame()

# df1 = pd.read_excel(r'C:\Users\徐浩然\Desktop\930951perf.xlsx', sheet_name='930951perf',index_col=0,parse_dates=[0])
# df2 = pd.read_excel(r'C:\Users\徐浩然\Desktop\930609perf.xlsx', sheet_name='930609perf',index_col=0,parse_dates=[0])



for i in range(len(labels)):
    portfolio.insert(i, labels[i], get_close(labels[i],'2019-01-01','2023-12-31')['close'])
# portfolio['bond']=df1['收盘Close']
# portfolio['fund']=df2['收盘Close']
# print(df1.iloc[4:6,100:200])
portfolio = portfolio.dropna()
portfolio.to_excel(r'C:\Users\徐浩然\Desktop\stock.xlsx',sheet_name='stock')
portfolio=pd.read_excel(r'C:\Users\徐浩然\Desktop\stock.xlsx', sheet_name='stock',index_col=0,parse_dates=[0])
# print(portfolio)
plt.figure(figsize=(8,4))
plt.plot(portfolio)
plt.tight_layout()
plt.legend(labels,frameon=False)
# plt.legend(labels,frameon=False,ncol=4,loc='upper center',bbox_to_anchor=(0.5,1.12))
# plt.savefig(r'C:/Users/徐浩然/Desktop/stock.png',dpi=400)

plt.show()