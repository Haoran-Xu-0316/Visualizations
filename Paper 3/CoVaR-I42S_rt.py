import math
# import proplot
from datetime import datetime

import matplotlib.dates as dates
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.interpolate as sci
import scipy.optimize as sco
import seaborn as sns

#全局设置-----------------------------------------------------------------------------------------------------------------
plt.rcParams['font.sans-serif'] = ['Palatino Linotype']
# plt.rcParams["font.weight"] = "bold"
plt.rcParams['font.size'] = 13
plt.rcParams['axes.unicode_minus'] = True
plt.rcParams['lines.linewidth'] = 0.8
plt.rcParams['axes.xmargin'] = 0

pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
plt.rcParams['axes.labelsize'] = 0
yHE=pd.read_excel(r'C:\Users\徐浩然\Desktop\P4 ESG\CoVaR.xlsx', sheet_name='HE',index_col=0,parse_dates=[0])
nHE=pd.read_excel(r'C:\Users\徐浩然\Desktop\P4 NOESG\CoVaR.xlsx', sheet_name='HE',index_col=0,parse_dates=[0])
yDB=pd.read_excel(r'C:\Users\徐浩然\Desktop\P4 ESG\CoVaR.xlsx', sheet_name='DB',index_col=0,parse_dates=[0])
nDB=pd.read_excel(r'C:\Users\徐浩然\Desktop\P4 NOESG\CoVaR.xlsx', sheet_name='DB',index_col=0,parse_dates=[0])
yFF=pd.read_excel(r'C:\Users\徐浩然\Desktop\P4 ESG\CoVaR.xlsx', sheet_name='FF',index_col=0,parse_dates=[0])
nFF=pd.read_excel(r'C:\Users\徐浩然\Desktop\P4 NOESG\CoVaR.xlsx', sheet_name='FF',index_col=0,parse_dates=[0])
yII=pd.read_excel(r'C:\Users\徐浩然\Desktop\P4 ESG\CoVaR.xlsx', sheet_name='II',index_col=0,parse_dates=[0])
nII=pd.read_excel(r'C:\Users\徐浩然\Desktop\P4 NOESG\CoVaR.xlsx', sheet_name='II',index_col=0,parse_dates=[0])
yST=pd.read_excel(r'C:\Users\徐浩然\Desktop\P4 ESG\CoVaR.xlsx', sheet_name='ST',index_col=0,parse_dates=[0])
nST=pd.read_excel(r'C:\Users\徐浩然\Desktop\P4 NOESG\CoVaR.xlsx', sheet_name='ST',index_col=0,parse_dates=[0])
yCP=pd.read_excel(r'C:\Users\徐浩然\Desktop\P4 ESG\CoVaR.xlsx', sheet_name='CP',index_col=0,parse_dates=[0])
nCP=pd.read_excel(r'C:\Users\徐浩然\Desktop\P4 NOESG\CoVaR.xlsx', sheet_name='CP',index_col=0,parse_dates=[0])
yFS=pd.read_excel(r'C:\Users\徐浩然\Desktop\P4 ESG\CoVaR.xlsx', sheet_name='FS',index_col=0,parse_dates=[0])
nFS=pd.read_excel(r'C:\Users\徐浩然\Desktop\P4 NOESG\CoVaR.xlsx', sheet_name='FS',index_col=0,parse_dates=[0])
yFC=pd.read_excel(r'C:\Users\徐浩然\Desktop\P4 ESG\CoVaR.xlsx', sheet_name='FC',index_col=0,parse_dates=[0])
nFC=pd.read_excel(r'C:\Users\徐浩然\Desktop\P4 NOESG\CoVaR.xlsx', sheet_name='FC',index_col=0,parse_dates=[0])
yAM=pd.read_excel(r'C:\Users\徐浩然\Desktop\P4 ESG\CoVaR.xlsx', sheet_name='AM',index_col=0,parse_dates=[0])
nAM=pd.read_excel(r'C:\Users\徐浩然\Desktop\P4 NOESG\CoVaR.xlsx', sheet_name='AM',index_col=0,parse_dates=[0])
ySS=pd.read_excel(r'C:\Users\徐浩然\Desktop\P4 ESG\CoVaR.xlsx', sheet_name='SS',index_col=0,parse_dates=[0])
nSS=pd.read_excel(r'C:\Users\徐浩然\Desktop\P4 NOESG\CoVaR.xlsx', sheet_name='SS',index_col=0,parse_dates=[0])

