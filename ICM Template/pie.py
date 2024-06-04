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
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'For Agriculture', 'ForDomestic Use', 'For Industry', 'Artificial Ecosystem Water Replenishment'
sizes = [6150, 540,1770,1540]


fig1, ax1 = plt.subplots(figsize=(10,6))
ax1.pie(sizes, explode=None, labels=labels, autopct='%1.1f%%',pctdistance=0.5,wedgeprops=None,textprops={'color':'white','style':''},radius=1, labeldistance=None,shadow=False, startangle=90, colors=c1list)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.legend(ncol=4,loc='lower center',bbox_to_anchor=(0.5,-0.1))
# plt.savefig(r'C:/Users/徐浩然/Desktop/美赛Figure_Template\7.png',dpi=400)

plt.show()