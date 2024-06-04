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

# labels=['600028.sh', '601857.sh', '600023.SH','601390.sh']#有贵州茅台
labels=['600028.SH', '601857.SH', '600023.SH','600021.SH']#无贵州茅台

# labels=['600028.sh', '601857.sh', '600023.SH','601390.sh','601111.sh']#无贵州茅台
# labels=['600028.sh', '601857.sh', '600023.SH','601390.sh','601111.sh','600519.sh']#有贵州茅台
number=len(labels)
portfolio=pd.DataFrame()

df1 = pd.read_excel(r'C:\Users\徐浩然\Desktop\930951perf.xlsx', sheet_name='930951perf',index_col=0,parse_dates=[0])
# df2 = pd.read_excel(r'C:\Users\徐浩然\Desktop\930609perf.xlsx', sheet_name='930609perf',index_col=0,parse_dates=[0])
df2 = pd.read_excel(r'C:\Users\徐浩然\Desktop\中证50债券指数 (H11016).xlsx', sheet_name='H11016perf',index_col=0,parse_dates=[0])



for i in range(len(labels)):
    portfolio.insert(i, labels[i], get_close(labels[i],'2019-01-01','2023-12-31')['close'])
portfolio['930951']=df1['收盘Close']
portfolio['H11016']=df2['收盘Close']
portfolio = portfolio.dropna()

# plt.figure()
#计算收益率
rets = np.log(portfolio / portfolio.shift(1))
# print(rets)
# plt.plot(rets)
# print(rets)
aa=0.8
cc='viridis'
d=rets.iloc[:, 4:6]
number=len(rets.columns)
plt.subplots(figsize=(10,8))
plt.subplot(321)
a=sns.kdeplot(data=rets.iloc[:, 0:1],fill=True,palette=cc,alpha=aa, linewidth=0)
plt.ylabel('')

plt.subplot(322)
b=sns.kdeplot(data=rets.iloc[:, 1:2],fill=True,palette=cc,alpha=aa, linewidth=0)
plt.ylabel('')

plt.subplot(323)
c=sns.kdeplot(data=rets.iloc[:, 2:3],fill=True,palette=cc,alpha=aa, linewidth=0)
plt.ylabel('')

plt.subplot(324)
d=sns.kdeplot(data=rets.iloc[:, 3:4],fill=True,palette=cc,alpha=aa, linewidth=0)
plt.ylabel('')

plt.subplot(325)
e=sns.kdeplot(data=rets.iloc[:, 4:5],fill=True,palette=cc,alpha=aa, linewidth=0)
plt.ylabel('')

plt.subplot(326)
f=sns.kdeplot(data=rets.iloc[:, 5:6],fill=True,palette=cc,alpha=aa, linewidth=0)
plt.ylabel('')

sns.move_legend(a,loc='upper right',frameon=False)
sns.move_legend(b,loc='upper right',frameon=False)
sns.move_legend(c,loc='upper right',frameon=False)
sns.move_legend(d,loc='upper right',frameon=False)
sns.move_legend(e,loc='upper right',frameon=False)
sns.move_legend(f,loc='upper right',frameon=False)
plt.ylabel('')
plt.tight_layout()
#
plt.savefig(r'C:/Users/徐浩然/Desktop/d.png',dpi=400)

plt.show()
print('Done')