RT=pd.read_excel(r'C:\Users\徐浩然\Desktop\P4 Data\rt.xlsx', sheet_name='rt',index_col=0,parse_dates=[0])
#HE	DB	FF	II	ST	CP	FS	FC	AM	SS	NOESG	ESG
HE=RT['HE']
DB=RT['DB']
FF=RT['FF']
II=RT['II']
ST=RT['ST']
CP=RT['CP']
FS=RT['FS']
FC=RT['FC']
AM=RT['AM']
SS=RT['SS']
ESG=RT['ESG']
NESG=RT['NESG']
##
#46085B
#433D85
#3A688A
#3C9289
#53B578
#97D34F
#F1E543
C_1=['#3A688A']
C_2=['#46085B']
C_3=['#F1E543']
C_4=['#53B578']
C1=['#1E3350']
C2=['#7A1F17']
a=0.4
ll=0
sss=3
gg='#E7E6E6'
pr={'style':'italic','weight':'bold'}

plt.subplots(figsize=(18,25))


plt.subplot(10,4,1)
sns.scatterplot(ESG,s=sss, edgecolor='none', color=gg)
sns.lineplot(yHE[['VaRD2','VaRU2']],palette=C_1,dashes=False,legend=False)
sns.lineplot(yHE[['CoVaRD2','CoVaRU2']],palette=C_2,dashes=False,legend=False)
sns.lineplot(yHE[['CBMD2','CBMU2']],palette=C_3,dashes=False,legend=False)
sns.lineplot(yHE[['deltaCDw2','deltaCUp2']],palette=C_4,dashes=False,legend=False)
plt.legend(['HE - ESG'],frameon=False,loc='upper right',handlelength=0,prop=pr)
plt.xlabel('')
plt.ylabel('')
legend_handle = plt.gca().get_legend().legendHandles[0]
legend_handle.set_visible(False)
plt.subplot(10,4,2)
sns.lineplot(yHE[['deltaCDw2_pct']],palette=C1,dashes=False,legend=False)
sns.lineplot(yHE[['deltaCUp2_pct']],palette=C2,dashes=False,legend=False)

plt.subplot(10,4,3)
sns.scatterplot(NESG,s=sss, edgecolor='none', color=gg)
sns.lineplot(nHE[['VaRD2','VaRU2']],palette=C_1,dashes=False,legend=False)
sns.lineplot(nHE[['CoVaRD2','CoVaRU2']],palette=C_2,dashes=False,legend=False)
sns.lineplot(nHE[['CBMD2','CBMU2']],palette=C_3,dashes=False,legend=False)
sns.lineplot(nHE[['deltaCDw2','deltaCUp2']],palette=C_4,dashes=False,legend=False)
plt.legend(['HE - NESG'],frameon=False,loc='upper right',handlelength=0,prop=pr)
plt.xlabel('')
plt.ylabel('')
legend_handle = plt.gca().get_legend().legendHandles[0]
legend_handle.set_visible(False)
plt.subplot(10,4,4)
sns.lineplot(nHE[['deltaCDw2_pct']],palette=C1,dashes=False,legend=False)
sns.lineplot(nHE[['deltaCUp2_pct']],palette=C2,dashes=False,legend=False)






