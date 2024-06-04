import math
from datetime import datetime

import matplotlib.dates as dates
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.interpolate as sci
import scipy.optimize as sco
import seaborn as sns
import tushare as ts

#全局设置-----------------------------------------------------------------------------------------------------------------
plt.rcParams['font.sans-serif'] = ['Palatino Linotype']
# plt.rcParams["font.weight"] = "bold"
# plt.rcParams['font.style']='italic'
plt.rcParams['font.size'] = 12.5
fs=12.5
plt.rcParams['axes.unicode_minus'] = True
plt.rcParams['lines.linewidth'] = 0.3
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
ll=['EUA',	'SZA',	'HBA', 'PMI', 'CEI', 'GBI']

l = []

for i in range(len(ll)):
    if i + 1 <= len(ll):
        for j in range(i + 1, len(ll)):
            l.append(f"{ll[i]} - {ll[j]}")

#-----------------------------------------------------------------------------------------------------------------------
pcit=pd.read_excel(r'C:\Users\徐浩然\Desktop\P2 Results\All_pci.xlsx', sheet_name='Total',index_col=0,parse_dates=[0])
pci13=pd.read_excel(r'C:\Users\徐浩然\Desktop\P2 Results\All_pci.xlsx', sheet_name='1-3',index_col=0,parse_dates=[0])
pci36=pd.read_excel(r'C:\Users\徐浩然\Desktop\P2 Results\All_pci.xlsx', sheet_name='3-6',index_col=0,parse_dates=[0])
pci6=pd.read_excel(r'C:\Users\徐浩然\Desktop\P2 Results\All_pci.xlsx', sheet_name='6',index_col=0,parse_dates=[0])
d=pd.read_excel(r'C:\Users\徐浩然\Desktop\P2 Results\All_to.xlsx', sheet_name='to',parse_dates=[0])

#-----------------------------------------------------------------------------------------------------------------------
P_pcit=pd.read_excel(r'C:\Users\徐浩然\Desktop\P2 Results\Positive_pci.xlsx', sheet_name='Total',index_col=0,parse_dates=[0])
P_pci13=pd.read_excel(r'C:\Users\徐浩然\Desktop\P2 Results\Positive_pci.xlsx', sheet_name='1-3',index_col=0,parse_dates=[0])
P_pci36=pd.read_excel(r'C:\Users\徐浩然\Desktop\P2 Results\Positive_pci.xlsx', sheet_name='3-6',index_col=0,parse_dates=[0])
P_pci6=pd.read_excel(r'C:\Users\徐浩然\Desktop\P2 Results\Positive_pci.xlsx', sheet_name='6',index_col=0,parse_dates=[0])

#-----------------------------------------------------------------------------------------------------------------------
N_pcit=pd.read_excel(r'C:\Users\徐浩然\Desktop\P2 Results\Negative_pci.xlsx', sheet_name='Total',index_col=0,parse_dates=[0])
N_pci13=pd.read_excel(r'C:\Users\徐浩然\Desktop\P2 Results\Negative_pci.xlsx', sheet_name='1-3',index_col=0,parse_dates=[0])
N_pci36=pd.read_excel(r'C:\Users\徐浩然\Desktop\P2 Results\Negative_pci.xlsx', sheet_name='3-6',index_col=0,parse_dates=[0])
N_pci6=pd.read_excel(r'C:\Users\徐浩然\Desktop\P2 Results\Negative_pci.xlsx', sheet_name='6',index_col=0,parse_dates=[0])

#-----------------------------------------------------------------------------------------------------------------------


d=d.iloc[:,0]
c1='#6C6D4B'
c2='#C1BB9F'
c3='#F6D8C0'
c4='#C06B5E'
c11='firebrick'
c22='#2F5597'
c33='sienna'
c44='darkslateblue'
c55='black'
c66='dimgrey'
c77='#493F36'
c88='teal'
bg='grey'
loc='upper left'

fr={'style':'italic','weight':'bold'}







# PCI-----------------------------------------------------------------------------------------------------------------------
plt.subplots(figsize=(15,11))
for i in range(math.comb(len(ll), 2)):
    plt.subplot(5,3,i+1)
    plt.fill_between(d, pcit.iloc[:, i], label='Total', color=c1,linewidth=0)
    plt.fill_between(d, pci13.iloc[:, i], label='1-5', color=c2,linewidth=0)
    plt.fill_between(d, pci36.iloc[:, i], label='5-22', color=c3,linewidth=0)
    plt.fill_between(d, pci6.iloc[:, i], label='22-inf', color=c4,linewidth=0)

    plt.plot(pcit.iloc[:, i], color=c1)
    plt.plot(pci13.iloc[:, i], color=c2)
    plt.plot(pci36.iloc[:, i], color=c3)
    plt.plot(pci6.iloc[:, i], color=c4)

    plt.plot(P_pcit.iloc[:, i], color=c11, label='Total')
    plt.plot(P_pci13.iloc[:, i], color=c22, label='1-5')
    plt.plot(P_pci36.iloc[:, i], color=c33, label='5-22')
    plt.plot(P_pci6.iloc[:, i], color=c44, label='22-inf')

    plt.plot(N_pcit.iloc[:, i], color=c55, label='Total',ls='--')
    plt.plot(N_pci13.iloc[:, i], color=c66, label='1-5',ls='--')
    plt.plot(N_pci36.iloc[:, i], color=c77, label='5-22',ls='--')
    plt.plot(N_pci6.iloc[:, i], color=c88, label='22-inf',ls='--')



    plt.xlim(pd.Timestamp('2014-04-29'), pd.Timestamp('2024-01-08'))
    plt.ylim(ymin=0)
    plt.xticks(fontsize=fs)
    plt.yticks(fontsize=fs)
    plt.margins(x=0)

    le = plt.legend(labels=[l[i]], frameon=False, loc=loc, handlelength=0, prop=fr)
    le.legendHandles[0].set_visible(False)

