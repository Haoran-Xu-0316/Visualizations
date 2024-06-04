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
plt.rcParams['font.size'] = 12
fs=12
plt.rcParams['axes.unicode_minus'] = True
plt.rcParams['lines.linewidth'] = 0.4
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
ll=['EUA',	'SZA',	'HBA', 'PMI', 'CEI', 'GBI']

l = []

for i in range(len(ll)):
    if i + 1 <= len(ll):
        for j in range(i + 1, len(ll)):
            l.append(f"{ll[i]} - {ll[j]}")

#-----------------------------------------------------------------------------------------------------------------------

net=pd.read_excel(r'C:\Users\徐浩然\Desktop\P2 Results\All_net.xlsx', sheet_name='net',index_col=0,parse_dates=[0])
d=pd.read_excel(r'C:\Users\徐浩然\Desktop\P2 Results\All_to.xlsx', sheet_name='to',parse_dates=[0])

#-----------------------------------------------------------------------------------------------------------------------

P_net=pd.read_excel(r'C:\Users\徐浩然\Desktop\P2 Results\Positive_net.xlsx', sheet_name='net',index_col=0,parse_dates=[0])

#-----------------------------------------------------------------------------------------------------------------------

N_net=pd.read_excel(r'C:\Users\徐浩然\Desktop\P2 Results\Negative_net.xlsx', sheet_name='net',index_col=0,parse_dates=[0])

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
#bbox_to_anchor=(0 if i % 2 == 0 else 1, 0 if i < 2 else 1)

fr={'style':'italic','weight':'bold'}






## NET-----------------------------------------------------------------------------------------------------------------------

plt.subplots(figsize=(12,7.5))
for i in range(len(ll)):
    plt.subplot(3, 2, i+1)
    plt.fill_between(d, net.iloc[:, i],label='Total',color=c1,linewidth=0)
    plt.fill_between(d, net.iloc[:, i+len(ll)],label='1-5',color=c2,linewidth=0)
    plt.fill_between(d, net.iloc[:, i+len(ll)*2],label='5-22',color=c3,linewidth=0)
    plt.fill_between(d, net.iloc[:, i+len(ll)*3],label='22-inf',color=c4,linewidth=0)

    plt.plot(net.iloc[:, i],color=c1)
    plt.plot(net.iloc[:, i+len(ll)],color=c2)
    plt.plot(net.iloc[:, i+len(ll)*2],color=c3)
    plt.plot(net.iloc[:, i+len(ll)*3],color=c4)

    plt.plot(P_net.iloc[:, i],color=c11,label='P_Total')
    plt.plot(P_net.iloc[:, i+len(ll)],color=c22,label='P_1-5')
    plt.plot(P_net.iloc[:, i+len(ll)*2],color=c33,label='P_5-22')
    plt.plot(P_net.iloc[:, i+len(ll)*3],color=c44,label='P_22-inf')

    plt.plot(N_net.iloc[:, i],color=c55,label='N_Total',ls='--')
    plt.plot(N_net.iloc[:, i+len(ll)],color=c66,label='N_1-5',ls='--')
    plt.plot(N_net.iloc[:, i+len(ll)*2],color=c77,label='N_5-22',ls='--')
    plt.plot(N_net.iloc[:, i+len(ll)*3],color=c88,label='N_22-inf',ls='--')


    plt.xlim(pd.Timestamp('2014-04-29'), pd.Timestamp('2024-01-08'))

    plt.xticks(fontsize=fs)
    plt.yticks(fontsize=fs)
    plt.margins(x=0)

    le = plt.legend(labels=[ll[i]], frameon=False, loc=loc, handlelength=0, prop=fr)
    le.legendHandles[0].set_visible(False)

plt.subplots_adjust(
top=0.988,
bottom=0.04,
left=0.05,
right=0.966,
hspace=0.19,
wspace=0.105)
plt.savefig(r'C:/Users/徐浩然/Desktop/Paper 2 Figure/NET.pdf',dpi=400)





## NET Asy-----------------------------------------------------------------------------------------------------------------------

