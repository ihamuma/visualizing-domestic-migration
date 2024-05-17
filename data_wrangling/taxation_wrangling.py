import pandas as pd
import os

folder_path = 'raw_data/taxation_records_2011-2022'

dfs = {}
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        file_path = os.path.join(folder_path, filename)
        df = pd.read_csv(file_path, encoding='ISO-8859-1', sep=';')
        key = os.path.splitext(filename)[0] + '_df'
        dfs[key] = df

reference_columns = dfs['taxation_2011_df'].columns

identical_columns = True

for name, df in dfs.items():
    if not df.columns.equals(reference_columns):
        identical_columns = False
        print(f'{name} does not have identical columns.')

if identical_columns:
    print('All dfs have identical columns.')
else:
    print('Not all dfs have identical columns.')

print('2016', dfs['taxation_2016_df'].columns)
print('2017', dfs['taxation_2017_df'].columns)