from __future__ import division

import matplotlib.pyplot as plt
import numpy
import numpy as np
import pandas as pd
import pycwt as wavelet
import pywt
import tushare as ts
from pycwt.helpers import find
from scipy.signal import coherence

#全局设置----------------------------------------------------------------------------------------------------------------
plt.rcParams['font.sans-serif'] = ['Palatino Linotype']
plt.rcParams['font.size'] = 12
plt.rcParams['axes.unicode_minus'] = False
# plt.style.use('seaborn-ticks')

pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
#API获取数据--------------------------------------------------------------------------------------------------------------
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
df1 = pd.read_excel(r'C:\Users\徐浩然\Desktop\930951perf.xlsx', sheet_name='930951perf',index_col=0,parse_dates=[0])
ret1 = np.log(df1['收盘Close'] / df1['收盘Close'].shift(1))
ret1 = ret1.to_frame()
ret1 = ret1.iloc[1:]
ret1.columns.values[0] = '收盘Close'
x1=ret1['收盘Close'].values

df2 = pd.read_excel(r'C:\Users\徐浩然\Desktop\000300perf.xlsx', sheet_name='000300perf',index_col=0,parse_dates=[0])
ret2 = np.log(df2['收盘Close'] / df2['收盘Close'].shift(1))
ret2 = ret2.to_frame()
ret2 = ret2.iloc[1:]
ret2.columns.values[0] = '收盘Close'
x2=ret2['收盘Close'].values

#计算相干性-----------------------------------------------------------------------------------------------------------------
f, coh = coherence(x1, x2)
#开始绘制WTC------------------------------------------------------------------------------------------------------------------
dat = coh
N = dat.size

t0 = 2011
t1= 2023
dt = (t1-t0)/N
t = numpy.arange(0, N) * dt + t0
t[-1]=t1
print(t)

p = numpy.polyfit(t - t0, dat, 1)
dat_notrend = dat - numpy.polyval(p, t - t0)
std = dat_notrend.std()  # Standard deviation 标准差
var = std ** 2  # Variance 方差

dat_norm = dat_notrend / std  # Normalized dataset 正态标准化之后的数据


mother = wavelet.Morlet(6)
s0 = 1.5 * dt  # Starting scale, in this case 2 * 0.25 years = 6 months
dj = 1 / 12  # Twelve sub-octaves per octaves
J = 5 / dj  # Seven powers of two with dj sub-octaves
alpha, _, _ = wavelet.ar1(dat)  # Lag-1 autocorrelation for red noise

wave, scales, freqs, coi, fft, fftfreqs = wavelet.cwt(dat_norm, dt, dj, s0, J, mother)
power = (numpy.abs(wave)) ** 2
period = 1 / freqs

signif, fft_theor = wavelet.significance(1.0, dt, scales, 0, alpha,significance_level=0.95,wavelet=mother)
sig95 = numpy.ones([1, N]) * signif[:, None]
sig95 = power / sig95

#-----------------------------------------------------------------------------------------------------------------------
fig, bx = plt.subplots(figsize=(16,4))
bx.invert_yaxis()
levels = [0.0625, 0.125, 0.25, 0.5, 1, 2, 4, 8, 16]
f=bx.contourf(t, numpy.log2(period), numpy.log2(power), numpy.log2(levels),extend='both', cmap=plt.cm.viridis,interpolation='bicubic')
#-----------------------------------------------------------------------------------------------------------------------
extent = [t.min(), t.max(), 0, max(period)]
l=bx.contour(t, numpy.log2(period), sig95, [-99, 1], colors='k', linewidths=2,extent=extent)

sig=bx.fill(numpy.concatenate([t, t[-1:] + dt, t[-1:] + dt,t[:1] - dt, t[:1] - dt]),
        numpy.concatenate([numpy.log2(coi), [1e-9], numpy.log2(period[-1:]),numpy.log2(period[-1:]), [1e-9]]),
        'k', alpha=0.3,
        # hatch='x'
        )
# bx.set_title('Wavelet Coherence Spectrum')
bx.set_ylabel('Period (years)')
bx.set_ylabel('Period (years)')


Yticks = 2 ** numpy.arange(numpy.ceil(numpy.log2(period.min())),numpy.ceil(numpy.log2(period.max())))

bx.set_yticks(numpy.log2(Yticks))
bx.set_yticklabels(Yticks)
bx.set_ylim(numpy.log2([period.max(), period.min()]))
bx.set_xlim([t.min(), t.max()])
bx.set_xticks(np.arange(t0,t1+1,1))
# fig.colorbar
#vmin, vmax
plt.tight_layout()

#-----------------------------------------------------------------------------------------------------------------------
plt.savefig(r'C:/Users/徐浩然/Desktop/小波.png',dpi=400)

plt.show()
