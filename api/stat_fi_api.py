import pandas as pd
import requests

url = 'https://pxdata.stat.fi:443/PxWeb/api/v1/en/StatFin/muutl/statfin_muutl_pxt_11a5.px'
json_query = {
    "query": [
        {
            "code": "Tulomaakunta",
            "selection": {
                "filter": "item",
                "values": [
                    "SSS",
                    "MK01",
                    "MK02",
                    "MK04",
                    "MK05",
                    "MK06",
                    "MK07",
                    "MK08",
                    "MK09",
                    "MK10",
                    "MK11",
                    "MK12",
                    "MK13",
                    "MK14",
                    "MK15",
                    "MK16",
                    "MK17",
                    "MK18",
                    "MK19",
                    "MK21"
                ]
            }
        },
        {
            "code": "Lähtömaakunta",
            "selection": {
                "filter": "item",
                "values": [
                    "SSS",
                    "MK01",
                    "MK02",
                    "MK04",
                    "MK05",
                    "MK06",
                    "MK07",
                    "MK08",
                    "MK09",
                    "MK10",
                    "MK11",
                    "MK12",
                    "MK13",
                    "MK14",
                    "MK15",
                    "MK16",
                    "MK17",
                    "MK18",
                    "MK19",
                    "MK21"
                ]
            }
        },
        {
            "code": "Syntyperä",
            "selection": {
                "filter": "item",
                "values": [
                    "SSS",
                    "1",
                    "11",
                    "12",
                    "2",
                    "22",
                    "21"
                ]
            }
        }
    ],
    "response": {
        "format": "json-stat2"
    }
}

response = requests.post(url, json=json_query)

if response.status_code == 200:
    print("Request was successful.")
    data = response.json()
    print(pd.DataFrame(data))
else:
    print(f"Request failed with status code {response.status_code}")
    print(response.text)
