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
from matplotlib import cm
from mpl_toolkits.mplot3d import axes3d
from pycop import student
from scipy.special import gamma
from scipy.stats import t

#全局设置-----------------------------------------------------------------------------------------------------------------
# plt.rcParams['font.sans-serif']=['Microsoft YaHei']
plt.rcParams['font.sans-serif'] = ['Palatino Linotype']
# plt.rcParams["font.weight"] = "bold"
plt.rcParams['font.size'] = 14
plt.rcParams['axes.unicode_minus'] = True
plt.rcParams['lines.linewidth'] = 1
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
plt.rcParams['axes.xmargin'] = 0
plt.rcParams['axes.ymargin'] = 0
plt.rcParams['axes.zmargin'] = 0

def get_pdf(u, v, param):

    rho = param[0]
    nu = param[1]

    term1 = gamma((nu + 2) / 2) * gamma(nu / 2)
    term2 = gamma((nu + 1) / 2) ** 2

    u_ = t.ppf(u, df=nu)
    v_ = t.ppf(v, df=nu)

    det_rho = 1 - rho ** 2
    multid = (-2 * u_ * v_ * rho + (u_ ** 2) + (v_ ** 2)) / det_rho
    term3 = (1 + multid / nu) ** ((nu + 2) / 2)

    prod1 = (1 + (u_ ** 2) / nu) ** ((nu + 1) / 2)
    prod2 = (1 + (v_ ** 2) / nu) ** ((nu + 1) / 2)
    prod = prod1 * prod2

    return (1 / np.sqrt(det_rho)) * (term1 * prod) / (term2 * term3)


def plot_bivariate_3d(X, Y, Z, bounds,loc1,loc2,lo3,par):
    ax = fig.add_subplot(loc1,loc2,lo3, projection='3d')
    ax.set_xticks(np.linspace(bounds[0], bounds[1], 6))
    ax.set_yticks(np.linspace(bounds[0], bounds[1], 6))
    ax.set_xlim(bounds)
    ax.set_ylim(bounds)

    # D9D9D9 灰色
    # '#1E3350' 蓝色

    ax.plot_surface(X, Y, Z, edgecolor='#1E3350', lw=0,cmap=cm.RdBu_r,
                    rstride=1, cstride=1,
                    alpha=0.4)

    ax.set(xlim=[X.min(), X.max()], ylim=[Y.min(), Y.max()], zlim=[Z.min(), Z.max()])

    ax.contourf(X, Y, Z, zdir='z', offset=0, cmap='RdBu_r',alpha=0.6)
    ax.contourf(X, Y, Z, zdir='x', offset=0, cmap='RdBu_r',alpha=0.6)
    ax.contourf(X, Y, Z, zdir='y', offset=1, cmap='RdBu_r',alpha=0.6)


    # ax.contour(X, Y, Z, zdir='z', offset=0, cmap='RdBu_r')
    # ax.contour(X, Y, Z, zdir='x', offset=0, cmap='RdBu_r')
    # ax.contour(X, Y, Z, zdir='y', offset=1, cmap='RdBu_r')
    ax.text2D(0.95, 0.95, chr(961)+' = '+f"{par[0]:.2f}"+', '+chr(957)+' = '+f"{par[1]:.2f}",horizontalalignment='right',fontweight='bold',style='italic' ,transform=ax.transAxes)
    ax.text2D(0.05, 0.95, par[2],horizontalalignment='left',fontweight='bold',style='italic' ,transform=ax.transAxes)
    # ax.view_init(elev=30, azim=45)
    ax.xaxis.set_tick_params(pad=0.5)
    ax.yaxis.set_tick_params(pad=0.5)
    ax.zaxis.set_tick_params(pad=0.5)


    ax.xaxis._axinfo['tick']['outward_factor'] = 0
    ax.xaxis._axinfo['tick']['inward_factor'] = 0.25
    ax.yaxis._axinfo['tick']['outward_factor'] = 0
    ax.yaxis._axinfo['tick']['inward_factor'] = 0.25
    ax.zaxis._axinfo['tick']['outward_factor'] = 0
    ax.zaxis._axinfo['tick']['inward_factor'] = 0.25

####  fontweight={a numeric value in range 0-1000, 'ultralight', 'light', 'normal', 'regular', 'book', 'medium', 'roman', 'semibold', 'demibold', 'demi', 'bold', 'heavy', 'extra bold', 'black'}
    ax.grid(False)







def plot_pdf(param,loc1,loc2,lo3,Nsplit=50):
    bounds = [0 + 1e-1 / 2, 1 - 1e-1 / 2]
    U_grid, V_grid = np.meshgrid(
        np.linspace(bounds[0], bounds[1], Nsplit),
        np.linspace(bounds[0], bounds[1], Nsplit))
    Z = np.array([get_pdf(uu, vv, param) for uu, vv in zip(np.ravel(U_grid), np.ravel(V_grid))])
    Z = Z.reshape(U_grid.shape)
    plot_bivariate_3d(U_grid, V_grid, Z, [0, 1],loc1,loc2,lo3,par=param)





fig=plt.figure(figsize=(18,14.4))#S&P500
plot_pdf([0.61,8.10,'NESG - HE'],4,5,1)
plot_pdf([0.79,5.43,'NESG - DB'],4,5,2)
plot_pdf([0.76,5.33,'NESG - FF'],4,5,3)
plot_pdf([0.81,7.02,'NESG - II'],4,5,4)
plot_pdf([0.77,11.63,'NESG - ST'],4,5,5)
plot_pdf([0.63,7.77,'NESG - CP'],4,5,6)
plot_pdf([0.81,5.93,'NESG - FS'],4,5,7)
plot_pdf([0.74,8.51,'NESG - FC'],4,5,8)
plot_pdf([0.81,5.79,'NESG - AM'],4,5,9)
plot_pdf([0.70,5.97,'NESG - SS'],4,5,10)

plot_pdf([0.60,7.90,'ESG - HE'],4,5,11)#ESG
plot_pdf([0.78,4.92,'ESG - DB'],4,5,12)
plot_pdf([0.73,5.11,'ESG - FF'],4,5,13)
plot_pdf([0.79,6.35,'ESG - II'],4,5,14)
plot_pdf([0.76,9.62,'ESG - ST'],4,5,15)
plot_pdf([0.62,7.77,'ESG - CP'],4,5,16)
plot_pdf([0.79,5.72,'ESG - FS'],4,5,17)
plot_pdf([0.73,8.97,'ESG - FC'],4,5,18)
plot_pdf([0.80,5.42,'ESG - AM'],4,5,19)
plot_pdf([0.69,6.04,'ESG - SS'],4,5,20)



plt.tight_layout()
plt.savefig(r'C:/Users/徐浩然/Desktop/P4 Figs/3D.pdf',dpi=2000)
plt.show()