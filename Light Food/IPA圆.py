import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import Wedge
from matplotlib.ticker import FuncFormatter

pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.sans-serif']=['Microsoft YaHei']
clist=['#EAF6DE','#B3D0AB',"#77A67E",'#527D5D','#19422A']
C = LinearSegmentedColormap.from_list('Blues',clist,N=256)
fig, ax = plt.subplots(figsize=(6,6))
plt.fill_between((0,100),0,100,color='#EAF6DE')
# 创建半圆
semicircle1 = Wedge((0, 0), 25, 0, 90,color='#19422A')
semicircle2 = Wedge((0, 0), 50, 0, 90,color='#527D5D')
semicircle3 = Wedge((0, 0), 75, 0, 90,color="#77A67E")
semicircle4 = Wedge((0, 0), 100, 0, 90,color='#B3D0AB')
semicircle5 = Wedge((0, 0), 120, 0, 90,color='#EAF6DE')

ax.add_patch(semicircle4)
ax.add_patch(semicircle3)
ax.add_patch(semicircle2)
ax.add_patch(semicircle1)
def to_percent(temp, position):
    return "%1.0f"%(temp) + "%"

plt.gca().yaxis.set_major_formatter(FuncFormatter(to_percent))

plt.gca().xaxis.set_major_formatter(FuncFormatter(to_percent))


# 设置xy轴等长，否则不圆

plt.xticks(np.arange(0,101,20))
plt.yticks(np.arange(0,101,20))
plt.xlim(0,120)
plt.ylim(0,120)
# def plot(x,y):
x=73.78
y=81.25
plt.scatter(x,y,label='已筛选')
plt.plot([0,x],[0,y],linestyle='--')
plt.text(x-15,
             y+6,
             (x,y),
             fontsize=12,
             # verticalalignment="top",
             # horizontalalignment="right"
         color='black'
             )
x=73.17
y=59.31
plt.scatter(x,y,label='未筛选')
plt.plot([0,x],[0,y],linestyle='--')
plt.text(x-15,
             y+6,
             (x,y),
             fontsize=12,
             # verticalalignment="top",
             # horizontalalignment="right"
         color='black'
             )


# a=plot(73.78,81.25)
# b=plot(73.17,59.31)

ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')


plt.axhline(y=100,xmin=0, xmax=0.83333,c='black',ls="--",lw=1)
plt.axvline(x=100 ,ymin=0, ymax=0.83333,c='black',ls="--",lw=1)
# plt.axis('equal')
plt.legend(frameon=False,loc='upper center')
plt.savefig(r'C:/Users/徐浩然/Desktop/轻食Figure/IPA圆.png',dpi=400)

plt.show()