from .stat_fi_api_helpers import get_migration_data, get_employment_data
from .stat_fi_queries import migration_url, migration_query, age_values, employment_url, employment_query
import os

def verify_and_create_files():
    migration_file_path = os.path.join('raw_data', 'migration.parquet')
    employment_file_path = os.path.join('raw_data', 'employment.parquet')

    if not os.path.isfile(migration_file_path):
        print('No migration data file found. Creating API requests.')

        migration_ages = age_values["selection"]["values"]

        migration_df = get_migration_data(migration_url, migration_query, migration_ages)
        migration_df.to_parquet(migration_file_path, engine='pyarrow')

        print(f'Migration data successfully written to {migration_file_path}')
    else:
        print(f'Migration data file found at {migration_file_path}')

    if not os.path.isfile(employment_file_path):
        print('No migration data file found. Creating API request.')
        
        employment_df = get_employment_data(employment_url, employment_query)
        employment_df.to_parquet(employment_file_path, engine='pyarrow')

        print(f'Employment data successfully written to {employment_file_path}')
    else:
        print(f'Employment data file found at {employment_file_path}')