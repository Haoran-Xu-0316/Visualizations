import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

plt.rcParams['axes.unicode_minus'] = False  # 解决负号不显示的问题
pd.set_option('display.unicode.east_asian_width', True)
sns.set_theme(style='ticks', palette='deep', font='Arial', font_scale=1, color_codes=True, rc=None)



df1 = pd.read_excel(r'C:\Users\徐浩然\Desktop\材料\statistic\statistic_id1194682_number-of-iot-connected-devices-worldwide-2019-2030-by-vertical.xlsx', sheet_name='Data',index_col=0)
df2 = pd.read_excel(r'C:\Users\徐浩然\Desktop\材料\statistic\statistic_id1194701_number-of-iot-connected-devices-worldwide-2019-2030-by-use-case.xlsx', sheet_name='Data',index_col=0)
df3 = pd.read_excel(r'C:\Users\徐浩然\Desktop\材料\statistic\statistic_id1194677_number-of-iot-connected-devices-2020-2030-by-region.xlsx', sheet_name='Data',index_col=0)
df4 = pd.read_excel(r'C:\Users\徐浩然\Desktop\材料\statistic\statistic_id1194688_number-of-iot-connected-devices-worldwide-2019-2030-by-communications-technology.xlsx', sheet_name='Data',index_col=0)


C='coolwarm'
fig, axs = plt.subplots(2,2,figsize=(40,12))
plt.subplots_adjust(left=0.1, bottom=0.11, right=0.8, top=0.88, wspace=0.55, hspace=0.17)
plt.ticklabel_format(axis="y", style='plain')
#-----------------------------------------------------------------------------------------------------------------------
#ax1
ax1=df1.plot.bar(stacked=True,width=0.8, linewidth=0, figsize=(23, 15),edgecolor="Black",  clip_on=False,cmap=C,fontsize=15,ax=axs[0][1])
ax1.set_ylabel('',fontsize=8)
ax1.legend(frameon=False,bbox_to_anchor=(1,1),fontsize=13,labelspacing=0.1)
ax1.xaxis.set_tick_params(rotation=30)

#ax2
ax2=df2.plot.bar(stacked=True,width=0.8, linewidth=0, figsize=(23, 15),edgecolor="Black",  clip_on=False,cmap=C,fontsize=15,ax=axs[1][1])
ax2.set_ylabel('',fontsize=8)
ax2.legend(frameon=False,bbox_to_anchor=(1,1),fontsize=13,labelspacing=0.1)
ax2.xaxis.set_tick_params(rotation=30)

#ax3

ax3=df3.plot.bar(stacked=True,width=0.8, linewidth=0, figsize=(23, 15),edgecolor="Black",  clip_on=False,cmap=C,fontsize=15,ax=axs[0][0])
ax3.set_ylabel('',fontsize=8)
ax3.legend(frameon=False,bbox_to_anchor=(1,1),fontsize=13,labelspacing=0.1)
ax3.xaxis.set_tick_params(rotation=30)

#ax4

ax4=df4.plot.bar(stacked=True,width=0.8, linewidth=0, figsize=(23, 15),edgecolor="Black",  clip_on=False,cmap=C,fontsize=15,ax=axs[1][0])
ax4.set_ylabel('',fontsize=8)
ax4.legend(frameon=False,bbox_to_anchor=(1,1),fontsize=13,labelspacing=0.1)
ax4.xaxis.set_tick_params(rotation=30)
#-----------------------------------------------------------------------------------------------------------------------

#plt.tight_layout()

plt.savefig(r'C:/Users/徐浩然/Desktop/United.png',dpi=500)
plt.show()
