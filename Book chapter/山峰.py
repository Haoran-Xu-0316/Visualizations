import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from joypy import joyplot
from matplotlib.colors import ListedColormap

df = pd.read_excel(r'C:\Users\徐浩然\Desktop\材料\shanfeng.xlsx', sheet_name='Sheet1')

plt.rcParams['font.sans-serif'] = ['Arial']
cmap=plt.get_cmap('Oranges')
newcolors=cmap(np.linspace(0, 1, 4))
newcmap = ListedColormap(newcolors[1:4])
fix, ax=joyplot(df,figsize=(12,5),fade=True,ylim='min',colormap=newcmap
              # ,gird=True                             #添加网格线
              #,xlabelsize=12                         #x轴标签的大小
              # ,ylabelsize=12                         #y轴标签的大小
              # ,xrot=30                               #x轴刻度线标签旋转角度
              # ,yrot=-30                               #y轴刻度线标签旋转角度
              #, fade=True                             #则显示渐变色
              # ,linecolor=‘b                      #曲线的颜色
              # ,blackground=none                        #背景颜色
              #overlap=1                                 #控制重叠程度
              # ‘title'=none
)
plt.savefig(r'C:/Users/徐浩然/Desktop/山峰.png',dpi=400)
plt.show()