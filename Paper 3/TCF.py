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
plt.rcParams['font.size'] = 14
plt.rcParams['axes.unicode_minus'] = True
plt.rcParams['lines.linewidth'] = 1
# plt.rcParams['axes.xlim'] = (0, 1)
plt.rcParams['axes.xmargin'] = 0
plt.rcParams['axes.ymargin'] = 0
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
plt.rcParams['axes.labelsize'] = 0
yHE=pd.read_excel(r'C:\Users\徐浩然\Desktop\P4 ESG\Concentration Function.xlsx', sheet_name='HE',index_col=0,parse_dates=[0])
nHE=pd.read_excel(r'C:\Users\徐浩然\Desktop\P4 NOESG\Concentration Function.xlsx', sheet_name='HE',index_col=0,parse_dates=[0])
yDB=pd.read_excel(r'C:\Users\徐浩然\Desktop\P4 ESG\Concentration Function.xlsx', sheet_name='DB',index_col=0,parse_dates=[0])
nDB=pd.read_excel(r'C:\Users\徐浩然\Desktop\P4 NOESG\Concentration Function.xlsx', sheet_name='DB',index_col=0,parse_dates=[0])
yFF=pd.read_excel(r'C:\Users\徐浩然\Desktop\P4 ESG\Concentration Function.xlsx', sheet_name='FF',index_col=0,parse_dates=[0])
nFF=pd.read_excel(r'C:\Users\徐浩然\Desktop\P4 NOESG\Concentration Function.xlsx', sheet_name='FF',index_col=0,parse_dates=[0])
yII=pd.read_excel(r'C:\Users\徐浩然\Desktop\P4 ESG\Concentration Function.xlsx', sheet_name='II',index_col=0,parse_dates=[0])
nII=pd.read_excel(r'C:\Users\徐浩然\Desktop\P4 NOESG\Concentration Function.xlsx', sheet_name='II',index_col=0,parse_dates=[0])
yST=pd.read_excel(r'C:\Users\徐浩然\Desktop\P4 ESG\Concentration Function.xlsx', sheet_name='ST',index_col=0,parse_dates=[0])
nST=pd.read_excel(r'C:\Users\徐浩然\Desktop\P4 NOESG\Concentration Function.xlsx', sheet_name='ST',index_col=0,parse_dates=[0])
yCP=pd.read_excel(r'C:\Users\徐浩然\Desktop\P4 ESG\Concentration Function.xlsx', sheet_name='CP',index_col=0,parse_dates=[0])
nCP=pd.read_excel(r'C:\Users\徐浩然\Desktop\P4 NOESG\Concentration Function.xlsx', sheet_name='CP',index_col=0,parse_dates=[0])
yFS=pd.read_excel(r'C:\Users\徐浩然\Desktop\P4 ESG\Concentration Function.xlsx', sheet_name='FS',index_col=0,parse_dates=[0])
nFS=pd.read_excel(r'C:\Users\徐浩然\Desktop\P4 NOESG\Concentration Function.xlsx', sheet_name='FS',index_col=0,parse_dates=[0])
yFC=pd.read_excel(r'C:\Users\徐浩然\Desktop\P4 ESG\Concentration Function.xlsx', sheet_name='FC',index_col=0,parse_dates=[0])
nFC=pd.read_excel(r'C:\Users\徐浩然\Desktop\P4 NOESG\Concentration Function.xlsx', sheet_name='FC',index_col=0,parse_dates=[0])
yAM=pd.read_excel(r'C:\Users\徐浩然\Desktop\P4 ESG\Concentration Function.xlsx', sheet_name='AM',index_col=0,parse_dates=[0])
nAM=pd.read_excel(r'C:\Users\徐浩然\Desktop\P4 NOESG\Concentration Function.xlsx', sheet_name='AM',index_col=0,parse_dates=[0])
ySS=pd.read_excel(r'C:\Users\徐浩然\Desktop\P4 ESG\Concentration Function.xlsx', sheet_name='SS',index_col=0,parse_dates=[0])
nSS=pd.read_excel(r'C:\Users\徐浩然\Desktop\P4 NOESG\Concentration Function.xlsx', sheet_name='SS',index_col=0,parse_dates=[0])


