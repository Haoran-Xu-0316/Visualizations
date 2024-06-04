# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from matplotlib.collections import PolyCollection
import matplotlib.pyplot as plt
import numpy as np





df = pd.read_excel(r'C:\Users\徐浩然\Desktop\P2 Results_50\All_total.xlsx', sheet_name='total')
date= df.iloc[:, 0]

xx = np.linspace(0, len(date), len(date))
def polygon_under_timeseries(y):
    return list(zip(xx, y)) + [(xx[-1], 0), (xx[0], 0)]
def fill_between_3d(series,z, c, alpha=0.6):
    verts = [polygon_under_timeseries(series)]
    poly = PolyCollection(verts,  alpha=alpha,linewidths=0, color=c)
    ax.add_collection3d(poly, zs=z, zdir='y')




#----------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------




#全局设置-----------------------------------------------------------------------------------------------------------------
plt.rcParams['font.sans-serif'] = ['Palatino Linotype']
# plt.rcParams["font.weight"] = "bold"
# plt.rcParams['font.style']='italic'
plt.rcParams['font.size'] = 12
plt.rcParams['axes.unicode_minus'] = True
plt.rcParams['lines.linewidth'] = 0.5
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
plt.rcParams['axes.xmargin'] = 0
plt.rcParams['axes.ymargin'] = 0
plt.rcParams['axes.zmargin'] = 0


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
l=['22-inf','P. 22-inf','N. 22-inf','5-22','P. 5-22','N. 5-22','1-5','P. 1-5','N. 1-5','Total','P. Total','N. Total']
l.reverse()



sub=['(a) 50-step-ahead','(b) 100-step-ahead','(c) 150-step-ahead','(d) 200-step-ahead']
#-----------------------------------------------------------------------------------------------------------------------

