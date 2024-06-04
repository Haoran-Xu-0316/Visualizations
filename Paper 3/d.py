import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import multivariate_normal

# 定义均值和协方差矩阵
mean = np.array([0, 0])
covariance = np.array([[1, 0.5], [0.5, 1]])

# 创建一个网格
x, y = np.meshgrid(np.linspace(-3, 3, 500), np.linspace(-3, 3, 500))
pos = np.dstack((x, y))

# 计算二维正态分布的概率密度值
pdf_values = multivariate_normal.pdf(pos, mean=mean, cov=covariance)

# 绘制概率密度图像
plt.figure(figsize=(8, 8))
plt.contourf(x, y, pdf_values, cmap='viridis')
plt.colorbar()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('2D Gaussian Probability Density')
plt.show()



# 定义均值和协方差矩阵
mean = np.array([0, 0])
covariance = np.array([[1, 0.5], [0.5, 1]])

# 创建一个网格
x, y = np.meshgrid(np.linspace(-3, 3, 500), np.linspace(-3, 3, 500))
pos = np.dstack((x, y))

# 计算二维正态分布的概率密度值
pdf_values = multivariate_normal.pdf(pos, mean=mean, cov=covariance)

# 绘制三维概率密度图像
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(x, y, pdf_values, cmap='viridis')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('PDF Value')
ax.set_title('3D Gaussian Probability Density')

plt.show()
