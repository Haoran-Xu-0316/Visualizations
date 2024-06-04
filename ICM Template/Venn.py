import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.colors import LinearSegmentedColormap
from matplotlib_venn import venn3

plt.rcParams['font.sans-serif'] = ['Arial']
plt.rcParams['font.size'] = 12
plt.rcParams['axes.unicode_minus'] = False
plt.style.use('seaborn-ticks')
# dataframe全显示
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)

c1list=[(16/255,70/255,128/255),(49/255,124/255,183/255),(109/255,173/255,209/255),(182/255,215/255,232/255),(233/255,241/255,244/255),(251/255,227/255,213/255),(246/255,178/255,147/255),(220/255,109/255,87/255),(183/255,34/255,48/255),(109/255,1/255,31/255)]
c2list=[(40/255,86/255,119/255),(177/255,193/255,204/255),(214/255,156/255,147/255),(229/255,207/255,194/255),(141/255,164/255,147/255)]
c3list=[(40/255,86/255,119/255),(177/255,193/255,204/255),(214/255,156/255,147/255),(229/255,207/255,194/255),(141/255,164/255,147/255),(59/255,72/255,47/255)]

C1 = LinearSegmentedColormap.from_list('Blues',c1list,N=256)
C2 = LinearSegmentedColormap.from_list('Blues',c2list,N=256)
C3 = LinearSegmentedColormap.from_list('Blues',c3list,N=256)

a = [12, 9, 6, 13, 10, 12]
b = [8, 6, 10, 7, 9, 11]
c = [11, 12, 9, 12, 13, 9]

a1 = set(a)
b1 = set(b)
c1 = set(c)

plt.figure()  # 创建画布

g = venn3(subsets=[a1, b1, c1],  # 绘图数据集
          set_labels=('A', 'B', 'C'),  # 设置组名
          set_colors=plt.get_cmap('Blues')(np.arange(100,301,100)), # 设置圈的颜色，中间颜色不能修改
          alpha=0.6,  # 透明度
          normalize_to=1.0)

plt.tight_layout()
plt.savefig(r'C:/Users/徐浩然/Desktop/美赛Figure_Template\232.png',dpi=400)
plt.show()