# plt.tight_layout()
plt.subplots_adjust(top=0.988,
bottom=0.035,
left=0.04,
right=0.974,
hspace=0.23,
wspace=0.125)
plt.savefig(r'C:/Users/徐浩然/Desktop/Paper 2 Figure/PCI.pdf', dpi=400)


# PCI Asy-----------------------------------------------------------------------------------------------------------------
plt.subplots(figsize=(15,11))
for i in range(math.comb(len(ll), 2)):
    plt.subplot(5,3,i+1)
    plt.fill_between(d, N_pcit.iloc[:, i] - P_pcit.iloc[:, i], label='Total', color=c1,linewidth=0)
    plt.fill_between(d, N_pci13.iloc[:, i] - P_pci13.iloc[:, i], label='1-5', color=c2,linewidth=0)
    plt.fill_between(d, N_pci36.iloc[:, i] - P_pci36.iloc[:, i], label='5-22', color=c3,linewidth=0)
    plt.fill_between(d, N_pci6.iloc[:, i] - P_pci6.iloc[:, i], label='22-inf', color=c4,linewidth=0)

    plt.plot(N_pcit.iloc[:, i] - P_pcit.iloc[:, i], color=c1)
    plt.plot(N_pci13.iloc[:, i] - P_pci13.iloc[:, i], color=c2)
    plt.plot(N_pci36.iloc[:, i] - P_pci36.iloc[:, i], color=c3)
    plt.plot(N_pci6.iloc[:, i] - P_pci6.iloc[:, i], color=c4)



    plt.xlim(pd.Timestamp('2014-04-29'), pd.Timestamp('2024-01-08'))

    plt.xticks(fontsize=fs)
    plt.yticks(fontsize=fs)
    plt.margins(x=0)

    le = plt.legend(labels=[l[i]], frameon=False, loc=loc, handlelength=0, prop=fr)
    le.legendHandles[0].set_visible(False)

# plt.tight_layout()
plt.subplots_adjust(top=0.988,
bottom=0.035,
left=0.04,
right=0.974,
hspace=0.23,
wspace=0.125)
plt.savefig(r'C:/Users/徐浩然/Desktop/Paper 2 Figure/PCIDinA.pdf', dpi=400)






# PCI
plt.subplots(figsize=(15,11))
for i in range(math.comb(len(ll), 2)):
    plt.subplot(5,3,i+1)
    plt.fill_between(d, (N_pcit.iloc[:, i] - P_pcit.iloc[:, i])/pcit.iloc[:, i], label='Total', color=c1,linewidth=0)
    plt.fill_between(d, (N_pci13.iloc[:, i] - P_pci13.iloc[:, i])/pci13.iloc[:, i], label='1-5', color=c2,linewidth=0)
    plt.fill_between(d, (N_pci36.iloc[:, i] - P_pci36.iloc[:, i])/pci36.iloc[:, i], label='5-22', color=c3,linewidth=0)
    plt.fill_between(d, (N_pci6.iloc[:, i] - P_pci6.iloc[:, i])/pci6.iloc[:, i], label='22-inf', color=c4,linewidth=0)

    plt.plot((N_pcit.iloc[:, i] - P_pcit.iloc[:, i])/pcit.iloc[:, i], color=c1)
    plt.plot((N_pci13.iloc[:, i] - P_pci13.iloc[:, i])/pci13.iloc[:, i], color=c2)
    plt.plot((N_pci36.iloc[:, i] - P_pci36.iloc[:, i])/pci36.iloc[:, i], color=c3)
    plt.plot((N_pci6.iloc[:, i] - P_pci6.iloc[:, i])/pci6.iloc[:, i], color=c4)



    plt.xlim(pd.Timestamp('2014-04-29'), pd.Timestamp('2024-01-08'))
    plt.ylim(-50,50)
    plt.yticks([-50,-25,0,25,50])
    plt.xticks(fontsize=fs)
    plt.yticks(fontsize=fs)
    plt.margins(x=0)

    le = plt.legend(labels=[l[i]], frameon=False, loc=loc, handlelength=0, prop=fr)
    le.legendHandles[0].set_visible(False)

plt.subplots_adjust(top=0.988,
bottom=0.035,
left=0.04,
right=0.974,
hspace=0.23,
wspace=0.125)
plt.savefig(r'C:/Users/徐浩然/Desktop/Paper 2 Figure/PCI%inA.pdf', dpi=400)





plt.show()
