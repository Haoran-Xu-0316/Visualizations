
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

#全局设置-----------------------------------------------------------------------------------------------------------------
plt.rcParams['font.sans-serif'] = ['Palatino Linotype']
# plt.rcParams["font.weight"] = "bold"
plt.rcParams['font.size'] = 10
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['lines.linewidth'] = 1
plt.rcParams['axes.xmargin'] = 0

pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
plt.rcParams['axes.labelsize'] = 0


r=pd.read_excel(r'C:\Users\徐浩然\Desktop\P4 Data\Sectordata.xlsx', sheet_name='Sheet1',index_col=0,parse_dates=[0])
nr=(r-np.mean(r))/np.std(r)
# nr=np.log(r/r.shift(1))
plt.figure(figsize=(10,5))
sns.lineplot(nr,palette='viridis',dashes=False,legend=True)
# sns.move_legend()
plt.legend(frameon=False,loc='lower right',ncol=2)
# plt.legend((line1, line2), ['1st', '2nd']loc=0,
#            title='legends', ncol=2, markerfirst=False,
#            numpoints=2, frameon=True, fancybox=True,
#            facecolor='gray', edgecolor='r', shadow=True)

plt.tight_layout()
plt.show()