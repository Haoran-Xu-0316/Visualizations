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
sns.scatterplot(HE,s=sss, edgecolor='none', color=gg)
sns.lineplot(yHE[['VaRD1','VaRU1']],palette=C_1,dashes=False,legend=False)
sns.lineplot(yHE[['CoVaRD1','CoVaRU1']],palette=C_2,dashes=False,legend=False)
sns.lineplot(yHE[['CBMD1','CBMU1']],palette=C_3,dashes=False,legend=False)
sns.lineplot(yHE[['deltaCDw1','deltaCUp1']],palette=C_4,dashes=False,legend=False)
plt.legend(['ESG - HE'],frameon=False,loc='upper right',handlelength=0,prop=pr)
plt.xlabel('')
plt.ylabel('')
legend_handle = plt.gca().get_legend().legendHandles[0]
legend_handle.set_visible(False)
plt.subplot(10,4,2)
sns.lineplot(yHE[['deltaCDw1_pct']],palette=C1,dashes=False,legend=False)
sns.lineplot(yHE[['deltaCUp1_pct']],palette=C2,dashes=False,legend=False)

plt.subplot(10,4,3)
sns.scatterplot(HE,s=sss, edgecolor='none', color=gg)
sns.lineplot(nHE[['VaRD1','VaRU1']],palette=C_1,dashes=False,legend=False)
sns.lineplot(nHE[['CoVaRD1','CoVaRU1']],palette=C_2,dashes=False,legend=False)
sns.lineplot(nHE[['CBMD1','CBMU1']],palette=C_3,dashes=False,legend=False)
sns.lineplot(nHE[['deltaCDw1','deltaCUp1']],palette=C_4,dashes=False,legend=False)
plt.legend(['NESG - HE'],frameon=False,loc='upper right',handlelength=0,prop=pr)
plt.xlabel('')
plt.ylabel('')
legend_handle = plt.gca().get_legend().legendHandles[0]
legend_handle.set_visible(False)
plt.subplot(10,4,4)
sns.lineplot(nHE[['deltaCDw1_pct']],palette=C1,dashes=False,legend=False)
sns.lineplot(nHE[['deltaCUp1_pct']],palette=C2,dashes=False,legend=False)






plt.subplot(10,4,5)
sns.scatterplot(DB,s=sss, edgecolor='none', color=gg)
sns.lineplot(yDB[['VaRD1','VaRU1']],palette=C_1,dashes=False,legend=False)
sns.lineplot(yDB[['CoVaRD1','CoVaRU1']],palette=C_2,dashes=False,legend=False)
sns.lineplot(yDB[['CBMD1','CBMU1']],palette=C_3,dashes=False,legend=False)
sns.lineplot(yDB[['deltaCDw1','deltaCUp1']],palette=C_4,dashes=False,legend=False)
plt.legend(['ESG - DB'],frameon=False,loc='upper right',handlelength=0,prop=pr)
plt.xlabel('')
plt.ylabel('')
legend_handle = plt.gca().get_legend().legendHandles[0]
legend_handle.set_visible(False)
plt.subplot(10,4,6)
sns.lineplot(yDB[['deltaCDw1_pct']],palette=C1,dashes=False,legend=False)
sns.lineplot(yDB[['deltaCUp1_pct']],palette=C2,dashes=False,legend=False)

plt.subplot(10,4,7)
sns.scatterplot(DB,s=sss, edgecolor='none', color=gg)
sns.lineplot(nDB[['VaRD1','VaRU1']],palette=C_1,dashes=False,legend=False)
sns.lineplot(nDB[['CoVaRD1','CoVaRU1']],palette=C_2,dashes=False,legend=False)
sns.lineplot(nDB[['CBMD1','CBMU1']],palette=C_3,dashes=False,legend=False)
sns.lineplot(nDB[['deltaCDw1','deltaCUp1']],palette=C_4,dashes=False,legend=False)
plt.legend(['NESG - DB'],frameon=False,loc='upper right',handlelength=0,prop=pr)
plt.xlabel('')
plt.ylabel('')
legend_handle = plt.gca().get_legend().legendHandles[0]
legend_handle.set_visible(False)
plt.subplot(10,4,8)
sns.lineplot(nDB[['deltaCDw1_pct']],palette=C1,dashes=False,legend=False)
sns.lineplot(nDB[['deltaCUp1_pct']],palette=C2,dashes=False,legend=False)








