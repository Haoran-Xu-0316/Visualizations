import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# 创建数据
my_count = ["France", "Australia", "Japan", "USA", "Germany", "Congo", "China", "England", "Spain", "Greece", "Marocco",
            "South Africa", "Indonesia", "Peru", "Chili", "Brazil"]
df = pd.DataFrame({
    "country": np.repeat(my_count, 10),
    "years": list(range(2000, 2010)) * 16,
    "value": np.random.rand(160)
})

# 创建网格
g = sns.FacetGrid(df, col='country', hue='country', col_wrap=4, )

# 添加曲线图
g = g.map(plt.plot, 'years', 'value')

# 面积图
g = g.map(plt.fill_between, 'years', 'value', alpha=0.2).set_titles("{col_name} country")

# 标题
g = g.set_titles("{col_name}")

# 总标题
plt.subplots_adjust(top=0.92)
g = g.fig.suptitle('Evolution of the value of stuff in 16 countries')

plt.tight_layout()
plt.savefig(r'C:/Users/徐浩然/Desktop/美赛Figure_Template\5232311.png',dpi=400)

plt.show()