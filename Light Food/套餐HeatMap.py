import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap

pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)

df = pd.read_excel(r'C:/Users/徐浩然/Desktop/psss.xlsx',sheet_name='209209064_1516_1516adjust')  # 以pandas库的read_csv函数读取csv文件
print(df.head())
plt.rcParams['font.sans-serif']=['Microsoft YaHei']
plt.rcParams['font.size'] = 12
plt.rcParams['axes.unicode_minus'] = False

clist=['#EAF6DE','#B3D0AB',"#77A67E",'#527D5D','#19422A']
# clist=['#F1F5C9','#CEDEA2','#98B574','#678B4A','#435C28']
CC = LinearSegmentedColormap.from_list('Blues',clist,N=256)
C='#527D5D'

h=plt.contourf(corrmat)