plt.subplot(10,4,9)
sns.scatterplot(FF,s=sss, edgecolor='none', color=gg)
sns.lineplot(yFF[['VaRD1','VaRU1']],palette=C_1,dashes=False,legend=False)
sns.lineplot(yFF[['CoVaRD1','CoVaRU1']],palette=C_2,dashes=False,legend=False)
sns.lineplot(yFF[['CBMD1','CBMU1']],palette=C_3,dashes=False,legend=False)
sns.lineplot(yFF[['deltaCDw1','deltaCUp1']],palette=C_4,dashes=False,legend=False)
plt.legend(['ESG - FF'],frameon=False,loc='upper right',handlelength=0,prop=pr)
plt.xlabel('')
plt.ylabel('')
legend_handle = plt.gca().get_legend().legendHandles[0]
legend_handle.set_visible(False)
plt.subplot(10,4,10)
sns.lineplot(yFF[['deltaCDw1_pct']],palette=C1,dashes=False,legend=False)
sns.lineplot(yFF[['deltaCUp1_pct']],palette=C2,dashes=False,legend=False)

plt.subplot(10,4,11)
sns.scatterplot(FF,s=sss, edgecolor='none', color=gg)
sns.lineplot(nFF[['VaRD1','VaRU1']],palette=C_1,dashes=False,legend=False)
sns.lineplot(nFF[['CoVaRD1','CoVaRU1']],palette=C_2,dashes=False,legend=False)
sns.lineplot(nFF[['CBMD1','CBMU1']],palette=C_3,dashes=False,legend=False)
sns.lineplot(nFF[['deltaCDw1','deltaCUp1']],palette=C_4,dashes=False,legend=False)
plt.legend(['NESG - FF'],frameon=False,loc='upper right',handlelength=0,prop=pr)
plt.xlabel('')
plt.ylabel('')
legend_handle = plt.gca().get_legend().legendHandles[0]
legend_handle.set_visible(False)
plt.subplot(10,4,12)
sns.lineplot(nFF[['deltaCDw1_pct']],palette=C1,dashes=False,legend=False)
sns.lineplot(nFF[['deltaCUp1_pct']],palette=C2,dashes=False,legend=False)









plt.subplot(10,4,13)
sns.scatterplot(II,s=sss, edgecolor='none', color=gg)
sns.lineplot(yII[['VaRD1','VaRU1']],palette=C_1,dashes=False,legend=False)
sns.lineplot(yII[['CoVaRD1','CoVaRU1']],palette=C_2,dashes=False,legend=False)
sns.lineplot(yII[['CBMD1','CBMU1']],palette=C_3,dashes=False,legend=False)
sns.lineplot(yII[['deltaCDw1','deltaCUp1']],palette=C_4,dashes=False,legend=False)
plt.legend(['ESG - II'],frameon=False,loc='upper right',handlelength=0,prop=pr)
plt.xlabel('')
plt.ylabel('')
legend_handle = plt.gca().get_legend().legendHandles[0]
legend_handle.set_visible(False)
plt.subplot(10,4,14)
sns.lineplot(yII[['deltaCDw1_pct']],palette=C1,dashes=False,legend=False)
sns.lineplot(yII[['deltaCUp1_pct']],palette=C2,dashes=False,legend=False)

plt.subplot(10,4,15)
sns.scatterplot(II,s=sss, edgecolor='none', color=gg)
sns.lineplot(nII[['VaRD1','VaRU1']],palette=C_1,dashes=False,legend=False)
sns.lineplot(nII[['CoVaRD1','CoVaRU1']],palette=C_2,dashes=False,legend=False)
sns.lineplot(nII[['CBMD1','CBMU1']],palette=C_3,dashes=False,legend=False)
sns.lineplot(nII[['deltaCDw1','deltaCUp1']],palette=C_4,dashes=False,legend=False)
plt.legend(['NESG - II'],frameon=False,loc='upper right',handlelength=0,prop=pr)
plt.xlabel('')
plt.ylabel('')
legend_handle = plt.gca().get_legend().legendHandles[0]
legend_handle.set_visible(False)
plt.subplot(10,4,16)
sns.lineplot(nII[['deltaCDw1_pct']],palette=C1,dashes=False,legend=False)
sns.lineplot(nII[['deltaCUp1_pct']],palette=C2,dashes=False,legend=False)









