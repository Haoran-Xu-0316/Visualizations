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

# labels=['600028.sh', '600519.sh', '601919.SH','601808.sh']#有贵州茅台
labels=['600028.SH', '601857.SH', '600023.SH','600021.SH']#选的


number=len(labels)
portfolio=pd.DataFrame()

df1 = pd.read_excel(r'C:\Users\徐浩然\Desktop\930951perf.xlsx', sheet_name='930951perf',index_col=0,parse_dates=[0])
df2 = pd.read_excel(r'C:\Users\徐浩然\Desktop\中证50债券指数 (H11016).xlsx', sheet_name='H11016perf',index_col=0,parse_dates=[0])
df3 = pd.read_excel(r'C:\Users\徐浩然\Desktop\000300perf.xlsx', sheet_name='000300perf',index_col=0,parse_dates=[0])
dfs = pd.read_excel(r'C:\Users\徐浩然\Desktop\000016cons.xls', sheet_name='000016cons.xls',index_col=0,parse_dates=[0])


for i in range(len(labels)):
    portfolio.insert(i, labels[i], get_close(labels[i],'2019-01-01','2023-12-31')['close'])
portfolio['930951']=df1['收盘Close']
portfolio['H11016']=df2['收盘Close']
# portfolio['000300']=df3['收盘Close']
portfolio = portfolio.dropna()
# print(portfolio)
# plt.figure()
#计算收益率
rets = np.log(portfolio / portfolio.shift(1))
print(rets)

# print(rets)
# plt.plot(rets)
print(rets)

number=len(rets.columns)

# print(rets)
# plt.figure()
# sns.kdeplot(
#    data=rets,
#    fill=True,
#     # common_norm=False,
#     palette="crest",
#    alpha=.5, linewidth=0)



# plt.legend(frameon=False)
# plt.figure()
# pair=sns.pairplot(rets,diag_kind='kde')
# pair.map_lower(sns.kdeplot, levels=4, color=".2")
#收益率时间序列展示
# F=sns.FacetGrid(rets,col=labels)
# F.map(sns.lineplot)
# plt.figure(figsize=(8,4))
# sns.lineplot(rets)
#相关系数热力图------------------------------------------------------------------------------------------------------------
corr=rets.corr()

plt.figure(figsize=(10,4))
sns.heatmap(corr,square=False,annot=True,fmt='.3f',cmap='viridis',annot_kws = {'fontweight': 'bold'})
plt.tight_layout()
#annot=True,fmt=".4f", linecolor='black',robust=True,linewidth=0.3,cmap=C, vmin=0.09, vmax=0.11,cbar_kws={"orientation":"vertical"}
#协方差热力图--------------------------------------------------------------------------------------------------------------
# cov=rets.cov()*252
# # plt.figure()
# # sns.heatmap(cov,annot=True)
plt.savefig(r'C:/Users/徐浩然/Desktop/hm.png',dpi=400)

plt.tight_layout()
plt.show()