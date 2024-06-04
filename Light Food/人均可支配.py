import geopandas
import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import statsmodels
from matplotlib import font_manager
from matplotlib.colors import LinearSegmentedColormap

# my_font=font_manager.FontProperties(fname="C:\Windows\Fonts\simsun.ttc")

plt.rcParams['font.size'] = 12
plt.rcParams['axes.unicode_minus'] = False
# plt.rcParams['sans.serif'] = ['SimSun']

rc = {'font.sans-serif': 'Microsoft YaHei',
      'axes.unicode_minus': False,"mathtext.fontset": 'stix'}
sns.set(style='ticks' ,rc=rc)
ticklabels_style = {
    "fontname": "Times New Roman",
}

# plt.style.use('seaborn-ticks')
# dataframe全显示
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)

# clist=['#EAF6DE','#B3D0AB',"#77A67E",'#527D5D','#19422A']
# # clist=['#F1F5C9','#CEDEA2','#98B574','#678B4A','#435C28']
# C = LinearSegmentedColormap.from_list('Blues',clist,N=256)

#B3D0AB
#19422A
df = pd.read_excel(r'C:\Users\徐浩然\Desktop\人均可支配.xls', sheet_name='Sheet0')
plt.figure(figsize=(12,5))


sns.barplot(x=df['Y'],y=df['中国居民人均可支配收入（万元）'],color='#B3D0AB')
#
# plt.xticks(range(0,1101,100))
# plt.yticks(range(0,10,1))
# plt.legend(frameon=False)
# plt.ylabel('')
plt.xlabel('')

plt.savefig(r'C:/Users/徐浩然/Desktop/轻食Figure/人均.png',dpi=400)

plt.show()