import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import statsmodels
from matplotlib import font_manager
from matplotlib.colors import LinearSegmentedColormap

my_font=font_manager.FontProperties(fname="C:\Windows\Fonts\simsun.ttc")

# plt.rcParams['font.serif'] = ['Simsun']
plt.rcParams['font.size'] = 12
plt.rcParams['axes.unicode_minus'] = False
plt.style.use('seaborn-ticks')



rc = {'font.sans-serif': 'Microsoft YaHei',
      'axes.unicode_minus': False,"mathtext.fontset": 'stix'}
sns.set(context='notebook', rc=rc)
ticklabels_style = {
    "fontname": "Times New Roman",
}
# dataframe全显示
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
clist=['#EAF6DE','#B3D0AB',"#77A67E",'#527D5D','#19422A']
# clist=['#F1F5C9','#CEDEA2','#98B574','#678B4A','#435C28']
C = LinearSegmentedColormap.from_list('Blues',clist,N=256)

# data
# df = pd.read_excel(r'C:\Users\徐浩然\Desktop\correlation.xlsx', sheet_name='产品因素',index_col=0 )

df = pd.read_excel(r'C:\Users\徐浩然\Desktop\correlation.xlsx', sheet_name='产品因素',index_col=0)
plt.subplots(figsize=(10,5))

# plot
heat=sns.heatmap(df, annot=True,fmt=".4f", linecolor='black',robust=True,linewidth=0.3,cmap=C, vmin=0, vmax=1,cbar_kws={"orientation":"vertical"})
heat.xaxis.set_tick_params(rotation=30)
heat.yaxis.set_tick_params(rotation=30)
# plt.xticks(**ticklabels_style)
# plt.yticks(**ticklabels_style)


# adjustment & save
plt.tight_layout()
heat.set_ylabel('')
plt.savefig(r'C:/Users/徐浩然/Desktop/轻食Figure\产品因素',dpi=400)

plt.show()
