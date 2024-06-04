import circlify
import matplotlib.pyplot as plt

# 创建画布, 包含一个子图
fig, ax = plt.subplots(figsize=(14, 14))

# 标题
ax.set_title('Repartition of the world population')

# 移除坐标轴
ax.axis('off')

# 人口数据
data = [{'id': 'World', 'datum': 6964195249, 'children': [
    {'id': "North America", 'datum': 450448697,
     'children': [
         {'id': "United States", 'datum': 308865000},
         {'id': "Mexico", 'datum': 107550697},
         {'id': "Canada", 'datum': 34033000}
     ]},
    {'id': "South America", 'datum': 278095425,
     'children': [
         {'id': "Brazil", 'datum': 192612000},
         {'id': "Colombia", 'datum': 45349000},
         {'id': "Argentina", 'datum': 40134425}
     ]},
    {'id': "Europe", 'datum': 209246682,
     'children': [
         {'id': "Germany", 'datum': 81757600},
         {'id': "France", 'datum': 65447374},
         {'id': "United Kingdom", 'datum': 62041708}
     ]},
    {'id': "Africa", 'datum': 311929000,
     'children': [
         {'id': "Nigeria", 'datum': 154729000},
         {'id': "Ethiopia", 'datum': 79221000},
         {'id': "Egypt", 'datum': 77979000}
     ]},
    {'id': "Asia", 'datum': 2745929500,
     'children': [
         {'id': "China", 'datum': 1336335000},
         {'id': "India", 'datum': 1178225000},
         {'id': "Indonesia", 'datum': 231369500}
     ]}
]}]

# 使用circlify()计算, 获取圆的大小, 位置
circles = circlify.circlify(
    data,
    show_enclosure=False,
    target_enclosure=circlify.Circle(x=0, y=0, r=1)
)

lim = max(
    max(
        abs(circle.x) + circle.r,
        abs(circle.y) + circle.r,
    )
    for circle in circles
)
plt.xlim(-lim, lim)
plt.ylim(-lim, lim)

for circle in circles:
    if circle.level != 2:
        continue
    x, y, r = circle
    ax.add_patch(plt.Circle((x, y), r, alpha=0.5, linewidth=2, color="lightblue"))

for circle in circles:
    if circle.level != 3:
        continue
    x, y, r = circle
    label = circle.ex["id"]
    ax.add_patch(plt.Circle((x, y), r, alpha=0.5, linewidth=2, color="#69b3a2"))
    plt.annotate(label, (x, y), ha='center', color="white")

for circle in circles:
    if circle.level != 2:
        continue
    x, y, r = circle
    label = circle.ex["id"]
    plt.annotate(label, (x, y), va='center', ha='center',
                 bbox=dict(facecolor='white', edgecolor='black', boxstyle='round', pad=.5))

plt.show()