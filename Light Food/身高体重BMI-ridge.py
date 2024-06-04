import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from joypy import joyplot
from matplotlib.colors import LinearSegmentedColormap, ListedColormap

plt.rcParams['font.serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False

plt.rcParams['font.size'] = 12
plt.style.use('seaborn-ticks')
# dataframe全显示
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)

# clist=['#EAF6DE','#B3D0AB',"#77A67E",'#527D5D','#19422A']
clist=['#19422A','#EAF6DE']

C = LinearSegmentedColormap.from_list('Blues',clist,N=256)
data=pd.read_excel(r'C:\Users\徐浩然\Desktop\Data ZD.xlsx',sheet_name='Sheet3')

fix, ax=joyplot(data, column=['男性','女性'],by='Weight', overlap=0.5, alpha=0.7, colormap=C,fade=False
                # ,ylabelsize=12                         #y轴标签的大小
                # ,xrot=30                               #x轴刻度线标签旋转角度
                # ,yrot=-30                               #y轴刻度线标签旋转角度
                #, fade=True                             #则显示渐变色
                # ,linecolor=‘b                      #曲线的颜色
                # ,blackground=none                        #背景颜色
                #overlap=1                                 #控制重叠程度
#                 # ‘title'=none
#                 , column=['SepalLengthCm', 'PetalLengthCm']
#                 , by='Species'  # 分组的列
#
#                 # ,gird=True                             #添加网格线
#                 # ,xlabelsize=12                         #x轴标签的大小
#                 # ,ylabelsize=12                         #y轴标签的大小
#                 # ,xrot=30                               #x轴刻度线标签旋转角度
#                 # , yrot=60                               #y轴刻度线标签旋转角度
#                 # ,hist=flase                             #直方图
#                 # , fade=True                             #则显示渐变色
#                 , ylim='max'  # 共享y轴的刻度
#                 # ,  ll=‘true                              #曲线下的填充颜色
#                 # ,linecolor=‘b                      #曲线的颜色
#                 # ,blackground=none                        #背景颜色
#                 # ,overlap=1                                 #控制重叠程度
#                 # ‘title'=none                            #添加图表的标题
#                 , colormap=plt.cm.rainbow  # 彩虹色
# #    色谱

)
plt.tight_layout()
plt.savefig(r'C:/Users/徐浩然/Desktop/轻食Figure/身高体重BMI.png',dpi=400)

print(data)
plt.show()