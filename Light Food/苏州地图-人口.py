import geopandas
import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['font.size'] = 12
plt.rcParams['axes.unicode_minus'] = False
plt.style.use('seaborn-ticks')
# dataframe全显示
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)

clist=['#EAF6DE','#B3D0AB',"#77A67E",'#527D5D','#19422A']
# clist=['#F1F5C9','#CEDEA2','#98B574','#678B4A','#435C28']
C = LinearSegmentedColormap.from_list('Blues',clist,N=256)

SZ=gpd.read_file(r'C:\Users\徐浩然\Desktop\苏州地图.json')
# SZ.to_excel(r'C:/Users/徐浩然/Desktop/SZMAP.xlsx'
df = pd.read_excel(r'C:\Users\徐浩然\Desktop\SZMAP.xlsx', sheet_name='Sheet1')
SZ['Population']=df['Population']
# SZ.drop(['childrenNum','level','parent','subFeatureIndex'])
print(SZ)
SZ.to_excel(r'C:\Users\徐浩然\Desktop\MAPDF.xlsx')
SZ.plot(column= 'Population',cmap=C,legend=True,vmin=50,vmax=220)
plt.axis('off')
#['boxplot', 'equalinterval', 'fisherjenks', 'fisherjenkssampled', 'headtailbreaks', 'jenkscaspall', 'jenkscaspallforced',
# 'jenkscaspallsampled', 'maxp', 'maximumbreaks', 'naturalbreaks', 'quantiles', 'percentiles', 'stdmean', 'userdefined']

plt.tight_layout()
plt.savefig(r'C:/Users/徐浩然/Desktop/轻食Figure/苏州地图-人口.png',dpi=400)
plt.show()
