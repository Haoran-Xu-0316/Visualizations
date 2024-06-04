#Number of IoT connected devices 2020-2030, by region
#Number of Internet of Things (IoT) connected devices from 2020 to 2030 (in millions), by region

from typing import List, Tuple

import matplotlib.cm as mcm
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib.ticker import PercentFormatter

plt.rcParams['axes.unicode_minus'] = False  # 解决负号不显示的问题

pd.set_option('display.unicode.east_asian_width', True)
sns.set_theme(style='ticks', palette='deep', font='Arial', font_scale=1, color_codes=True, rc=None)

pd.set_option('display.unicode.east_asian_width', True)
df = pd.read_excel(r'C:\Users\徐浩然\Desktop\材料\statistic\statistic_id1194677_number-of-iot-connected-devices-2020-2030-by-region.xlsx', sheet_name='Data',index_col=0)
bar=df.plot.bar(stacked=True,width=0.8, linewidth=0, figsize=(15, 7),edgecolor="Black",  clip_on=False,cmap='copper')
bar.legend(frameon=False,bbox_to_anchor=(1,0.99))
#bar.margins(x=0,y=0)
bar.xaxis.set_tick_params(rotation=30)

#bar.spines['top'].set_visible(False)
#bar.spines['bottom'].set_visible(False)

plt.tight_layout()
plt.savefig(r'C:/Users/徐浩然/Desktop/region.png',dpi=400)
plt.show()