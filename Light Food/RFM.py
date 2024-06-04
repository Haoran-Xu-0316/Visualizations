import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.art3d as art3d
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import Circle, PathPatch
from matplotlib.text import TextPath
from matplotlib.transforms import Affine2D

plt.rcParams['font.sans-serif']=['Microsoft YaHei']
plt.rcParams['font.size'] = 12
plt.rcParams['axes.unicode_minus'] = False

pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)


clist=['#EAF6DE','#B3D0AB',"#77A67E",'#527D5D','#19422A']
cclist=['#19422A','#527D5D',"#77A67E",'#B3D0AB']

C = LinearSegmentedColormap.from_list('Blues',clist,N=256)
CC = LinearSegmentedColormap.from_list('Blues',cclist,N=256)




# df = pd.read_excel(r'C:\Users\徐浩然\Desktop\rfm.xls', sheet_name='Sheet1',index_col=0)



# # Plot
# plt.figure(figsize=(10,10))
# ax = plt.axes(projection='3d')
#
# ax.scatter(df['PCA11'], df['PCA21'], df['PCA31'],data=df,c="#6C8EBF",linewidth=0.5,edgecolor='black',s=30,label='聚类类别_1')
# ax.scatter(-4, df['PCA21'], df['PCA31'], zdir='z', c="#DAE8FC",linewidth=0)
# ax.scatter(df['PCA11'], 3, df['PCA31'], zdir='z', c="#DAE8FC",linewidth=0)
# ax.scatter(df['PCA11'], df['PCA21'], -4, zdir='z', c='#DAE8FC',linewidth=0)
#
#
# ax.scatter(df['PCA12'], df['PCA22'],df['PCA32'],data=df,c='#FFBE99',linewidth=0.5,edgecolor='black',s=30,label='聚类类别_1')
# ax.scatter(-4, df['PCA22'],df['PCA32'], zdir='z', c='#FFE6CC',linewidth=0)
# ax.scatter(df['PCA12'], 3,df['PCA32'], zdir='z', c='#FFE6CC',linewidth=0)
# ax.scatter(df['PCA12'], df['PCA22'],-4, zdir='z', c='#FFE6CC',linewidth=0)
#
#
# ax.scatter(df['PCA13'], df['PCA23'], df['PCA33'],data=df,c='#77A67E',linewidth=0.5,edgecolor='black',s=30,label='聚类类别_1')
# ax.scatter(-4, df['PCA23'], df['PCA33'], zdir='z', c='#D5E8D4',linewidth=0)
# ax.scatter(df['PCA13'], 3, df['PCA33'], zdir='z', c='#D5E8D4',linewidth=0)
# ax.scatter(df['PCA13'], df['PCA23'], -4, zdir='z', c='#D5E8D4',linewidth=0)
#
# ax.scatter(df['PCA14'], df['PCA24'], df['PCA34'],data=df,c='#FF9999',linewidth=0.5,edgecolor='black',s=30,label='聚类类别_1')
# ax.scatter(-4, df['PCA24'], df['PCA34'], zdir='z', c='#F8CECC',linewidth=0)
# ax.scatter(df['PCA14'], 3, df['PCA34'], zdir='z', c='#F8CECC',linewidth=0)
# ax.scatter(df['PCA14'], df['PCA24'], -4, zdir='z', c='#F8CECC',linewidth=0)
#
#
#
# ax.set_xticks(np.arange(-4,4))
# ax.set_xlim(-4,4)
# ax.set_yticks(np.arange(-4,4))
# ax.set_ylim(-4,4)
# ax.set_zticks(np.arange(-4,5))
# ax.set_zlim(-4,4)
# ax.grid(False)
#
# ax.set_xlabel('PCA1')
# ax.set_ylabel('PCA2')
# ax.set_zlabel('PCA3')
# # ax.view_init(elev=46, azim=33)
# plt.legend(frameon=False,loc='lower right',bbox_to_anchor=(1.07,0.1))
# # plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=None)
# plt.savefig(r'C:/Users/徐浩然/Desktop/轻食Figure/1.png',dpi=400)

x=[1,2,3,4,5,6,7,8,9,10]
y=[8470,5825,4461,3403,3010,2654,2401,2189,2012,1904]

plt.figure(figsize=(18,6))
plt.subplot(1,2,1)
plt.plot(x,y,color='#19422A',linewidth=2,alpha=0.7,marker='*')
plt.yticks(np.arange(1000,9001,1000))
plt.xticks(np.arange(1,11,1))
plt.xlabel('聚类个数')
plt.ylabel('距离平方和')
plt.subplot(1,2,2)
label=['聚类类别_1','聚类类别_2','聚类类别_3','聚类类别_4']
data=[37500,26040,19790,16670]
plt.pie(data, explode=None,labels=label, autopct='%1.3f%%',pctdistance=0.5,wedgeprops=None,textprops={'color':'black'},radius=1, labeldistance=None,shadow=False, startangle=90, colors=plt.get_cmap(CC)(np.arange(4)/4))
plt.legend(loc='lower center',frameon=False,ncol=2,bbox_to_anchor=(0.5,-0.1))
plt.subplots_adjust(left=0.125, bottom=0.11, right=0.9, top=0.88, wspace=0, hspace=0.2)
# plt.savefig(r'C:/Users/徐浩然/Desktop/rfm.png',dpi=400)
plt.show()

