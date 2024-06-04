
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pylab import mpl

mpl.rcParams['font.size'] = 12
plt.rcParams['axes.unicode_minus'] = False  # 解决负号不显示的问题


pd.set_option('display.unicode.east_asian_width', True)
sns.set_theme(style='ticks', palette='deep', font='Arial', font_scale=1, color_codes=True, rc=None)

df = pd.read_excel(r'C:\Users\徐浩然\Desktop\材料\20 Pile.xls', sheet_name='Sheet0',index_col=0)
bar=df.plot.bar(stacked=True,width=0.6, linewidth=0,figsize=(12, 6),edgecolor="Black",  clip_on=False,cmap='coolwarm')
bar.legend_.remove()
bar.set_ylim(0,1800000)
bar.xaxis.set_tick_params(rotation=0)
plt.ticklabel_format(axis="y", style='plain')
bar.set_ylabel('Number of Public Charging Piles')
bar.legend(frameon=False,bbox_to_anchor=(1,0.92),labelspacing=0.3)
plt.subplots_adjust(left=None, bottom=None, right=0.8, top=None, wspace=None, hspace=None)
# plt.savefig(r'C:/Users/徐浩然/Desktop/Pile.png',dpi=400)
plt.show()

