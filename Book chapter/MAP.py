
import geopandas as gpd
import mapclassify
import matplotlib.patches as mpatches
import matplotlib.patheffects as pe
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.rcParams['font.sans-serif'] = ['Arial']

provinces = {
    '吉林省': [125.326800, 43.896160], '黑龙江省': [126.662850, 45.742080],
    '辽宁省': [123.429250, 41.835710], '内蒙古自治区': [111.765220, 40.817330],
    '新疆维吾尔自治区': [87.627100, 43.793430], '青海省': [101.780110, 36.620870],
    '北京市': [116.407170, 39.904690], '天津市': [117.199370, 39.085100],
    '上海市': [121.473700, 31.230370], '重庆市': [106.550730, 29.564710],
    '河北省': [114.469790, 38.035990], '河南省': [113.753220, 34.765710],
    '陕西省': [108.954240, 34.264860], '江苏省': [118.762950, 32.060710],
    '山东省': [117.020760, 36.668260], '山西省': [112.562720, 37.873430],
    '甘肃省': [103.826340, 36.059420], '宁夏回族自治区': [106.258670, 38.471170],
    '四川省': [104.075720, 30.650890], '西藏自治区': [91.117480, 29.647250],
    '安徽省': [117.285650, 31.861570], '浙江省': [120.153600, 30.265550],
    '湖北省': [114.342340, 30.545390], '湖南省': [112.983400, 28.112660],
    '福建省': [119.296590, 26.099820], '江西省': [115.910040, 28.674170],
    '贵州省': [106.707220, 26.598200], '云南省': [102.709730, 25.045300],
    '广东省': [113.266270, 23.131710], '广西壮族自治区': [108.327540, 22.815210],
    '香港': [114.165460, 22.275340], '澳门': [113.549130, 22.198750],
    '海南省': [110.348630, 20.019970], '台湾省': [121.520076, 25.030724],
}

pp=pd.DataFrame(provinces,).T

bj=gpd.read_file(r'C:\Users\徐浩然\Desktop\map.json')

df = pd.read_excel(r'C:\Users\徐浩然\Desktop\材料\地图+饼图.xlsx', sheet_name='Sheet1')

x = np.cos(2 * np.pi * np.linspace(0, 2))
y = np.sin(2 * np.pi * np.linspace(0, 2))
xy = np.row_stack([[0, 0], np.column_stack([x, y])])


bj['Charging & Switching Facilities']=df['Charging & Switching Facilities']
bj['Public Charging Stations']=df['Public Charging Stations']
bj['Public Charging Piles']=df['Public Charging Piles']
bj['Shared Private Piles']=df['Shared Private Piles']
bj['Total']=df['Total']
fig, ax = plt.subplots(figsize=(10, 10))

ax=bj.plot(ax=ax,column='Total',scheme='maxp',legend=False,cmap='Oranges',edgecolor='black',linewidth=0.1)
xp=list(df['坐'])
yp=list(df['标'])
#ax.scatter(k[0],k[1],marker=xy)
#
color=['black','firebrick','#C7DEF1','#224878']
k=7
r=[1.0,1.0,1.0,1.0]
for i in range(34):
    rrr=[df.iloc[i][2]/df.iloc[i][6],df.iloc[i][3]/df.iloc[i][6],df.iloc[i][4]/df.iloc[i][6],df.iloc[i][5]/df.iloc[i][6]]
    rr=[0,0+df.iloc[i][6],0+df.iloc[i][2]/df.iloc[i][6]+df.iloc[i][3]/df.iloc[i][6],0+df.iloc[i][2]/df.iloc[i][6]+df.iloc[i][3]/df.iloc[i][6]+df.iloc[i][4]/df.iloc[i][6]]
    r=[rr[0]+rrr[0],rr[1]+rrr[1],rr[2]+rrr[2],rr[3]+rrr[3]]
    for j in range(4):
        x = np.cos(2 * np.pi * np.linspace(rr[j], r[j]))
        y = np.sin(2 * np.pi * np.linspace(rr[j], r[j]))
        xy = np.row_stack([[0, 0], np.column_stack([x, y])])
        ax.scatter(xp[i], yp[i], marker=xy, facecolor=color[j],s=df.iloc[i][6]/100,alpha=0.98,linewidth=0.2,edgecolor='black')
plt.axis('off')


#legend 1
labels = ["1","2",'3','4']
patches = [mpatches.Patch(color=color[i],label="{:s}".format(labels[i])) for i in range(len(color))]
#leg1 = ax.legend(handles=patches,fontsize=15,loc=4,title="CI",title_fontsize=17,bbox_to_anchor=(0.99,0.2))


#legend 2
cmap = plt.get_cmap("viridis")
bp = mapclassify.NaturalBreaks(np.array(bj["Total"]),k=k+1)
if len(bp.bins) < k:
    k = len(bp.bins)-1
patches2 = []
for i in range(k):
    facecolor=cmap(i*(1/(k-1)))
    label=f'{bp.bins[i]} - {bp.bins[i+1]}'
    patches2.append(mpatches.Patch(facecolor=facecolor,label=label))
#leg2 = ax.legend(handles=patches2,fontsize=10,loc='lower left',title="Total CI",title_fontsize=10,frameon=False)


#plt.gca().add_artist(leg1)
plt.savefig(r'C:/Users/徐浩然/Desktop/MAP.png',dpi=600)
print(df)


plt.show()

