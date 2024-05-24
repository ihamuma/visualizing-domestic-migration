from matplotlib.font_manager import fontManager, FontProperties
from sammon_mapping.sammon import sammon
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

year = '2019'

sammon_by_year_df = pd.read_parquet(f'processed_data/pca_by_year.parquet')

years = sammon_by_year_df['Year'].to_numpy()
values = sammon_by_year_df.drop(columns=['Year']).to_numpy()

X = sammon(values, 2)

x_coords = [x[0] for x in X[0]]
y_coords = [y[1] for y in X[0]]

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
plt.title(f'Domestic Migration 2002-2022 (Sammon)', fontproperties=prop)

plt.savefig(f'visualization/results/Sammon Migration by Year.png', dpi=300)

plt.show()