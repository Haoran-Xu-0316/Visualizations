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
# plt.rcParams['font.sans-serif']=['Microsoft YaHei']
plt.rcParams['font.sans-serif'] = ['Palatino Linotype']
# plt.rcParams["font.weight"] = "bold"
plt.rcParams['font.size'] = 16
plt.rcParams['axes.unicode_minus'] = True
plt.rcParams['lines.linewidth'] = 0.7
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
plt.rcParams['axes.xmargin'] = 0

#HE	DB	FF	II	ST	CP	FS	FC	AM	SS	NOESG	ESG


nHE=pd.read_excel(r'C:\Users\徐浩然\Desktop\P4 NOESG\Tau_Taildep.xlsx', sheet_name='HE',index_col=0,parse_dates=[0])
yHE=pd.read_excel(r'C:\Users\徐浩然\Desktop\P4 ESG\Tau_Taildep.xlsx', sheet_name='HE',index_col=0,parse_dates=[0])

nDB=pd.read_excel(r'C:\Users\徐浩然\Desktop\P4 NOESG\Tau_Taildep.xlsx', sheet_name='DB',index_col=0,parse_dates=[0])
yDB=pd.read_excel(r'C:\Users\徐浩然\Desktop\P4 ESG\Tau_Taildep.xlsx', sheet_name='DB',index_col=0,parse_dates=[0])

nFF=pd.read_excel(r'C:\Users\徐浩然\Desktop\P4 NOESG\Tau_Taildep.xlsx', sheet_name='FF',index_col=0,parse_dates=[0])
yFF=pd.read_excel(r'C:\Users\徐浩然\Desktop\P4 ESG\Tau_Taildep.xlsx', sheet_name='FF',index_col=0,parse_dates=[0])

nII=pd.read_excel(r'C:\Users\徐浩然\Desktop\P4 NOESG\Tau_Taildep.xlsx', sheet_name='II',index_col=0,parse_dates=[0])
yII=pd.read_excel(r'C:\Users\徐浩然\Desktop\P4 ESG\Tau_Taildep.xlsx', sheet_name='II',index_col=0,parse_dates=[0])

nST=pd.read_excel(r'C:\Users\徐浩然\Desktop\P4 NOESG\Tau_Taildep.xlsx', sheet_name='ST',index_col=0,parse_dates=[0])
yST=pd.read_excel(r'C:\Users\徐浩然\Desktop\P4 ESG\Tau_Taildep.xlsx', sheet_name='ST',index_col=0,parse_dates=[0])

nCP=pd.read_excel(r'C:\Users\徐浩然\Desktop\P4 NOESG\Tau_Taildep.xlsx', sheet_name='CP',index_col=0,parse_dates=[0])
yCP=pd.read_excel(r'C:\Users\徐浩然\Desktop\P4 ESG\Tau_Taildep.xlsx', sheet_name='CP',index_col=0,parse_dates=[0])

nFS=pd.read_excel(r'C:\Users\徐浩然\Desktop\P4 NOESG\Tau_Taildep.xlsx', sheet_name='FS',index_col=0,parse_dates=[0])
yFS=pd.read_excel(r'C:\Users\徐浩然\Desktop\P4 ESG\Tau_Taildep.xlsx', sheet_name='FS',index_col=0,parse_dates=[0])

nFC=pd.read_excel(r'C:\Users\徐浩然\Desktop\P4 NOESG\Tau_Taildep.xlsx', sheet_name='FC',index_col=0,parse_dates=[0])
yFC=pd.read_excel(r'C:\Users\徐浩然\Desktop\P4 ESG\Tau_Taildep.xlsx', sheet_name='FC',index_col=0,parse_dates=[0])

nAM=pd.read_excel(r'C:\Users\徐浩然\Desktop\P4 NOESG\Tau_Taildep.xlsx', sheet_name='AM',index_col=0,parse_dates=[0])
yAM=pd.read_excel(r'C:\Users\徐浩然\Desktop\P4 ESG\Tau_Taildep.xlsx', sheet_name='AM',index_col=0,parse_dates=[0])

nSS=pd.read_excel(r'C:\Users\徐浩然\Desktop\P4 NOESG\Tau_Taildep.xlsx', sheet_name='SS',index_col=0,parse_dates=[0])
ySS=pd.read_excel(r'C:\Users\徐浩然\Desktop\P4 ESG\Tau_Taildep.xlsx', sheet_name='SS',index_col=0,parse_dates=[0])

ll='upper left'

C1='#1E3350'
C2='#7A1F17'
pr={'style':'italic','weight':'bold'}

plt.subplots(figsize=(12,16))
#
plt.subplot(521)
plt.plot(nHE[['tau']],label='NOESG',color=C1)
plt.plot(yHE[['tau']],label='ESG',color=C2)
plt.axhline(y=0.42,color='black',linestyle='--',linewidth=0.8)
plt.axhline(y=0.41,color='black',linestyle='-.',linewidth=0.8)
plt.legend(['HE'],frameon=False,loc=ll,handlelength=0,prop=pr)
legend_handle = plt.gca().get_legend().legendHandles[0]
legend_handle.set_visible(False)


