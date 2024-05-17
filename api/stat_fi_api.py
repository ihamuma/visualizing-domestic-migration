from datetime import datetime
import pandas as pd
import requests
import json
import os

import stat_fi_query

url = 'https://pxdata.stat.fi:443/PxWeb/api/v1/en/StatFin/muutl/statfin_muutl_pxt_11a5.px'

json_query = stat_fi_query.json_query

response = requests.post(url, json=json_query)

if response.status_code == 200:
    print("Request was successful.")
    data = response.json()

    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
    
    file_path = os.path.join('raw_data', f'stat_fi_response_data_{timestamp}.json')
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    
    print(f"Data has been written to {file_path}")
else:
    print(f"Request failed with status code {response.status_code}")
    print(response.text)