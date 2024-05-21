import json
import os

with open('raw_data/employment_data_mapping_raw.json') as file:
    data = json.load(file)

values = data['variables'][0]['values']
value_texts = data['variables'][0]['valueTexts']

value_text_mapping = dict(zip(values, value_texts))

file_path = os.path.join('raw_data', 'employment_data_mapping.json')
with open(file_path, 'w') as json_file:
        json.dump(value_text_mapping, json_file, indent=4)