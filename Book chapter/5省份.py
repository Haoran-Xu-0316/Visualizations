import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pylab import mpl

mpl.rcParams['font.size'] = 12
def changey(x, y):
    return int(x/1000)


plt.rcParams['axes.unicode_minus'] = False  # 解决负号不显示的问题

pd.set_option('display.unicode.east_asian_width', True)
sns.set_theme(style='ticks', palette='deep', font='Arial', font_scale=1, color_codes=True, rc=None)

pd.set_option('display.unicode.east_asian_width', True)
df1 = pd.read_excel(r'C:\Users\徐浩然\Desktop\材料\公共类充电桩5省份20171130-20221130.xls', sheet_name='Sheet0',index_col=0)
df2 = pd.read_excel(r'C:\Users\徐浩然\Desktop\材料\公共充电站5省份20200530-20221130.xls', sheet_name='Sheet0',index_col=0)
df3 = pd.read_excel(r'C:\Users\徐浩然\Desktop\材料\共享私桩数量5省份20210131-1130.xls', sheet_name='Sheet0',index_col=0)
df4 = pd.read_excel(r'C:\Users\徐浩然\Desktop\材料\换电站保有数量5省份20200531-20221130.xls', sheet_name='Sheet0',index_col=0)

fig, axs = plt.subplots(2,2,figsize=(15,8))
plt.ticklabel_format(axis="y", style='plain')

#ax1
plt.subplot(221)
ax1=sns.lineplot(data=df1,dashes=False)
ax1.set_ylabel('Number of Public Charging Piles')
sns.move_legend(ax1, "lower center", bbox_to_anchor=(.5, 1), ncol=5, title=None, frameon=False,columnspacing=0.4)
ax1.xaxis.set_tick_params(rotation=30)

#ax2
plt.subplot(222)
ax2=sns.lineplot(data=df2,dashes=False)
ax2.set_ylabel('Number of Public Charging Stations')
sns.move_legend(ax2, "lower center",bbox_to_anchor=(.5, 1), ncol=5, title=None, frameon=False,columnspacing=0.4)
ax2.xaxis.set_tick_params(rotation=30)

#ax3
plt.subplot(223)
ax3=sns.lineplot(data=df3,dashes=False)
ax3.set_ylabel('Number of Shared Private Piles')
sns.move_legend(ax3, "lower center", bbox_to_anchor=(.5, 1), ncol=5, title=None, frameon=False,columnspacing=0.4)
ax3.xaxis.set_tick_params(rotation=30)

#ax4
plt.subplot(224)
ax4=sns.lineplot(data=df4,dashes=False)
ax4.set_ylabel('Number of Battery-swap Stations')
sns.move_legend(ax4, "lower center",bbox_to_anchor=(.5, 1), ncol=5, title=None, frameon=False,columnspacing=0.4)
ax4.xaxis.set_tick_params(rotation=30)
plt.subplots_adjust(left=None, bottom=None, right=None, top=0.95, wspace=0.18, hspace=0.3)
plt.savefig(r'C:/Users/徐浩然/Desktop/5省份.png',dpi=400)
# plt.tight_layout()
plt.show()