#HE	DB	FF	II	ST	CP	FS	FC	AM	SS	NOESG	ESG

C_Sim=['#D9D9D9']
C_Q=['#7A1F17']
C_elr=['black']
C_tlr=['#1E3350']
C_f='grey'
a=0.4
ll=0
pr={'style':'italic','weight':'bold'}


ll='lower center'
plt.subplots(figsize=(18,14.4))


plt.subplot(4,5,11)
sns.lineplot(yHE.iloc[:, :-4],palette=C_Sim,dashes=False,legend=False)
sns.lineplot(yHE[['Q05','Q95']],palette=C_Q,dashes=False,legend=False)
sns.lineplot(yHE[['lr_th']],palette=C_tlr,dashes=False,legend=False)
sns.lineplot(yHE[['lr_emp']],palette=C_elr,dashes=False,legend=False)
plt.legend(['HE - ESG'],frameon=False,loc=ll,handlelength=0,prop=pr)
# plt.fill_between(s,CF12['Q05'],CF12['Q95'],color=C_f,alpha=a, linewidth=ll)
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.xticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
plt.gca().set_aspect('equal', adjustable='box')

plt.subplot(4,5,12)
sns.lineplot(yDB.iloc[:, :-4],palette=C_Sim,dashes=False,legend=False)
sns.lineplot(yDB[['Q05','Q95']],palette=C_Q,dashes=False,legend=False)
sns.lineplot(yDB[['lr_th']],palette=C_tlr,dashes=False,legend=False)
sns.lineplot(yDB[['lr_emp']],palette=C_elr,dashes=False,legend=False)
plt.legend(['DB - ESG'],frameon=False,loc=ll,handlelength=0,prop=pr)
# plt.fill_between(s,CF12['Q05'],CF12['Q95'],color=C_f,alpha=a, linewidth=ll)
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.xticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
plt.gca().set_aspect('equal', adjustable='box')

plt.subplot(4,5,13)
sns.lineplot(yFF.iloc[:, :-4],palette=C_Sim,dashes=False,legend=False)
sns.lineplot(yFF[['Q05','Q95']],palette=C_Q,dashes=False,legend=False)
sns.lineplot(yFF[['lr_th']],palette=C_tlr,dashes=False,legend=False)
sns.lineplot(yFF[['lr_emp']],palette=C_elr,dashes=False,legend=False)
plt.legend(['FF - ESG'],frameon=False,loc=ll,handlelength=0,prop=pr)
# plt.fill_between(s,CF12['Q05'],CF12['Q95'],color=C_f,alpha=a, linewidth=ll)
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.xticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
plt.gca().set_aspect('equal', adjustable='box')

plt.subplot(4,5,14)
sns.lineplot(yII.iloc[:, :-4],palette=C_Sim,dashes=False,legend=False)
sns.lineplot(yII[['Q05','Q95']],palette=C_Q,dashes=False,legend=False)
sns.lineplot(yII[['lr_th']],palette=C_tlr,dashes=False,legend=False)
sns.lineplot(yII[['lr_emp']],palette=C_elr,dashes=False,legend=False)
plt.legend(['II - ESG'],frameon=False,loc=ll,handlelength=0,prop=pr)
# plt.fill_between(s,CF12['Q05'],CF12['Q95'],color=C_f,alpha=a, linewidth=ll)
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.xticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
plt.gca().set_aspect('equal', adjustable='box')

plt.subplot(4,5,15)
sns.lineplot(yST.iloc[:, :-4],palette=C_Sim,dashes=False,legend=False)
sns.lineplot(yST[['Q05','Q95']],palette=C_Q,dashes=False,legend=False)
sns.lineplot(yST[['lr_th']],palette=C_tlr,dashes=False,legend=False)
sns.lineplot(yST[['lr_emp']],palette=C_elr,dashes=False,legend=False)
plt.legend(['ST - ESG'],frameon=False,loc=ll,handlelength=0,prop=pr)
# plt.fill_between(s,CF12['Q05'],CF12['Q95'],color=C_f,alpha=a, linewidth=ll)
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.xticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
plt.gca().set_aspect('equal', adjustable='box')