plt.subplot(522)
plt.plot(nDB[['tau']],label='NOESG',color=C1)
plt.plot(yDB[['tau']],label='ESG',color=C2)
plt.axhline(y=0.58,color='black',linestyle='--',linewidth=0.8)
plt.axhline(y=0.57,color='black',linestyle='-.',linewidth=0.8)
plt.legend(['DB'],frameon=False,loc=ll,handlelength=0,prop=pr)
legend_handle = plt.gca().get_legend().legendHandles[0]
legend_handle.set_visible(False)


plt.subplot(523)
plt.plot(nFF[['tau']],label='NOESG',color=C1)
plt.plot(yFF[['tau']],label='ESG',color=C2)
plt.axhline(y=0.55,color='black',linestyle='--',linewidth=0.8)
plt.axhline(y=0.52,color='black',linestyle='-.',linewidth=0.8)
plt.legend(['FF'],frameon=False,loc=ll,handlelength=0,prop=pr)
legend_handle = plt.gca().get_legend().legendHandles[0]
legend_handle.set_visible(False)




plt.subplot(524)
plt.plot(nII[['tau']],label='NOESG',color=C1)
plt.plot(yII[['tau']],label='ESG',color=C2)
plt.axhline(y=0.60,color='black',linestyle='--',linewidth=0.8)
plt.axhline(y=0.58,color='black',linestyle='-.',linewidth=0.8)
plt.legend(['II'],frameon=False,loc=ll,handlelength=0,prop=pr)
legend_handle = plt.gca().get_legend().legendHandles[0]
legend_handle.set_visible(False)




plt.subplot(525)
plt.plot(nST[['tau']],label='NOESG',color=C1)
plt.plot(yST[['tau']],label='ESG',color=C2)
plt.axhline(y=0.56,color='black',linestyle='--',linewidth=0.8)
plt.axhline(y=0.55,color='black',linestyle='-.',linewidth=0.8)
plt.legend(['ST'],frameon=False,loc=ll,handlelength=0,prop=pr)
legend_handle = plt.gca().get_legend().legendHandles[0]
legend_handle.set_visible(False)




plt.subplot(526)
plt.plot(nCP[['tau']],label='NOESG',color=C1)
plt.plot(yCP[['tau']],label='ESG',color=C2)
plt.axhline(y=0.44,color='black',linestyle='--',linewidth=0.8)
plt.axhline(y=0.42,color='black',linestyle='-.',linewidth=0.8)
plt.legend(['CP'],frameon=False,loc=ll,handlelength=0,prop=pr)
legend_handle = plt.gca().get_legend().legendHandles[0]
legend_handle.set_visible(False)




plt.subplot(527)
plt.plot(nFS[['tau']],label='NOESG',color=C1)
plt.plot(yFS[['tau']],label='ESG',color=C2)
plt.axhline(y=0.60,color='black',linestyle='--',linewidth=0.8)
plt.axhline(y=0.58,color='black',linestyle='-.',linewidth=0.8)
plt.legend(['FS'],frameon=False,loc=ll,handlelength=0,prop=pr)
legend_handle = plt.gca().get_legend().legendHandles[0]
legend_handle.set_visible(False)



plt.subplot(528)
plt.plot(nFC[['tau']],label='NOESG',color=C1)
plt.plot(yFC[['tau']],label='ESG',color=C2)
plt.axhline(y=0.53,color='black',linestyle='--',linewidth=0.8)
plt.axhline(y=0.52,color='black',linestyle='-.',linewidth=0.8)
plt.legend(['FC'],frameon=False,loc=ll,handlelength=0,prop=pr)
legend_handle = plt.gca().get_legend().legendHandles[0]
legend_handle.set_visible(False)



plt.subplot(529)
plt.plot(nAM[['tau']],label='NOESG',color=C1)
plt.plot(yAM[['tau']],label='ESG',color=C2)
plt.axhline(y=0.61,color='black',linestyle='--',linewidth=0.8)
plt.axhline(y=0.59,color='black',linestyle='-.',linewidth=0.8)
plt.legend(['AM'],frameon=False,loc=ll,handlelength=0,prop=pr)
legend_handle = plt.gca().get_legend().legendHandles[0]
legend_handle.set_visible(False)




plt.subplot(5,2,10)
plt.plot(nSS[['tau']],label='NOESG',color=C1)
plt.plot(ySS[['tau']],label='ESG',color=C2)
plt.axhline(y=0.50,color='black',linestyle='--',linewidth=0.8)
plt.axhline(y=0.48,color='black',linestyle='-.',linewidth=0.8)
plt.legend(['SS'],frameon=False,loc=ll,handlelength=0,prop=pr)
legend_handle = plt.gca().get_legend().legendHandles[0]
legend_handle.set_visible(False)


plt.subplots_adjust(
top=0.985,
bottom=0.034,
left=0.051,
right=0.98,
hspace=0.18,
wspace=0.11
)
# plt.legend()
# plt.tight_layout()
plt.savefig(r'C:/Users/徐浩然/Desktop/P4 Figs/tau.pdf',dpi=2000)

plt.show()
