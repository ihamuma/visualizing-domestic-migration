from matplotlib.font_manager import fontManager, FontProperties
from sklearn import decomposition
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

year = '2021'
origins = ('21', '22')

pca_by_region_df = pd.read_parquet(f'processed_data/pca_by_region_{origins[0]}-{origins[1]}_{year}.parquet')

regions = pca_by_region_df['Region'].to_list()
values = pca_by_region_df.drop(columns=['Region']).values.tolist()

pca = decomposition.PCA(n_components=2)
pca.fit(values)
X = pca.transform(values)

x_coords = [x[0] for x in X]
y_coords = [y[1] for y in X]

sns.set(style="darkgrid")
plt.rcParams['grid.color'] = 'white'
plt.rcParams['axes.unicode_minus'] = False

sns.scatterplot(x=x_coords, y=y_coords)

font_path = 'fonts/cmunrm.ttf'
fontManager.addfont(font_path)

prop = FontProperties(fname=font_path)

for i, (x, y) in enumerate(zip(x_coords, y_coords)):
    plt.text(x, y, str(regions[i]), color='red', fontsize=8, fontproperties=prop)

plt.xticks(fontproperties=prop)
plt.yticks(fontproperties=prop)
plt.title(f'Domestic Migration by Region, Origins {origins[0]}, {origins[1]} - {year} (PCA)', fontproperties=prop)

plt.savefig(f'visualization/results/PCA Migration by Region, Incoming {origins[0]}-{origins[1]} {year}.png')

plt.show()