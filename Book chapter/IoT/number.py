#Number of IoT connected devices worldwide 2019-2021, with forecasts to 2030
#Number of Internet of Things (IoT) connected devices worldwide from 2019 to 2021, with forecasts from 2022 to 2030 (in billions)

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

plt.rcParams['axes.unicode_minus'] = False  # 解决负号不显示的问题

pd.set_option('display.unicode.east_asian_width', True)
sns.set_theme(context={'figure.figsize':[10, 5]}, style='ticks', palette='deep', font='Arial', font_scale=1, color_codes=True, rc=None)

df = pd.read_excel(r'C:\Users\徐浩然\Desktop\材料\statistic\statistic_id1183457_number-of-iot-connected-devices-worldwide-2019-2021-with-forecasts-to-2030 .xlsx', sheet_name='Data new')
print(df)
ax=sns.barplot(df,x='Time',y='values',color='#FFAF6F')
ax.set_xlabel(None)
ax.set_ylabel(None)
ax.xaxis.set_tick_params(rotation=30)
ax.set_ylabel('billions')

plt.bar_label(ax.containers[0])
plt.savefig(r'C:/Users/徐浩然/Desktop/IoTnumbernew.png',dpi=400)
plt.show()