import pandas as pd
import os

# Script for transposing incoming migration data for all regions for a single year to allow for PCA.
year = '2021'

migration_df = pd.read_parquet('raw_data/migration.parquet')

migration_df = migration_df[migration_df['Year'] == int(year)]
migration_df = migration_df.drop(columns=['Year'])

migration_df.loc[:, 'new_column'] = migration_df.apply(lambda row: row['Region of departure'] + '-' +
                                                       row['Origin'] + '-' +
                                                       row['Sex'] + '-' +
                                                       row['Age'], axis=1)

print(migration_df.describe())
print(migration_df.head())

transformed_migration_df = migration_df.pivot_table(
    index='Region of arrival', columns='new_column', values='Value')
transformed_migration_df = transformed_migration_df.reset_index()
transformed_migration_df = transformed_migration_df.fillna(0)
print(transformed_migration_df.describe())
print(transformed_migration_df.head())

pca_by_region_file_path = os.path.join(
    'processed_data', f'migration_transformed_incoming_pca_by_region_{year}.parquet')
transformed_migration_df.to_parquet(pca_by_region_file_path, engine='pyarrow')
