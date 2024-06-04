import pandas as pd
import tushare as ts
import matplotlib.pyplot as plt
pro = ts.pro_api('f9d25f4ab3f0abe5e04fdf76c32e8c8a5cc94e384774da025098ec6e')
import statsmodels.api as sm
import sys
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
from pypfopt.expected_returns import mean_historical_return
from pypfopt.risk_models import risk_matrix
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pypfopt import risk_models
from pypfopt import plotting
from pypfopt.efficient_frontier import EfficientFrontier
from pypfopt import objective_functions
plt.rcParams['font.size'] = 12
import seaborn as sns
plt.rcParams['font.family'] = 'Microsoft YaHei'
#获取进行选股的股票池


df = pd.read_excel(r'C:\Users\徐浩然\Desktop\BF\央企50&央企ESG50（加注）.xls',sheet_name='央企ESG50')

stocks_codes = df['成份券代码Constituent Code'].tolist()

print(stocks_codes)
#获取进行选股的股票池
# stocks_codes = ['603993.sh','601989.sh','601988.sh','601881.sh','601878.sh','601857.sh','601818.sh',
#               '601800.sh','601766.sh','601688.sh','601668.sh','601628.sh','601601.sh','601398.sh',
#               '601390.sh','601360.sh','601336.sh','601328.sh','601318.sh','601288.sh','601229.sh',
#               '601211.sh','601186.sh','601169.sh','601166.sh','601088.sh','601006.sh','600999.sh',
#               '600958.sh','600887.sh','600703.sh','600690.sh','600606.sh','600585.sh','600547.sh',
#               '600519.sh','600340.sh','600309.sh','600276.sh','600111.sh','600104.sh','600050.sh',
#               '600048.sh','600036.sh','600030.sh','600029.sh','600028.sh','600019.sh','600016.sh',
#               '600000.sh']

## risk free rate
rf=0.03
startdate='20210101'
enddate='20221231'

def get_price():
    price=pd.DataFrame()
    pct=pd.DataFrame()
    for i in range(len(stocks_codes)):
        k = pro.daily(ts_code=stocks_codes[i],start_date=startdate,end_date=enddate)
        k.sort_values(by="trade_date", ascending=True, inplace=True)
        per = k[["pct_chg"]]/100 ##百分比问题
        pct["%s" % stocks_codes[i]] = per
        k = k[['close']]
        price["%s" % stocks_codes[i]] = k
        price.fillna(method='ffill', axis=0, limit=30)
        pct.fillna(method='ffill', axis=0, limit=30)
    return price, pct
prices,pct = get_price()


print(pct)
mu = mean_historical_return(prices,frequency=252)
S = risk_matrix(prices,frequency=252)


ef = EfficientFrontier(mu, S)
ef.add_objective(objective_functions.L2_reg, gamma=0.1)
w = dict(ef.max_sharpe())
# print(w)
# print('+++市场组合weights+++')
# ef.save_weights_to_file("weights.txt")
# print(ef.clean_weights())
# print('+++市场组合performance+++')
# ef.portfolio_performance(verbose=True)

weighted_returns = pct.apply(lambda row: row * pd.Series(w), axis=1)
total_weighted_returns = weighted_returns.sum(axis=1)-rf
# 输出加权结果
plt.figure(figsize=(12,7))
s = pd.Series(w)
s = s[s != 0]
s_sorted = s.sort_values()
print(s_sorted)
sl=s_sorted.index.tolist()
s_sorted = s_sorted.reset_index(drop=True)
s_sorted.plot.barh(color='slategrey')
plt.yticks(range(len(s_sorted)), sl)
plt.tight_layout()
plt.savefig(r'C:/Users/徐浩然/Desktop/BF/权重_央企_E.svg', dpi=400)
# plt.plot(total_weighted_returns)
#plt.show()





fig, ax = plt.subplots(figsize=(12,7))

ef = EfficientFrontier(mu, S)
ef.add_objective(objective_functions.L2_reg, gamma=0.1)

ef_max_sharpe = ef.deepcopy()

# Find the tangency portfolio
ef_max_sharpe.max_sharpe()
ret_tangent, std_tangent, _ = ef_max_sharpe.portfolio_performance()

risk_range = np.linspace(0.0, 0.80, 100)
plotting.plot_efficient_frontier(ef, ax=ax, show_assets=True,facecolor='red')

for line in ax.lines:
    line.set_color('#203864')
