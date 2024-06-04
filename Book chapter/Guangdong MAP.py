import geopandas as gpd
import mapclassify
import matplotlib.patches as mpatches
import matplotlib.patheffects as pe
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.patches import PathPatch
from shapely.geometry import Polygon

plt.rcParams['font.sans-serif'] = ['Arial']
#显示所有列
pd.set_option('display.max_columns', None)
#显示所有行
pd.set_option('display.max_rows', None)
bj=gpd.read_file(r'C:\Users\徐浩然\Desktop\广东map.json')
df = pd.read_excel(r'C:\Users\徐浩然\Desktop\材料\地图+饼图.xlsx', sheet_name='Sheet3')
bj['score']=df['score']
fig, ax = plt.subplots(figsize=(10, 10))
#['boxplot', 'equalinterval', 'fisherjenks', 'fisherjenkssampled', 'headtailbreaks', 'jenkscaspall', 'jenkscaspallforced',
# 'jenkscaspallsampled', 'maxp', 'maximumbreaks', 'naturalbreaks', 'quantiles', 'percentiles', 'stdmean', 'userdefined']
ax=bj.plot(ax=ax,column='score',legend=False,cmap='Oranges',edgecolor='black',linewidth=0.5,legend_kwds={'shrink': 0.3})

# ax.annotate('Zhaoqing', xy=(113.2710, 23.1350), xytext=(-20, -10),
#             textcoords='offset points', ha='center', va='center',
#             fontsize=12, color='black')

ax.annotate('Zhaoqing', xy=(112.2710, 23.5), xytext=(110.5, 23.8),
            fontsize=12, color='black', fontweight='bold',
            arrowprops=dict(arrowstyle='-|>', lw=1, color='black', relpos=(0.5, 0)))
ax.annotate('Guangzhou', xy=(113.5, 23.4), xytext=(113., 21.2),
            fontsize=12, color='black', fontweight='bold',
            arrowprops=dict(arrowstyle='-|>', lw=1, color='black', relpos=(0.5, 0)))
ax.annotate('Shenzhen', xy=(114., 22.7), xytext=(114.8, 22),
            fontsize=12, color='black', fontweight='bold',
            arrowprops=dict(arrowstyle='-|>', lw=1, color='black', relpos=(0.5, 0)))
# xmin, ymin, xmax, ymax = 114, 22, 115, 23
# # poly = Polygon([(xmin, ymin), (xmin, ymax), (xmax, ymax), (xmax, ymin)])
# poly = bj.iloc[9]['geometry']
# print(poly)
#
# # 创建一个路径补丁对象
# patch = PathPatch(poly, facecolor='none', edgecolor='black', hatch='/', lw=2)
# #
# #
# ax.add_patch(patch)



plt.axis('off')
plt.tight_layout()
plt.savefig(r'C:/Users/徐浩然/Desktop/广东MAP.png',dpi=600)
# print(bj)
plt.show()

