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
from mpl_toolkits.mplot3d import axes3d
from pycop import student
from scipy.special import gamma
from scipy.stats import t

#全局设置-----------------------------------------------------------------------------------------------------------------
# plt.rcParams['font.sans-serif']=['Microsoft YaHei']
plt.rcParams['font.sans-serif'] = ['Palatino Linotype']
# plt.rcParams["font.weight"] = "bold"
plt.rcParams['font.size'] = 15
plt.rcParams['axes.unicode_minus'] = True
plt.rcParams['lines.linewidth'] = 1
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
plt.rcParams['axes.labelsize'] = 0

# sns.set_theme(style="white")

lll=['HE','DB','FF', 'II', 'ST', 'CP','FS','FC','AM','SS']

nes=[]
es=[]
for i in range(len(lll)):
    es.append(f"{lll[i]} - ESG")
    nes.append(f"{lll[i]} - NESG")
pr={'style':'italic','weight':'bold'}

u=pd.read_excel(r'C:\Users\徐浩然\Desktop\P4 ESG\ReadData.xlsx', sheet_name='U',index_col=0,parse_dates=[0])
rt=pd.read_excel(r'C:\Users\徐浩然\Desktop\P4 ESG\ReadData.xlsx', sheet_name='rt',index_col=0,parse_dates=[0])
f, ax = plt.subplots(5, 4, figsize=(18,22.5), sharex=False, sharey=False, subplot_kw={'aspect': 'equal'})

# cmap = sns.color_palette("viridis_r",as_cmap=True)

cmap = sns.color_palette("RdBu_r",as_cmap=True)

fill=True
clip=(-5,5)
thresh=0
levels=15
cut=20
size=0.5


sns.kdeplot(x=rt.iloc[:,0], y=rt.iloc[:,10],  cmap=cmap, fill=fill,clip=clip, cut=cut, thresh=thresh, levels=levels,ax=ax[0,0])
sns.kdeplot(x=rt.iloc[:,1], y=rt.iloc[:,10],  cmap=cmap, fill=fill,clip=clip, cut=cut, thresh=thresh, levels=levels,ax=ax[0,1])
sns.kdeplot(x=rt.iloc[:,2], y=rt.iloc[:,10],  cmap=cmap, fill=fill,clip=clip, cut=cut, thresh=thresh, levels=levels,ax=ax[1,0])
sns.kdeplot(x=rt.iloc[:,3], y=rt.iloc[:,10],  cmap=cmap, fill=fill,clip=clip, cut=cut, thresh=thresh, levels=levels,ax=ax[1,1])
sns.kdeplot(x=rt.iloc[:,4], y=rt.iloc[:,10],  cmap=cmap, fill=fill,clip=clip, cut=cut, thresh=thresh, levels=levels,ax=ax[2,0])
sns.kdeplot(x=rt.iloc[:,5], y=rt.iloc[:,10],  cmap=cmap, fill=fill,clip=clip, cut=cut, thresh=thresh, levels=levels,ax=ax[2,1])
sns.kdeplot(x=rt.iloc[:,6], y=rt.iloc[:,10],  cmap=cmap, fill=fill,clip=clip, cut=cut, thresh=thresh, levels=levels,ax=ax[3,0])
sns.kdeplot(x=rt.iloc[:,7], y=rt.iloc[:,10],  cmap=cmap, fill=fill,clip=clip, cut=cut, thresh=thresh, levels=levels,ax=ax[3,1])
sns.kdeplot(x=rt.iloc[:,8], y=rt.iloc[:,10],  cmap=cmap, fill=fill,clip=clip, cut=cut, thresh=thresh, levels=levels,ax=ax[4,0])
sns.kdeplot(x=rt.iloc[:,9], y=rt.iloc[:,10],  cmap=cmap, fill=fill,clip=clip, cut=cut, thresh=thresh, levels=levels,ax=ax[4,1])

sns.scatterplot(x=rt.iloc[:,0], y=rt.iloc[:,10], s=size, edgecolor='black',color='black',ax=ax[0,0])
sns.scatterplot(x=rt.iloc[:,1], y=rt.iloc[:,10], s=size, edgecolor='black',color='black',ax=ax[0,1])
sns.scatterplot(x=rt.iloc[:,2], y=rt.iloc[:,10], s=size, edgecolor='black',color='black',ax=ax[1,0])
sns.scatterplot(x=rt.iloc[:,3], y=rt.iloc[:,10], s=size, edgecolor='black',color='black',ax=ax[1,1])
sns.scatterplot(x=rt.iloc[:,4], y=rt.iloc[:,10], s=size, edgecolor='black',color='black',ax=ax[2,0])
sns.scatterplot(x=rt.iloc[:,5], y=rt.iloc[:,10], s=size, edgecolor='black',color='black',ax=ax[2,1])
sns.scatterplot(x=rt.iloc[:,6], y=rt.iloc[:,10], s=size, edgecolor='black',color='black',ax=ax[3,0])
sns.scatterplot(x=rt.iloc[:,7], y=rt.iloc[:,10], s=size, edgecolor='black',color='black',ax=ax[3,1])
sns.scatterplot(x=rt.iloc[:,8], y=rt.iloc[:,10], s=size, edgecolor='black',color='black',ax=ax[4,0])
sns.scatterplot(x=rt.iloc[:,9], y=rt.iloc[:,10], s=size, edgecolor='black',color='black',ax=ax[4,1])




