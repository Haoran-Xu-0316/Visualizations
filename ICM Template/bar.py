import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap

plt.rcParams['font.sans-serif'] = ['Arial']
plt.rcParams['font.size'] = 12
plt.rcParams['axes.unicode_minus'] = False
plt.style.use('seaborn-ticks')
# dataframe全显示
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)

c1list=[(16/255,70/255,128/255),(49/255,124/255,183/255),(109/255,173/255,209/255),(182/255,215/255,232/255),(233/255,241/255,244/255),(251/255,227/255,213/255),(246/255,178/255,147/255),(220/255,109/255,87/255),(183/255,34/255,48/255),(109/255,1/255,31/255)]
c2list=[(40/255,86/255,119/255),(177/255,193/255,204/255),(214/255,156/255,147/255),(229/255,207/255,194/255),(141/255,164/255,147/255)]
#c2list=[(40/255,86/255,119/255),(177/255,193/255,204/255),(214/255,156/255,147/255),(229/255,207/255,194/255),(141/255,164/255,147/255),(59/255,72/255,47/255)]

C1 = LinearSegmentedColormap.from_list('Blues',c1list,N=256)
C2 = LinearSegmentedColormap.from_list('Blues',c2list,N=256)

# make data:
np.random.seed(3)
x = 0.5 + np.arange(8)
y = np.random.uniform(2, 7, len(x))
labels = ['A', 'B', 'C', 'D','E','F','G','H']

# plot
fig, ax = plt.subplots()

ax.bar(labels , y, width=0.8, edgecolor="white", linewidth=0.7,color=c2list)

#ax.set(xlim=(0, 8), xticks=np.arange(0, 8),ylim=(0, 8), yticks=np.arange(0, 8))
plt.tight_layout()
plt.savefig(r'C:/Users/徐浩然/Desktop/美赛Figure_Template\1312.png',dpi=400)


plt.show()