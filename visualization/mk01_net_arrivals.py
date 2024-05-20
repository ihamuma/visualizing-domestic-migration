import pandas as pd
import matplotlib.pyplot as plt

migration_df = pd.read_parquet('raw_data/migration.parquet', engine='pyarrow')
mk01_arrivals = migration_df[(migration_df['Region of arrival'] == 'MK01')]
mk01_arrivals = mk01_arrivals.groupby(['Year', 'Region of arrival'])['Value'].sum().reset_index()
mk01_arrivals = mk01_arrivals.rename(columns={'Value': 'Arrivals'})

mk01_departures = migration_df[(migration_df['Region of departure'] == 'MK01')]
mk01_departures = mk01_departures.groupby(['Year', 'Region of departure'])['Value'].sum().reset_index()
mk01_departures = mk01_departures.rename(columns={'Value': 'Departures'})

mk01_net = mk01_arrivals.merge(mk01_departures, how='left', on='Year')
mk01_net['Net gain'] = mk01_net.apply(lambda row: row['Arrivals'] - row['Departures'], axis=1)

plt.plot(mk01_net['Year'].astype('int'), mk01_net['Net gain'], marker='o')
plt.xlabel('Year')
plt.xticks(mk01_net['Year'][::2])
plt.ylabel('Net Migration')
plt.title('Net Migration - MK01 (Uusimaa)')
plt.grid(True)
plt.savefig('visualization/results/MK01 Net Migration.png')
plt.show()