sns.kdeplot(x=rt.iloc[:,0], y=rt.iloc[:,11],  cmap=cmap, fill=fill,clip=clip, cut=cut, thresh=thresh, levels=levels,ax=ax[0,2])
sns.kdeplot(x=rt.iloc[:,1], y=rt.iloc[:,11],  cmap=cmap, fill=fill,clip=clip, cut=cut, thresh=thresh, levels=levels,ax=ax[0,3])
sns.kdeplot(x=rt.iloc[:,2], y=rt.iloc[:,11],  cmap=cmap, fill=fill,clip=clip, cut=cut, thresh=thresh, levels=levels,ax=ax[1,2])
sns.kdeplot(x=rt.iloc[:,3], y=rt.iloc[:,11],  cmap=cmap, fill=fill,clip=clip, cut=cut, thresh=thresh, levels=levels,ax=ax[1,3])
sns.kdeplot(x=rt.iloc[:,4], y=rt.iloc[:,11],  cmap=cmap, fill=fill,clip=clip, cut=cut, thresh=thresh, levels=levels,ax=ax[2,2])
sns.kdeplot(x=rt.iloc[:,5], y=rt.iloc[:,11],  cmap=cmap, fill=fill,clip=clip, cut=cut, thresh=thresh, levels=levels,ax=ax[2,3])
sns.kdeplot(x=rt.iloc[:,6], y=rt.iloc[:,11],  cmap=cmap, fill=fill,clip=clip, cut=cut, thresh=thresh, levels=levels,ax=ax[3,2])
sns.kdeplot(x=rt.iloc[:,7], y=rt.iloc[:,11],  cmap=cmap, fill=fill,clip=clip, cut=cut, thresh=thresh, levels=levels,ax=ax[3,3])
sns.kdeplot(x=rt.iloc[:,8], y=rt.iloc[:,11],  cmap=cmap, fill=fill,clip=clip, cut=cut, thresh=thresh, levels=levels,ax=ax[4,2])
sns.kdeplot(x=rt.iloc[:,9], y=rt.iloc[:,11],  cmap=cmap, fill=fill,clip=clip, cut=cut, thresh=thresh, levels=levels,ax=ax[4,3])

sns.scatterplot(x=rt.iloc[:,0], y=rt.iloc[:,11], s=size, edgecolor='black',color='black',ax=ax[0,2])
sns.scatterplot(x=rt.iloc[:,1], y=rt.iloc[:,11], s=size, edgecolor='black',color='black',ax=ax[0,3])
sns.scatterplot(x=rt.iloc[:,2], y=rt.iloc[:,11], s=size, edgecolor='black',color='black',ax=ax[1,2])
sns.scatterplot(x=rt.iloc[:,3], y=rt.iloc[:,11], s=size, edgecolor='black',color='black',ax=ax[1,3])
sns.scatterplot(x=rt.iloc[:,4], y=rt.iloc[:,11], s=size, edgecolor='black',color='black',ax=ax[2,2])
sns.scatterplot(x=rt.iloc[:,5], y=rt.iloc[:,11], s=size, edgecolor='black',color='black',ax=ax[2,3])
sns.scatterplot(x=rt.iloc[:,6], y=rt.iloc[:,11], s=size, edgecolor='black',color='black',ax=ax[3,2])
sns.scatterplot(x=rt.iloc[:,7], y=rt.iloc[:,11], s=size, edgecolor='black',color='black',ax=ax[3,3])
sns.scatterplot(x=rt.iloc[:,8], y=rt.iloc[:,11], s=size, edgecolor='black',color='black',ax=ax[4,2])
sns.scatterplot(x=rt.iloc[:,9], y=rt.iloc[:,11], s=size, edgecolor='black',color='black',ax=ax[4,3])


for row in ax:
    for subplot in row:
        subplot.axis('off')
        subplot.set(xlim=(-5, 5), ylim=(-5, 5))

# 索引前两列，从上到下的10个子图
for i in range(5):
    for j in range(2):
        ax[i, j].text(x=0,y=4.2,s=nes[i * 2 + j], fontsize=16,  va='center', ha='center',fontstyle='italic',fontweight='bold',color='white')

for i in range(5):
    for j in range(2, 4):
        ax[i, j].text(x=0,y=4.2,s=es[i * 2 + (j - 2)], fontsize=16, va='center', ha='center',fontstyle='italic',fontweight='bold',color='white')


# plt.tight_layout()

#
plt.subplots_adjust(
top=0.99,
bottom=0.01,
left=0.012,
right=0.988,
hspace=0.053,
wspace=0.053
)




plt.savefig(r'C:/Users/徐浩然/Desktop/P4 Figs/counter.pdf',dpi=2000)
plt.show()


