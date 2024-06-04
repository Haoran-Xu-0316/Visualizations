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
# labels=['600021.SH','601111.sh','600519.sh']#无贵州茅台
# labels=['600036.SH','601288.SH','601857.SH','601988.SH','600519.SH','601398.SH','603288.SH','601919.SH','601808.sh']#无贵州茅台
# labels=['600021.SH','600028.SH', '601857.SH', '601688.SH',]#无贵州茅台
# labels = [
#     "601318.SH",  # 中国平安保险股份有限公司
#     "601857.SH",  # 中国石油化工股份有限公司
#     "600028.SH",  # 中国石化股份有限公司
#     "600050.SH",  # 中国联通股份有限公司
#     "601668.SH",  # 中国建筑股份有限公司
#
#     "601601.SH",  # 中国太平洋保险（集团）股份有限公司
#     "600000.SH",  # 上海浦东发展银行股份有限公司
#     "600104.SH",  # 上海汽车集团股份有限公司
#     "601319.SH"   # 中国人民保险集团股份有限公司
# ]

# labels=['000568.SH', '000858.SZ', '600519.SH', '600809.SH', '002304']
# labels=['601857.SH']#无贵州茅台
# labels=['000001.SZ','000002.SZ','600000.SH']


number=len(labels)
portfolio=pd.DataFrame()
#
# df1 = pd.read_excel(r'C:\Users\徐浩然\Desktop\930951perf.xlsx', sheet_name='930951perf',index_col=0,parse_dates=[0])
#
# df3 = pd.read_excel(r'C:\Users\徐浩然\Desktop\000300perf.xlsx', sheet_name='000300perf',index_col=0,parse_dates=[0])
# df2 = pd.read_excel(r'C:\Users\徐浩然\Desktop\中证50债券指数 (H11016).xlsx', sheet_name='H11016perf',index_col=0,parse_dates=[0])


for i in range(len(labels)):
    portfolio.insert(i, labels[i], get_close(labels[i],'2019-01-01','2023-12-31')['close'])
# portfolio['930951']=df1['收盘Close']
# portfolio['H11016']=df2['收盘Close']
# portfolio['000300']=df3['收盘Close']
portfolio = portfolio.dropna()
# print(portfolio)
# plt.figure()
#计算收益率
rets = np.log(portfolio / portfolio.shift(1))



# rets.to_excel(r'C:\Users\徐浩然\Desktop\rrr.xlsx',sheet_name='0')
# rets=pd.read_excel(r'C:\Users\徐浩然\Desktop\rrr.xlsx',sheet_name='0',index_col=0,parse_dates=[0])
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

# plt.figure()
# sns.heatmap(corr,square=True,annot=True,cmap='viridis')
# plt.tight_layout()
#annot=True,fmt=".4f", linecolor='black',robust=True,linewidth=0.3,cmap=C, vmin=0.09, vmax=0.11,cbar_kws={"orientation":"vertical"}
#协方差热力图--------------------------------------------------------------------------------------------------------------
cov=rets.cov()*252
# plt.figure()
# sns.heatmap(cov,annot=True)

#Monte Carlos MPT投资组合优化----------------------------------------------------------------------------------------------
noa = number #换投资资产时需要调整
# weights = np.random.random(noa)
# weights /= np.sum(weights)
# np.dot(weights.T, np.dot(rets.cov() * 252, weights))
#
prets = []
pvols = []
for p in range(5000):
    weights = np.random.random(noa)
    weights /= np.sum(weights)
    prets.append(np.sum(rets.mean() * weights) * 252)
    pvols.append(np.sqrt(np.dot(weights.T, np.dot(rets.cov() * 252, weights))))

