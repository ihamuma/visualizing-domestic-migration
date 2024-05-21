import pandas as pd
import numpy as np
import json
import os

with open('raw_data/stat_fi_response_data_2024-05-17_17-27-40.json') as f:
    data = json.load(f)

columns = [col['text'] for col in data['columns']]
data_points = [
    {**dict(zip(columns, d['key'])), 'Value': d['values'][0]}
    for d in data['data']
]

migration_between_regions_df = pd.DataFrame(data_points)

print(migration_between_regions_df.columns)

with open('raw_data/clean_mapping_stat_fi_domestic_migration_data.json') as mf:
    mapping_dict = json.load(mf)

migration_between_regions_df['Region of arrival descriptive'] = migration_between_regions_df['Region of arrival'].apply(lambda x: mapping_dict['Region of arrival'].get(x, np.nan))
migration_between_regions_df['Region of departure descriptive'] = migration_between_regions_df['Region of departure'].apply(lambda x: mapping_dict['Region of departure'].get(x, np.nan))
migration_between_regions_df['Origin descriptive'] = migration_between_regions_df['Origin'].apply(lambda x: mapping_dict['Origin'].get(x, np.nan))

print(migration_between_regions_df.columns)
print(migration_between_regions_df.head())