import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap

pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)

df = pd.read_excel(r'C:/Users/徐浩然/Desktop/psss.xlsx',sheet_name='209209064_1516_1516adjust')  # 以pandas库的read_csv函数读取csv文件
print(df.head())
plt.rcParams['font.sans-serif']=['Microsoft YaHei']
plt.rcParams['font.size'] = 12
plt.rcParams['axes.unicode_minus'] = False

clist=['#EAF6DE','#B3D0AB',"#77A67E",'#527D5D','#19422A']
# clist=['#F1F5C9','#CEDEA2','#98B574','#678B4A','#435C28']
CC = LinearSegmentedColormap.from_list('Blues',clist,N=256)
C='#527D5D'



corrmat = df.corr()
f, ax = plt.subplots(figsize=(14, 10))
sns.heatmap(corrmat,square=True,cmap=CC,vmin=0,vmax=0.3)
# h=plt.contourf(corrmat)
plt.savefig(r'C:/Users/徐浩然/Desktop/轻食Figure/Heatmap.png',dpi=400)

plt.figure(figsize=(12, 12))

plt.subplot(3, 3, 1)  # subplot函数划分了4行3列的画布区域，第三个参数表示图像在其中的位置
sns.boxplot(x='性别', data=df,color=C)

plt.subplot(3, 3, 2)
sns.boxplot(x='年龄段', data=df,color=C)

plt.subplot(3, 3, 3)
sns.boxplot(x='学历', data=df,color=C)

plt.subplot(3, 3, 4)
sns.boxplot(x='职业', data=df,color=C)

plt.subplot(3, 3, 5)
sns.boxplot(x='可支配收入', data=df,color=C)

plt.subplot(3, 3, 6)
sns.boxplot(x='月总消费', data=df,color=C)

plt.subplot(3, 3, 7)
sns.boxplot(x='BMI', data=df,color=C)

plt.subplot(3, 3, 8)
sns.boxplot(x='愿意消费的金额', data=df,color=C)

plt.subplot(3, 3, 9)
sns.boxplot(x='购买方式', data=df,color=C)

plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=0.275)
plt.savefig(r'C:/Users/徐浩然/Desktop/轻食Figure/box.png',dpi=400)

plt.show()