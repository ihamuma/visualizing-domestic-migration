import pandas as pd
import os

year = '2022'

migration_df = pd.read_parquet('raw_data/migration.parquet')

migration_df = migration_df[migration_df['Year'] == int(year)].reset_index(drop=True)
migration_df = migration_df.drop(columns=['Year'])

migration_df = migration_df.groupby(['Region of arrival', 'Region of departure'])['Value'].sum().reset_index()

pca_by_region_file_path = os.path.join('processed_data', f'directional_graph_{year}.parquet')
migration_df.to_parquet(pca_by_region_file_path, engine='pyarrow')