plt.subplot(4,5,16)
sns.lineplot(yCP.iloc[:, :-4],palette=C_Sim,dashes=False,legend=False)
sns.lineplot(yCP[['Q05','Q95']],palette=C_Q,dashes=False,legend=False)
sns.lineplot(yCP[['lr_th']],palette=C_tlr,dashes=False,legend=False)
sns.lineplot(yCP[['lr_emp']],palette=C_elr,dashes=False,legend=False)
plt.legend(['CP - ESG'],frameon=False,loc=ll,handlelength=0,prop=pr)
# plt.fill_between(s,CF12['Q05'],CF12['Q95'],color=C_f,alpha=a, linewidth=ll)
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.xticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
plt.gca().set_aspect('equal', adjustable='box')

plt.subplot(4,5,17)
sns.lineplot(yFS.iloc[:, :-4],palette=C_Sim,dashes=False,legend=False)
sns.lineplot(yFS[['Q05','Q95']],palette=C_Q,dashes=False,legend=False)
sns.lineplot(yFS[['lr_th']],palette=C_tlr,dashes=False,legend=False)
sns.lineplot(yFS[['lr_emp']],palette=C_elr,dashes=False,legend=False)
plt.legend(['FS - ESG'],frameon=False,loc=ll,handlelength=0,prop=pr)
# plt.fill_between(s,CF12['Q05'],CF12['Q95'],color=C_f,alpha=a, linewidth=ll)
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.xticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
plt.gca().set_aspect('equal', adjustable='box')

plt.subplot(4,5,18)
sns.lineplot(yFC.iloc[:, :-4],palette=C_Sim,dashes=False,legend=False)
sns.lineplot(yFC[['Q05','Q95']],palette=C_Q,dashes=False,legend=False)
sns.lineplot(yFC[['lr_th']],palette=C_tlr,dashes=False,legend=False)
sns.lineplot(yFC[['lr_emp']],palette=C_elr,dashes=False,legend=False)
plt.legend(['FC - ESG'],frameon=False,loc=ll,handlelength=0,prop=pr)
# plt.fill_between(s,CF12['Q05'],CF12['Q95'],color=C_f,alpha=a, linewidth=ll)
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.xticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
plt.gca().set_aspect('equal', adjustable='box')

plt.subplot(4,5,19)
sns.lineplot(yAM.iloc[:, :-4],palette=C_Sim,dashes=False,legend=False)
sns.lineplot(yAM[['Q05','Q95']],palette=C_Q,dashes=False,legend=False)
sns.lineplot(yAM[['lr_th']],palette=C_tlr,dashes=False,legend=False)
sns.lineplot(yAM[['lr_emp']],palette=C_elr,dashes=False,legend=False)
plt.legend(['AM - ESG'],frameon=False,loc=ll,handlelength=0,prop=pr)
# plt.fill_between(s,CF12['Q05'],CF12['Q95'],color=C_f,alpha=a, linewidth=ll)
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.xticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
plt.gca().set_aspect('equal', adjustable='box')

plt.subplot(4,5,20)
sns.lineplot(ySS.iloc[:, :-4],palette=C_Sim,dashes=False,legend=False)
sns.lineplot(ySS[['Q05','Q95']],palette=C_Q,dashes=False,legend=False)
sns.lineplot(ySS[['lr_th']],palette=C_tlr,dashes=False,legend=False)
sns.lineplot(ySS[['lr_emp']],palette=C_elr,dashes=False,legend=False)
plt.legend(['SS - ESG'],frameon=False,loc=ll,handlelength=0,prop=pr)
# plt.fill_between(s,CF12['Q05'],CF12['Q95'],color=C_f,alpha=a, linewidth=ll)
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.xticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
plt.gca().set_aspect('equal', adjustable='box')


