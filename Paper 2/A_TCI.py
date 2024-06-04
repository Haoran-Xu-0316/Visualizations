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
plt.rcParams['font.size'] = 12
plt.rcParams['axes.unicode_minus'] = True
plt.rcParams['lines.linewidth'] = 0.5
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
ll=['EUA',	'SZA',	'HBA', 'PMI', 'CEI', 'GBI']

l = []

for i in range(len(ll)):
    if i + 1 <= len(ll):
        for j in range(i + 1, len(ll)):
            l.append(f"{ll[i]}-{ll[j]}")

#-----------------------------------------------------------------------------------------------------------------------
tci=pd.read_excel(r'C:\Users\徐浩然\Desktop\P2 Results\All_total.xlsx', sheet_name='total',index_col=0,parse_dates=[0])
net=pd.read_excel(r'C:\Users\徐浩然\Desktop\P2 Results\All_net.xlsx', sheet_name='net',index_col=0,parse_dates=[0])
t=pd.read_excel(r'C:\Users\徐浩然\Desktop\P2 Results\All_to.xlsx', sheet_name='to',index_col=0,parse_dates=[0])
f=pd.read_excel(r'C:\Users\徐浩然\Desktop\P2 Results\All_from.xlsx', sheet_name='from',index_col=0,parse_dates=[0])
d=pd.read_excel(r'C:\Users\徐浩然\Desktop\P2 Results\All_to.xlsx', sheet_name='to',parse_dates=[0])



#-----------------------------------------------------------------------------------------------------------------------
P_tci=pd.read_excel(r'C:\Users\徐浩然\Desktop\P2 Results\Positive_total.xlsx', sheet_name='total',index_col=0,parse_dates=[0])
P_net=pd.read_excel(r'C:\Users\徐浩然\Desktop\P2 Results\Positive_net.xlsx', sheet_name='net',index_col=0,parse_dates=[0])
P_t=pd.read_excel(r'C:\Users\徐浩然\Desktop\P2 Results\Positive_to.xlsx', sheet_name='to',index_col=0,parse_dates=[0])
P_f=pd.read_excel(r'C:\Users\徐浩然\Desktop\P2 Results\Positive_from.xlsx', sheet_name='from',index_col=0,parse_dates=[0])


#-----------------------------------------------------------------------------------------------------------------------
N_tci=pd.read_excel(r'C:\Users\徐浩然\Desktop\P2 Results\Negative_total.xlsx', sheet_name='total',index_col=0,parse_dates=[0])
N_net=pd.read_excel(r'C:\Users\徐浩然\Desktop\P2 Results\Negative_net.xlsx', sheet_name='net',index_col=0,parse_dates=[0])
N_t=pd.read_excel(r'C:\Users\徐浩然\Desktop\P2 Results\Negative_to.xlsx', sheet_name='to',index_col=0,parse_dates=[0])
N_f=pd.read_excel(r'C:\Users\徐浩然\Desktop\P2 Results\Negative_from.xlsx', sheet_name='from',index_col=0,parse_dates=[0])

#-----------------------------------------------------------------------------------------------------------------------

C=['#FFDDB7','#9C3434','dimgrey','#E3A085','#334666']
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
fs=12
#-----------------------------------------------------------------------------------------------------------------------

## TCI----------------------------------------------------------------------------------------------------------------------
plt.figure(figsize=(10,4))

