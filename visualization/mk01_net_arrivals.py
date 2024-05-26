from matplotlib.font_manager import fontManager, FontProperties
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

migration_df = pd.read_parquet('raw_data/migration.parquet', engine='pyarrow')
mk01_arrivals = migration_df[(migration_df['Region of arrival'] == 'MK01')]
mk01_arrivals = mk01_arrivals.groupby(['Year', 'Region of arrival'])['Value'].sum().reset_index()
mk01_arrivals = mk01_arrivals.rename(columns={'Value': 'Arrivals'})

mk01_departures = migration_df[(migration_df['Region of departure'] == 'MK01')]
mk01_departures = mk01_departures.groupby(['Year', 'Region of departure'])['Value'].sum().reset_index()
mk01_departures = mk01_departures.rename(columns={'Value': 'Departures'})

mk01_net = mk01_arrivals.merge(mk01_departures, how='left', on='Year')
mk01_net['Net gain'] = mk01_net.apply(lambda row: row['Arrivals'] - row['Departures'], axis=1)

sns.set(style="darkgrid")
plt.rcParams['axes.unicode_minus'] = False

font_path = 'fonts/cmunrm.ttf'
fontManager.addfont(font_path)

prop = FontProperties(fname=font_path)

plt.figure(figsize=(9, 5))
sns.lineplot(data=mk01_net, x='Year', y='Net gain', marker='o')

plt.xlabel('Year', fontproperties=prop)
plt.xticks(mk01_net['Year'][::2], fontproperties=prop)
plt.yticks(fontproperties=prop)
plt.ylabel('Net Migration', fontproperties=prop)
plt.title('Net Migration - MK01 (Uusimaa)', fontproperties=prop)

plt.savefig('visualization/results/MK01 Net Migration.png', dpi=300)
plt.show()