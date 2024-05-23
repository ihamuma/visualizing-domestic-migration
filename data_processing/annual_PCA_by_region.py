from tqdm import tqdm
import pandas as pd
import os

# Script for transposing incoming migration data for all regions for a single year to allow for PCA.
year = '2021'

migration_df = pd.read_parquet('raw_data/migration.parquet')

migration_df = migration_df[migration_df['Year'] == int(year)]
migration_df = migration_df.drop(columns=['Year'])

regions = migration_df['Region of arrival'].unique()

all_regions = []
for region in tqdm(regions):
    region_arrivals = migration_df[(migration_df['Region of arrival'] == region)]
    region_arrivals = region_arrivals.groupby(['Region of arrival', 'Origin', 'Sex', 'Age'])['Value'].sum().reset_index()
    region_arrivals = region_arrivals.rename(columns={'Value': 'Arrivals'})

    region_departures = migration_df[(migration_df['Region of departure'] == region)]
    region_departures = region_departures.groupby(['Region of departure',  'Origin', 'Sex', 'Age'])['Value'].sum().reset_index()
    region_departures = region_departures.rename(columns={'Value': 'Departures'})

    region_net = region_arrivals.merge(region_departures, how='left', on=['Origin', 'Sex', 'Age'])
    region_net['Net migration'] = region_net.apply(lambda row: row['Arrivals'] - row['Departures'], axis=1)
    region_net = region_net.rename(columns={'Region of arrival': 'Region'})
    region_net = region_net.drop(columns=['Arrivals', 'Region of departure', 'Departures'])

    all_regions.append(region_net)

all_regions_df = pd.concat(all_regions)

all_regions_df.loc[:, 'new_column'] = all_regions_df.apply(lambda row: row['Origin'] + '-' + 
                                                                       row['Sex'] + '-' +  
                                                                       row['Age'], axis=1)

transformed_migration_df = all_regions_df.pivot_table(index='Region', columns='new_column', values='Net migration')
transformed_migration_df = transformed_migration_df.reset_index()
transformed_migration_df = transformed_migration_df.fillna(0)

pca_by_region_file_path = os.path.join('processed_data', f'migration_transformed_pca_by_region_{year}.parquet')
transformed_migration_df.to_parquet(pca_by_region_file_path, engine='pyarrow')