plt.subplot(10,4,5)
sns.scatterplot(ESG,s=sss, edgecolor='none', color=gg)
sns.lineplot(yDB[['VaRD2','VaRU2']],palette=C_1,dashes=False,legend=False)
sns.lineplot(yDB[['CoVaRD2','CoVaRU2']],palette=C_2,dashes=False,legend=False)
sns.lineplot(yDB[['CBMD2','CBMU2']],palette=C_3,dashes=False,legend=False)
sns.lineplot(yDB[['deltaCDw2','deltaCUp2']],palette=C_4,dashes=False,legend=False)
plt.legend(['DB - ESG'],frameon=False,loc='upper right',handlelength=0,prop=pr)
plt.xlabel('')
plt.ylabel('')
legend_handle = plt.gca().get_legend().legendHandles[0]
legend_handle.set_visible(False)
plt.subplot(10,4,6)
sns.lineplot(yDB[['deltaCDw2_pct']],palette=C1,dashes=False,legend=False)
sns.lineplot(yDB[['deltaCUp2_pct']],palette=C2,dashes=False,legend=False)

plt.subplot(10,4,7)
sns.scatterplot(NESG,s=sss, edgecolor='none', color=gg)
sns.lineplot(nDB[['VaRD2','VaRU2']],palette=C_1,dashes=False,legend=False)
sns.lineplot(nDB[['CoVaRD2','CoVaRU2']],palette=C_2,dashes=False,legend=False)
sns.lineplot(nDB[['CBMD2','CBMU2']],palette=C_3,dashes=False,legend=False)
sns.lineplot(nDB[['deltaCDw2','deltaCUp2']],palette=C_4,dashes=False,legend=False)
plt.legend(['DB - NESG'],frameon=False,loc='upper right',handlelength=0,prop=pr)
plt.xlabel('')
plt.ylabel('')
legend_handle = plt.gca().get_legend().legendHandles[0]
legend_handle.set_visible(False)
plt.subplot(10,4,8)
sns.lineplot(nDB[['deltaCDw2_pct']],palette=C1,dashes=False,legend=False)
sns.lineplot(nDB[['deltaCUp2_pct']],palette=C2,dashes=False,legend=False)








plt.subplot(10,4,9)
sns.scatterplot(ESG,s=sss, edgecolor='none', color=gg)
sns.lineplot(yFF[['VaRD2','VaRU2']],palette=C_1,dashes=False,legend=False)
sns.lineplot(yFF[['CoVaRD2','CoVaRU2']],palette=C_2,dashes=False,legend=False)
sns.lineplot(yFF[['CBMD2','CBMU2']],palette=C_3,dashes=False,legend=False)
sns.lineplot(yFF[['deltaCDw2','deltaCUp2']],palette=C_4,dashes=False,legend=False)
plt.legend(['FF - ESG'],frameon=False,loc='upper right',handlelength=0,prop=pr)
plt.xlabel('')
plt.ylabel('')
legend_handle = plt.gca().get_legend().legendHandles[0]
legend_handle.set_visible(False)
plt.subplot(10,4,10)
sns.lineplot(yFF[['deltaCDw2_pct']],palette=C1,dashes=False,legend=False)
sns.lineplot(yFF[['deltaCUp2_pct']],palette=C2,dashes=False,legend=False)

plt.subplot(10,4,11)
sns.scatterplot(NESG,s=sss, edgecolor='none', color=gg)
sns.lineplot(nFF[['VaRD2','VaRU2']],palette=C_1,dashes=False,legend=False)
sns.lineplot(nFF[['CoVaRD2','CoVaRU2']],palette=C_2,dashes=False,legend=False)
sns.lineplot(nFF[['CBMD2','CBMU2']],palette=C_3,dashes=False,legend=False)
sns.lineplot(nFF[['deltaCDw2','deltaCUp2']],palette=C_4,dashes=False,legend=False)
plt.legend(['FF - NESG'],frameon=False,loc='upper right',handlelength=0,prop=pr)
plt.xlabel('')
plt.ylabel('')
legend_handle = plt.gca().get_legend().legendHandles[0]
legend_handle.set_visible(False)
plt.subplot(10,4,12)
sns.lineplot(nFF[['deltaCDw2_pct']],palette=C1,dashes=False,legend=False)
sns.lineplot(nFF[['deltaCUp2_pct']],palette=C2,dashes=False,legend=False)









