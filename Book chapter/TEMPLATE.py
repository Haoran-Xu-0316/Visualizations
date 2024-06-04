import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

plt.rcParams['axes.unicode_minus'] = False  # 解决负号不显示的问题

pd.set_option('display.unicode.east_asian_width', True)
sns.set_theme(context={'figure.figsize':[10, 5]}, style='ticks', palette='deep', font='Arial', font_scale=1, color_codes=True, rc=None)

df = pd.read_excel(r'C:\Users\徐浩然\Desktop\分公司笔数20220101-20230101.xls', sheet_name='Sheet0',index_col=0)

print(df)

ax= sns.lineplot(data=df,dashes=False)
plt.xlabel("xxx")
plt.ylabel("number")

#绘制平行于 x 轴额度水平参考线
#plt.axhline(y, c, ls, lw, label)
#绘制垂直于 x 轴的参考区域
#plt.axvspan( xmin, xmax ,facecolor, alpha)



sns.move_legend(ax, "lower center",bbox_to_anchor=(0.5,1), ncol=5, title=None, frameon=False)
#plt.savefig(r'C:/Users/徐浩然/Desktop/figure.png',dpi=400)
plt.show()

