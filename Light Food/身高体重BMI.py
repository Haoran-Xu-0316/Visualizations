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
# axs=sns.relplot(data=df, x="体重", y="身高", hue="性别",size="BMI", sizes=(15, 200),palette=clist,linewidth=0.2,alpha=0.9)

g = sns.JointGrid()
ax=sns.scatterplot(data=df, x="体重", y="身高", hue="性别",size="BMI", sizes=(0, 250),palette=clist,linewidth=0.2,alpha=0.9,ax=g.ax_joint)

# sns.jointplot(data=df, x="体重", y="身高", hue="性别", kind="kde")
# sns.histplot(data=df, x="体重" ,fill=True, linewidth=1.5, ax=g.ax_marg_x,kde=True,color='#19422A')

sns.kdeplot(data=df,y="身高", linewidth=1.2,hue='性别', ax=g.ax_marg_y, fill=True, common_norm=False, alpha=.7,palette=clist,legend=False)
sns.kdeplot(data=df, x="体重" ,fill=True, hue='性别', ax=g.ax_marg_x,palette=clist,linewidth=1.2,common_norm=False,legend=False,alpha=.7)

ax_marg_x = g.ax_marg_x
ax_marg_y = g.ax_marg_y

# 隐藏刻度
ax_marg_x.tick_params(axis="both", which="both", labelsize=0, length=0)
ax_marg_y.tick_params(axis="both", which="both", labelsize=0, length=0)

# sns.move_legend(loc='lower center')
# plt.tight_layout()
g.fig.set_size_inches(10,7)

sns.move_legend(ax, 'lower right',bbox_to_anchor=(1.38,0.3), frameon=False)
plt.subplots_adjust(left=0.09, bottom=0.074, right=0.737, top=0.97, wspace=0.2, hspace=0.2)

plt.savefig(r'C:/Users/徐浩然/Desktop/身高体重BMI.png',dpi=400)
plt.show()