plt.subplot(10,4,13)
sns.scatterplot(ESG,s=sss, edgecolor='none', color=gg)
sns.lineplot(yII[['VaRD2','VaRU2']],palette=C_1,dashes=False,legend=False)
sns.lineplot(yII[['CoVaRD2','CoVaRU2']],palette=C_2,dashes=False,legend=False)
sns.lineplot(yII[['CBMD2','CBMU2']],palette=C_3,dashes=False,legend=False)
sns.lineplot(yII[['deltaCDw2','deltaCUp2']],palette=C_4,dashes=False,legend=False)
plt.legend(['II - ESG'],frameon=False,loc='upper right',handlelength=0,prop=pr)
plt.xlabel('')
plt.ylabel('')
legend_handle = plt.gca().get_legend().legendHandles[0]
legend_handle.set_visible(False)
plt.subplot(10,4,14)
sns.lineplot(yII[['deltaCDw2_pct']],palette=C1,dashes=False,legend=False)
sns.lineplot(yII[['deltaCUp2_pct']],palette=C2,dashes=False,legend=False)

plt.subplot(10,4,15)
sns.scatterplot(NESG,s=sss, edgecolor='none', color=gg)
sns.lineplot(nII[['VaRD2','VaRU2']],palette=C_1,dashes=False,legend=False)
sns.lineplot(nII[['CoVaRD2','CoVaRU2']],palette=C_2,dashes=False,legend=False)
sns.lineplot(nII[['CBMD2','CBMU2']],palette=C_3,dashes=False,legend=False)
sns.lineplot(nII[['deltaCDw2','deltaCUp2']],palette=C_4,dashes=False,legend=False)
plt.legend(['II - NESG'],frameon=False,loc='upper right',handlelength=0,prop=pr)
plt.xlabel('')
plt.ylabel('')
legend_handle = plt.gca().get_legend().legendHandles[0]
legend_handle.set_visible(False)
plt.subplot(10,4,16)
sns.lineplot(nII[['deltaCDw2_pct']],palette=C1,dashes=False,legend=False)
sns.lineplot(nII[['deltaCUp2_pct']],palette=C2,dashes=False,legend=False)









plt.subplot(10,4,17)
sns.scatterplot(ESG,s=sss, edgecolor='none', color=gg)
sns.lineplot(yST[['VaRD2','VaRU2']],palette=C_1,dashes=False,legend=False)
sns.lineplot(yST[['CoVaRD2','CoVaRU2']],palette=C_2,dashes=False,legend=False)
sns.lineplot(yST[['CBMD2','CBMU2']],palette=C_3,dashes=False,legend=False)
sns.lineplot(yST[['deltaCDw2','deltaCUp2']],palette=C_4,dashes=False,legend=False)
plt.legend(['ST - ESG'],frameon=False,loc='upper right',handlelength=0,prop=pr)
plt.xlabel('')
plt.ylabel('')
legend_handle = plt.gca().get_legend().legendHandles[0]
legend_handle.set_visible(False)
plt.subplot(10,4,18)
sns.lineplot(yST[['deltaCDw2_pct']],palette=C1,dashes=False,legend=False)
sns.lineplot(yST[['deltaCUp2_pct']],palette=C2,dashes=False,legend=False)

