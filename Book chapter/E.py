import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pylab import mpl

mpl.rcParams['font.size'] = 12

plt.rcParams['axes.unicode_minus'] = False  # 解决负号不显示的问题

pd.set_option('display.unicode.east_asian_width', True)
sns.set_theme( style='ticks', palette='deep', font='Arial', font_scale=1, color_codes=True, rc=None)

df = pd.read_excel(r'C:\Users\徐浩然\Desktop\材料\Electricity.xlsx', sheet_name='Sheet1')


fig, ax = plt.subplots(figsize=(12, 6))
plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=None)


ax.plot(df['T'],df['E'],color='black',linewidth=3)
ax.set_xlabel(None)
ax.set_ylim(0,25)
ax.fill_between(df['T'],0,df['E'], alpha=0.7,color=plt.get_cmap("Oranges")(0.4),label='Total Charging')
# ax.xaxis.set_tick_params(rotation=30)
ax.set_ylabel('Charging Electricity (billion kWh)')




plt.savefig(r'C:/Users/徐浩然/Desktop/E.png',dpi=400)
plt.show()


