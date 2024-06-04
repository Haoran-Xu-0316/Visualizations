from arch import arch_model
import math
# import proplot

from datetime import datetime
from statsmodels.stats.diagnostic import acorr_ljungbox
import matplotlib.dates as dates
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.interpolate as sci
import scipy.optimize as sco
import seaborn as sns
df=pd.read_excel(r"C:\Users\徐浩然\Desktop\DCC-data-China\Hedging Assets\hedging assets.xlsx", sheet_name="All-log",index_col=0,parse_dates=[0])


# CSI 300	S&P 500	Bond	Gold	WTI	Bitcoin
# 012345
# 删除包含缺失值的行
df = df.dropna()

# 移除最后30行
df = df.iloc[:-30, :]

am = arch_model(df.iloc[:,5],mean='Zero',p=1,o=1,q=1)
res = am.fit()
print(res.summary())
print(res.loglikelihood,res.aic,res.bic)
# print(df.iloc[:,5])
# 提取残差
residuals = res.resid

# 进行LB检验
lb_test_stat, lb_p_value = acorr_ljungbox(residuals, lags=10)
print(f"LB test statistic: {lb_test_stat}")
print(f"LB p-value: {lb_p_value}")

# 进行ARCH检验
arch_test_stat = res.arch_lm_test(lags=10)
# print(arch_test_stat)