from matplotlib.font_manager import fontManager, FontProperties
from sklearn import decomposition
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

pca_by_year_df = pd.read_parquet('processed_data/pca_by_year.parquet')
print(pca_by_year_df.describe())
print(pca_by_year_df.head())

years = pca_by_year_df['Year'].to_list()
values = pca_by_year_df.drop(columns=['Year']).values.tolist()

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
    plt.text(x, y, str(years[i]), color='red', fontsize=8, fontproperties=prop)

plt.xticks(fontproperties=prop)
plt.yticks(fontproperties=prop)
plt.title('Domestic Migration 2002-2022 (PCA)', fontproperties=prop)

plt.savefig('visualization/results/PCA Migration 2002-2022.png', dpi=300)

plt.show()