plt.subplot(4,5,1)
sns.lineplot(nHE.iloc[:, :-4],palette=C_Sim,dashes=False,legend=False)
sns.lineplot(nHE[['Q05','Q95']],palette=C_Q,dashes=False,legend=False)
sns.lineplot(nHE[['lr_th']],palette=C_tlr,dashes=False,legend=False)
sns.lineplot(nHE[['lr_emp']],palette=C_elr,dashes=False,legend=False)
plt.legend(['HE - NESG'],frameon=False,loc=ll,handlelength=0,prop=pr)
# plt.fill_between(s,CF12['Q05'],CF12['Q95'],color=C_f,alpha=a, linewidth=ll)
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.xticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
plt.gca().set_aspect('equal', adjustable='box')

plt.subplot(4,5,2)
sns.lineplot(nDB.iloc[:, :-4],palette=C_Sim,dashes=False,legend=False)
sns.lineplot(nDB[['Q05','Q95']],palette=C_Q,dashes=False,legend=False)
sns.lineplot(nDB[['lr_th']],palette=C_tlr,dashes=False,legend=False)
sns.lineplot(nDB[['lr_emp']],palette=C_elr,dashes=False,legend=False)
plt.legend(['DB - NESG'],frameon=False,loc=ll,handlelength=0,prop=pr)
# plt.fill_between(s,CF12['Q05'],CF12['Q95'],color=C_f,alpha=a, linewidth=ll)
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.xticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
plt.gca().set_aspect('equal', adjustable='box')

plt.subplot(4,5,3)
sns.lineplot(nFF.iloc[:, :-4],palette=C_Sim,dashes=False,legend=False)
sns.lineplot(nFF[['Q05','Q95']],palette=C_Q,dashes=False,legend=False)
sns.lineplot(nFF[['lr_th']],palette=C_tlr,dashes=False,legend=False)
sns.lineplot(nFF[['lr_emp']],palette=C_elr,dashes=False,legend=False)
plt.legend(['FF - NESG'],frameon=False,loc=ll,handlelength=0,prop=pr)
# plt.fill_between(s,CF12['Q05'],CF12['Q95'],color=C_f,alpha=a, linewidth=ll)
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.xticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
plt.gca().set_aspect('equal', adjustable='box')

plt.subplot(4,5,4)
sns.lineplot(nII.iloc[:, :-4],palette=C_Sim,dashes=False,legend=False)
sns.lineplot(nII[['Q05','Q95']],palette=C_Q,dashes=False,legend=False)
sns.lineplot(nII[['lr_th']],palette=C_tlr,dashes=False,legend=False)
sns.lineplot(nII[['lr_emp']],palette=C_elr,dashes=False,legend=False)
plt.legend(['II - NESG'],frameon=False,loc=ll,handlelength=0,prop=pr)
# plt.fill_between(s,CF12['Q05'],CF12['Q95'],color=C_f,alpha=a, linewidth=ll)
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.xticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
plt.gca().set_aspect('equal', adjustable='box')

plt.subplot(4,5,5)
sns.lineplot(nST.iloc[:, :-4],palette=C_Sim,dashes=False,legend=False)
sns.lineplot(nST[['Q05','Q95']],palette=C_Q,dashes=False,legend=False)
sns.lineplot(nST[['lr_th']],palette=C_tlr,dashes=False,legend=False)
sns.lineplot(nST[['lr_emp']],palette=C_elr,dashes=False,legend=False)
plt.legend(['ST - NESG'],frameon=False,loc=ll,handlelength=0,prop=pr)
# plt.fill_between(s,CF12['Q05'],CF12['Q95'],color=C_f,alpha=a, linewidth=ll)
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.xticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
plt.gca().set_aspect('equal', adjustable='box')



