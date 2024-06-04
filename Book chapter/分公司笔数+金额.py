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
df1 = pd.read_excel(r'C:\Users\徐浩然\Desktop\材料\笔数20210103-20230101.xls', sheet_name='Sheet0',index_col=0)
df2 = pd.read_excel(r'C:\Users\徐浩然\Desktop\材料\金额20210103-20230101.xls', sheet_name='Sheet0',index_col=0)

fig, axs = plt.subplots(figsize = (20, 5),ncols=2)
plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=None)
plt.ticklabel_format(axis="y", style='plain')

#ax1
ax1=sns.lineplot(data=df1,dashes=False,ax=axs[0])
ax1.set_ylabel('Number of Payment Transactions (RMB\'000)')
sns.move_legend(ax1, "lower center", bbox_to_anchor=(.5, 1), ncol=5, title=None, frameon=False)
ax1.xaxis.set_tick_params(rotation=30)
ax1.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(changey))

#ax2
ax2=sns.lineplot(data=df2,dashes=False,ax=axs[1])
ax2.set_ylabel('Payment Transaction Amount (RMB\'000)')
sns.move_legend(ax2, "lower center",bbox_to_anchor=(.5, 1), ncol=5, title=None, frameon=False)
ax2.xaxis.set_tick_params(rotation=30)
ax2.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(changey))


plt.savefig(r'C:/Users/徐浩然/Desktop/笔数+金额.png',dpi=400)
plt.show()

