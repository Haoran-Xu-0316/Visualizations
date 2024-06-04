import statsmodels.api as sm
import pandas as pd
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn import linear_model
import pandas
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from patsy import dmatrices

from statsmodels.stats.outliers_influence import variance_inflation_factor

import tushare as ts
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn import linear_model

pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)


plt.rcParams['font.sans-serif'] = ['Palatino Linotype']

plt.rcParams['font.size'] = 12.5




df = pd.read_excel(r'C:\Users\徐浩然\Desktop\Eco_Final\reg_fin.xlsx',sheet_name='202223')

medians = df.median()
df = df.fillna(medians)

# 定义一个函数来检测和替换离群值
def replace_outliers_with_median(column):
    median = column.median()
    mean = column.mean()
    std = column.std()
    lower_bound = mean - 3 * std
    upper_bound = mean + 3 * std
    return column.apply(lambda x: median if x < lower_bound or x > upper_bound else x)

# 对DataFrame的每一列应用该函数
df = df.apply(replace_outliers_with_median)


# df['rt'] = (df['rt'])*252
# df.iloc[:, 1:17] = np.log(df.iloc[:, 1:17])
# df['rt'] = (df['rt'])**2
# df['ESG'] = df['ESG'])
# df['ESG'] = np.log(df['ESG'])
# df['E'] = np.log(df['E'])
# df['S'] = np.log(df['S'])
# df['G'] = np.log(df['G'])
# df['interestdebt'] = np.log(df['interestdebt'])
df['vol'] = np.log(df['vol'])
# df['netdebt'] = np.log(df['netdebt'])

# print(df)
# corr_matrix = df.corr()
#
#
# plt.figure(figsize=(8, 6))
# sns.pairplot(df)
#
# sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
#
# plt.show()
#
#








#
#
#




y, X = dmatrices('debt_to_assets ~ ESG + vol + netprofit_margin + assets_turn + cash_ratio + ocf_to_debt + eps', data=df, return_type='dataframe')
# VIF dataframe
vif_data = pd.DataFrame()
vif_data["feature"] = X.columns
vif_data["VIF"] = [variance_inflation_factor(X.values, i)
                   for i in range(len(X.columns))]
print(vif_data)

# y = df['debt_to_assets']
# X = sm.add_constant(X)
plt.figure()
plt.plot(y)
plt.show()
mod = sm.OLS(y, X)
res = mod.fit()
print(res.summary())









pred_ols = res.get_prediction()
iv_l = pred_ols.summary_frame()["obs_ci_lower"]
iv_u = pred_ols.summary_frame()["obs_ci_upper"]
im_l = pred_ols.summary_frame()["mean_ci_lower"]
im_u = pred_ols.summary_frame()["mean_ci_upper"]

fig, ax = plt.subplots(figsize=(10, 5))

ax.plot(y, "o", label="Observations")
ax.plot(y, "b-", label="Observations Line")
ax.plot(res.fittedvalues, "r--.", label="OLS")
ax.fill_between(X.index,iv_u,iv_l,color='lightgrey',label='95% Prediction Interval')
ax.fill_between(X.index,im_u,im_l,color='grey',label='95% Confidence Interval')
ax.margins(x=0)

# ax.plot(iv_u, "r--")
# ax.plot(iv_l, "r--")
ax.legend(loc="lower left",frameon=False)
plt.tight_layout()

plt.show()




plt.figure(figsize=(10,5))
#create instance of influence
influence = res.get_influence()
#obtain standardized residuals
standardized_residuals = influence.resid_studentized_internal
plt.scatter(df.index,standardized_residuals)

ax.margins(x=0)
plt.axhline(y=0, color='black', linestyle='--', linewidth=1)
plt.tight_layout()
plt.show()
