import pandas as pd

migration_df = pd.read_parquet('raw_data/migration.parquet')
employment_df = pd.read_parquet('raw_data/employment.parquet')
print(migration_df.dtypes)
print(employment_df.dtypes)