# plt.fill_between(pd.date_range(start='2015-03-01', end='2015-03-31', freq='D'), 0,52,color=bg, alpha=0.3, linewidth=0)
# plt.fill_between(pd.date_range(start='2015-11-30', end='2015-12-12', freq='D'), 0,52,color=bg, alpha=0.3, linewidth=0)
# plt.fill_between(pd.date_range(start='2016-04-21', end='2016-04-22', freq='D'), 0,52,color=bg, alpha=0.3, linewidth=0)
# plt.fill_between(pd.date_range(start='2018-12-02', end='2018-12-14', freq='D'), 0,52,color=bg, alpha=0.3, linewidth=0)
# plt.fill_between(pd.date_range(start='2019-12-02', end='2019-12-13', freq='D'), 0,52,color=bg, alpha=0.3, linewidth=0)
# plt.fill_between(pd.date_range(start='2015-01-01', end='2015-02-01', freq='D'), 0,52,color=bg, alpha=0.3, linewidth=0)
#
# plt.fill_between(pd.date_range(start='2015-06-01', end='2015-07-01', freq='D'), 0,52,color=bg, alpha=0.3, linewidth=0)
# plt.fill_between(pd.date_range(start='2019-05-20', end='2019-06-03', freq='D'), 0,52,color=bg, alpha=0.3, linewidth=0)
# plt.fill_between(pd.date_range(start='2020-01-01', end='2020-02-01', freq='D'), 0,52,color=bg, alpha=0.3, linewidth=0)
# plt.fill_between(pd.date_range(start='2021-07-21', end='2021-08-21', freq='D'), 0,52,color=bg, alpha=0.3, linewidth=0)
# plt.fill_between(pd.date_range(start='2016-02-01', end='2016-02-28', freq='D'), 0,52,color=bg, alpha=0.3, linewidth=0)
# plt.fill_between(pd.date_range(start='2016-12-01', end='2016-12-30', freq='D'), 0,52,color=bg, alpha=0.3, linewidth=0)
#
# plt.fill_between(pd.date_range(start='2017-06-30', end='2017-10-01', freq='D'), 0,52,color=bg, alpha=0.3, linewidth=0)
# plt.fill_between(pd.date_range(start='2018-07-20', end='2018-08-30', freq='D'), 0,52,color=bg, alpha=0.3, linewidth=0)
# plt.fill_between(pd.date_range(start='2014-06', end='2015-01', freq='M'), 0,52,color=bg, alpha=0.3, linewidth=0)
# plt.fill_between(pd.date_range(start='2015-06-12', end='2015-08-26', freq='D'), 0,52,color=bg, alpha=0.3, linewidth=0)
# plt.fill_between(pd.date_range(start='2018-01', end='2018-02', freq='M'), 0,52,color=bg, alpha=0.3, linewidth=0)
# plt.fill_between(pd.date_range(start='2019-12-31', end='2022-12-31', freq='D'), 0,52,color=bg, alpha=0.3, linewidth=0)



plt.fill_between(d, tci.iloc[:, 0], label='Total', color=c1,linewidth=0)
plt.fill_between(d, tci.iloc[:, 1], label='1-5', color=c2,linewidth=0)
plt.fill_between(d, tci.iloc[:, 2], label='5-22', color=c3,linewidth=0)
plt.fill_between(d, tci.iloc[:, 3], label='22-inf', color=c4,linewidth=0)
plt.plot(tci.iloc[:, 0], color=c1)
plt.plot(tci.iloc[:, 1], color=c2)
plt.plot(tci.iloc[:, 2], color=c3)
plt.plot(tci.iloc[:, 3], color=c4)

plt.plot(P_tci.iloc[:, 0], color=c11,label='P. Total')
plt.plot(P_tci.iloc[:, 1], color=c22,label='P. 1-5')
plt.plot(P_tci.iloc[:, 2], color=c33,label='P. 5-22')
plt.plot(P_tci.iloc[:, 3], color=c44,label='P. 22-inf')

plt.plot(N_tci.iloc[:, 0], color=c55,label='N. Total',ls='--')
plt.plot(N_tci.iloc[:, 1], color=c66,label='N. 1-5',ls='--')
plt.plot(N_tci.iloc[:, 2], color=c77,label='N. 5-22',ls='--')
plt.plot(N_tci.iloc[:, 3], color=c88,label='N. 22-inf',ls='--')



plt.xlim(pd.Timestamp('2014-04-29'), pd.Timestamp('2024-01-08'))
plt.ylim(ymin=0)
plt.xticks(fontsize=fs)
plt.yticks(fontsize=fs)

