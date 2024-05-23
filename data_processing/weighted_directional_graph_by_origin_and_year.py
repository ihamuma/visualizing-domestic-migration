import pandas as pd
import os

year = '2021'
origins = ('21', '22')

migration_df = pd.read_parquet('raw_data/migration.parquet')

migration_df = migration_df[migration_df['Origin'].isin(origins)]
migration_df = migration_df[migration_df['Year'] == int(year)].reset_index(drop=True)
migration_df = migration_df.drop(columns=['Year'])

migration_df = migration_df.groupby(['Region of arrival', 'Region of departure'])['Value'].sum().reset_index()

pca_by_region_file_path = os.path.join('processed_data', f'directional_graph_{origins[0]}-{origins[1]}_{year}.parquet')
migration_df.to_parquet(pca_by_region_file_path, engine='pyarrow')