fig=plt.figure(figsize=(20,20))
for i in range(2):
    for j in range(2):

        if i == 0 & j == 0:
            tci = pd.read_excel(r'C:\Users\徐浩然\Desktop\P2 Results_50\All_total.xlsx', sheet_name='total',index_col=0,parse_dates=[0])
            P_tci = pd.read_excel(r'C:\Users\徐浩然\Desktop\P2 Results_50\Positive_total.xlsx', sheet_name='total',index_col=0,parse_dates=[0])
            N_tci = pd.read_excel(r'C:\Users\徐浩然\Desktop\P2 Results_50\Negative_total.xlsx', sheet_name='total',index_col=0,parse_dates=[0])

            print('00')

        if i == 0 & j == 1:
            tci = pd.read_excel(r'C:\Users\徐浩然\Desktop\P2 Results_100\All_total.xlsx', sheet_name='total',index_col=0, parse_dates=[0])
            P_tci = pd.read_excel(r'C:\Users\徐浩然\Desktop\P2 Results_100\Positive_total.xlsx', sheet_name='total',index_col=0, parse_dates=[0])
            N_tci = pd.read_excel(r'C:\Users\徐浩然\Desktop\P2 Results_100\Negative_total.xlsx', sheet_name='total',index_col=0, parse_dates=[0])
            print('01')
        if i == 1 & j == 0:
            tci = pd.read_excel(r'C:\Users\徐浩然\Desktop\P2 Results_150\All_total.xlsx', sheet_name='total',index_col=0, parse_dates=[0])
            P_tci = pd.read_excel(r'C:\Users\徐浩然\Desktop\P2 Results_150\Positive_total.xlsx', sheet_name='total',index_col=0, parse_dates=[0])
            N_tci = pd.read_excel(r'C:\Users\徐浩然\Desktop\P2 Results_150\Negative_total.xlsx', sheet_name='total',index_col=0, parse_dates=[0])
            print('10')
        if i == 1 & j == 1:
            tci = pd.read_excel(r'C:\Users\徐浩然\Desktop\P2 Results_200\All_total.xlsx', sheet_name='total',index_col=0, parse_dates=[0])
            P_tci = pd.read_excel(r'C:\Users\徐浩然\Desktop\P2 Results_200\Positive_total.xlsx', sheet_name='total',index_col=0, parse_dates=[0])
            N_tci = pd.read_excel(r'C:\Users\徐浩然\Desktop\P2 Results_200\Negative_total.xlsx', sheet_name='total',index_col=0, parse_dates=[0])
            print('11')

        ax = fig.add_subplot(2, 2, 2*i+j+1, projection='3d')


        x = np.arange(len(date))

        f1 = tci.iloc[:, 0].values
        f2 = P_tci.iloc[:, 0].values
        f3 = N_tci.iloc[:, 0].values
        f4 = tci.iloc[:, 1].values
        f5 = P_tci.iloc[:, 1].values
        f6 = N_tci.iloc[:, 1].values
        f7 = tci.iloc[:, 2].values
        f8 = P_tci.iloc[:, 2].values
        f9 = N_tci.iloc[:, 2].values
        f10 = tci.iloc[:, 3].values
        f11 = P_tci.iloc[:, 3].values
        f12 = N_tci.iloc[:, 3].values

        set01 = [x, 2 * np.ones(len(x)), np.zeros(len(x))]
        set02 = [x, 1 * np.ones(len(x)), np.zeros(len(x))]
        set03 = [x, 0 * np.ones(len(x)), np.zeros(len(x))]
        set04 = [x, 5 * np.ones(len(x)), np.zeros(len(x))]
        set05 = [x, 4 * np.ones(len(x)), np.zeros(len(x))]
        set06 = [x, 3 * np.ones(len(x)), np.zeros(len(x))]
        set07 = [x, 8 * np.ones(len(x)), np.zeros(len(x))]
        set08 = [x, 7 * np.ones(len(x)), np.zeros(len(x))]
        set09 = [x, 6 * np.ones(len(x)), np.zeros(len(x))]
        set010 = [x, 11 * np.ones(len(x)), np.zeros(len(x))]
        set011 = [x, 10 * np.ones(len(x)), np.zeros(len(x))]
        set012 = [x, 9 * np.ones(len(x)), np.zeros(len(x))]

        set1 = [x, 2 * np.ones(len(x)), f1]
        set2 = [x, 1 * np.ones(len(x)), f2]
        set3 = [x, 0 * np.ones(len(x)), f3]
        set4 = [x, 5 * np.ones(len(x)), f4]
        set5 = [x, 4 * np.ones(len(x)), f5]
        set6 = [x, 3 * np.ones(len(x)), f6]
        set7 = [x, 8 * np.ones(len(x)), f7]
        set8 = [x, 7 * np.ones(len(x)), f8]
        set9 = [x, 6 * np.ones(len(x)), f9]
        set10 = [x, 11 * np.ones(len(x)), f10]
        set11 = [x, 10 * np.ones(len(x)), f11]
        set12 = [x, 9 * np.ones(len(x)), f12]



        fill_between_3d(f3, 0, c=c55)
        # ax.plot(*set3, c=c55)
        fill_between_3d(f2, 1, c=c11)
        # ax.plot(*set2, c=c11)
        fill_between_3d(f1, 2, c=c1)
        # ax.plot(*set1, c=c1)
        fill_between_3d(f6, 3, c=c66)
        # ax.plot(*set6, c=c66)
        fill_between_3d(f5, 4, c=c22)
        # ax.plot(*set5, c=c22)
        fill_between_3d(f4, 5, c=c2)
        # ax.plot(*set4, c=c2)
        fill_between_3d(f9, 6, c=c77)
        # ax.plot(*set9, c=c77)
        fill_between_3d(f8, 7, c=c33)
        # ax.plot(*set8, c=c33)
        fill_between_3d(f7, 8, c=c3)
        # ax.plot(*set7, c=c3)
        fill_between_3d(f12, 9, c=c88)
        # ax.plot(*set12, c=c88)
        fill_between_3d(f11, 10, c=c44)
        # ax.plot(*set11, c=c44)
        fill_between_3d(f10, 11, c=c4)
        # ax.plot(*set10, c=c4)

        ax.invert_yaxis()



        ax.set_xticks(x, tci.index.strftime('%Y'))
        ax.xaxis.set_major_locator(MaxNLocator(nbins=10))
        # ax.tick_params(axis='y', which='both', pad=10)
        ax.set_yticks(range(0, 12))
        ax.set_yticklabels(l, ha='left', va='center')

        ax.set_zlim(0, 50)



        ax.zaxis._axinfo['juggled'] = (1, 2, 0)
        ax.xaxis._axinfo['tick']['outward_factor'] = 0
        ax.xaxis._axinfo['tick']['inward_factor'] = 0.2
        ax.yaxis._axinfo['tick']['outward_factor'] = 0
        ax.yaxis._axinfo['tick']['inward_factor'] = 0.2
        ax.zaxis._axinfo['tick']['outward_factor'] = 0.2
        ax.zaxis._axinfo['tick']['inward_factor'] = 0.0

        ax.text2D(0.05, 0.95, sub[2*i+j], horizontalalignment='left', fontweight='bold',fontsize=17,transform=ax.transAxes)


        # ax.set_zlim(0, max(np.max(f1), np.max(f2), np.max(f3)))
        ax.grid(False)
        # ax.view_init(elev=30, azim=-60)
fig.subplots_adjust(top=0.9,
bottom=0.21,
left=0.125,
right=0.875,
hspace=0.0,
wspace=0.0)
# fig.subplots_adjust(hspace=0.0,wspace=0.1)
# fig.tight_layout()
plt.savefig(r'C:/Users/徐浩然/Desktop/Paper 2 Figure/Rob_TCI.pdf',dpi=300,bbox_inches='tight')
plt.show()
