import matplotlib.pyplot as plt
import seaborn as sns
from pandas.plotting import parallel_coordinates

# 读取数据
data = sns.load_dataset('iris', data_home='seaborn-data', cache=True)

# 创建图表
parallel_coordinates(data, 'species', colormap=plt.get_cmap("Set2"))

# 显示
plt.show()