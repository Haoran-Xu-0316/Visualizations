# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 14:04:23 2019

@author: artmenlope
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


def fill_between_3d(ax, x1, y1, z1, x2, y2, z2, mode=1, c='steelblue', alpha=0.6):
    """

    Function similar to the matplotlib.pyplot.fill_between function but
    for 3D plots.

    input:

        ax -> The axis where the function will plot.

        x1 -> 1D array. x coordinates of the first line.
        y1 -> 1D array. y coordinates of the first line.
        z1 -> 1D array. z coordinates of the first line.

        x2 -> 1D array. x coordinates of the second line.
        y2 -> 1D array. y coordinates of the second line.
        z2 -> 1D array. z coordinates of the second line.

    modes:

        mode = 1 -> Fill between the lines using the shortest distance between
                    both. Makes a lot of single trapezoids in the diagonals
                    between lines and then adds them into a single collection.

        mode = 2 -> Uses the lines as the edges of one only 3d polygon.

    Other parameters (for matplotlib):

        c -> the color of the polygon collection.
        alpha -> transparency of the polygon collection.

    """

    if mode == 1:

        for i in range(len(x1) - 1):
            verts = [(x1[i], y1[i], z1[i]), (x1[i + 1], y1[i + 1], z1[i + 1])] + \
                    [(x2[i + 1], y2[i + 1], z2[i + 1]), (x2[i], y2[i], z2[i])]

            ax.add_collection3d(Poly3DCollection([verts],
                                                 alpha=alpha,
                                                 linewidths=0,
                                                 color=c))

    if mode == 2:
        verts = [(x1[i], y1[i], z1[i]) for i in range(len(x1))] + \
                [(x2[i], y2[i], z2[i]) for i in range(len(x2))]

        ax.add_collection3d(Poly3DCollection([verts], alpha=alpha, color=c))


#----------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------



import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
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


        x = np.arange(len(tci.index))

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

        set01 = [x, 9 * np.ones(len(x)), np.zeros(len(x))]
        set02 = [x, 10 * np.ones(len(x)), np.zeros(len(x))]
        set03 = [x, 11 * np.ones(len(x)), np.zeros(len(x))]
        set04 = [x, 6 * np.ones(len(x)), np.zeros(len(x))]
        set05 = [x, 7 * np.ones(len(x)), np.zeros(len(x))]
        set06 = [x, 8 * np.ones(len(x)), np.zeros(len(x))]
        set07 = [x, 3 * np.ones(len(x)), np.zeros(len(x))]
        set08 = [x, 4 * np.ones(len(x)), np.zeros(len(x))]
        set09 = [x, 5 * np.ones(len(x)), np.zeros(len(x))]
        set010 = [x, 0 * np.ones(len(x)), np.zeros(len(x))]
        set011 = [x, 1 * np.ones(len(x)), np.zeros(len(x))]
        set012 = [x, 2 * np.ones(len(x)), np.zeros(len(x))]

        set1 = [x, 9 * np.ones(len(x)), f1]
        set2 = [x, 10 * np.ones(len(x)), f2]
        set3 = [x, 11 * np.ones(len(x)), f3]
        set4 = [x, 6 * np.ones(len(x)), f4]
        set5 = [x, 7 * np.ones(len(x)), f5]
        set6 = [x, 8 * np.ones(len(x)), f6]
        set7 = [x, 3 * np.ones(len(x)), f7]
        set8 = [x, 4 * np.ones(len(x)), f8]
        set9 = [x, 5 * np.ones(len(x)), f9]
        set10 = [x, 0 * np.ones(len(x)), f10]
        set11 = [x, 1 * np.ones(len(x)), f11]
        set12 = [x, 2 * np.ones(len(x)), f12]




        # fill_between_3d(ax, *set03, *set3, mode=1, c=c55, alpha=0.7)
        ax.plot(*set3, c=c55)
        # fill_between_3d(ax, *set02, *set2, mode=1, c=c11, alpha=0.7)
        ax.plot(*set2, c=c11)
        fill_between_3d(ax, *set01, *set1, mode=1, c=c1, alpha=0.7)
        ax.plot(*set1, c=c1)
        # fill_between_3d(ax, *set06, *set6, mode=1, c=c66, alpha=0.7)
        ax.plot(*set6, c=c66)
        # fill_between_3d(ax, *set05, *set5, mode=1, c=c22, alpha=0.7)
        ax.plot(*set5, c=c22)
        fill_between_3d(ax, *set04, *set4, mode=1, c=c2, alpha=0.7)
        ax.plot(*set4, c=c2)
        # fill_between_3d(ax, *set09, *set9, mode=1, c=c77, alpha=0.7)
        ax.plot(*set9, c=c77)
        # fill_between_3d(ax, *set08, *set8, mode=1, c=c33, alpha=0.7)
        ax.plot(*set8, c=c33)
        fill_between_3d(ax, *set07, *set7, mode=1, c=c3, alpha=0.7)
        ax.plot(*set7, c=c3)
        # fill_between_3d(ax, *set012, *set12, mode=1, c=c88, alpha=0.7)
        ax.plot(*set12, c=c88)
        # fill_between_3d(ax, *set011, *set11, mode=1, c=c44, alpha=0.7)
        ax.plot(*set11, c=c44)
        fill_between_3d(ax, *set010, *set10, mode=1, c=c4, alpha=0.7)
        ax.plot(*set10, c=c4)


















        ax.set_xticks(x, tci.index.strftime('%Y'))
        ax.xaxis.set_major_locator(MaxNLocator(nbins=10))
        # ax.tick_params(axis='y', which='both', pad=10)
        ax.set_yticks(range(0, 12))
        ax.set_yticklabels(l, ha='left', va='center')
        # ax.set_box_aspect([7, 7*3.14159, 4])

        ax.xaxis._axinfo["grid"].update({"linewidth": 0.3, "linestyle": '--', "color": 'k'})
        ax.yaxis._axinfo["grid"].update({"linewidth": 0.3, "linestyle": '--', "color": 'k'})
        ax.zaxis._axinfo["grid"].update({"linewidth": 0.3, "linestyle": '--', "color": 'k'})

        # ax.xaxis.set_pane_color((0, 0, 0, 0))
        # ax.yaxis.set_pane_color((0, 0, 0, 0))
        # ax.zaxis.set_pane_color((0, 0, 0, 0))
        #
        # ax.tick_params(axis='z', direction='in')
        # ax.tick_params(axis='x', direction='in')
        # ax.tick_params(axis='y', direction='in')
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
plt.savefig(r'C:/Users/徐浩然/Desktop/Paper 2 Figure/Rob_TCI_p.svg',dpi=300,bbox_inches='tight')
plt.show()
