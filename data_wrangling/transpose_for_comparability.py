import pandas as pd

migration_df = pd.read_parquet('raw_data/migration.parquet')

mk01_arrivals_df = migration_df[migration_df['Region of arrival'] == 'MK01']

mk01_arrivals_df.loc[:, 'new_column'] = mk01_arrivals_df.apply(lambda row: row['Region of departure'] + '-' + 
                                          row['Origin'] + '-' + row['Sex'] + '-' +  row['Age'], axis=1)
unique_new_columns = mk01_arrivals_df['new_column'].unique()
value_counts =  mk01_arrivals_df['new_column'].value_counts()
#print(value_counts)

test_df = pd.DataFrame()
test_df['Year'] = mk01_arrivals_df['Year'].unique()
test_df_2 = mk01_arrivals_df.loc[mk01_arrivals_df['new_column'] == 'MK02-11-1-0-17']
test_df_2 = test_df_2[{'Year', 'Value', 'new_column'}]
test_df_2 = test_df_2.rename(columns=({'Value': 'MK02-11-1-0-17'}))
test_df_2 = test_df_2[{'Year', 'MK02-11-1-0-17'}]
test_df = test_df.merge(test_df_2, how='left', on='Year')
print(test_df.head())

# Either:
# Trust ordering of Years. Trust adding values to it won't fuck around with the order of the values.
# Or:
# Separate each unique 'new_column' into its own DF.
# Merge with test_df on Year.
# Rename 'Value' to unique 'new_column'
# 
# Both need to be repeated 1152 times. wth to do?
#
# No questions asked, merging seems like the safer option in order to preserve Year-Value linkage!
# Will be one hell of a computation-intensive for-loop, but wth else to do at this point :)