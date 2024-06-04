import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from joypy import joyplot
from matplotlib.colors import LinearSegmentedColormap, ListedColormap

plt.rcParams['font.sans-serif'] = ['Arial']
plt.rcParams['font.size'] = 12
plt.rcParams['axes.unicode_minus'] = False
plt.style.use('seaborn-ticks')
# dataframe全显示
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)

clist=[(16/255,70/255,128/255),(49/255,124/255,183/255),(109/255,173/255,209/255),(182/255,215/255,232/255),(233/255,241/255,244/255),(251/255,227/255,213/255),(246/255,178/255,147/255),(220/255,109/255,87/255),(183/255,34/255,48/255),(109/255,1/255,31/255)]
C = LinearSegmentedColormap.from_list('Blues',clist,N=256)
data=pd.read_excel(r'C:\Users\徐浩然\Desktop\ridge.xlsx')

fix, ax=joyplot(data,by='city',overlap=0.5
              # ,ylabelsize=12                         #y轴标签的大小
              # ,xrot=30                               #x轴刻度线标签旋转角度
              # ,yrot=-30                               #y轴刻度线标签旋转角度
              #, fade=True                             #则显示渐变色
              # ,linecolor=‘b                      #曲线的颜色
              # ,blackground=none                        #背景颜色
              #overlap=1                                 #控制重叠程度
              # ‘title'=none
)
plt.tight_layout()
# plt.savefig(r'C:/Users/徐浩然/Desktop/美赛Figure_Template\1453461.png',dpi=400)

print(data)
plt.show()