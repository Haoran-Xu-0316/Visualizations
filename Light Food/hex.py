import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap

rc = {'font.sans-serif': 'Microsoft YaHei',  'axes.unicode_minus': False,"mathtext.fontset": 'stix'}
sns.set(context='notebook', rc=rc,style='ticks')
# clist=['#EAF6DE','#B3D0AB',"#77A67E",'#527D5D','#19422A']
plt.rcParams['font.size'] = 12
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
clist=['#B3D0AB','#527D5D']
C = LinearSegmentedColormap.from_list('Blues',clist,N=256)

df = pd.read_excel(r'C:\Users\徐浩然\Desktop\Data ZD.xlsx', sheet_name='身高体重bmi')

g=sns.jointplot(x=df['体重'], y=df['身高'], kind="hex",color="#527D5D",marginal_kws=dict(kde="brivariate"))
# g.plot_marginals(sns.rugplot, color='firebrick', height=-.1, clip_on=False)
ax_marg_x = g.ax_marg_x
ax_marg_y = g.ax_marg_y

# 隐藏刻度
ax_marg_x.tick_params(axis="both", which="both", labelsize=0, length=0)
ax_marg_y.tick_params(axis="both", which="both", labelsize=0, length=0)
# plt.tight_layout()
g.fig.set_size_inches(10,7)
# g.fig.set_size_inches(13,5)

plt.subplots_adjust(left=0.09, bottom=0.074, right=0.737, top=0.97, wspace=0.2, hspace=0.2)

plt.savefig(r'C:/Users/徐浩然/Desktop/BMI.png',dpi=400)
plt.show()