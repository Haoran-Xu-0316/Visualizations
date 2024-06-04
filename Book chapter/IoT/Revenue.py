import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

plt.rcParams['axes.unicode_minus'] = False  # 解决负号不显示的问题

pd.set_option('display.unicode.east_asian_width', True)
sns.set_theme(context={'figure.figsize':[10, 5]}, style='ticks', palette='deep', font='Arial', font_scale=1, color_codes=True, rc=None)

df = pd.read_excel(r'C:\Users\徐浩然\Desktop\材料\statistic\IoT Rev.xlsx', sheet_name='Sheet1',index_col=0)

print(df)

sns.relplot(data=df,x="Rev", y="CAGR", hue='Category',sizes=(40, 400), alpha=.5, palette="muted", height=6)
plt.show()