import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from scipy.stats import t

# 创建一个网格
n = 100  # 网格点数
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)
X, Y = np.meshgrid(x, y)

# 计算PDF值
df = 3  # 自由度
pdf_values = t.pdf(np.sqrt(X**2 + Y**2) / np.sqrt(df), df) / (np.pi * df)

# 创建3D PDF图
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# 绘制3D图
ax.plot_surface(X, Y, pdf_values, cmap='viridis')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('PDF Value')
ax.set_title('Student Copula 3D PDF Plot')

# 显示图形
plt.show()
