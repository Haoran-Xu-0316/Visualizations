import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Set global settings
plt.rcParams['font.sans-serif'] = ['Palatino Linotype']
plt.rcParams['font.size'] = 12
plt.rcParams['axes.unicode_minus'] = False
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
plt.rcParams['axes.labelsize'] = 0

# Read data from Excel files
u = pd.read_excel('C:/Users/徐浩然/Desktop/P4 ESG/ReadData.xlsx', sheet_name='U', index_col=0, parse_dates=[0])
rt = pd.read_excel('C:/Users/徐浩然/Desktop/P4 ESG/ReadData.xlsx', sheet_name='rt', index_col=0, parse_dates=[0])

# Create subplots
f, ax = plt.subplots(10, 2, figsize=(18, 18), sharex=False, sharey=False)

# Set plot parameters
cmap = sns.color_palette("Spectral_r", as_cmap=True)
fill = True
clip = (-5, 5)
thresh = 0
levels = 15
cut = 20
size = 0.5

# Loop through subplots
for i in range(10):
    # Plot for the first column (y=rt.iloc[:, 11])
    sns.kdeplot(x=rt.iloc[:, i], y=rt.iloc[:, 10], cmap=cmap, fill=fill, clip=clip, cut=cut, thresh=thresh,
                levels=levels, ax=ax[i, 0])
    sns.scatterplot(x=rt.iloc[:, i], y=rt.iloc[:, 10], s=size, color='black', ax=ax[i, 0])
    ax[i, 0].axis('off')
    ax[i, 0].set(xlim=(-5, 5), ylim=(-5, 5))

    # Plot for the second column (y=rt.iloc[:, 12])
    sns.kdeplot(x=rt.iloc[:, i], y=rt.iloc[:, 11], cmap=cmap, fill=fill, clip=clip, cut=cut, thresh=thresh,
                levels=levels, ax=ax[i, 1])
    sns.scatterplot(x=rt.iloc[:, i], y=rt.iloc[:, 11], s=size, color='black', ax=ax[i, 1])
    ax[i, 1].axis('off')
    ax[i, 1].set(xlim=(-5, 5), ylim=(-5, 5))

# Save and show the plot
plt.tight_layout()
plt.savefig('C:/Users/徐浩然/Desktop/P4 Figs/counter.png', dpi=300)
plt.show()
