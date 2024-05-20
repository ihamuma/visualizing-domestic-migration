import pandas as pd
import requests
import json
import os

def stat_fi_api_request(url, json_query):
    response = requests.post(url, json=json_query)

    if response.status_code == 200:
        print('API request was successful.')
        data = response.json()
        return data
    else:
        print(f"API request failed with status code {response.status_code}")
        print(response.text)
        return None

def write_to_json_file(data, file_name):
    file_path = os.path.join('raw_data', file_name)
    
    try:
        with open(file_path, 'w') as new_file:
            json.dump(data, new_file, indent=4)
        return f"Data has been written to {file_path}"
    except Exception as e:
        return 'Writing to file failed due to Exception ' + str(e)
    
def create_dataframe_from_stat_fi_format(json_data):
    columns = [col['text'] for col in json_data['columns']]
    data_points = [
        {**dict(zip(columns, d['key'])), 'Value': d['values'][0]}
        for d in json_data['data']
    ]

    return pd.DataFrame(data_points)