plt.subplot(4,5,6)
sns.lineplot(nCP.iloc[:, :-4],palette=C_Sim,dashes=False,legend=False)
sns.lineplot(nCP[['Q05','Q95']],palette=C_Q,dashes=False,legend=False)
sns.lineplot(nCP[['lr_th']],palette=C_tlr,dashes=False,legend=False)
sns.lineplot(nCP[['lr_emp']],palette=C_elr,dashes=False,legend=False)
plt.legend(['CP - NESG'],frameon=False,loc=ll,handlelength=0,prop=pr)
# plt.fill_between(s,CF12['Q05'],CF12['Q95'],color=C_f,alpha=a, linewidth=ll)
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.xticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
plt.gca().set_aspect('equal', adjustable='box')

plt.subplot(4,5,7)
sns.lineplot(nFS.iloc[:, :-4],palette=C_Sim,dashes=False,legend=False)
sns.lineplot(nFS[['Q05','Q95']],palette=C_Q,dashes=False,legend=False)
sns.lineplot(nFS[['lr_th']],palette=C_tlr,dashes=False,legend=False)
sns.lineplot(nFS[['lr_emp']],palette=C_elr,dashes=False,legend=False)
plt.legend(['FS - NESG'],frameon=False,loc=ll,handlelength=0,prop=pr)
# plt.fill_between(s,CF12['Q05'],CF12['Q95'],color=C_f,alpha=a, linewidth=ll)
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.xticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
plt.gca().set_aspect('equal', adjustable='box')

plt.subplot(4,5,8)
sns.lineplot(nFC.iloc[:, :-4],palette=C_Sim,dashes=False,legend=False)
sns.lineplot(nFC[['Q05','Q95']],palette=C_Q,dashes=False,legend=False)
sns.lineplot(nFC[['lr_th']],palette=C_tlr,dashes=False,legend=False)
sns.lineplot(nFC[['lr_emp']],palette=C_elr,dashes=False,legend=False)
plt.legend(['FC - NESG'],frameon=False,loc=ll,handlelength=0,prop=pr)
# plt.fill_between(s,CF12['Q05'],CF12['Q95'],color=C_f,alpha=a, linewidth=ll)
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.xticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
plt.gca().set_aspect('equal', adjustable='box')

plt.subplot(4,5,9)
sns.lineplot(nAM.iloc[:, :-4],palette=C_Sim,dashes=False,legend=False)
sns.lineplot(nAM[['Q05','Q95']],palette=C_Q,dashes=False,legend=False)
sns.lineplot(nAM[['lr_th']],palette=C_tlr,dashes=False,legend=False)
sns.lineplot(nAM[['lr_emp']],palette=C_elr,dashes=False,legend=False)
plt.legend(['AM - NESG'],frameon=False,loc=ll,handlelength=0,prop=pr)
# plt.fill_between(s,CF12['Q05'],CF12['Q95'],color=C_f,alpha=a, linewidth=ll)
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.xticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
plt.gca().set_aspect('equal', adjustable='box')

plt.subplot(4,5,10)
sns.lineplot(nSS.iloc[:, :-4],palette=C_Sim,dashes=False,legend=False)
sns.lineplot(nSS[['Q05','Q95']],palette=C_Q,dashes=False,legend=False)
sns.lineplot(nSS[['lr_th']],palette=C_tlr,dashes=False,legend=False)
sns.lineplot(nSS[['lr_emp']],palette=C_elr,dashes=False,legend=False)
plt.legend(['SS - NESG'],frameon=False,loc=ll,handlelength=0,prop=pr)
# plt.fill_between(s,CF12['Q05'],CF12['Q95'],color=C_f,alpha=a, linewidth=ll)
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.xticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
plt.gca().set_aspect('equal', adjustable='box')

#HE	DB	FF	II	ST	CP	FS	FC	AM	SS	NOESG	ESG



plt.subplots_adjust(top=0.981,bottom=0.04,left=0.031,right=0.982,hspace=0.2,wspace=0.2)

# plt.tight_layout()
plt.savefig(r'C:/Users/徐浩然/Desktop/P4 Figs/TCF.pdf',dpi=2000)
plt.show()



