
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pylab import mpl

mpl.rcParams['font.size'] = 12
plt.rcParams['axes.unicode_minus'] = False  # 解决负号不显示的问题

plt.rcParams['font.sans-serif'] = ['Arial']
pd.set_option('display.unicode.east_asian_width', True)
fig, ax= plt.subplots(figsize=(12,6))
df1 = pd.read_excel(r'C:\Users\徐浩然\Desktop\材料\2001-2022NEVSale.xlsx', sheet_name='Sheet1')
df2 = pd.read_excel(r'C:\Users\徐浩然\Desktop\材料\2001-2022NEVSale.xlsx', sheet_name='Sheet2')
plt.rcParams['hatch.color'] = plt.get_cmap('Oranges')(0.2)
plt.rcParams['hatch.linewidth'] = 2
df1['Time'] = [str(i) for i in df1['Time']]
ax.bar(df1['Time'],df1['Sale'],color=plt.get_cmap('Oranges')(0.4),label='Sales')

# ax.xaxis.set_tick_params(rotation=30)
#plt.bar_label(bar.containers[0])

line=ax.twinx()
plt.plot(df1['Time'],df2['yoy'],color='black',linewidth=2,label='Growth Rate',marker='X')
line.set_ylim(-50,400)
# line.xaxis.set_tick_params(rotation=30)
fig.legend(bbox_to_anchor=(0.37,0.88),ncol=2,frameon=False)
ax.set_ylabel('Sales of NEVs (thousand)')
line.set_ylabel('(%)',rotation=180,labelpad=10)
#plt.tight_layout()

plt.savefig(r'C:/Users/徐浩然/Desktop/Sales & GR.png',dpi=400)
plt.show()

