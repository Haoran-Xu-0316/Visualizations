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


df = pd.read_excel(r'C:\Users\徐浩然\Desktop\大量表+支付金额.xlsx', sheet_name='Sheet2')
# axs=sns.relplot(data=df, x="体重", y="身高", hue="性别",size="BMI", sizes=(15, 200),palette=clist,linewidth=0.2,alpha=0.9)
plt.figure(figsize=(10,6))
g=sns.scatterplot(data=df,x='引申重要性',y='满意度',color='#19422A',linewidth=1.5,edgecolor="#527D5D")
plt.axhline(y=3.752098,c='black',ls="--",lw=1)
plt.axvline(x=0.112122 ,c='black',ls="--",lw=1)
# sns.move_legend(loc='lower center')
# plt.tight_layout()
# g.fig.set_size_inches(10,7)
plt.text(0.1274,3.8228,'第Ⅰ象限：优势区')
plt.text(0.1035,3.8228,'第Ⅱ象限：维持区')
plt.text(0.1035,3.747,'第Ⅲ象限：改进区')
plt.text(0.1274,3.747,'第Ⅳ象限：劣势区')
plt.fill_between((0.112122,0.136),3.752098,3.828,color='#D5E8D4',alpha=0.5,linewidth=0)
plt.fill_between((0.087,0.112122),3.752098,3.828,color='#DAE8FC',alpha=0.5,linewidth=0)
plt.fill_between((0.112122,0.136),3.69 ,3.752098,color='#F8CECC',alpha=0.5,linewidth=0)
plt.fill_between((0.087,0.112122),3.69 ,3.752098,color='#FFF2CC',alpha=0.5,linewidth=0)
# sns.move_legend(g, 'lower right',bbox_to_anchor=(1.38,0.3), frameon=False)
# plt.subplots_adjust(left=0.09, bottom=0.074, right=0.737, top=0.97, wspace=0.2, hspace=0.2)
plt.margins(x=0)
plt.margins(y=0)
plt.savefig(r'C:/Users/徐浩然/Desktop/轻食Figure/IPA1.png',dpi=400)
plt.show()