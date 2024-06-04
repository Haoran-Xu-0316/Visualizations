import math
# import proplot
from datetime import datetime

import matplotlib.dates as dates
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.interpolate as sci
import scipy.optimize as sco
import seaborn as sns


plt.rcParams['font.sans-serif'] = ['Palatino Linotype']
# plt.rcParams["font.weight"] = "bold"
plt.rcParams['font.size'] = 12
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['lines.linewidth'] = 1
plt.rcParams['axes.xmargin'] = 0

_, ax = plt.subplots(figsize=(10, 10))
corr = pd.read_excel(r'C:\Users\徐浩然\Desktop\P4 Data\Table.xlsx', sheet_name='Matrix', index_col=0)
cmap = sns.diverging_palette(220, 10, as_cmap=True)
_ = sns.heatmap(
    corr,
    cmap=cmap,
    square=True,
    ax=ax,
    annot=True,
    cbar_kws={'shrink':0.78},
    annot_kws={'fontweight': 'bold'})


plt.tight_layout()
plt.savefig(r'C:/Users/徐浩然/Desktop/P4 Figs/cor.png',dpi=300)
plt.show()