plt.subplot(10,4,17)
sns.scatterplot(ST,s=sss, edgecolor='none', color=gg)
sns.lineplot(yST[['VaRD1','VaRU1']],palette=C_1,dashes=False,legend=False)
sns.lineplot(yST[['CoVaRD1','CoVaRU1']],palette=C_2,dashes=False,legend=False)
sns.lineplot(yST[['CBMD1','CBMU1']],palette=C_3,dashes=False,legend=False)
sns.lineplot(yST[['deltaCDw1','deltaCUp1']],palette=C_4,dashes=False,legend=False)
plt.legend(['ESG - ST'],frameon=False,loc='upper right',handlelength=0,prop=pr)
plt.xlabel('')
plt.ylabel('')
legend_handle = plt.gca().get_legend().legendHandles[0]
legend_handle.set_visible(False)
plt.subplot(10,4,18)
sns.lineplot(yST[['deltaCDw1_pct']],palette=C1,dashes=False,legend=False)
sns.lineplot(yST[['deltaCUp1_pct']],palette=C2,dashes=False,legend=False)

plt.subplot(10,4,19)
sns.scatterplot(ST,s=sss, edgecolor='none', color=gg)
sns.lineplot(nST[['VaRD1','VaRU1']],palette=C_1,dashes=False,legend=False)
sns.lineplot(nST[['CoVaRD1','CoVaRU1']],palette=C_2,dashes=False,legend=False)
sns.lineplot(nST[['CBMD1','CBMU1']],palette=C_3,dashes=False,legend=False)
sns.lineplot(nST[['deltaCDw1','deltaCUp1']],palette=C_4,dashes=False,legend=False)
plt.legend(['NESG - ST'],frameon=False,loc='upper right',handlelength=0,prop=pr)
plt.xlabel('')
plt.ylabel('')
legend_handle = plt.gca().get_legend().legendHandles[0]
legend_handle.set_visible(False)
plt.subplot(10,4,20)
sns.lineplot(nST[['deltaCDw1_pct']],palette=C1,dashes=False,legend=False)
sns.lineplot(nST[['deltaCUp1_pct']],palette=C2,dashes=False,legend=False)








plt.subplot(10,4,21)
sns.scatterplot(CP,s=sss, edgecolor='none', color=gg)
sns.lineplot(yCP[['VaRD1','VaRU1']],palette=C_1,dashes=False,legend=False)
sns.lineplot(yCP[['CoVaRD1','CoVaRU1']],palette=C_2,dashes=False,legend=False)
sns.lineplot(yCP[['CBMD1','CBMU1']],palette=C_3,dashes=False,legend=False)
sns.lineplot(yCP[['deltaCDw1','deltaCUp1']],palette=C_4,dashes=False,legend=False)
plt.legend(['ESG - CP'],frameon=False,loc='upper right',handlelength=0,prop=pr)
plt.xlabel('')
plt.ylabel('')
legend_handle = plt.gca().get_legend().legendHandles[0]
legend_handle.set_visible(False)
plt.subplot(10,4,22)
sns.lineplot(yCP[['deltaCDw1_pct']],palette=C1,dashes=False,legend=False)
sns.lineplot(yCP[['deltaCUp1_pct']],palette=C2,dashes=False,legend=False)

plt.subplot(10,4,23)
sns.scatterplot(CP,s=sss, edgecolor='none', color=gg)
sns.lineplot(nCP[['VaRD1','VaRU1']],palette=C_1,dashes=False,legend=False)
sns.lineplot(nCP[['CoVaRD1','CoVaRU1']],palette=C_2,dashes=False,legend=False)
sns.lineplot(nCP[['CBMD1','CBMU1']],palette=C_3,dashes=False,legend=False)
sns.lineplot(nCP[['deltaCDw1','deltaCUp1']],palette=C_4,dashes=False,legend=False)
plt.legend(['NESG - CP'],frameon=False,loc='upper right',handlelength=0,prop=pr)
plt.xlabel('')
plt.ylabel('')
legend_handle = plt.gca().get_legend().legendHandles[0]
legend_handle.set_visible(False)
plt.subplot(10,4,24)
sns.lineplot(nCP[['deltaCDw1_pct']],palette=C1,dashes=False,legend=False)
sns.lineplot(nCP[['deltaCUp1_pct']],palette=C2,dashes=False,legend=False)