plt.subplot(10,4,19)
sns.scatterplot(NESG,s=sss, edgecolor='none', color=gg)
sns.lineplot(nST[['VaRD2','VaRU2']],palette=C_1,dashes=False,legend=False)
sns.lineplot(nST[['CoVaRD2','CoVaRU2']],palette=C_2,dashes=False,legend=False)
sns.lineplot(nST[['CBMD2','CBMU2']],palette=C_3,dashes=False,legend=False)
sns.lineplot(nST[['deltaCDw2','deltaCUp2']],palette=C_4,dashes=False,legend=False)
plt.legend(['ST - NESG'],frameon=False,loc='upper right',handlelength=0,prop=pr)
plt.xlabel('')
plt.ylabel('')
legend_handle = plt.gca().get_legend().legendHandles[0]
legend_handle.set_visible(False)
plt.subplot(10,4,20)
sns.lineplot(nST[['deltaCDw2_pct']],palette=C1,dashes=False,legend=False)
sns.lineplot(nST[['deltaCUp2_pct']],palette=C2,dashes=False,legend=False)








plt.subplot(10,4,21)
sns.scatterplot(ESG,s=sss, edgecolor='none', color=gg)
sns.lineplot(yCP[['VaRD2','VaRU2']],palette=C_1,dashes=False,legend=False)
sns.lineplot(yCP[['CoVaRD2','CoVaRU2']],palette=C_2,dashes=False,legend=False)
sns.lineplot(yCP[['CBMD2','CBMU2']],palette=C_3,dashes=False,legend=False)
sns.lineplot(yCP[['deltaCDw2','deltaCUp2']],palette=C_4,dashes=False,legend=False)
plt.legend(['CP - ESG'],frameon=False,loc='upper right',handlelength=0,prop=pr)
plt.xlabel('')
plt.ylabel('')
legend_handle = plt.gca().get_legend().legendHandles[0]
legend_handle.set_visible(False)
plt.subplot(10,4,22)
sns.lineplot(yCP[['deltaCDw2_pct']],palette=C1,dashes=False,legend=False)
sns.lineplot(yCP[['deltaCUp2_pct']],palette=C2,dashes=False,legend=False)

plt.subplot(10,4,23)
sns.scatterplot(NESG,s=sss, edgecolor='none', color=gg)
sns.lineplot(nCP[['VaRD2','VaRU2']],palette=C_1,dashes=False,legend=False)
sns.lineplot(nCP[['CoVaRD2','CoVaRU2']],palette=C_2,dashes=False,legend=False)
sns.lineplot(nCP[['CBMD2','CBMU2']],palette=C_3,dashes=False,legend=False)
sns.lineplot(nCP[['deltaCDw2','deltaCUp2']],palette=C_4,dashes=False,legend=False)
plt.legend(['CP - NESG'],frameon=False,loc='upper right',handlelength=0,prop=pr)
plt.xlabel('')
plt.ylabel('')
legend_handle = plt.gca().get_legend().legendHandles[0]
legend_handle.set_visible(False)
plt.subplot(10,4,24)
sns.lineplot(nCP[['deltaCDw2_pct']],palette=C1,dashes=False,legend=False)
sns.lineplot(nCP[['deltaCUp2_pct']],palette=C2,dashes=False,legend=False)










plt.subplot(10,4,25)
sns.scatterplot(ESG,s=sss, edgecolor='none', color=gg)
sns.lineplot(yFS[['VaRD2','VaRU2']],palette=C_1,dashes=False,legend=False)
sns.lineplot(yFS[['CoVaRD2','CoVaRU2']],palette=C_2,dashes=False,legend=False)
sns.lineplot(yFS[['CBMD2','CBMU2']],palette=C_3,dashes=False,legend=False)
sns.lineplot(yFS[['deltaCDw2','deltaCUp2']],palette=C_4,dashes=False,legend=False)
plt.legend(['FS - ESG'],frameon=False,loc='upper right',handlelength=0,prop=pr)
plt.xlabel('')
plt.ylabel('')
legend_handle = plt.gca().get_legend().legendHandles[0]
legend_handle.set_visible(False)

plt.subplot(10,4,26)
sns.lineplot(yFS[['deltaCDw2_pct']],palette=C1,dashes=False,legend=False)
sns.lineplot(yFS[['deltaCUp2_pct']],palette=C2,dashes=False,legend=False)

