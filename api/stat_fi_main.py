from stat_fi_api_helpers import get_migration_data, get_employment_data
import stat_fi_queries
import os

migration_file_path = os.path.join('raw_data', 'migration.parquet')
employment_file_path = os.path.join('raw_data', 'employment.parquet')

if not os.path.isfile(migration_file_path):
    migr_url = stat_fi_queries.migration_url
    migr_query = stat_fi_queries.migration_query
    migr_ages = stat_fi_queries.age_values["selection"]["values"]

    migration_df = get_migration_data(migr_url, migr_query, migr_ages)
    migration_df.to_parquet(migration_file_path, engine='pyarrow')

if not os.path.isfile(employment_file_path):
    empl_url = stat_fi_queries.employment_url
    empl_query = stat_fi_queries.employment_query
    
    employment_df = get_employment_data(empl_url, empl_query)
    employment_df.to_parquet(employment_file_path, engine='pyarrow')