ax.scatter(std_tangent, ret_tangent, marker="*", s=200, c="darkred", zorder=4)
# Generate random portfolios
n_samples = 10000
w = np.random.dirichlet(np.ones(ef.n_assets), n_samples)
rets = w.dot(ef.expected_returns)
stds = np.sqrt(np.diag(w @ ef.cov_matrix @ w.T))
sharpes = (rets-rf) / stds
x=np.linspace(0, 0.5, 10)
ax.plot(x, ((ret_tangent-rf)/std_tangent)*x+rf,color='peru')
ax.scatter(stds, rets, marker=".", c=sharpes, cmap="RdBu",s=15)
ax.set_xlabel('波动率')
ax.set_ylabel('收益率')
ax.set_xlim(xmin=0)
ax.legend(['有效前沿','资产','最大夏普比率','资本市场线'],frameon=False)
plt.tight_layout()
plt.savefig(r'C:/Users/徐浩然/Desktop/BF/组合_央企_E.svg', dpi=400)
#plt.show()






# 将股票分为六个组
def group_stocks(stocks, date):
    # 划分大小市值
    list_mv = []
    df_stocks = pd.DataFrame()
    count = 0
    for i in stocks:
        count += 1
        a = pro.daily_basic(ts_code=i, trade_date=date)
        print(a)
        a = a["circ_mv"].values

        list_mv.append(float(a))
        print("第%d支股票市值计算完成" % count)
    df_stocks["code"] = stocks_codes
    df_stocks["mv"] = list_mv
    df_stocks["SB"] = df_stocks["mv"].map(lambda x: "B" if x > df_stocks["mv"].median() else "S")

    # 划分高中低账面市值比
    list_bm = []
    count = 0
    for i in stocks_codes:
        count += 1
        b = pro.daily_basic(ts_code=i, trade_date=date)
        b = 1 / b["pb"].values
        list_bm.append(float(b))
        print("第%d支股票账面市值比计算完成" % count)
    df_stocks["bm"] = list_bm
    df_stocks["HML"] = df_stocks["bm"].apply(lambda x: "H" if x >= df_stocks["bm"].quantile(0.7)
    else ("L" if x <= df_stocks["bm"].quantile(0.3) else "M"))

    return df_stocks

df_stocks=group_stocks(stocks_codes,20211231)





#分别计算六个组的日收益率
def groups_return(stocks,start,end):
    SL = stocks[stocks["SB"].isin(["S"])&stocks["HML"].isin(["L"])].code.tolist()
    sum_SL = df_stocks[df_stocks["SB"].isin(["S"])&df_stocks["HML"].isin(["L"])]["mv"].sum()
    SM = stocks[stocks["SB"].isin(["S"])&stocks["HML"].isin(["M"])].code.tolist()
    sum_SM = df_stocks[df_stocks["SB"].isin(["S"])&df_stocks["HML"].isin(["M"])]["mv"].sum()
    SH = stocks[stocks["SB"].isin(["S"])&stocks["HML"].isin(["H"])].code.tolist()
    sum_SH = df_stocks[df_stocks["SB"].isin(["S"])&df_stocks["HML"].isin(["H"])]["mv"].sum()
    BL = stocks[stocks["SB"].isin(["B"])&stocks["HML"].isin(["L"])].code.tolist()
    sum_BL = df_stocks[df_stocks["SB"].isin(["B"])&df_stocks["HML"].isin(["L"])]["mv"].sum()
    BM = stocks[stocks["SB"].isin(["B"])&stocks["HML"].isin(["M"])].code.tolist()
    sum_BM = df_stocks[df_stocks["SB"].isin(["B"])&df_stocks["HML"].isin(["M"])]["mv"].sum()
    BH = stocks[stocks["SB"].isin(["B"])&stocks["HML"].isin(["H"])].code.tolist()
    sum_BH = df_stocks[df_stocks["SB"].isin(["B"])&df_stocks["HML"].isin(["H"])]["mv"].sum()
    groups = [SL,SM,SH,BL,BM,BH]
    sums = [sum_SL,sum_SM,sum_SH,sum_BL,sum_BM,sum_BH]
    groups_names = ["SL","SM","SH","BL","BM","BH"]
    df_groups = pd.DataFrame(columns=groups_names)
    count=0
    for group in groups:
        df1 = pd.DataFrame()


        for i in range(len(group)):

            data = pro.daily(ts_code=group[i],start_date=start,end_date=end)
            data.fillna(method='ffill', axis=0, limit=30)
            data.sort_values(by="trade_date",inplace=True)
            data = data["pct_chg"]*df_stocks["mv"][i]


            df1[group[i]] = data
        df_groups[groups_names[count]] = df1.apply(lambda x:x.sum()/sums[count],axis=1)/100

        print("%s组计算完成"%groups_names[count])
        count += 1

    return df_groups

