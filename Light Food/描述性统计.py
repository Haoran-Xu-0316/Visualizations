import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pylab as pl
import seaborn as sns
from matplotlib import cm, ticker
from matplotlib.colors import LinearSegmentedColormap

# rc = {'font.sans-serif': 'Microsoft YaHei',  'axes.unicode_minus': False,"mathtext.fontset": 'stix'}
# sns.set(context='notebook', rc=rc,style='ticks')
plt.rcParams['font.size'] = 10
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']

clist=['#EAF6DE','#B3D0AB',"#77A67E",'#527D5D','#19422A']
cclist=['#19422A','#527D5D',"#77A67E",'#B3D0AB']

C = LinearSegmentedColormap.from_list('Blues',clist,N=256)
CC = LinearSegmentedColormap.from_list('Blues',cclist,N=256)

# ----------------------------------------------------------------------------------------------------------------------
# plt.figure()
# label=['男','女']
# data=[545,555]
# plt.pie(data, explode=None,labels=label, autopct='%1.1f%%',pctdistance=0.5,wedgeprops=None,textprops={'color':'black','fontsize':10},radius=1, labeldistance=None,shadow=False, startangle=90, colors=['#527D5D','#B3D0AB'])
# plt.legend(loc='lower center',frameon=False,ncol=2,bbox_to_anchor=(0.5,0))
# plt.tight_layout()
# # plt.savefig(r'C:/Users/徐浩然/Desktop/轻食Figure/1.png',dpi=400)
# plt.savefig(r'C:/Users/徐浩然/Desktop/1.png',dpi=400)
# # ----------------------------------------------------------------------------------------------------------------------
# plt.figure(figsize=(10,3))
# d1=[0.1473,0.2345,0.1745,0.1491,0.1464,0.1482]
# d2=[0.1445,0.2361,0.1705,0.1473,0.1564,0.1452]
# label=['18岁以下','18-24岁','25-30岁','31-40岁','41-50岁','51岁及以上']
# x_width = range(0, len(d1))
# x1_width = [i - 0.15 for i in x_width]
# x2_width = [i + 0.15 for i in x_width]
# plt.bar(x1_width, d1, color='#527D5D', width=0.3, label="既有消费者")
# plt.bar(x2_width, d2,  color='#B3D0AB', width=0.3, label="总样本")
# plt.ylim((0.0,0.25))
# plt.gca().yaxis.set_major_formatter(ticker.PercentFormatter(xmax=1, decimals=1))
# plt.legend(frameon=False)
# x = range(len(label))
# plt.xticks(x, label)
# plt.tight_layout()
# plt.savefig(r'C:/Users/徐浩然/Desktop/轻食Figure/2.png',dpi=400)
# # ----------------------------------------------------------------------------------------------------------------------
# plt.figure()
# label=['1000元及以下','1001~3000元','3001~5000元','5001~7000元','7001~10000元','10001~15000元','15001~20000元','20000元以上']
# data=[117,242,236,85,113,104,100,103]
# plt.bar(label,data,color=plt.get_cmap(CC)(np.arange(8)/8))
# pl.xticks(rotation=30)
# plt.tight_layout()
# plt.savefig(r'C:/Users/徐浩然/Desktop/轻食Figure/3.png',dpi=400)
 # ----------------------------------------------------------------------------------------------------------------------
