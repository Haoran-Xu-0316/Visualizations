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
clist=['#EAF6DE','#B3D0AB',"#77A67E",'#527D5D','#19422A']

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
df = pd.read_excel(r'C:\Users\徐浩然\Desktop\气泡.xlsx', sheet_name='Sheet1')


# axs=sns.relplot(data=df, x="体重", y="身高", hue="性别",size="BMI", sizes=(15, 200),palette=clist,linewidth=0.2,alpha=0.9)
plt.figure(figsize=(12,10))
g=sns.scatterplot(data=df,x='横坐标',y='纵坐标',size='主题的频率',sizes=(100,7000),alpha=0.5,color='#77A67E',linewidth=2,edgecolor='#19422A',legend=False)
# plt.axhline(y=3.752098,c='black',ls="--",lw=1)
g=sns.scatterplot(data=df,x='X',y='Y',size='S',sizes=(7000,7000),alpha=0.7,color='#F8CECC',linewidth=2,edgecolor='#B85450',legend=False)
for i,j,k in zip(df['横坐标'],df['纵坐标'],df['图中主题的序号']):
    plt.text(i-0.006,j-0.007,df['图中主题的序号'][k-1])
    print(k)
# plt.axvline(x=0.112122 ,c='black',ls="--",lw=1)
# sns.move_legend(loc='lower center')
# plt.tight_layout()
# g.fig.set_size_inches(10,7)
ax = plt.gca()    # 得到图像的Axes对象
ax.spines['right'].set_color('none')   # 将图像右边的轴设为透明
ax.spines['top'].set_color('none')     # 将图像上面的轴设为透明
ax.xaxis.set_ticks_position('bottom')    # 将x轴刻度设在下面的坐标轴上
ax.yaxis.set_ticks_position('left')         # 将y轴刻度设在左边的坐标轴上
ax.spines['bottom'].set_position(('data', 0))   # 将两个坐标轴的位置设在数据点原点
ax.spines['left'].set_position(('data', 0))
ax.set_xlabel('')
ax.set_ylabel('')
ax.set_xlim(-0.4,0.4)
ax.set_ylim(-0.4,0.4)
# sns.move_legend(g, 'lower left',frameon=False,labelspacing=5)
# plt.subplots_adjust(left=0.09, bottom=0.074, right=0.737, top=0.97, wspace=0.2, hspace=0.2)

plt.savefig(r'C:/Users/徐浩然/Desktop/轻食Figure/qt.png',dpi=400)
plt.show()