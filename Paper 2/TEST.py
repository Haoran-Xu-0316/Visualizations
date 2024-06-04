from matplotlib.collections import PolyCollection
import matplotlib.pyplot as plt
import numpy as np

# 生成示例时间序列数据
num_series = 12
x = np.linspace(0, 10, 100)
time_series_data = np.random.rand(100, num_series)  # 生成12个随机的时间序列数据

# 定义函数以创建多边形填充时间序列折线图下方的多边形顶点列表
def polygon_under_timeseries(x, y):
    verts = []
    for i in range(y.shape[1]):  # 遍历每一列数据
        verts.extend(list(zip(x, y[:, i])))
        verts.append((x[-1], 0))  # 添加每个时间序列数据的末尾点
        verts.append((x[0], 0))   # 添加每个时间序列数据的起始点
    return verts

# 创建3D图
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 预定义颜色列表
colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k', 'orange', 'purple', 'brown', 'pink', 'gray']

# 遍历每个时间序列数据，为每个时间序列创建一个PolyCollection对象，并将其添加到3D图中
for i in range(num_series):
    verts = [polygon_under_timeseries(x, time_series_data[:, i:i+1])]
    alpha = 0.5
    # (i + 1) / (num_series + 1)  # 设置透明度，范围从0.1到1
    poly = PolyCollection(verts, alpha=alpha, facecolors=colors[i % len(colors)])  # 使用预定义颜色
    zs = np.array([i] * len(verts))  # 创建一个与多边形集合数量相匹配的zs数组
    ax.add_collection3d(poly, zs=zs, zdir='y')

# 设置坐标轴标签和范围
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# 调整坐标轴ticks使其居中，并添加距离到ticks的间距
ax.set_xticks(np.arange(0, 11, 1))
ax.set_xticklabels(np.arange(0, 11, 1), rotation=45)
ax.xaxis.set_ticks_position('both')
ax.yaxis.set_ticks_position('both')
ax.zaxis.set_ticks_position('both')
ax.tick_params(axis='both', which='both', direction='inout', pad=0)  # 设置tick距离

# 设置坐标轴范围和ticks
ax.set_xlim(0, 10)
ax.set_ylim(0, num_series - 1)
ax.set_zlim(0, 1)

plt.show()
