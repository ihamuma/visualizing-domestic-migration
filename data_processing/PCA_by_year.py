import pandas as pd
import os

# Transform migration data to allow for only numerical values in cells, enabling PCA

migration_df = pd.read_parquet('raw_data/migration.parquet')

migration_df.loc[:, 'new_column'] = migration_df.apply(lambda row: row['Region of arrival'] + '-' + 
                                                                   row['Region of departure']+ '-' + 
                                                                   row['Origin'] + '-' + 
                                                                   row['Sex'] + '-' +  
                                                                   row['Age'], axis=1)

transformed_migration_df = migration_df.pivot_table(index='Year', columns='new_column', values='Value')
transformed_migration_df = transformed_migration_df.reset_index()

migration_file_path = os.path.join('processed_data', 'migration_transformed_pca_by_year.parquet')
transformed_migration_df.to_parquet(migration_file_path, engine='pyarrow')