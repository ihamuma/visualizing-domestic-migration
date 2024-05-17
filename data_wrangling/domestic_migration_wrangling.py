import pandas as pd
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

print(migration_between_regions_df)