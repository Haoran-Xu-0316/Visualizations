
from pypfopt.expected_returns import mean_historical_return
from pypfopt.risk_models import risk_matrix
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pypfopt import risk_models
from pypfopt import plotting
from pypfopt.efficient_frontier import EfficientFrontier
from pypfopt import objective_functions




rf=0.02
plt.rcParams['font.family'] = 'Microsoft YaHei'
# 读取CSV文件
import pandas as pd
import tushare as ts
import matplotlib.pyplot as plt
pro = ts.pro_api('d689cb3c1d8c8a618e49ca0bb64f4d6de2f70e28ab5f76a867b31ac7')
import statsmodels.api as sm

from pypfopt.expected_returns import mean_historical_return
from pypfopt.risk_models import risk_matrix
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pypfopt import risk_models
from pypfopt import plotting
from pypfopt.efficient_frontier import EfficientFrontier
from pypfopt import objective_functions
import seaborn as sns
plt.rcParams['font.family'] = 'Microsoft YaHei'
#获取进行选股的股票池
#获取进行选股的股票池
stocks_codes = ['603993.sh','601989.sh','601988.sh','601881.sh','601878.sh','601857.sh','601818.sh',
              '601800.sh','601766.sh','601688.sh','601668.sh','601628.sh','601601.sh','601398.sh',
              '601390.sh','601360.sh','601336.sh','601328.sh','601318.sh','601288.sh','601229.sh',
              '601211.sh','601186.sh','601169.sh','601166.sh','601088.sh','601006.sh','600999.sh',
              '600958.sh','600887.sh','600703.sh','600690.sh','600606.sh','600585.sh','600547.sh',
              '600519.sh','600340.sh','600309.sh','600276.sh','600111.sh','600104.sh','600050.sh',
              '600048.sh','600036.sh','600030.sh','600029.sh','600028.sh','600019.sh','600016.sh',
              '600000.sh']

## risk free rate
rf=0.035
startdate='20230101'
enddate='20231231'

def get_price():
    price=pd.DataFrame()
    for i in range(len(stocks_codes)):
        k = pro.daily(ts_code=stocks_codes[i],start_date=startdate,end_date=enddate)
        k.sort_values(by="trade_date", ascending=True, inplace=True)
        k = k[['close']]
        price["%s" % stocks_codes[i]] = k
    return price
prices=get_price()

# print(df)
mu = mean_historical_return(prices,frequency=252)
S = risk_matrix(prices,frequency=252)

print(mu)


fig, ax = plt.subplots(figsize=(8,5))

ef = EfficientFrontier(mu, S)
w = ef.max_sharpe()
print('+++市场组合weights+++')
print(ef.clean_weights())
print('+++市场组合performance+++')
ef.portfolio_performance(verbose=True)

ef_max_sharpe = ef.deepcopy()

# Find the tangency portfolio
ef_max_sharpe.max_sharpe()
ret_tangent, std_tangent, _ = ef_max_sharpe.portfolio_performance()

risk_range = np.linspace(0.0, 0.80, 100)
plotting.plot_efficient_frontier(ef, ax=ax, show_assets=False,color='red')

for line in ax.lines:
    line.set_color('darkblue')
ax.scatter(std_tangent, ret_tangent, marker="*", s=100, c="darkred", zorder=4)
# Generate random portfolios
n_samples = 10000
w = np.random.dirichlet(np.ones(ef.n_assets), n_samples)
rets = w.dot(ef.expected_returns)
stds = np.sqrt(np.diag(w @ ef.cov_matrix @ w.T))
sharpes = (rets-rf) / stds
x=np.linspace(0, 0.5, 10)
ax.plot(x, ((ret_tangent-rf)/std_tangent)*x+rf)
ax.scatter(stds, rets, marker=".", c=sharpes, cmap="viridis")

ax.set_xlim(xmin=0)
ax.legend(['有效前沿','最大夏普比率','资本市场线'],frameon=False)
plt.tight_layout()
# plt.savefig("ef_scatter.png", dpi=200)
plt.show()