gr=groups_return(df_stocks,startdate,enddate)
# print(gr)

#计算每日SMB，HML
def SMB_HML(data):
    data["SMB"] = (data["SL"]+data["SM"]+data["SH"])/3-(data["BL"]+data["BM"]+data["BH"])/3
    data["HML"] = (data["SH"]+data["BH"])/2-(data["SL"]+data["BL"])/2

    return data


data=SMB_HML(gr)
# print(data)




def selection(data,start,end,stocks_codes):
    MKT = pro.index_daily(ts_code="000016.SH",start_date=start,end_date=end)##获取市场组合price
    MKT.fillna(method='ffill', axis=0, limit=30)
    MKT.sort_values(by="trade_date",ascending=True,inplace=True)
    plt.plot(MKT["close"])
    #plt.show()
    plt.plot(total_weighted_returns)
    #plt.show()


    MKT = (MKT["pct_chg"]/100-rf).tolist() ##计算市场组合收益率
    # MKT = total_weighted_returns ##计算行为市场组合收益率
    plt.plot(MKT)
    #plt.show()
    print(len(MKT))
    print(data)

    data["MKT"] = MKT
    print(data)
    data = data.iloc[10:470]
    data.drop(data.columns[0:6],axis=1,inplace=True)
    data.fillna(method='ffill', axis=0, limit=30)

    for i in range(len(stocks_codes)):
        a = pro.daily(ts_code=stocks_codes[i],start_date=start,end_date=end)
        a.fillna(method='ffill', axis=0, limit=30)
        a=a.iloc[10:470]
        print(a)
        a.sort_values(by="trade_date", ascending=True, inplace=True)
        a = (a["pct_chg"] / 100 - rf).tolist()
        data["%s" % stocks_codes[i]] = a

    return data


# sys.stdout = open(r'C:\Users\徐浩然\Desktop\BF\output_C_N.txt', 'w')


df_final=selection(data,startdate,enddate,stocks_codes)
print(df_final)
# print(df_final)
#回归找出阿尔法最大的股票组合
def OLS(df_final,Name):
    results = pd.DataFrame(columns=['MKT_Coefficient'], index=stocks_codes)
    stocks_return = df_final.iloc[:,3:53]
    # print(stocks_return)
    CAR = pd.DataFrame()
    for i in range(len(stocks_return.columns)):
        # print(i)
        x = df_final.iloc[:,0:3]
        y = stocks_return.iloc[:,i]
        X = sm.add_constant(x)
        model = sm.OLS(y,X)
        result = model.fit()
        print(result.summary())

        results.loc[stocks_codes[i], 'MKT_Coefficient'] = result.params['MKT']
        y_fitted = result.fittedvalues
        # fig, ax = plt.subplots(figsize=(8, 6))
        # ax.plot(x, y, 'o', label='data')
        # ax.plot(x, y_fitted, 'r--.', label='OLS')
        # ax.legend(loc='best')
        CAR[stocks_codes[i]] = (y - y_fitted).cumsum()
        row_means = CAR.mean(axis=1)
        CAR['Mean'] = row_means

        print(i)
    print(CAR)
    plt.figure(figsize=(12,7))
    sns.lineplot(CAR,legend=False,palette='RdBu')
    sns.lineplot(CAR['Mean'], legend=False, color='k',linewidth=2)
    plt.ylabel('CAR/CAAR')
    plt.margins(x=0)
    plt.tight_layout()
    plt.savefig(r'C:/Users/徐浩然/Desktop/BF/宏观CAR_{}.svg'.format(Name), dpi=400)
    #plt.show()
    CAR.to_excel(r'C:\Users\徐浩然\Desktop\BF\CAR_{}.xls'.format(Name))
    # results.columns = stocks_return.columns
    # results.rename(index={"const":"Alpha"},inplace=True)
    # z =results.sort_values(by="Alpha",axis=1,ascending=False)
    # stocks_lists = z.columns.values.tolist()
    # top_stocks = stocks_lists[:10]
    # return top_stocks

    return results
# beta=OLS(df_final,"C_ESG")
# beta=OLS(df_final,"C_NESG")
# beta=OLS(df_final,"B_ESG")
beta=OLS(df_final,"B_NESG")
# sys.stdout = sys.__stdout__
print(beta)
#
