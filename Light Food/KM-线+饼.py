import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap

plt.rcParams['font.sans-serif']=['Microsoft YaHei']
plt.rcParams['font.size'] = 12
plt.rcParams['axes.unicode_minus'] = False
# # plt.style.use('seaborn-ticks')
# # dataframe全显示
# pd.set_option('display.max_columns',None)
# pd.set_option('display.max_rows',None)

clist=['#EAF6DE','#B3D0AB',"#77A67E",'#527D5D','#19422A']
cclist=['#19422A','#527D5D',"#77A67E",'#B3D0AB']

C = LinearSegmentedColormap.from_list('Blues',clist,N=256)
CC = LinearSegmentedColormap.from_list('Blues',cclist,N=256)


x=[1,2,3,4,5,6,7,8,9,10]
y=[45593,
36816,
30445,
26595,
25733,
25089,
24474,
23789,
23050,
22358]

plt.figure(figsize=(18,6))
plt.subplot(1,2,1)
plt.plot(x,y,color='#19422A',linewidth=2,alpha=0.7,marker='*')
plt.yticks(np.arange(20000,50001,5000))
plt.xticks(np.arange(1,11,1))
plt.xlabel('聚类个数')
plt.ylabel('距离平方和')
plt.subplot(1,2,2)
label=['聚类类别_1','聚类类别_2','聚类类别_3','聚类类别_4']
data=[267,251,302,280]
plt.pie(data, explode=None,labels=label, autopct='%1.3f%%',pctdistance=0.5,wedgeprops=None,textprops={'color':'black'},radius=1, labeldistance=None,shadow=False, startangle=90, colors=plt.get_cmap(CC)(np.arange(4)/4))
plt.legend(loc='lower center',frameon=False,ncol=2,bbox_to_anchor=(0.5,-0.1))
plt.subplots_adjust(left=0.125, bottom=0.11, right=0.9, top=0.88, wspace=0, hspace=0.2)
# plt.savefig(r'C:/Users/徐浩然/Desktop/轻食Figure/线+饼.png',dpi=400)
plt.savefig(r'C:/Users/徐浩然/Desktop/线+饼.png',dpi=400)



plt.figure(figsize=(18,6))
plt.subplot(1,2,1)
df = pd.read_excel(r'C:\Users\徐浩然\Desktop\聚类.xlsx', sheet_name='Sheet1',index_col=0)
g=sns.scatterplot(data=df,x='PCA1',y='PCA2',hue='聚类种类',linewidth=0.8,edgecolor="black",alpha=0.8,palette=["#6C8EBF",'#FFBE99','#D5E8D4','#FF9999'])
plt.subplot(1,2,2)
k=sns.kdeplot(data=df,x='PCA1',y='PCA2',hue='聚类类别',fill=False,palette=["#6C8EBF",'#FFBE99','#D5E8D4','#FF9999'])
sns.move_legend(g,loc='lower right',frameon=False, title=None)
sns.move_legend(k,loc='lower right',frameon=False, title=None)
# plt.savefig(r'C:/Users/徐浩然/Desktop/轻食Figure/cluster.png',dpi=400)
plt.savefig(r'C:/Users/徐浩然/Desktop/cluster.png',dpi=400)
plt.show()
