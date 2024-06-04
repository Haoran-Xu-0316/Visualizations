

import geopandas
import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import font_manager
from matplotlib.colors import LinearSegmentedColormap

plt.rcParams['font.sans-serif']=['Microsoft YaHei']

data=[0.4270792134820076, 0.4475347465064742, 0.48565009627290223, 0.4623174349132963, 0.45674859682217817, 0.4664831611635802, 0.45815952507445296, 0.4416579028400702, 0.5172325786070099, 0.4711120340665695, 0.4841016956618482, 0.5040468111940802, 0.4822484086307299, 0.5160536069347011, 0.5377264219400197, 0.4634693580860069, 0.49320696192385516, 0.47654415299660474, 0.5076671923775771, 0.4758570092032124, 0.505285178380465, 0.47210844492360504, 0.4926628790163008, 0.5141840303450448, 0.4939356829482934]
plt.figure(figsize=(10,6))
plt.plot(data,color='#527D5D',marker='X')
plt.xticks(np.arange(0,26,5))
plt.xlabel('主题数目')
plt.ylabel('Coherence')

plt.savefig(r'C:/Users/徐浩然/Desktop/轻食Figure/qt折线.png',dpi=400)

# plt.ylim(0.325,0.525)
plt.show()