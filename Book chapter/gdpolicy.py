
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from pylab import mpl

mpl.rcParams['font.size'] = 12
plt.rcParams['axes.unicode_minus'] = False  # 解决负号不显示的问题

plt.rcParams['font.sans-serif'] = ['Arial']

pd.set_option('display.unicode.east_asian_width', True)
fig, bar= plt.subplots(figsize=(12,6))
df = pd.read_excel(r'C:\Users\徐浩然\Desktop\材料\gdpolicy.xlsx', sheet_name='Sheet1')
cmap = plt.get_cmap('Oranges')
plt.rcParams['hatch.color'] = cmap(0.2)
plt.rcParams['hatch.linewidth'] = 2
bar.bar(df['t'],df['no'],color=cmap(0.4),hatch='*',width=.6)
bar.set_xlabel(None)
bar.set_xticks(np.arange(2013,2023,1))
# bar.xaxis.set_tick_params(rotation=30)
bar.set_ylim(0,35)
#plt.bar_label(bar.containers[0])
bar.set_ylabel('Number of Polices')



fig.legend(bbox_to_anchor=(0.28,0.87),ncol=3,frameon=False)
plt.savefig(r'C:/Users/徐浩然/Desktop/gdpolicy.png',dpi=400)
plt.show()

print(df)