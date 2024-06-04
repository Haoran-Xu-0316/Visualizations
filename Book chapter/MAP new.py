
import geopandas as gpd
import mapclassify
import matplotlib.patches as mpatches
import matplotlib.patheffects as pe
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.colors import LinearSegmentedColormap, ListedColormap
from pylab import mpl

mpl.rcParams['font.size'] = 12
plt.rcParams['font.sans-serif'] = ['Arial']
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)


bj=gpd.read_file(r'C:\Users\徐浩然\Desktop\map.json')

df = pd.read_excel(r'C:\Users\徐浩然\Desktop\材料\地图+饼图.xlsx', sheet_name='Sheet1')



cmap=plt.get_cmap('Oranges')
newcolors=cmap(np.linspace(0, 1, 500))
newcmap = ListedColormap(newcolors[50:400])
bj['Charging & Switching Facilities']=df['Charging & Switching Facilities']
bj['Public Charging Stations']=df['Public Charging Stations']
bj['Public Charging Piles']=df['Public Charging Piles']
bj['Shared Private Piles']=df['Shared Private Piles']
bj['Total']=df['Total']
fig, ax = plt.subplots(figsize=(10, 10))
#['boxplot', 'equalinterval', 'fisherjenks', 'fisherjenkssampled', 'headtailbreaks', 'jenkscaspall', 'jenkscaspallforced',
# 'jenkscaspallsampled', 'maxp', 'maximumbreaks', 'naturalbreaks', 'quantiles', 'percentiles', 'stdmean', 'userdefined']
ax=bj.plot(ax=ax,column='Total',legend=False,cmap="Oranges",edgecolor='black',linewidth=0.5,legend_kwds={'shrink': 0.3})

ax.annotate('Beijing', xy=(116.7, 40.2), xytext=(105, 48),
            fontsize=12, color='black', fontweight='bold',
            arrowprops=dict(arrowstyle='-|>', lw=1, color='black', relpos=(0.5, 0)))
ax.annotate('Shanghai', xy=(121, 31), xytext=(125, 31),
            fontsize=12, color='black', fontweight='bold',
            arrowprops=dict(arrowstyle='-|>', lw=1, color='black', relpos=(0.5, 0)))
ax.annotate('Jiangsu', xy=(119.2, 33), xytext=(125, 34),
            fontsize=12, color='black', fontweight='bold',
            arrowprops=dict(arrowstyle='-|>', lw=1, color='black', relpos=(0.5, 0)))
ax.annotate('Zhejiang', xy=(119.3, 29), xytext=(125, 28),
            fontsize=12, color='black', fontweight='bold',
            arrowprops=dict(arrowstyle='-|>', lw=1, color='black', relpos=(0.5, 0)))
ax.annotate('Guangdong', xy=(113, 23), xytext=(100, 17),
            fontsize=12, color='black', fontweight='bold',
            arrowprops=dict(arrowstyle='-|>', lw=1, color='black', relpos=(0.5, 0)))

plt.tight_layout()
#caption=,colorbar=True,  legend_kwds={'loc': 'lower left',  'title': 'infection number','title_fontsize': 6, 'fontsize': 6,   'shadow': True}
plt.axis('off')


plt.savefig(r'C:/Users/徐浩然/Desktop/MAP.png',dpi=800)
print(bj)


plt.show()

