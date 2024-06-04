import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap

plt.rcParams['font.sans-serif']=['Microsoft YaHei']
plt.rcParams['font.size'] = 12
plt.rcParams['axes.unicode_minus'] = False
# dataframe全显示
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)

clist=['#EAF6DE','#B3D0AB',"#77A67E",'#527D5D','#19422A']
plt.figure(figsize=(10,7))

# Load the example tips dataset
df = pd.read_excel(r'C:\Users\徐浩然\Desktop\影响因素+反馈行为.xlsx', sheet_name='Sheet1')


sns.violinplot(data=df, x="反馈", y="值", hue="性别",
             split=True, inner="quart", linewidth=1,
              palette={"男性": '#527D5D', "女性": '#B3D0AB'})
# plt.tight_layout()
plt.legend(frameon=False,ncol=2,loc='upper center',bbox_to_anchor=(0.5,1.02))
plt.ylabel('')
plt.xlabel('')
plt.savefig(r'C:/Users/徐浩然/Desktop/轻食Figure/反馈小提琴.png',dpi=400)

plt.show()