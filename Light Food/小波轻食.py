from __future__ import division

import matplotlib.pyplot as plt
import numpy
import numpy as np
import pandas as pd
import pycwt as wavelet
import tushare as ts
from matplotlib.colors import LinearSegmentedColormap
from scipy import stats
from scipy.signal import coherence

#全局设置----------------------------------------------------------------------------------------------------------------
plt.rcParams['font.sans-serif']=['Microsoft YaHei']
plt.rcParams['font.size'] = 12
plt.rcParams['axes.unicode_minus'] = False
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)


dat = pd.read_excel(r'C:\Users\徐浩然\Desktop\result.xlsx', sheet_name='result',parse_dates=[0])
dat = dat.set_index('date').sort_index()
datt= dat['v'].values
dat = np.log(dat / dat.shift(1))
dat = dat.dropna()
dtt=dat
dat = dat['v'].values
x = np.arange(1 ,1827)

daat = pd.read_excel(r'C:\Users\徐浩然\Desktop\result.xlsx', sheet_name='Sheet1',parse_dates=[0])
print(len(daat['v'].values))
daat = daat.set_index('date').sort_index()

daat=daat.T
df = pd.read_excel(r'C:\Users\徐浩然\Desktop\Global GDP.xls', sheet_name='U',index_col=0)
y=np.array(daat)
cmap=plt.get_cmap('Greens_r')
C=cmap(np.arange(0,1,3))
print(C)
def gaussian_smooth(x, y, grid, sd):
    """平滑曲线"""
    weights = np.transpose([stats.norm.pdf(grid, m, sd) for m in x])
    weights = weights / weights.sum(0)
    return (weights * y).sum(1)
grid = np.linspace(0 ,1826, num=1000)
y_smoothed = [gaussian_smooth(x, y_, grid, 1) for y_ in y]
y=np.array(daat)
c=plt.get_cmap('Greens_r')


C=[c(0.1),c(0.3),c(0.8)]
# print()
#开始绘制WTC--------------------------------------------------------------------------------------------------------------


N = dat.size

#控制日期-----------------------------------------------------------------------------------------------------------------
t0 = 2018.05
t1= 2023.05
dt = (t1-t0)/N
t = numpy.arange(0, N)*dt+t0
t[-1]=t1
XXX=['2018-05','2019-05','2020-05','2021-05','2022-05','2023-05']
#标准正太分布-------------------------------------------------------------------------------------------------------------
p = numpy.polyfit(t-t0, dat, 1)
dat_notrend = dat-numpy.polyval(p, t-t0)
std = dat_notrend.std()  # Standard deviation
var = std ** 2  # Variance
dat_norm = dat_notrend / std  # Normalized dataset

#母小波------------------------------------------------------------------------------------------------------------------
mother = wavelet.Morlet(6)
s0 = 1*dt  # Starting scale
dj = 1/14 # Twelve sub-octaves per octaves
J = 5/dj  # Seven powers of two with dj sub-octaves
alpha, _, _ = wavelet.ar1(dat)  # Lag-1 autocorrelation for red noise

wave, scales, freqs, coi, fft, fftfreqs = wavelet.cwt(dat_norm, dt, dj, s0, J, mother)
power = (numpy.abs(wave)) ** 2
period = 1/freqs

signif, fft_theor = wavelet.significance(1.0, dt, scales, 0, alpha,significance_level=0.95,wavelet=mother)
sig95 = numpy.ones([1, N]) * signif[:, None]
sig95 = power/sig95

#绘制主体-----------------------------------------------------------------------------------------------------------------
fig, bx = plt.subplots(figsize=(10,8),ncols=1,nrows=4)
#数据--------------------------------------------------------------------------------------------------------------------
l=bx[0].plot(datt,color='#527D5D',linewidth=1)
ll=bx[2].plot(dat,color='#527D5D',linewidth=1)
bx[1].stackplot(grid, y_smoothed, colors=C, baseline="weighted_wiggle")
bx[1].set_xlim(0,len(dat))
bx[1].set_xticks([])
#小波--------------------------------------------------------------------------------------------------------------------
bx[3].invert_yaxis()
levels = [0.0625, 0.125, 0.25, 0.5, 1, 2, 4, 8, 16]
f=bx[3].contourf(t, numpy.log2(period), numpy.log2(power), numpy.log2(levels),
              extend='both', cmap=plt.cm.Greens_r
              ,interpolation='bicubic',
              alpha=1
              )

#设置黑色圈圈--------------------------------------------------------------------------------------------------------------
extent = [t.min(), t.max(), 0, max(period)]
l=bx[3].contour(t, numpy.log2(period), sig95, [-99, 1], colors='k', linewidths=1,extent=extent,)

# 设置COI----------------------------------------------------------------------------------------------------------------
sig=bx[3].fill(numpy.concatenate([t, t[-1:] + dt, t[-1:] + dt,t[:1] - dt, t[:1] - dt]),
        numpy.concatenate([numpy.log2(coi), [1e-9], numpy.log2(period[-1:]),numpy.log2(period[-1:]), [1e-9]]),
        'k', alpha=0.3,
        # hatch='x'
        )

#设置刻度-----------------------------------------------------------------------------------------------------------------
# bx.set_title('Wavelet Coherence Spectrum')
# bx.set_ylabel('Period (years)')

ss=['22.81','11.41','5.70','2.85','1.43']
Yticks = 2 ** numpy.arange(numpy.ceil(numpy.log2(period.min())),numpy.ceil(numpy.log2(period.max())))
bx[3].set_yticks(numpy.log2(Yticks))
bx[3].set_yticklabels(ss)
bx[3].set_ylim(numpy.log2([period.max(), period.min()]))
bx[3].set_xlim([t.min(), t.max()])
bx[3].set_xticks(np.arange(t0,t1+1,1),XXX)




bx[0].set_xlim(0,len(datt))
bx[1].set_xlim(0,len(datt))

bx[2].set_xticks([])
bx[0].set_xticks([])
bx[2].set_xlim(0,len(dat))


fig.subplots_adjust(left=0.109, bottom=0.065, right=0.954, top=0.974, wspace=0.2, hspace =0.115)
# plt.margins(0,0)
#设置色条-----------------------------------------------------------------------------------------------------------------
# fig.colorbar(f)
#vmin, vmax

#-----------------------------------------------------------------------------------------------------------------------
# plt.tight_layout()
# plt.savefig(r'C:/Users/徐浩然/Desktop/轻食小波.png',dpi=400)

plt.show()
print(np.arange(0,len(dat),len(dat)/6),np.arange(t0,t1+1,1))