plt.subplot(10,4,25)
sns.scatterplot(FS,s=sss, edgecolor='none', color=gg)
sns.lineplot(yFS[['VaRD1','VaRU1']],palette=C_1,dashes=False,legend=False)
sns.lineplot(yFS[['CoVaRD1','CoVaRU1']],palette=C_2,dashes=False,legend=False)
sns.lineplot(yFS[['CBMD1','CBMU1']],palette=C_3,dashes=False,legend=False)
sns.lineplot(yFS[['deltaCDw1','deltaCUp1']],palette=C_4,dashes=False,legend=False)
plt.legend(['ESG - FS'],frameon=False,loc='upper right',handlelength=0,prop=pr)
plt.xlabel('')
plt.ylabel('')
legend_handle = plt.gca().get_legend().legendHandles[0]
legend_handle.set_visible(False)
plt.subplot(10,4,26)
sns.lineplot(yFS[['deltaCDw1_pct']],palette=C1,dashes=False,legend=False)
sns.lineplot(yFS[['deltaCUp1_pct']],palette=C2,dashes=False,legend=False)

plt.subplot(10,4,27)
sns.scatterplot(FS,s=sss, edgecolor='none', color=gg)
sns.lineplot(nFS[['VaRD1','VaRU1']],palette=C_1,dashes=False,legend=False)
sns.lineplot(nFS[['CoVaRD1','CoVaRU1']],palette=C_2,dashes=False,legend=False)
sns.lineplot(nFS[['CBMD1','CBMU1']],palette=C_3,dashes=False,legend=False)
sns.lineplot(nFS[['deltaCDw1','deltaCUp1']],palette=C_4,dashes=False,legend=False)
plt.legend(['NESG - FS'],frameon=False,loc='upper right',handlelength=0,prop=pr)
plt.xlabel('')
plt.ylabel('')
legend_handle = plt.gca().get_legend().legendHandles[0]
legend_handle.set_visible(False)
plt.subplot(10,4,28)
sns.lineplot(nFS[['deltaCDw1_pct']],palette=C1,dashes=False,legend=False)
sns.lineplot(nFS[['deltaCUp1_pct']],palette=C2,dashes=False,legend=False)









plt.subplot(10,4,29)
sns.scatterplot(FC,s=sss, edgecolor='none', color=gg)
sns.lineplot(yFC[['VaRD1','VaRU1']],palette=C_1,dashes=False,legend=False)
sns.lineplot(yFC[['CoVaRD1','CoVaRU1']],palette=C_2,dashes=False,legend=False)
sns.lineplot(yFC[['CBMD1','CBMU1']],palette=C_3,dashes=False,legend=False)
sns.lineplot(yFC[['deltaCDw1','deltaCUp1']],palette=C_4,dashes=False,legend=False)
plt.legend(['ESG - FC'],frameon=False,loc='upper right',handlelength=0,prop=pr)
plt.xlabel('')
plt.ylabel('')
legend_handle = plt.gca().get_legend().legendHandles[0]
legend_handle.set_visible(False)
plt.subplot(10,4,30)
sns.lineplot(yFC[['deltaCDw1_pct']],palette=C1,dashes=False,legend=False)
sns.lineplot(yFC[['deltaCUp1_pct']],palette=C2,dashes=False,legend=False)

plt.subplot(10,4,31)
sns.scatterplot(FC,s=sss, edgecolor='none', color=gg)
sns.lineplot(nFC[['VaRD1','VaRU1']],palette=C_1,dashes=False,legend=False)
sns.lineplot(nFC[['CoVaRD1','CoVaRU1']],palette=C_2,dashes=False,legend=False)
sns.lineplot(nFC[['CBMD1','CBMU1']],palette=C_3,dashes=False,legend=False)
sns.lineplot(nFC[['deltaCDw1','deltaCUp1']],palette=C_4,dashes=False,legend=False)
plt.legend(['NESG - FC'],frameon=False,loc='upper right',handlelength=0,prop=pr)
plt.xlabel('')
plt.ylabel('')
legend_handle = plt.gca().get_legend().legendHandles[0]
legend_handle.set_visible(False)
plt.subplot(10,4,32)
sns.lineplot(nFC[['deltaCDw1_pct']],palette=C1,dashes=False,legend=False)
sns.lineplot(nFC[['deltaCUp1_pct']],palette=C2,dashes=False,legend=False)







