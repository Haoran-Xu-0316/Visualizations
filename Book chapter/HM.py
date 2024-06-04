
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pylab import mpl

mpl.rcParams['font.size'] = 12
sns.set_theme(context={'figure.figsize':[12, 6]},style='ticks', palette='deep', font='Arial', color_codes=True, rc=None)

df = pd.read_excel(r'C:\Users\徐浩然\Desktop\材料\shanfeng.xlsx', sheet_name='Sheet1',index_col='city')
df=df.T
print(df)
hm=sns.heatmap(df, annot=False,cmap='Oranges')
hm.set_xlabel(None)
#hm.xaxis.set_tick_params(rotation=75)
plt.subplots_adjust(left=0.265, bottom=0.2, right=0.959, top=0.88, wspace=None, hspace=None)

plt.savefig(r'C:/Users/徐浩然/Desktop/HMAP.png',dpi=400)
print(df)
plt.show()