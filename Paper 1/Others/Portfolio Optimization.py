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
labels=['600104.sh',"600887.sh",'601166.sh','600033.sh','600063.sh']
number=len(labels)
portfolio=pd.DataFrame()

for i in range(len(labels)):
    portfolio.insert(i, labels[i], get_close(labels[i],'2020-01-01','2022-12-31')['close'])
portfolio = portfolio.dropna()
#计算收益率
rets = np.log(portfolio / portfolio.shift(1))
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
# sns.heatmap(corr,annot=True,cmap='viridis')
#annot=True,fmt=".4f", linecolor='black',robust=True,linewidth=0.3,cmap=C, vmin=0.09, vmax=0.11,cbar_kws={"orientation":"vertical"}
#协方差热力图--------------------------------------------------------------------------------------------------------------
cov=rets.cov()*252
# plt.figure()
# sns.heatmap(cov,annot=True)
#计算累计收益率------------------------------------------------------------------------------------------------------------
# 定义累积收益曲线绘制函数
# stock_return = rets.copy()
# def cumulative_returns(name_list):
#     plt.figure()
#     for name in name_list:
#         CumulativeReturns = ((1+stock_return[name]).cumprod()-1)
#         CumulativeReturns.plot()
#给定权重----------------------------------------------------------------------------------------------------------------
# 设置组合权重，存储为numpy数组类型
# portfolio_weights = np.array([0.32, 0.15, 0.10, 0.18, 0.25])
# # 计算加权的股票收益
# WeightedReturns = stock_return.mul(portfolio_weights, axis=1)
# # 计算投资组合的收益
# stock_return['portfolio'] = WeightedReturns.sum(axis=1)
# stock_return=stock_return.iloc[1:,:]
# cumulative_returns(['portfolio'])
#等权重------------------------------------------------------------------------------------------------------------------
# # 设置投资组合中股票的数目
# numstocks = number
# # 平均分配每一项的权重
# portfolio_weights_ew = np.repeat(1/numstocks, numstocks)
# # 计算等权重组合的收益
# stock_return['Portfolio_EW'] = stock_return.mul(portfolio_weights_ew, axis=1).sum(axis=1)
# # 绘制累积收益曲线
# cumulative_returns(['Portfolio_EW'])
#市值权重-----------------------------------------------------------------------------------------------------------------

#Monte Carlos MPT投资组合优化----------------------------------------------------------------------------------------------
noa = number #换投资资产时需要调整
weights = np.random.random(noa)
weights /= np.sum(weights)
np.dot(weights.T, np.dot(rets.cov() * 252, weights))

prets = []
pvols = []
for p in range(2500):
    weights = np.random.random(noa)
    weights /= np.sum(weights)
    prets.append(np.sum(rets.mean() * weights) * 252)
    pvols.append(np.sqrt(np.dot(weights.T, np.dot(rets.cov() * 252, weights))))

prets = np.array(prets)
pvols = np.array(pvols)

plt.figure(figsize=(8, 4))
plt.scatter(pvols, prets, c=prets / pvols, marker='o',cmap='viridis')# 此处无风险利率为0
# plt.grid(True)
plt.xlabel('Expected Volatility')
plt.ylabel('Expected Return')
plt.colorbar(label='Sharpe Ratio')
plt.tight_layout()
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

# 投资组合优化
# 首先建立一个方便的函数，为输入的权重向量 / 数组给出重要的投资组合统计数字：
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
    return np.array([pret, pvol, pret-0.03/ pvol])# 无风险收益


# 最优化投资组合的推导是一个约束最优化问题

# 最小化函数minimize很通用，考虑了参数的（不）等式约束和参数的范围。
# 我们从夏普指数的最大化开始。 正式地说，最小化夏普指数的负值：
def min_func_sharpe(weights):
    return -statistics(weights)[2]

# 约束是所有参数（权重）的总和为1。 这可以用minimize函数的约定表达如下
cons = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})

# 我们还将参数值（权重）限制在0和l之间。 这些值以多个元组组成的一个元组形式提供给最小化函数：
bnds = tuple((0, 1) for x in range(noa))

# 优化函数调用中忽略的唯一输入是起始参数列表（对权重的初始猜测）。我们简单地使用平均分布：
noa * [1. / noa, ]
# [0.2, 0.2, 0.2, 0.2, 0.2]

opts = sco.minimize(min_func_sharpe, noa * [1. / noa, ], method='SLSQP', bounds=bnds, constraints=cons)
# Wall time: 1.2 s
'''
opts
# fun: -0.7689821435140733
# jac: array([3.62539694e-01, 3.84121098e-01, 1.03567891e-01,
#             -1.06185675e-04, 2.67580152e-04])
# message: 'Optimization terminated successfully.'
# nfev: 59
# nit: 8
# njev: 8
# status: 0
# success: True
# x: array([2.69140628e-17, 5.93820112e-17, 0.00000000e+00,
#           7.15876612e-01, 2.84123388e-01])

opts['x'].round(3)
# array([ 0.   ,  0.   ,  0.   ,  0.716,  0.284])
'''
# 最优化工作得出 一个投资组合，仅由5种资产中的2种组成