plt.subplot(10,4,33)
sns.scatterplot(AM,s=sss, edgecolor='none', color=gg)
sns.lineplot(yAM[['VaRD1','VaRU1']],palette=C_1,dashes=False,legend=False)
sns.lineplot(yAM[['CoVaRD1','CoVaRU1']],palette=C_2,dashes=False,legend=False)
sns.lineplot(yAM[['CBMD1','CBMU1']],palette=C_3,dashes=False,legend=False)
sns.lineplot(yAM[['deltaCDw1','deltaCUp1']],palette=C_4,dashes=False,legend=False)
plt.legend(['ESG - AM'],frameon=False,loc='upper right',handlelength=0,prop=pr)
plt.xlabel('')
plt.ylabel('')
legend_handle = plt.gca().get_legend().legendHandles[0]
legend_handle.set_visible(False)
plt.subplot(10,4,34)
sns.lineplot(yAM[['deltaCDw1_pct']],palette=C1,dashes=False,legend=False)
sns.lineplot(yAM[['deltaCUp1_pct']],palette=C2,dashes=False,legend=False)

plt.subplot(10,4,35)
sns.scatterplot(AM,s=sss, edgecolor='none', color=gg)
sns.lineplot(nAM[['VaRD1','VaRU1']],palette=C_1,dashes=False,legend=False)
sns.lineplot(nAM[['CoVaRD1','CoVaRU1']],palette=C_2,dashes=False,legend=False)
sns.lineplot(nAM[['CBMD1','CBMU1']],palette=C_3,dashes=False,legend=False)
sns.lineplot(nAM[['deltaCDw1','deltaCUp1']],palette=C_4,dashes=False,legend=False)
plt.legend(['NESG - AM'],frameon=False,loc='upper right',handlelength=0,prop=pr)
plt.xlabel('')
plt.ylabel('')
legend_handle = plt.gca().get_legend().legendHandles[0]
legend_handle.set_visible(False)
plt.subplot(10,4,36)
sns.lineplot(nAM[['deltaCDw1_pct']],palette=C1,dashes=False,legend=False)
sns.lineplot(nAM[['deltaCUp1_pct']],palette=C2,dashes=False,legend=False)










plt.subplot(10,4,37)
sns.scatterplot(SS,s=sss, edgecolor='none', color=gg)
sns.lineplot(ySS[['VaRD1','VaRU1']],palette=C_1,dashes=False,legend=False)
sns.lineplot(ySS[['CoVaRD1','CoVaRU1']],palette=C_2,dashes=False,legend=False)
sns.lineplot(ySS[['CBMD1','CBMU1']],palette=C_3,dashes=False,legend=False)
sns.lineplot(ySS[['deltaCDw1','deltaCUp1']],palette=C_4,dashes=False,legend=False)
plt.legend(['ESG - SS'],frameon=False,loc='upper right',handlelength=0,prop=pr)
plt.xlabel('')
plt.ylabel('')
legend_handle = plt.gca().get_legend().legendHandles[0]
legend_handle.set_visible(False)
plt.subplot(10,4,38)
sns.lineplot(ySS[['deltaCDw1_pct']],palette=C1,dashes=False,legend=False)
sns.lineplot(ySS[['deltaCUp1_pct']],palette=C2,dashes=False,legend=False)

plt.subplot(10,4,39)
sns.scatterplot(SS,s=sss, edgecolor='none', color=gg)
sns.lineplot(nSS[['VaRD1','VaRU1']],palette=C_1,dashes=False,legend=False)
sns.lineplot(nSS[['CoVaRD1','CoVaRU1']],palette=C_2,dashes=False,legend=False)
sns.lineplot(nSS[['CBMD1','CBMU1']],palette=C_3,dashes=False,legend=False)
sns.lineplot(nSS[['deltaCDw1','deltaCUp1']],palette=C_4,dashes=False,legend=False)
plt.legend(['NESG - SS'],frameon=False,loc='upper right',handlelength=0,prop=pr)
plt.xlabel('')
plt.ylabel('')
legend_handle = plt.gca().get_legend().legendHandles[0]
legend_handle.set_visible(False)
plt.subplot(10,4,40)
sns.lineplot(nSS[['deltaCDw1_pct']],palette=C1,dashes=False,legend=False)
sns.lineplot(nSS[['deltaCUp1_pct']],palette=C2,dashes=False,legend=False)


plt.subplots_adjust(
top=0.992,
bottom=0.022,
left=0.029,
right=0.989,
hspace=0.17,
wspace=0.12
)


# plt.tight_layout()
plt.savefig(r'C:/Users/徐浩然/Desktop/P4 Figs/CoVaR-Stock2I4_rt.pdf',dpi=2000)
plt.show()