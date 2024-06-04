import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.colors import LinearSegmentedColormap
from scipy import stats

# 添加数据
x = np.arange(1 ,1827)

dat = pd.read_excel(r'C:\Users\徐浩然\Desktop\result.xlsx', sheet_name='Sheet1',parse_dates=[0])
print(len(dat['v'].values))
dat = dat.set_index('date').sort_index()

dat=dat.T
df = pd.read_excel(r'C:\Users\徐浩然\Desktop\Global GDP.xls', sheet_name='U',index_col=0)
y=np.array(dat)
# print(df,x,y)

plt.rcParams['font.sans-serif'] = ['Arial']
plt.rcParams['font.size'] = 12
plt.rcParams['axes.unicode_minus'] = False
# plt.style.use('seaborn-ticks')
# dataframe全显示
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)

c1list=[(16/255,70/255,128/255),(49/255,124/255,183/255),(109/255,173/255,209/255),(182/255,215/255,232/255),(233/255,241/255,244/255),(251/255,227/255,213/255),(246/255,178/255,147/255),(220/255,109/255,87/255),(183/255,34/255,48/255),(109/255,1/255,31/255)]
c2list=[(40/255,86/255,119/255),(177/255,193/255,204/255),(214/255,156/255,147/255),(229/255,207/255,194/255),(141/255,164/255,147/255)]
c3list=['#005020','#349D52','#B6E1AF']

C1 = LinearSegmentedColormap.from_list('Blues',c1list,N=256)
C2 = LinearSegmentedColormap.from_list('Blues',c2list,N=256)
C3 = LinearSegmentedColormap.from_list('Blues',c3list,N=256)
def gaussian_smooth(x, y, grid, sd):
    """平滑曲线"""
    weights = np.transpose([stats.norm.pdf(grid, m, sd) for m in x])
    weights = weights / weights.sum(0)
    return (weights * y).sum(1)


# 自定义颜色
COLORS = ["#D0D1E6", "#A6BDDB", "#74A9CF", "#2B8CBE", "#045A8D",(40/255,86/255,119/255),(177/255,193/255,204/255),(214/255,156/255,147/255),(229/255,207/255,194/255)]

# 创建画布
fig, ax = plt.subplots()

# 生成图表
grid = np.linspace(1 ,1827, num=1000)
y_smoothed = [gaussian_smooth(x, y_, grid, 1) for y_ in y]
ax.stackplot(grid, y_smoothed, colors=c3list, baseline="weighted_wiggle")
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_yticks([])
# plt.legend()
plt.tight_layout()
# plt.savefig(r'C:/Users/徐浩然/Desktop/GGDP-Figure/stream.png',dpi=400)
# 显示
plt.show()