# 使用优化中得到的投资组合权重， 得出如下统计数字
statistics(opts['x'].round(3))
# array([ 0.22201418,  0.28871174,  0.76898216])
# 预期收益率约为22.2%. 预期被动率约为28.9%， 得到的最优夏普指数为0.77

# 接下来， 我们最小化投资组合的方差。
# 这与被动率的最小化相同，我们定义一个函数对方差进行最小化：
def min_func_variance(weights):
    return statistics(weights)[1]**2

optv = sco.minimize(min_func_variance, noa * [1. / noa, ], method='SLSQP', bounds=bnds, constraints=cons)

'''
optv
# fun: 0.05137907199877911
# jac: array([0.10326265, 0.10273764, 0.10269385, 0.10276436, 0.102121])
# message: 'Optimization terminated successfully.'
# nfev: 71
# nit: 10
# njev: 10
# status: 0
# success: True
# x: array([0.04526382, 0.1335909, 0.05702634, 0.73177776, 0.03234118])

optv['x'].round(3)
# array([ 0.045,  0.134,  0.057,  0.732,  0.032])
# 投资组合中加入了全部资产。 这种组合可以得到绝对值最小方差投资组合
# 得到的预期收益率、波动率和夏普指数如下：
statistics(optv['x']).round(3)
# array([ 0.115,  0.227,  0.509])
'''


#-----------------------------------------------------------------------------------------------------------------------
def min_func_port(weights):
    return statistics(weights)[1]


# 在不同目标收益率水平（ trets ）中循环时。 最小化的一个条件会变化。
# 这就是每次循环中更新条件字典对象的原因：

trets = np.linspace(statistics(optv['x'])[0], 0.2, 50)
tvols = []
bnds = tuple((0, 1) for x in weights)
for tret in trets:
    cons = ({'type': 'eq', 'fun': lambda x: statistics(x)[0] - tret},
            {'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
    res = sco.minimize(min_func_port, noa * [1. / noa, ], method='SLSQP', bounds=bnds, constraints=cons)
    tvols.append(res['fun'])
tvols = np.array(tvols)

plt.figure(figsize=(8, 4))
# random portfolio composition
plt.scatter(pvols,prets,c=prets/pvols,marker='o')
# efficient frontier
plt.scatter(tvols,trets,c=trets/tvols,marker='x')
plt.plot(tvols,trets,c='black')
# portfolio with highest Sharpe ratio
plt.plot(statistics(opts['x'])[1],statistics(opts['x'])[0],'r*',markersize=15.0)
# minimum variance portfolio
plt.plot(statistics(optv['x'])[1],statistics(optv['x'])[0],'b*',markersize=15.0)

plt.grid(False)
plt.xlabel('Expected Volatility')
plt.ylabel('Expected Return')
plt.colorbar(label='Sharpe Ratio')


ind = np.argmin(tvols)
evols = tvols[ind:]
erets = trets[ind:]

tck = sci.splrep(evols, erets)

# 通过这条数值化路径，最终可以为有效边界定义一个连续可微函数
# 和对应的一阶导数函数df(x):

def f(x):
    """
    Efficient frontier function (splines approximation)
    :param x:
    :return:
    """
    return sci.splev(x, tck, der=0)


def df(x):
    """
    First derivative of efficient frontier function.
    :param x:
    :return:
    """
    return sci.splev(x, tck, der=1)
# 定义一个函数，返回给定参数集p=(a,b,x)
def equations(p, rf=0):
    eq1 = rf - p[0]
    eq2 = rf + p[1] * p[2] - f(p[2])
    eq3 = p[1]-df(p[2])
    return eq1,eq2,eq3

# 数值优化得到如下的值
opt=sco.fsolve(equations,[0.01,0.5,f(0.5)])
# opt
print(opt)
# array([ 0.01      ,  0.73464122,  0.29383737])
plt.figure(figsize=(8, 4))
# random portfolio composition
plt.scatter(pvols, prets, c=(prets - 0.01) / pvols, marker="o")
# efficient frontier
plt.plot(evols, erets, 'g', lw=2.5)
cx = np.linspace(0.0, 0.6)
plt.plot(cx, opt[0] + opt[1] * cx, lw=.5)
# capital market line
plt.plot(opt[2], f(opt[2]), 'r*', markersize=35.0)
plt.grid(False)
plt.xticks(np.arange(0,0.8,0.1))
plt.xlim(0,0.7)
# plt.axhline(0, color='k', ls='-', lw=2.0)
# plt.axvline(0, color='k', ls='-', lw=2.0)
plt.xlabel('Expected Volatility')
plt.ylabel('Expected Return')
plt.colorbar(label='Sharp Ratio')

# plt.savefig(r'C:/Users/徐浩然/Desktop/OP.png',dpi=400)

plt.show()
print('Done')
