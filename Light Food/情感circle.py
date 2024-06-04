import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import squarify
from matplotlib.colors import LinearSegmentedColormap
from pylab import mpl

pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)


plt.rcParams['font.sans-serif']=['Microsoft YaHei']
plt.rcParams['font.size'] = 15
plt.rcParams['axes.unicode_minus'] = False


plt.figure(figsize=(12,7))
labels = ['正向评论', '负向评论', '中性评论']
sizes = [81.8, 16.5, 1.7]

plt.rcParams['axes.unicode_minus'] = False

clist=['#EAF6DE','#B3D0AB',"#77A67E",'#527D5D','#19422A']
# clist=['#F1F5C9','#CEDEA2','#98B574','#678B4A','#435C28']
CC = LinearSegmentedColormap.from_list('Blues',clist,N=256)

cmap=['#527D5D','#B3D0AB','#EAF6DE']
l=['81.8%', '16.5%', '1.7%']
squarify.plot(sizes, label=labels, pad = False, value=l,alpha=0.8,edgecolor='black',linewidth=1,color=cmap)
# 标签字体大小的线性插值函数

plt.axis('off')
plt.savefig(r'C:/Users/徐浩然/Desktop/轻食Figure/circle.png',dpi=400)

# plt.tight_layout()
plt.show()