plt.subplots(figsize=(12,7.5))
for i in range(len(ll)):
    plt.subplot(3, 2, i+1)
    plt.fill_between(d, N_net.iloc[:, i] - P_net.iloc[:, i], label='Total', color=c1,linewidth=0)
    plt.fill_between(d, N_net.iloc[:, i+len(ll)] - P_net.iloc[:, i+len(ll)], label='1-5', color=c2,linewidth=0)
    plt.fill_between(d, N_net.iloc[:, i+len(ll)*2] - P_net.iloc[:, i+len(ll)*2], label='5-22', color=c3,linewidth=0)
    plt.fill_between(d, N_net.iloc[:, i+len(ll)*3] - P_net.iloc[:, i+len(ll)*3], label='22-inf', color=c4,linewidth=0)

    plt.plot(N_net.iloc[:, i] - P_net.iloc[:, i], color=c1)
    plt.plot(N_net.iloc[:, i+len(ll)] - P_net.iloc[:, i+len(ll)], color=c2)
    plt.plot(N_net.iloc[:, i+len(ll)*2] - P_net.iloc[:, i+len(ll)*2], color=c3)
    plt.plot(N_net.iloc[:, i+len(ll)*3] - P_net.iloc[:, i+len(ll)*3], color=c4)


    plt.xlim(pd.Timestamp('2014-04-29'), pd.Timestamp('2024-01-08'))

    plt.xticks(fontsize=fs)
    plt.yticks(fontsize=fs)
    plt.margins(x=0)

    le = plt.legend(labels=[ll[i]], frameon=False, loc=loc, handlelength=0, prop=fr)
    le.legendHandles[0].set_visible(False)

plt.subplots_adjust(
top=0.988,
bottom=0.04,
left=0.05,
right=0.966,
hspace=0.19,
wspace=0.105)
plt.savefig(r'C:/Users/徐浩然/Desktop/Paper 2 Figure/NETDinA.pdf',dpi=400)







plt.subplots(figsize=(12,7.5))
for i in range(len(ll)):
    plt.subplot(3, 2, i+1)
    plt.fill_between(d, (N_net.iloc[:, i] - P_net.iloc[:, i]) / net.iloc[:, i], label='Total', color=c1,linewidth=0)
    plt.fill_between(d, (N_net.iloc[:, i + len(ll)] - P_net.iloc[:, i + len(ll)]) / net.iloc[:, i + len(ll)], label='1-5',color=c2,linewidth=0)
    plt.fill_between(d, (N_net.iloc[:, i + len(ll) * 2] - P_net.iloc[:, i + len(ll) * 2]) / net.iloc[:, i + len(ll) * 2],label='5-22', color=c3,linewidth=0)
    plt.fill_between(d, (N_net.iloc[:, i + len(ll) * 3] - P_net.iloc[:, i + len(ll) * 3]) / net.iloc[:, i + len(ll) * 3],label='22-inf', color=c4,linewidth=0)

    plt.plot((N_net.iloc[:, i] - P_net.iloc[:, i]) / net.iloc[:, i], color=c1)
    plt.plot((N_net.iloc[:, i + len(ll)] - P_net.iloc[:, i + len(ll)]) / net.iloc[:, i + len(ll)], color=c2)
    plt.plot((N_net.iloc[:, i + len(ll) * 2] - P_net.iloc[:, i + len(ll) * 2]) / net.iloc[:, i + len(ll) * 2], color=c3)
    plt.plot((N_net.iloc[:, i + len(ll) * 3] - P_net.iloc[:, i + len(ll) * 3]) / net.iloc[:, i + len(ll) * 3], color=c4)


    plt.xlim(pd.Timestamp('2014-04-29'), pd.Timestamp('2024-01-08'))
    plt.ylim(-50,50)
    plt.yticks([-50,-25,0,25,50])
    plt.xticks(fontsize=fs)
    plt.yticks(fontsize=fs)
    plt.margins(x=0)

    le = plt.legend(labels=[ll[i]], frameon=False, loc=loc, handlelength=0, prop=fr)
    le.legendHandles[0].set_visible(False)

plt.subplots_adjust(
top=0.988,
bottom=0.04,
left=0.05,
right=0.966,
hspace=0.19,
wspace=0.105)
plt.savefig(r'C:/Users/徐浩然/Desktop/Paper 2 Figure/NET%inA.pdf',dpi=400)



plt.show()