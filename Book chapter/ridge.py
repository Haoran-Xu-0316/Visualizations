
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

plt.rcParams['axes.unicode_minus'] = False  # 解决负号不显示的问题

pd.set_option('display.unicode.east_asian_width', True)
sns.set_theme(style='ticks', palette='deep', font='Arial', font_scale=1, color_codes=True, rc=None)



df = pd.read_excel(r'C:\Users\徐浩然\Desktop\材料\销量20个国家20131231-20211231.xls', sheet_name='Sheet0',index_col=0)
bar=df.plot.bar(stacked=True,width=0.8, linewidth=0,figsize=(10, 5),edgecolor="Black",  clip_on=False,cmap='tab20')
bar.legend_.remove()

bar.xaxis.set_tick_params(rotation=30)
plt.savefig(r'C:/Users/徐浩然/Desktop/销量.png',dpi=400)
plt.show()

