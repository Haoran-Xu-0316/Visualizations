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

def plot(x,y):
    plt.plot([0, x], [0, y], linestyle='--')
    # plt.text(x - 15,
    #          y + 6,
    #          (x, y),
    #          fontsize=12,
    #          # # verticalalignment="top",
    #          # # horizontalalignment="right"
    #          # color='white'
    #          )
df = pd.read_excel(r'C:\Users\徐浩然\Desktop\大量表+支付金额.xlsx', sheet_name='Sheet2')


# axs=sns.relplot(data=df, x="体重", y="身高", hue="性别",size="BMI", sizes=(15, 200),palette=clist,linewidth=0.2,alpha=0.9)
plt.figure(figsize=(10,6))
g=sns.scatterplot(data=df,x='引申重要性',y='满意度',color="#527D5D",linewidth=2,edgecolor="#527D5D")
plt.axhline(y=3.752098,c='black',ls="--",lw=1)
plt.axvline(x=0.112122 ,c='black',ls="--",lw=1)
# sns.move_legend(loc='lower center')
# plt.tight_layout()
# g.fig.set_size_inches(10,7)

# sns.move_legend(g, 'lower right',bbox_to_anchor=(1.38,0.3), frameon=False)
# plt.subplots_adjust(left=0.09, bottom=0.074, right=0.737, top=0.97, wspace=0.2, hspace=0.2)

plt.savefig(r'C:/Users/徐浩然/Desktop/轻食Figure/IPA1.png',dpi=400)
plt.show()