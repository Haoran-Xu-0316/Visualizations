import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd

# 读取数据
file = "us_states_hexgrid.geojson.json"
geoData = gpd.read_file(file)
geoData['centroid'] = geoData['geometry'].apply(lambda x: x.centroid)

mariageData = pd.read_csv("State_mariage_rate.csv")
geoData['state'] = geoData['google_name'].str.replace(' \(United States\)', '')

geoData = geoData.set_index('state').join(mariageData.set_index('state'))

# 初始化
fig, ax = plt.subplots(1, figsize=(6, 4))

# 绘图
geoData.plot(
    ax=ax,
    column="y_2015",
    cmap="BuPu",
    norm=plt.Normalize(vmin=2, vmax=13),
    edgecolor='black',
    linewidth=.5
);

# 不显示坐标轴
ax.axis('off')

# 标题, 副标题,作者
ax.annotate('Mariage rate in the US', xy=(10, 340), xycoords='axes pixels', horizontalalignment='left',
            verticalalignment='top', fontsize=14, color='black')
ax.annotate('Yes, people love to get married in Vegas', xy=(10, 320), xycoords='axes pixels',
            horizontalalignment='left', verticalalignment='top', fontsize=11, color='#808080')
ax.annotate('xiao F', xy=(400, 0), xycoords='axes pixels', horizontalalignment='left', verticalalignment='top',
            fontsize=8, color='#808080')

# 每个网格
for idx, row in geoData.iterrows():
    ax.annotate(
        s=row['iso3166_2'],
        xy=row['centroid'].coords[0],
        horizontalalignment='center',
        va='center',
        color="white"
    )

# 添加颜色
sm = plt.cm.ScalarMappable(cmap='BuPu', norm=plt.Normalize(vmin=2, vmax=13))
# fig.colorbar(sm, orientation="horizontal", aspect=50, fraction=0.005, pad=0);

# 显示
plt.show()