import pandas as pd
import requests
import json
import os

import stat_fi_query
write_to_file = False

url = 'https://pxdata.stat.fi:443/PxWeb/api/v1/en/StatFin/muutl/statfin_muutl_pxt_11a5.px'

json_query = stat_fi_query.json_query

def stat_fi_api_request(url, json_query, write_to_file, file_name):
    response = requests.post(url, json=json_query)

    if response.status_code == 200:
        data = response.json()
        if write_to_file:
            return 'API request was successful. ' + write_to_file(data, file_name)
        return 'API request was successful.'
    else:
        return f"Request failed with status code {response.status_code}"

def write_to_json_file(data, file_name):
    file_path = os.path.join('raw_data', file_name)
    
    try:
        with open(file_path, 'w') as new_file:
            json.dump(data, new_file, indent=4)
        return f"Data has been written to {file_path}"
    except Exception as e:
        return 'Writing to file failed due to Excpetion ' + str(e)
