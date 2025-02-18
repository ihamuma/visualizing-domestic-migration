from tqdm import tqdm
import pandas as pd
import requests
import json
import os


def get_migration_data(url, json_query, age_ranges):
    migration_dfs = []

    for age in tqdm(age_ranges):
            age_query = form_age_query(age)
            json_query["query"].append(age_query)
            json_data = stat_fi_api_request(url, json_query)
            json_query["query"].pop()
            migration_df = create_dataframe_from_stat_fi_format(json_data)
            migration_dfs.append(migration_df)
    
    return pd.concat(migration_dfs)


def form_age_query(age):
    return {
            "code": "Ikä",
            "selection": {
                 "filter": "item",
                 "values": [
                      f"{age}"
                    ]
                }
            } 


def get_employment_data(url, json_query):
     json_data = stat_fi_api_request(url, json_query)
     employment_df = create_dataframe_from_stat_fi_format(json_data)
     return employment_df


def stat_fi_api_request(url, json_query):
    response = requests.post(url, json=json_query)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"API request failed with status code {response.status_code}")
        print(response.text)
        return None


def create_dataframe_from_stat_fi_format(json_data):
    columns = [col['text'] for col in json_data['columns']]
    data_points = [
        {**dict(zip(columns, d['key'])), 'Value': d['values'][0]}
        for d in json_data['data']
    ]

    return pd.DataFrame(data_points)

def fix_dataframe_dtypes(df):
    if 'Origin' in df.columns:
        return df.astype({'Year': 'int64',
                          'Region of arrival': 'string',
                          'Region of departure': 'string',
                          'Origin': 'string',
                          'Sex': 'string',
                          'Age': 'string',
                          'Value': 'int64'
                        })
    else:
        return df.astype({'Year': 'int64',
                          'Area': 'string',
                          'Industry': 'string',
                          'Sex': 'string',
                          'Value': 'int64'})

def write_to_json_file(data, file_name):
    file_path = os.path.join('raw_data', file_name)
    
    try:
        with open(file_path, 'w') as new_file:
            json.dump(data, new_file, indent=4)
        return f"Data has been written to {file_path}"
    except Exception as e:
        return 'Writing to file failed due to Exception ' + str(e)


def print_df_details(df):
    print('Shape\n', df.shape)
    print('Columns\n', df.columns)
    print('Describe\n', df.describe())
    print('Head\n', df.head())
