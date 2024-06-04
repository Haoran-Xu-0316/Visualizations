import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap

# # plt.rcParams['font.sans-serif'] = ['Arial']
# plt.rcParams['font.size'] = 12
# plt.rcParams['axes.unicode_minus'] = False
# # plt.style.use('seaborn-ticks')
# # dataframe全显示
# pd.set_option('display.max_columns',None)
# pd.set_option('display.max_rows',None)

clist=['#EAF6DE','#B3D0AB',"#77A67E",'#527D5D','#19422A']

C = LinearSegmentedColormap.from_list('Blues',clist,N=256)
df=pd.read_excel(r'C:\Users\徐浩然\Desktop\大量表+支付金额.xlsx',sheet_name='大量表1')

sns.pairplot(df, kind='reg',palette=clist)

# plt.savefig(r'C:/Users/徐浩然/Desktop/轻食Figure/pair.png',dpi=400)


plt.show()