from typing import List, Tuple

import matplotlib.cm as mcm
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap, ListedColormap
from matplotlib.ticker import PercentFormatter
from pylab import mpl

mpl.rcParams['font.size'] = 12
plt.rcParams['axes.unicode_minus'] = False  # 解决负号不显示的问题
plt.rcParams['font.sans-serif'] = ['Arial']

pd.set_option('display.unicode.east_asian_width', True)
sns.set_theme(style='ticks', palette='deep', font='Arial', color_codes=True, rc=None)
cmap=plt.get_cmap('Oranges_r')
newcolors=cmap(np.linspace(0, 1, 500))
newcmap = ListedColormap(newcolors[200:450])
pd.set_option('display.unicode.east_asian_width', True)
df = pd.read_excel(r'C:\Users\徐浩然\Desktop\材料\IoT 2030.xlsx', sheet_name='Sheet1',index_col=0)
df=df.T
bar=df.plot.bar(stacked=True,width=0.8, linewidth=0, figsize=(12, 6),edgecolor="Black",  clip_on=False,cmap=newcmap)
bar.legend(frameon=False,bbox_to_anchor=(1,0.99))
#bar.margins(x=0,y=0)
bar.xaxis.set_tick_params(rotation=30)
bar.set_ylim(0,10)
bar.set_ylabel('IoT Connections (billion)')
#bar.spines['top'].set_visible(False)
#bar.spines['bottom'].set_visible(False)

plt.tight_layout()

# plt.savefig(r'C:/Users/徐浩然/Desktop/IoT2023.png',dpi=400)
plt.show()


