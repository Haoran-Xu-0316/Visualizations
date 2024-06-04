
from typing import List, Tuple

import matplotlib.cm as mcm
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib.ticker import PercentFormatter

plt.rcParams['axes.unicode_minus'] = False  # 解决负号不显示的问题

pd.set_option('display.unicode.east_asian_width', True)
sns.set_theme(context={'figure.figsize':[10, 5]}, style='ticks', palette='deep', font='Arial', font_scale=1, color_codes=True, rc=None)

df = pd.read_excel(r'C:\Users\徐浩然\Desktop\材料\20国家销量百分比.xlsx', sheet_name='Sheet1',index_col=0)
barh=df.plot.barh(stacked=True,width=0.8, linewidth=0, xticks=range(0,101,10),figsize=(10, 5),edgecolor="Black",  clip_on=False,cmap='tab20')
barh.xaxis.set_major_formatter(PercentFormatter(100))
barh.legend(frameon=False,bbox_to_anchor=(1,0.99))
barh.margins(x=0,y=0)
barh.spines['top'].set_visible(False)
barh.spines['bottom'].set_visible(False)

plt.tight_layout()
plt.savefig(r'C:/Users/徐浩然/Desktop/销量百分比.png',dpi=400)
plt.show()

