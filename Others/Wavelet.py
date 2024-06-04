from __future__ import division

import matplotlib.pyplot as plt
import numpy
import numpy as np
import pandas as pd
import pycwt as wavelet
import tushare as ts
from scipy.signal import coherence

#全局设置----------------------------------------------------------------------------------------------------------------
plt.rcParams['font.sans-serif'] = ['Palatino Linotype']
plt.rcParams['font.size'] = 12
plt.rcParams['axes.unicode_minus'] = False
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
#获取数据--------------------------------------------------------------------------------------------------------------
ts.set_token('376ad9d1b8258927f4d4a8042e236755a89debdf118e62fb08edf641')
pro = ts.pro_api()

def get_close(ticker, start_date, end_date):
    df = pro.daily(ts_code=ticker,
                   start_date=start_date,
                   end_date=end_date)
    df = df.set_index('trade_date').sort_index()
    df_close = df[['close']]
    df_close=df_close.fillna(axis=0,method='ffill')
    return df_close
z1=get_close('600028.sh',20110101,20221231)
z2=get_close('600029.sh',20110101,20221231)

rets1 = np.log(z1 / z1.shift(1))
retss1 = rets1.iloc[1:]
x1=retss1['close'].values

rets2 = np.log(z2 / z2.shift(1))
retss2 = rets2.iloc[1:]
x2 = retss2['close'].values

#计算相干性---------------------------------------------------------------------------------------------------------------
f, coh = coherence(x1, x2)
#开始绘制WTC--------------------------------------------------------------------------------------------------------------
dat = coh
plt.figure()
plt.plot(dat)
N = dat.size

#控制日期-----------------------------------------------------------------------------------------------------------------
t0 = 2011
t1= 2023
dt = (t1-t0)/N
t = numpy.arange(0, N)*dt+t0
t[-1]=t1

#标准正太分布-------------------------------------------------------------------------------------------------------------
p = numpy.polyfit(t-t0, dat, 1)
dat_notrend = dat-numpy.polyval(p, t-t0)
std = dat_notrend.std()  # Standard deviation
var = std ** 2  # Variance
dat_norm = dat_notrend / std  # Normalized dataset

#母小波------------------------------------------------------------------------------------------------------------------
mother = wavelet.Morlet(6)
s0 = 1.5*dt  # Starting scale
dj = 1/12  # Twelve sub-octaves per octaves
J = 5/dj  # Seven powers of two with dj sub-octaves
alpha, _, _ = wavelet.ar1(dat)  # Lag-1 autocorrelation for red noise

wave, scales, freqs, coi, fft, fftfreqs = wavelet.cwt(dat_norm, dt, dj, s0, J, mother)
power = (numpy.abs(wave)) ** 2
period = 1/freqs

signif, fft_theor = wavelet.significance(1.0, dt, scales, 0, alpha,significance_level=0.95,wavelet=mother)
sig95 = numpy.ones([1, N]) * signif[:, None]
sig95 = power/sig95

#绘制主体-----------------------------------------------------------------------------------------------------------------
fig, bx = plt.subplots(figsize=(8,5))
bx.invert_yaxis()
levels = [0.0625, 0.125, 0.25, 0.5, 1, 2, 4, 8, 16]
f=bx.contourf(t, numpy.log2(period), numpy.log2(power), numpy.log2(levels),
              extend='both', cmap=plt.cm.Greens_r
              ,interpolation='bicubic',
              alpha=1
              )

#设置黑色圈圈--------------------------------------------------------------------------------------------------------------
extent = [t.min(), t.max(), 0, max(period)]
l=bx.contour(t, numpy.log2(period), sig95, [-99, 1], colors='k', linewidths=2,extent=extent)

# 设置COI----------------------------------------------------------------------------------------------------------------
sig=bx.fill(numpy.concatenate([t, t[-1:] + dt, t[-1:] + dt,t[:1] - dt, t[:1] - dt]),
        numpy.concatenate([numpy.log2(coi), [1e-9], numpy.log2(period[-1:]),numpy.log2(period[-1:]), [1e-9]]),
        'k', alpha=0.3,
        # hatch='x'
        )

#设置刻度-----------------------------------------------------------------------------------------------------------------
bx.set_title('Wavelet Coherence Spectrum')
bx.set_ylabel('Period (years)')

Yticks = 2 ** numpy.arange(numpy.ceil(numpy.log2(period.min())),numpy.ceil(numpy.log2(period.max())))
bx.set_yticks(numpy.log2(Yticks))
bx.set_yticklabels(Yticks)
bx.set_ylim(numpy.log2([period.max(), period.min()]))
bx.set_xlim([t.min(), t.max()])
bx.set_xticks(np.arange(t0,t1+1,1))

#设置色条-----------------------------------------------------------------------------------------------------------------
# fig.colorbar(f)
#vmin, vmax
#-----------------------------------------------------------------------------------------------------------------------
plt.tight_layout()
# plt.savefig(r'C:/Users/徐浩然/Desktop/wave.png',dpi=400)
plt.show()
