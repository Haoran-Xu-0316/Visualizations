
import matplotlib.cm as mcm
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap, ListedColormap
from matplotlib.ticker import PercentFormatter
from pylab import mpl

mpl.rcParams['font.size'] = 12
from typing import List, Tuple

plt.rcParams['axes.unicode_minus'] = False  # 解决负号不显示的问题
cmap=plt.get_cmap('Oranges_r')
newcolors=cmap(np.linspace(0, 1, 500))
newcmap = ListedColormap(newcolors[280:380])
pd.set_option('display.unicode.east_asian_width', True)
sns.set_theme(context={'figure.figsize':[10, 5]}, style='ticks', palette='deep', font='Arial', font_scale=1, color_codes=True, rc=None)

pd.set_option('display.unicode.east_asian_width', True)
df = pd.read_excel(r'C:\Users\徐浩然\Desktop\材料\公共类充电桩数量直流+交流20201130-20221130.xls', sheet_name='Sheet0',index_col=0)
ldf=pd.read_excel(r'C:\Users\徐浩然\Desktop\材料\公共类充电桩数量直流+交流20201130-20221130.xls', sheet_name='Sheet1',index_col=0)
bar=df.plot.bar(stacked=True,width=0.8, linewidth=0,edgecolor="black",  clip_on=False,cmap=newcmap,label='P')
bar.xaxis.set_tick_params(rotation=30)
bar.set_ylim(0,2000000)
bar.plot(ldf,color='black',label='Total', marker='v')
plt.legend(frameon=False,loc='upper center',ncol=3)
#barh.spines['top'].set_visible(False)
#barh.spines['bottom'].set_visible(False)
plt.ticklabel_format(axis="y", style='plain')
bar.set_ylabel('Number of Public Charging Piles')

#bar.spines['bottom'].set_visible(False)
plt.tight_layout()
plt.savefig(r'C:/Users/徐浩然/Desktop/AC+DC.png',dpi=400)
plt.show()