plt.subplot(10,4,27)
sns.scatterplot(NESG,s=sss, edgecolor='none', color=gg)
sns.lineplot(nFS[['VaRD2','VaRU2']],palette=C_1,dashes=False,legend=False)
sns.lineplot(nFS[['CoVaRD2','CoVaRU2']],palette=C_2,dashes=False,legend=False)
sns.lineplot(nFS[['CBMD2','CBMU2']],palette=C_3,dashes=False,legend=False)
sns.lineplot(nFS[['deltaCDw2','deltaCUp2']],palette=C_4,dashes=False,legend=False)
plt.legend(['FS - ESG'],frameon=False,loc='upper right',handlelength=0,prop=pr)
plt.xlabel('')
plt.ylabel('')
legend_handle = plt.gca().get_legend().legendHandles[0]
legend_handle.set_visible(False)
plt.subplot(10,4,28)
sns.lineplot(nFS[['deltaCDw2_pct']],palette=C1,dashes=False,legend=False)
sns.lineplot(nFS[['deltaCUp2_pct']],palette=C2,dashes=False,legend=False)









plt.subplot(10,4,29)
sns.scatterplot(ESG,s=sss, edgecolor='none', color=gg)
sns.lineplot(yFC[['VaRD2','VaRU2']],palette=C_1,dashes=False,legend=False)
sns.lineplot(yFC[['CoVaRD2','CoVaRU2']],palette=C_2,dashes=False,legend=False)
sns.lineplot(yFC[['CBMD2','CBMU2']],palette=C_3,dashes=False,legend=False)
sns.lineplot(yFC[['deltaCDw2','deltaCUp2']],palette=C_4,dashes=False,legend=False)
plt.legend(['FC - ESG'],frameon=False,loc='upper right',handlelength=0,prop=pr)
plt.xlabel('')
plt.ylabel('')
legend_handle = plt.gca().get_legend().legendHandles[0]
legend_handle.set_visible(False)
plt.subplot(10,4,30)
sns.lineplot(yFC[['deltaCDw2_pct']],palette=C1,dashes=False,legend=False)
sns.lineplot(yFC[['deltaCUp2_pct']],palette=C2,dashes=False,legend=False)

plt.subplot(10,4,31)
sns.scatterplot(NESG,s=sss, edgecolor='none', color=gg)
sns.lineplot(nFC[['VaRD2','VaRU2']],palette=C_1,dashes=False,legend=False)
sns.lineplot(nFC[['CoVaRD2','CoVaRU2']],palette=C_2,dashes=False,legend=False)
sns.lineplot(nFC[['CBMD2','CBMU2']],palette=C_3,dashes=False,legend=False)
sns.lineplot(nFC[['deltaCDw2','deltaCUp2']],palette=C_4,dashes=False,legend=False)
plt.legend(['FC - NESG'],frameon=False,loc='upper right',handlelength=0,prop=pr)
plt.xlabel('')
plt.ylabel('')
legend_handle = plt.gca().get_legend().legendHandles[0]
legend_handle.set_visible(False)
plt.subplot(10,4,32)
sns.lineplot(nFC[['deltaCDw2_pct']],palette=C1,dashes=False,legend=False)
sns.lineplot(nFC[['deltaCUp2_pct']],palette=C2,dashes=False,legend=False)







plt.subplot(10,4,33)
sns.scatterplot(ESG,s=sss, edgecolor='none', color=gg)
sns.lineplot(yAM[['VaRD2','VaRU2']],palette=C_1,dashes=False,legend=False)
sns.lineplot(yAM[['CoVaRD2','CoVaRU2']],palette=C_2,dashes=False,legend=False)
sns.lineplot(yAM[['CBMD2','CBMU2']],palette=C_3,dashes=False,legend=False)
sns.lineplot(yAM[['deltaCDw2','deltaCUp2']],palette=C_4,dashes=False,legend=False)
plt.legend(['AM - ESG'],frameon=False,loc='upper right',handlelength=0,prop=pr)
plt.xlabel('')
plt.ylabel('')
legend_handle = plt.gca().get_legend().legendHandles[0]
legend_handle.set_visible(False)
plt.subplot(10,4,34)
sns.lineplot(yAM[['deltaCDw2_pct']],palette=C1,dashes=False,legend=False)
sns.lineplot(yAM[['deltaCUp2_pct']],palette=C2,dashes=False,legend=False)

