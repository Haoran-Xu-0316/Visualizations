import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pylab as pl
import seaborn as sns
from matplotlib import cm, ticker
from matplotlib.colors import LinearSegmentedColormap

# rc = {'font.sans-serif': 'Microsoft YaHei',  'axes.unicode_minus': False,"mathtext.fontset": 'stix'}
# sns.set(context='notebook', rc=rc,style='ticks')
plt.rcParams['font.size'] = 10
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']

clist=['#EAF6DE','#B3D0AB',"#77A67E",'#527D5D','#19422A']
cclist=['#19422A','#527D5D',"#77A67E",'#B3D0AB']

C = LinearSegmentedColormap.from_list('Blues',clist,N=256)
CC = LinearSegmentedColormap.from_list('Blues',cclist,N=256)
# df = pd.read_excel(r'C:\Users\徐浩然\Desktop\result.xlsx', sheet_name='result',parse_dates=[0])
# ----------------------------------------------------------------------------------------------------------------------
d1=[192,175,194	,188,164,167,172]
d2=[234,214,172,189,176,159,167]
d1s=sum(d1)
d2s=sum(d2)
print(d1s,d2s)
label=['大众点评','小红书','抖音','美团','饿了么','Bilibili','微博']

fig, ax = plt.subplots(nrows=1,ncols=2,figsize=(10,3))

y_pos = np.arange(len(label))

ax[0].barh(y_pos, d1,align='center',label='男',color='#527D5D')
ax[0].set_xticks([])
ax[0].set_yticks([])
ax[1].set_xticks([])
ax[1].set_yticks([])

ax[0].invert_xaxis()  # labels read top-to-bottom
ax[1].barh(y_pos, d2,align='center',label='女',color='#B3D0AB')
ax[1].set_yticks(y_pos, labels=label)
ax[0].set_yticks(y_pos, labels=label)
ax[0].spines["left"].set_visible(False)
ax[0].spines["top"].set_visible(False)
ax[0].spines["bottom"].set_visible(False)
ax[1].spines["top"].set_visible(False)
ax[1].spines["bottom"].set_visible(False)
ax[1].spines["right"].set_visible(False)
ax[1].tick_params(bottom=False, top=False, left=True, right=False,pad=25)
ax[0].tick_params(bottom=False, top=False, left=False, right=True)
ax[0].yaxis.set_major_formatter(plt.NullFormatter())
ax[1].set_yticklabels(labels=label, ha="center")
fig.legend(frameon=False, ncols=2,bbox_to_anchor=(0.575,0.15))
fig.subplots_adjust(left=0.008, bottom=0.146, right=.986, top=0.88, wspace=0.18, hspace =0.2)

# plt.tight_layout()
plt.savefig(r'C:/Users/徐浩然/Desktop/1.png',dpi=400)

plt.show()

