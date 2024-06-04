import geopandas
import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import statsmodels
from matplotlib import font_manager
from matplotlib.colors import LinearSegmentedColormap

plt.rcParams['axes.unicode_minus'] = False  # 解决负号不显示的问题
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']

pd.set_option('display.unicode.east_asian_width', True)
# sns.set_theme(style='ticks', palette='deep', font='Arial', font_scale=1, color_codes=True, rc=None)

clist=['#527D5D','#B3D0AB']
C = LinearSegmentedColormap.from_list('Blues',clist,N=256)
df = pd.read_excel(r'C:\Users\徐浩然\Desktop\qt造图.xlsx', sheet_name='Sheet1',index_col=0)
bar=df.plot.barh(stacked=True,width=0.8, linewidth=0,figsize=(10, 5),edgecolor="Black",  clip_on=False,cmap=C)
bar.legend_.remove()
# ax.spines['top'].set_color('none')
# ax.spines['right'].set_color('none')
# ax.spines[''].set_color('none')

# bar.xaxis.set_tick_params(rotation=30)
plt.savefig(r'C:/Users/徐浩然/Desktop/轻食Figure/qt图.png',dpi=400)
plt.show()

