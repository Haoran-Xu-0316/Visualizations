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
from statsmodels.stats.diagnostic import het_white
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
df['ESG'] = np.log(df['ESG'])
df['E'] = np.log(df['E'])
df['S'] = np.log(df['S'])
df['G'] = np.log(df['G'])
# df['interestdebt'] = np.log(df['interestdebt'])
df['vol'] = np.log(df['vol'])
# df['vol'] = df['vol']/10000
# df['cash_ratio'] = 1/df['cash_ratio']
# df['ocf_to_debt'] = 1/df['ocf_to_debt']
# df['netdebt'] = np.log(df['netdebt'])

# print(df)

#








#
#
#




# y, X = dmatrices('debt_to_assets ~ G + vol + netprofit_margin + assets_turn + cash_ratio + ocf_to_debt + eps', data=df, return_type='dataframe')
y, X = dmatrices('debt_to_assets ~ G + vol + eps + netprofit_margin + assets_turn + cash_ratio + ocf_to_debt', data=df, return_type='dataframe')
# VIF dataframe

# corr_matrix = X.corr()
#
#
# plt.figure(figsize=(12, 12))
#
# sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
#
# plt.show()
# #



vif_data = pd.DataFrame()
vif_data["feature"] = X.columns
vif_data["VIF"] = [variance_inflation_factor(X.values, i)
                   for i in range(len(X.columns))]
print(vif_data)

# y = df['debt_to_assets']
# X = sm.add_constant(X)
# plt.figure()
# plt.plot(y)
# plt.show()
mod = sm.OLS(y, X)
res = mod.fit()
print(res.summary())


LM=het_white(res.resid,  res.model.exog)
labels = ['Test Statistic', 'Test Statistic p-value', 'F-Statistic', 'F-Test p-value']
print(dict(zip(labels, LM)))





pred_ols = res.get_prediction()
iv_l = pred_ols.summary_frame()["obs_ci_lower"]
iv_u = pred_ols.summary_frame()["obs_ci_upper"]
im_l = pred_ols.summary_frame()["mean_ci_lower"]
im_u = pred_ols.summary_frame()["mean_ci_upper"]

fig, ax = plt.subplots(figsize=(10, 4))


ax.plot(y, color='royalblue',linestyle="-",alpha=0.7)
ax.plot(y, "o", label="Observations")
ax.plot(res.fittedvalues, "r--.", label="OLS",linewidth=0.8)
ax.fill_between(X.index,iv_u,iv_l,color='lightgrey',label='95% Prediction Interval')
ax.fill_between(X.index,im_u,im_l,color='grey',label='95% Confidence Interval')
ax.margins(x=0)
plt.text(2,max(iv_u)-3,'(4) Regressor: G score',fontdict={'style':'normal', 'weight':'bold'})
plt.xlim(0,300)
# plt.ylim(0,130)
# ax.plot(iv_u, "r--")
# ax.plot(iv_l, "r--")
ax.legend(loc="lower right",frameon=False,ncols=2,fontsize=11)
plt.tight_layout()
# plt.savefig(r"C:\Users\徐浩然\Desktop\Eco_Final\G_fit.svg")
plt.show()




plt.figure(figsize=(10,4))
#create instance of influence
influence = res.get_influence()
#obtain standardized residuals
standardized_residuals = influence.resid_studentized_internal
plt.scatter(df.index,standardized_residuals)
plt.xlim(0,300)
ax.margins(x=0)
plt.axhline(y=0, color='black', linestyle='--', linewidth=1)
plt.text(2,max(standardized_residuals)-0.1,'(4) Regressor: G score',fontdict={'style':'normal', 'weight':'bold'})
plt.tight_layout()
# plt.savefig(r"C:\Users\徐浩然\Desktop\Eco_Final\G_res.svg")
plt.show()




# df = df.apply(replace_outliers_with_median)

y = df['debt_to_assets']
x_cols = ['ESG' , 'E' , 'S' , 'G' , 'vol' , 'netprofit_margin' , 'assets_turn'  ,'cash_ratio'  ,'ocf_to_debt' , 'eps']
x = df[x_cols]
fig = plt.figure(figsize=(18*1.2,7*1.2))
for i in range(10):
    plt.subplot(2,5,i + 1)  # 2行3列子图
    sns.scatterplot(x=x.iloc[:, i], y=y,color='#3762AF',edgecolor='#203864')

plt.tight_layout()
# plt.savefig(r"C:\Users\徐浩然\Desktop\Eco_Final\scar.svg")
plt.show()

x_cols = ['ESG' , 'E' , 'S' , 'G' , 'vol' , 'netprofit_margin' , 'assets_turn'  ,'cash_ratio'  ,'ocf_to_debt' , 'eps','debt_to_assets']
x = df[x_cols]
x.to_excel(r'C:\Users\徐浩然\Desktop\d.xlsx')
fig = plt.figure(figsize=(18*1.5,7*1.5))
for i in range(11):
    plt.subplot(2,6,i + 1)  # 2行3列子图
    sns.boxplot(data=df.iloc[:,i].to_numpy(), orient="v",width=0.75)

    plt.ylabel(x_cols[i])
    plt.xticks([])
plt.tight_layout()
# plt.savefig(r"C:\Users\徐浩然\Desktop\Eco_Final\box.svg")
plt.show()