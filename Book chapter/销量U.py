
from typing import List, Tuple

import matplotlib.cm as mcm
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib.ticker import PercentFormatter

plt.rcParams['axes.unicode_minus'] = False  # 解决负号不显示的问题

pd.set_option('display.unicode.east_asian_width', True)
sns.set_theme(style='ticks', palette='deep', font='Arial', font_scale=1, color_codes=True, rc=None)
df1 = pd.read_excel(r'C:\Users\徐浩然\Desktop\材料\销量20个国家20131231-20211231.xls', sheet_name='Sheet0',index_col=0)
df2= pd.read_excel(r'C:\Users\徐浩然\Desktop\材料\20国家销量百分比.xlsx', sheet_name='Sheet1',index_col=0)

fig,axes=plt.subplots(1,2,figsize=(20,5))
bar=df1.plot.bar(stacked=True,width=0.8, linewidth=0,figsize=(17, 5),edgecolor="Black",  clip_on=False,cmap='tab20',ax=axes[0])
bar.legend_.remove()
bar.xaxis.set_tick_params(rotation=30)

barh=df2.plot.barh(stacked=True,width=0.8, linewidth=0, xticks=range(0,101,10),figsize=(17, 5),edgecolor="Black",  clip_on=False,cmap='tab20',ax=axes[1])
barh.xaxis.set_major_formatter(PercentFormatter(100))
barh.legend(frameon=False,bbox_to_anchor=(1,0.99),labelspacing=0.41)
barh.margins(x=0,y=0)
barh.spines['top'].set_visible(False)
barh.spines['bottom'].set_visible(False)

plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=None)
plt.tight_layout()
# plt.savefig(r'C:/Users/徐浩然/Desktop/销量U.png',dpi=400)
plt.show()