# plt.figure()
# label=['1000元及以下','1001~3000元','3001~5000元','5001~7000元','7001~10000元','10001~15000元','15001~20000元','20000元以上']
# data=[87,158,242,197,94,117,110,95]
# plt.bar(label,data,color=plt.get_cmap(CC)(np.arange(8)/8))
# pl.xticks(rotation=30)
# plt.tight_layout()
# plt.savefig(r'C:/Users/徐浩然/Desktop/轻食Figure/33.png',dpi=400)
# # ----------------------------------------------------------------------------------------------------------------------
# plt.figure()
# label=['在校学生','企业人员','学校、研究机构从业者','政府及事业单位职员','自主创业','自由职业','普通工人','农民','退休']
# data=[191,146,110,116,111,137,136,97,56]
# plt.pie(data, explode=None,labels=label, autopct='%1.1f%%',pctdistance=1.15,wedgeprops=None,textprops={'color':'black'},radius=1, labeldistance=None,shadow=False, startangle=90, colors=plt.get_cmap(C)(np.arange(9)/9))
# plt.legend(loc='lower center',frameon=False,ncol=3,bbox_to_anchor=(0.5,-0.2))
# plt.tight_layout()
# plt.savefig(r'C:/Users/徐浩然/Desktop/轻食Figure/4.png',dpi=400)
# # ----------------------------------------------------------------------------------------------------------------------
# plt.figure()
# label=['朋友/亲人/同学告知','传统媒体','美食平台','网络社交平台','短视频平台','直播平台','喜欢的明星、主播推荐','广告宣传','偶然路过轻食餐厅']
# data=[372,339,384,343,361,339,328,345,309]
# plt.bar(label,data,color=plt.get_cmap(CC)(np.arange(9)/9))
# plt.xticks(rotation=90)
# plt.tight_layout()
# plt.savefig(r'C:/Users/徐浩然/Desktop/轻食Figure/5.png',dpi=400)
# # ----------------------------------------------------------------------------------------------------------------------
# plt.figure()
# label=['到店消费并在店内食用','到店消费后打包','外卖到家','网购包装产品','购买食材自己做']
# data=[222,235,269,241,194]
# plt.bar(label,data,color=plt.get_cmap(CC)(np.arange(5)/5))
# pl.xticks(rotation=30)
# plt.tight_layout()
# plt.savefig(r'C:/Users/徐浩然/Desktop/轻食Figure/6.png',dpi=400)
# # ----------------------------------------------------------------------------------------------------------------------
# plt.figure()
# label=['沙拉类','主食类','饮品类','甜点类','零食类']
# data=[255,246,217,234,213]
# plt.bar(label,data,color=plt.get_cmap(CC)(np.arange(5)/5))
# # pl.xticks(rotation=30)
# plt.tight_layout()
# plt.savefig(r'C:/Users/徐浩然/Desktop/轻食Figure/7.png',dpi=400)
# ----------------------------------------------------------------------------------------------------------------------
plt.figure()
label=['大众点评','小红书','抖音','美团','饿了么','Bilibili','微博']
data=[426,389,366,377,340,326,339]
plt.bar(label,data,color=plt.get_cmap(CC)(np.arange(7)/7))
# pl.xticks(rotation=30)
plt.tight_layout()
# plt.savefig(r'C:/Users/徐浩然/Desktop/轻食Figure/8.png',dpi=400)
plt.savefig(r'C:/Users/徐浩然/Desktop/8.png',dpi=400)
# # ----------------------------------------------------------------------------------------------------------------------
#
# plt.figure()
# label=['0-20元','21-40元','41-60元','61-80元','81-100元','101-125元','126-150元','151元及以上']
# data=[0.7,6.1,7.7,9.8,13.8,15.5,20.6,25.6]
# plt.pie(data, explode=None,labels=label, autopct='%1.1f%%',pctdistance=1.15,wedgeprops=None,textprops={'color':'black'},radius=1, labeldistance=None,shadow=False, startangle=90,colors=plt.get_cmap(C)(np.arange(7)/7))
# plt.legend(loc='lower center',frameon=False,ncol=4,bbox_to_anchor=(0.5,-0.15))
# plt.tight_layout()
# plt.savefig(r'C:/Users/徐浩然/Desktop/轻食Figure/9.png',dpi=400)
# # ----------------------------------------------------------------------------------------------------------------------
# plt.figure()
# label=['0-20元','21-40元','41-60元','61-80元','81-100元','101-125元','126-150元','151元及以上']
# data=[8,67,85,108,152,171,227,282]
# plt.pie(data, explode=None,labels=label, autopct='%1.1f%%',pctdistance=1.15,wedgeprops=None,textprops={'color':'black'},radius=1, labeldistance=None,shadow=False, startangle=90,colors=plt.get_cmap(C)(np.arange(7)/7))
# plt.legend(loc='lower center',frameon=False,ncol=4,bbox_to_anchor=(0.5,-0.15))
# plt.tight_layout()
# plt.savefig(r'C:/Users/徐浩然/Desktop/轻食Figure/10.png',dpi=400)
# # ----------------------------------------------------------------------------------------------------------------------
# plt.figure()
# label=['几乎每天都去','2-3次/周','1次/周','1次/半个月','1次/月','少于1次/月']
# data=[175,255,246,217,234,213]
# plt.barh(label,data,color=plt.get_cmap(CC)(np.arange(8)/8))
# plt.tight_layout()
# plt.savefig(r'C:/Users/徐浩然/Desktop/轻食Figure/11.png',dpi=400)
# # ----------------------------------------------------------------------------------------------------------------------
# # 潜在----------------------------------------------------------------------------------------------------------------------
# # ----------------------------------------------------------------------------------------------------------------------
# plt.figure()
# label=['男','女']
# data=[42,54]
# plt.pie(data, explode=None,labels=label, autopct='%1.1f%%',pctdistance=0.5,wedgeprops=None,textprops={'color':'black','fontsize':10},radius=1, labeldistance=None,shadow=False, startangle=90, colors=['#527D5D','#B3D0AB'])
# plt.legend(loc='lower center',frameon=False,ncol=2,bbox_to_anchor=(0.5,0))
# plt.tight_layout()
# # plt.savefig(r'C:/Users/徐浩然/Desktop/轻食Figure/浅1.png',dpi=400)
# plt.savefig(r'C:/Users/徐浩然/Desktop/浅1.png',dpi=400)
# ----------------------------------------------------------------------------------------------------------------------
# plt.figure()
# d1=[0.1250,0.1667,0.1354,0.1875,0.2188,0.1667]
# d2=[0.1445,0.2361,0.1705,0.1473,0.1564,0.1452]
# label=['18岁以下','18-24岁','25-30岁','31-40岁','41-50岁','51岁及以上']
# x_width = range(0, len(d1))
# x1_width = [i - 0.15 for i in x_width]
# x2_width = [i + 0.15 for i in x_width]
# plt.bar(x1_width, d1, color='#527D5D', width=0.3, label="潜在消费者")
# plt.bar(x2_width, d2,  color='#B3D0AB', width=0.3, label="总样本")
# plt.ylim((0.0,0.25))
# plt.gca().yaxis.set_major_formatter(ticker.PercentFormatter(xmax=1, decimals=1))
# plt.legend(frameon=False)
# x = range(len(label))
# plt.xticks(x, label)
# plt.tight_layout()
# # plt.savefig(r'C:/Users/徐浩然/Desktop/轻食Figure/浅2.png',dpi=400)
# plt.savefig(r'C:/Users/徐浩然/Desktop/浅2.png',dpi=400)
# # ----------------------------------------------------------------------------------------------------------------------
# plt.figure()
# label=['1000元及以下','1001~3000元','3001~5000元','5001~7000元','7001~10000元','10001~15000元','15001~20000元','20000元以上']
# data=[938,625,1979,2292,1042,729,1458,938]
# plt.pie(data, explode=None,labels=label, autopct='%1.1f%%',pctdistance=1.15,wedgeprops=None,textprops={'color':'black'},radius=1, labeldistance=None,shadow=False, startangle=90, colors=plt.get_cmap(CC)(np.arange(8)/8))
# pl.xticks(rotation=30)
# plt.legend(loc='lower center',frameon=False,ncol=4,bbox_to_anchor=(0.5,-0.15))
# plt.tight_layout()
# # plt.savefig(r'C:/Users/徐浩然/Desktop/轻食Figure/浅3.png',dpi=400)
# plt.savefig(r'C:/Users/徐浩然/Desktop/浅3.png',dpi=400)
# # ----------------------------------------------------------------------------------------------------------------------
# plt.figure()
# label=['1000元及以下','1001~3000元','3001~5000元','5001~7000元','7001~10000元','10001~15000元','15001~20000元','20000元以上']
# data=[521,2083,1979,1667,1146,1042,417,1146]
# plt.pie(data, explode=None,labels=label, autopct='%1.1f%%',pctdistance=1.15,wedgeprops=None,textprops={'color':'black'},radius=1, labeldistance=None,shadow=False, startangle=90, colors=plt.get_cmap(CC)(np.arange(8)/8))
# plt.xticks(rotation=30)
# plt.legend(loc='lower center',frameon=False,ncol=4,bbox_to_anchor=(0.5,-0.15))
# plt.tight_layout()
# plt.savefig(r'C:/Users/徐浩然/Desktop/轻食Figure/浅4.png',dpi=400)
# # ----------------------------------------------------------------------------------------------------------------------
# plt.figure()
# label=['分量不足','种类较少','价格较高','品质不高','不感兴趣，没有需求','不适合自己口味']
# data=[30,33,38,35,36,41]
# plt.bar(label,data,color=plt.get_cmap(CC)(np.arange(6)/6))
# plt.xticks(rotation=30)
# plt.tight_layout()
# plt.savefig(r'C:/Users/徐浩然/Desktop/轻食Figure/浅5.png',dpi=400)
# # ----------------------------------------------------------------------------------------------------------------------
# plt.figure()
# label=['减脂/健身需求','健康营养需求','方便快捷需求','放松身心需求','紧跟潮流需求']
# data=[47,39,36,45,46]
# plt.bar(label,data,color=plt.get_cmap(CC)(np.arange(5)/5))
# plt.xticks(rotation=30)
# plt.tight_layout()
# plt.savefig(r'C:/Users/徐浩然/Desktop/轻食Figure/浅6.png',dpi=400)
# # --------------------------------------------------------------------------------------------------------------------
# plt.figure(figsize=(10,3))
# label=['零食类','甜品类','饮品类','主食类','沙拉类']
# d1=[34,37,47,43,49]
# d2=[62,59,49,53,47]
# plt.barh(y=[0,1,2,3,4],width=d1,color='#527D5D',label='已选人数')
# plt.barh(y=[0,1,2,3,4],left=d1,width=d1,color='#B3D0AB',label='已选人数')
# x = range(len(label))
# plt.yticks(x, label)
# plt.tight_layout()
# plt.legend(frameon=False)
# plt.savefig(r'C:/Users/徐浩然/Desktop/轻食Figure/浅7.png',dpi=400)
# # --------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
plt.show()