prets = np.array(prets)
pvols = np.array(pvols)
#
# plt.figure(figsize=(9, 4))
# plt.scatter(pvols, prets, c=prets / pvols, marker='o',cmap='viridis')# 此处无风险利率为0
# # plt.grid(True)
# plt.xlabel('Expected Volatility')
# plt.ylabel('Expected Return')
# plt.colorbar(label='Sharpe Ratio')
# plt.tight_layout()
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#
# # 投资组合优化
# # 首先建立一个方便的函数，为输入的权重向量 / 数组给出重要的投资组合统计数字：
def statistics(weights):
    """
    Return portfolio statistics
    :param weights: weights for different securities in portfolio
    :return:
    pret:float
    expected portfolio return
    pvol:float
    expected portfolio volatility
    pret/pvol:float
    Sharpe ratio for rf=0
    """
    weights = np.array(weights)
    pret = np.sum(rets.mean() * weights) * 252
    pvol = np.sqrt(np.dot(weights.T, np.dot(rets.cov() * 252, weights)))
    return np.array([pret, pvol, pret/ pvol])# 无风险收益0.03

#
# # 最优化投资组合的推导是一个约束最优化问题
#
# # 最小化函数minimize很通用，考虑了参数的（不）等式约束和参数的范围。
# # 我们从夏普指数的最大化开始。 正式地说，最小化夏普指数的负值：
def min_func_sharpe(weights):
    return -statistics(weights)[2]

# # 约束是所有参数（权重）的总和为1。 这可以用minimize函数的约定表达如下
cons = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
#
# # 我们还将参数值（权重）限制在0和l之间。 这些值以多个元组组成的一个元组形式提供给最小化函数：
bnds = tuple((0, 1) for x in range(noa))
#
# # 优化函数调用中忽略的唯一输入是起始参数列表（对权重的初始猜测）。我们简单地使用平均分布：
noa * [1. / noa, ]
# # [0.2, 0.2, 0.2, 0.2, 0.2]
#
opts = sco.minimize(min_func_sharpe, noa * [1. / noa, ], method='SLSQP', bounds=bnds, constraints=cons)
# # Wall time: 1.2 s
# '''
# opts
# # fun: -0.7689821435140733
# # jac: array([3.62539694e-01, 3.84121098e-01, 1.03567891e-01,
# #             -1.06185675e-04, 2.67580152e-04])
# # message: 'Optimization terminated successfully.'
# # nfev: 59
# # nit: 8
# # njev: 8
# # status: 0
# # success: True
# # x: array([2.69140628e-17, 5.93820112e-17, 0.00000000e+00,
# #           7.15876612e-01, 2.84123388e-01])
#
# opts['x'].round(3)
# # array([ 0.   ,  0.   ,  0.   ,  0.716,  0.284])
# '''
# print('资产比例',opts['x'].round(4)*100)
# print('EVSS',statistics(opts['x']).round(3))
# # 接下来， 我们最小化投资组合的方差。
# # 这与被动率的最小化相同，我们定义一个函数对方差进行最小化：
def min_func_variance(weights):
    return statistics(weights)[1]**2
#
optv = sco.minimize(min_func_variance, noa * [1. / noa, ], method='SLSQP', bounds=bnds, constraints=cons)
#
#
#
# '''
# optv
# # fun: 0.05137907199877911
# # jac: array([0.10326265, 0.10273764, 0.10269385, 0.10276436, 0.102121])
# # message: 'Optimization terminated successfully.'
# # nfev: 71
# # nit: 10
# # njev: 10
# # status: 0
# # success: True
# # x: array([0.04526382, 0.1335909, 0.05702634, 0.73177776, 0.03234118])
#
# optv['x'].round(3)
# # array([ 0.045,  0.134,  0.057,  0.732,  0.032])
# # 投资组合中加入了全部资产。 这种组合可以得到绝对值最小方差投资组合
# # 得到的预期收益率、波动率和夏普指数如下：
# statistics(optv['x']).round(3)
# # array([ 0.115,  0.227,  0.509])
# '''
#
#
# #-----------------------------------------------------------------------------------------------------------------------
def min_func_port(weights):
    return statistics(weights)[1]

