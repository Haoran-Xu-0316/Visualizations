
from typing import List, Tuple

import matplotlib.cm as mcm
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.ticker import PercentFormatter

plt.rcParams['font.size'] = 12
plt.rcParams['axes.unicode_minus'] = False
# plt.rcParams['sans.serif'] = ['SimSun']

rc = {'font.sans-serif': 'Microsoft YaHei',
      'axes.unicode_minus': False,"mathtext.fontset": 'stix'}
sns.set(style='ticks' ,rc=rc)
ticklabels_style = {
    "fontname": "Times New Roman",
}
# clist=['#F1F5C9','#CEDEA2','#98B574','#678B4A','#435C28']
# clist=['#EAF6DE','#B3D0AB',"#77A67E",'#527D5D','#19422A']

# plt.style.use('seaborn-ticks')
# dataframe全显示
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)

df = pd.read_excel(r'C:\Users\徐浩然\Desktop\轻食灰色关联.xlsx', sheet_name='总权重',index_col=0)
barh=df.plot.barh(width=0.8, legend=False,linewidth=0, xticks=range(0,1,10),figsize=(10, 3),edgecolor="Black" , color='#B3D0AB')
# barh=df.plot.barh(stacked=True,width=1, linewidth=0,edgecolor="Black",  clip_on=False,cmap='coolwarm')
barh.xaxis.set_major_formatter(PercentFormatter(100))
barh.margins(y=0)
barh.spines['top'].set_visible(False)
barh.spines['bottom'].set_visible(False)
barh.spines['right'].set_visible(False)
barh.set_xlabel('')
plt.xticks([])
plt.ylabel('')
plt.bar_label(barh.containers[0],fontsize=10,padding=2,label_type='edge')

plt.tight_layout()
plt.savefig(r'C:/Users/徐浩然/Desktop/轻食Figure/总权重.png',dpi=400)
plt.show()

