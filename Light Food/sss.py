
import matplotlib.pyplot as plt

price = [11,9,9,12,11,10,10,1]

plt.rcParams['font.sans-serif'] =['Simhei']
plt.rcParams['axes.unicode_minus'] = False

fig, ax = plt.subplots(figsize=(8,5))
plt.barh(range(8), price, align = 'center',color='steelblue', alpha = 0.8)

plt.xlabel('运输时间（天）')
plt.ylabel('商品')

plt.title('每种商品的运输时间')

plt.yticks(range(8),['蜂蜜','家具B','家具A','纸盘','药品','香烟','苹果','榴莲'])

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
plt.savefig(r'C:/Users/徐浩然/Desktop/box.png',dpi=400)
plt.show()
