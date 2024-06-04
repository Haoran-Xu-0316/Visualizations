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


clist=['#B3D0AB',"#77A67E",'#527D5D','#19422A']
# clist=['#F1F5C9','#CEDEA2','#98B574','#678B4A','#435C28']
C = LinearSegmentedColormap.from_list('Blues',clist,N=256)

#B3D0AB
#19422A

df = pd.read_excel(r'C:\Users\徐浩然\Desktop\LR.xlsx', sheet_name='Sheet1')
print(df)
plt.figure(figsize=(9,5))
plt.plot(df['T'],df['N'],color='#527D5D',linewidth=2,label='文献数量')
plt.plot(df['T'],df['二'],color='#435C28',linewidth=1,linestyle='--',label='MA E=2')
plt.plot(df['T'],df['三'],color='#678B4A',linewidth=1,linestyle='--',label='MA E=3')
plt.plot(df['T'],df['四'],color='#98B574',linewidth=1,linestyle='--',label='MA E=4')
plt.plot(df['T'],df['五'],color='#CEDEA2',linewidth=1,linestyle='--',label='MA E=5')
plt.plot(df['T'],df['六'],color='#F1F5C9',linewidth=1,linestyle='--',label='MA E=6')

plt.xticks(range(1990,2026,5))
# plt.yticks(range(0,10,1))
plt.legend(frameon=False)
ax=plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
plt.ylabel('')
# plt.savefig(r'C:/Users/徐浩然/Desktop/轻食Figure/LR.png',dpi=400)
plt.savefig(r'C:/Users/徐浩然/Desktop/LR.png',dpi=400)

plt.show()