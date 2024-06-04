import matplotlib.pyplot as plt
import squarify

plt.rcParams['font.sans-serif'] = ['Arial']
from pylab import mpl

mpl.rcParams['font.size'] = 12
plt.figure(figsize=(12,5))
labels = ['BYD', 'SAIC', 'Tesla', 'Dongfeng','Geely','GAC','Changan','Chery','JAC','FAW','Others']
sizes = [27.0, 15.4, 10.3, 7.3,4.8,4.5,4.1,3.6,2.9,2.5,17.6]
c=plt.get_cmap("coolwarm")

cmap=[c(1),c(0.2),c(0.3),c(0.4),c(0.5),c(0.55),c(0.6),c(0.7),c(0.8),c(0.9),c(0.1),]
l =  ['27.0%', '15.4%', '10.3%', '7.3%','4.8%','4.5%','4.1%','3.6%','2.9%','2.5%','17.6%']
#color = ['red', 'green', 'blue', 'orange']
squarify.plot(sizes, label = labels, pad = False, value=l,alpha=0.8,edgecolor='black',linewidth=1,color=cmap)
plt.axis('off')
plt.savefig(r'C:/Users/徐浩然/Desktop/Tree.png',dpi=400)
plt.tight_layout()
plt.show()
