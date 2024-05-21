import pandas as pd

# Script for transposing incoming migration data for a single region to allow for only numerical values in cells.

migration_df = pd.read_parquet('raw_data/migration.parquet')

mk01_arrivals_df = migration_df[migration_df['Region of arrival'] == 'MK01']

mk01_arrivals_df.loc[:, 'new_column'] = mk01_arrivals_df.apply(lambda row: row['Region of departure'] + '-' + 
                                          row['Origin'] + '-' + row['Sex'] + '-' +  row['Age'], axis=1)
unique_new_columns = mk01_arrivals_df['new_column'].unique()

mk01_transformed = pd.DataFrame()
mk01_transformed['Year'] = mk01_arrivals_df['Year'].unique()

for column_name in unique_new_columns:
    helper_df = mk01_arrivals_df.loc[mk01_arrivals_df['new_column'] == column_name]
    helper_df = helper_df.rename(columns=({'Value': column_name}))
    helper_df = helper_df[['Year', column_name]]
    mk01_transformed = mk01_transformed.merge(helper_df, how='left', on='Year')

print(len(mk01_transformed.columns))
print(mk01_transformed.describe())
print(mk01_transformed.head())