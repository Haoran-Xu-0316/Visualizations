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


clist=['#EAF6DE','#B3D0AB',"#77A67E",'#527D5D','#19422A']
C = LinearSegmentedColormap.from_list('Blues',clist,N=256)

#B3D0AB
#19422A

df = pd.read_excel(r'C:\Users\徐浩然\Desktop\TCG.xls', sheet_name='Sheet1',,parse_dates=[0])
print(df)
fig=plt.figure(figsize=(12,5))


plt.bar(df['统计时间'],df['社会消费品零售总额（亿元）'],color='#B3D0AB',linestyle='-',label='社会消费品零售总额（亿元）')
plt.bar(df['统计时间'],df['限额以上企业消费品零售额（亿元）'],color='#77A67E',linestyle='--',label='限额以上企业消费品零售额（亿元）')

# plt.xticks(rotation=45)
plt.twinx()
plt.plot(df['统计时间'],df['社会消费品零售总额月度同比增长（%）'],color='#527D5D',linestyle='-',label='社会消费品零售总额月度同比增长（%）')
plt.plot(df['统计时间'],df['限额以上企业消费品零售额月度同比增长（%）'],color='#19422A',linestyle='-',label='限额以上企业消费品零售额月度同比增长（%）')

# plt.xticks(range(0,1101,100))
# plt.yticks(range(0,10,1))
# plt.legend(frameon=False)
# plt.ylabel('')
# plt.ylabel('TCG')
fig.legend(frameon=False,bbox_to_anchor=(0.945,0.94),ncol=4,columnspacing=0.1,fontsize=9)
plt.savefig(r'C:/Users/徐浩然/Desktop/TCG.png',dpi=400)

plt.show()