plt.subplot(10,4,35)
sns.scatterplot(NESG,s=sss, edgecolor='none', color=gg)
sns.lineplot(nAM[['VaRD2','VaRU2']],palette=C_1,dashes=False,legend=False)
sns.lineplot(nAM[['CoVaRD2','CoVaRU2']],palette=C_2,dashes=False,legend=False)
sns.lineplot(nAM[['CBMD2','CBMU2']],palette=C_3,dashes=False,legend=False)
sns.lineplot(nAM[['deltaCDw2','deltaCUp2']],palette=C_4,dashes=False,legend=False)
plt.legend(['AM - NESG'],frameon=False,loc='upper right',handlelength=0,prop=pr)
plt.xlabel('')
plt.ylabel('')
legend_handle = plt.gca().get_legend().legendHandles[0]
legend_handle.set_visible(False)
plt.subplot(10,4,36)
sns.lineplot(nAM[['deltaCDw2_pct']],palette=C1,dashes=False,legend=False)
sns.lineplot(nAM[['deltaCUp2_pct']],palette=C2,dashes=False,legend=False)










plt.subplot(10,4,37)
sns.scatterplot(ESG,s=sss, edgecolor='none', color=gg)
sns.lineplot(ySS[['VaRD2','VaRU2']],palette=C_1,dashes=False,legend=False)
sns.lineplot(ySS[['CoVaRD2','CoVaRU2']],palette=C_2,dashes=False,legend=False)
sns.lineplot(ySS[['CBMD2','CBMU2']],palette=C_3,dashes=False,legend=False)
sns.lineplot(ySS[['deltaCDw2','deltaCUp2']],palette=C_4,dashes=False,legend=False)
plt.legend(['SS - ESG'],frameon=False,loc='upper right',handlelength=0,prop=pr)
plt.xlabel('')
plt.ylabel('')
legend_handle = plt.gca().get_legend().legendHandles[0]
legend_handle.set_visible(False)
plt.subplot(10,4,38)
sns.lineplot(ySS[['deltaCDw2_pct']],palette=C1,dashes=False,legend=False)
sns.lineplot(ySS[['deltaCUp2_pct']],palette=C2,dashes=False,legend=False)

plt.subplot(10,4,39)
sns.scatterplot(NESG,s=sss, edgecolor='none', color=gg)
sns.lineplot(nSS[['VaRD2','VaRU2']],palette=C_1,dashes=False,legend=False)
sns.lineplot(nSS[['CoVaRD2','CoVaRU2']],palette=C_2,dashes=False,legend=False)
sns.lineplot(nSS[['CBMD2','CBMU2']],palette=C_3,dashes=False,legend=False)
sns.lineplot(nSS[['deltaCDw2','deltaCUp2']],palette=C_4,dashes=False,legend=False)
plt.legend(['SS - NESG'],frameon=False,loc='upper right',handlelength=0,prop=pr)
plt.xlabel('')
plt.ylabel('')
legend_handle = plt.gca().get_legend().legendHandles[0]
legend_handle.set_visible(False)
plt.subplot(10,4,40)
sns.lineplot(nSS[['deltaCDw2_pct']],palette=C1,dashes=False,legend=False)
sns.lineplot(nSS[['deltaCUp2_pct']],palette=C2,dashes=False,legend=False)


plt.subplots_adjust(
top=0.992,
bottom=0.022,
left=0.029,
right=0.989,
hspace=0.17,
wspace=0.12
)


# plt.tight_layout()
plt.savefig(r'C:/Users/徐浩然/Desktop/P4 Figs/CoVaR-I42Stock_rt.pdf',dpi=2000)
plt.show()