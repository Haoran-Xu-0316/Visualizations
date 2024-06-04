import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap, ListedColormap

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


cmap=plt.get_cmap('Oranges_r')
newcolors=cmap(np.linspace(0, 1, 500))
newcmap = ListedColormap(newcolors[280:380])
# pd.set_option('display.unicode.east_asian_width', True)
# sns.set_theme(context={'figure.figsize':[10, 4]}, style='ticks', palette='deep', font='Arial', font_scale=1, color_codes=True, rc=None)


df = pd.read_excel(r'C:\Users\徐浩然\Desktop\材料\公共类充电桩数量直流+交流20201130-20221130.xls', sheet_name='Sheet0',index_col=0)
ldf=pd.read_excel(r'C:\Users\徐浩然\Desktop\材料\公共类充电桩数量直流+交流20201130-20221130.xls', sheet_name='Sheet1',index_col=0)

bar=df.plot.bar(stacked=False,width=0.8, linewidth=0,edgecolor="black",  clip_on=False,cmap=newcmap,label='P')
bar.xaxis.set_tick_params(rotation=30)
bar.set_ylim(0,2000000)
bar.plot(ldf,color='black',label='Line', marker='v')
plt.legend(frameon=False,loc='upper center',ncol=3)

plt.ticklabel_format(axis="y", style='plain')

#bar.spines['bottom'].set_visible(False)
plt.tight_layout()
plt.savefig(r'C:/Users/徐浩然/Desktop/美赛Figure_Template\1890220023232320.png',dpi=400)
plt.show()