#
# # 在不同目标收益率水平（ trets ）中循环时。 最小化的一个条件会变化。
# # 这就是每次循环中更新条件字典对象的原因：
#
trets = np.linspace(statistics(optv['x'])[0], statistics(opts['x'])[0], 200)
# print(statistics(opts['x'])[0]*1.1,type(statistics(opts['x'])[0]))
tvols = []
bnds = tuple((0, 1) for x in weights)
for tret in trets:
    cons = ({'type': 'eq', 'fun': lambda x: statistics(x)[0] - tret},
            {'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
    res = sco.minimize(min_func_port, noa * [1. / noa, ], method='SLSQP', bounds=bnds, constraints=cons)
    tvols.append(res['fun'])
tvols = np.array(tvols)
print(tvols)
#
plt.figure(figsize=(8, 4))
# # random portfolio composition
plt.scatter(pvols,prets,c=prets/pvols,marker='o')
# # efficient frontier
# plt.scatter(tvols,trets,c=trets/tvols,marker='X')#marker
plt.plot(tvols,trets,c='black')
# # portfolio with highest Sharpe ratio
plt.plot(statistics(opts['x'])[1],statistics(opts['x'])[0],'b*',alpha=0.8,markersize=15.0,label='Maximium Sharpe Ratio')
# # minimum variance portfolio
plt.plot(statistics(optv['x'])[1],statistics(optv['x'])[0],'r*',alpha=0.8,markersize=15.0,label='Minimum Volatility')
# plt.grid(False)
plt.xlabel('Expected Volatility')
plt.ylabel('Expected Return')
plt.colorbar(label='Sharpe Ratio')
plt.legend(frameon=False,loc='upper center',bbox_to_anchor=(0.5,1.12),ncol=2)
plt.tight_layout()
# ind = np.argmin(tvols)
# evols = tvols[ind:]
# erets = trets[ind:]
#
# tck = sci.splrep(evols, erets)
#
# # 通过这条数值化路径，最终可以为有效边界定义一个连续可微函数
# # 和对应的一阶导数函数df(x):
#
# def f(x):
#     """
#     Efficient frontier function (splines approximation)
#     :param x:
#     :return:
#     """
#     return sci.splev(x, tck, der=0)
#
#
# def df(x):
#     """
#     First derivative of efficient frontier function.
#     :param x:
#     :return:
#     """
#     return sci.splev(x, tck, der=1)
# # 定义一个函数，返回给定参数集p=(a,b,x)
# def equations(p, rf=0):
#     eq1 = rf - p[0]
#     eq2 = rf + p[1] * p[2] - f(p[2])
#     eq3 = p[1]-df(p[2])
#     return eq1,eq2,eq3
#
# # 数值优化得到如下的值
# opt=sco.fsolve(equations,[0.01,0.5,f(0.5)])
# # opt
# # print(opt)
# # array([ 0.01      ,  0.73464122,  0.29383737])
# # plt.figure(figsize=(8, 4))
# # # random portfolio composition
# # plt.scatter(pvols, prets, c=(prets - 0.01) / pvols, marker="o")
# # # efficient frontier
# # # plt.plot(evols, erets, 'g', lw=2.5)
# # plt.plot(tvols,trets,c='black',linewidth=3)
# #
# # # print(evols,erets)
# # cx = np.linspace(0.0, 0.6)
# # plt.plot(cx, opt[0] + opt[1] * cx, lw=.5)
# # # capital market line
# # plt.plot(opt[2], f(opt[2]), 'r*', markersize=35.0)
# # plt.grid(False)
# # plt.xticks(np.arange(0,0.8,0.1))
# # plt.xlim(0,0.7)
# # # plt.axhline(0, color='k', ls='-', lw=2.0)
# # # plt.axvline(0, color='k', ls='-', lw=2.0)
# # plt.xlabel('Expected Volatility')
# # plt.ylabel('Expected Return')
# # plt.colorbar(label='Sharp Ratio')
#
#
# plt.savefig(r'C:/Users/徐浩然/Desktop/hm.png',dpi=400)

plt.show()
print('Done')