plt.legend(frameon=False, loc='upper center', ncol=6)
# plt.tight_layout()
plt.subplots_adjust(
top=0.98,
bottom=0.08,
left=0.058,
right=0.967,
hspace=0.2,
wspace=0.2)

plt.savefig(r'C:/Users/徐浩然/Desktop/Paper 2 Figure/TCI.pdf', dpi=400)







## TCI Asy----------------------------------------------------------------------------------------------------------------------
plt.figure(figsize=(10,4))
plt.fill_between(d, N_tci.iloc[:, 0]-P_tci.iloc[:, 0], label='Total', color=c1,linewidth=0)
plt.fill_between(d, N_tci.iloc[:, 1]-P_tci.iloc[:, 1], label='1-5', color=c2,linewidth=0)
plt.fill_between(d, N_tci.iloc[:, 2]-P_tci.iloc[:, 2], label='5-22', color=c3,linewidth=0)
plt.fill_between(d, N_tci.iloc[:, 3]-P_tci.iloc[:, 3], label='22-inf', color=c4,linewidth=0)

plt.plot(N_tci.iloc[:, 0]-P_tci.iloc[:, 0], color=c1)
plt.plot(N_tci.iloc[:, 1]-P_tci.iloc[:, 1], color=c2)
plt.plot(N_tci.iloc[:, 2]-P_tci.iloc[:, 2], color=c3)
plt.plot(N_tci.iloc[:, 3]-P_tci.iloc[:, 3], color=c4)




plt.xlim(pd.Timestamp('2014-04-29'), pd.Timestamp('2024-01-08'))
plt.xticks(fontsize=fs)
plt.yticks(fontsize=fs)
plt.margins(x=0)
plt.legend(frameon=False, loc='upper center', ncol=6)
# plt.tight_layout()
plt.subplots_adjust(
top=0.98,
bottom=0.08,
left=0.058,
right=0.967,
hspace=0.2,
wspace=0.2)

plt.savefig(r'C:/Users/徐浩然/Desktop/Paper 2 Figure/TCIDinA.pdf', dpi=400)









## TCI %Asy----------------------------------------------------------------------------------------------------------------------
plt.figure(figsize=(10,4))
plt.fill_between(d, ((N_tci.iloc[:, 0]-P_tci.iloc[:, 0])/tci.iloc[:, 0]), label='Total', color=c1,linewidth=0)
plt.fill_between(d, ((N_tci.iloc[:, 1]-P_tci.iloc[:, 1])/tci.iloc[:, 1]), label='1-5', color=c2,linewidth=0)
plt.fill_between(d, ((N_tci.iloc[:, 2]-P_tci.iloc[:, 2])/tci.iloc[:, 2]), label='5-22', color=c3,linewidth=0)
plt.fill_between(d, ((N_tci.iloc[:, 3]-P_tci.iloc[:, 3])/tci.iloc[:, 3]), label='22-inf', color=c4,linewidth=0)

plt.plot(((N_tci.iloc[:, 0]-P_tci.iloc[:, 0])/tci.iloc[:, 0]), color=c1)
plt.plot(((N_tci.iloc[:, 1]-P_tci.iloc[:, 1])/tci.iloc[:, 1]), color=c2)
plt.plot(((N_tci.iloc[:, 2]-P_tci.iloc[:, 2])/tci.iloc[:, 2]), color=c3)
plt.plot(((N_tci.iloc[:, 3]-P_tci.iloc[:, 3])/tci.iloc[:, 3]), color=c4)




plt.xlim(pd.Timestamp('2014-04-29'), pd.Timestamp('2024-01-08'))
plt.xticks(fontsize=fs)
plt.yticks(fontsize=fs)
plt.margins(x=0)
plt.legend(frameon=False, loc='upper center', ncol=6)
# plt.tight_layout()
plt.subplots_adjust(
top=0.98,
bottom=0.08,
left=0.058,
right=0.967,
hspace=0.2,
wspace=0.2)

plt.savefig(r'C:/Users/徐浩然/Desktop/Paper 2 Figure/TCI%inA.pdf', dpi=400)

plt.show()