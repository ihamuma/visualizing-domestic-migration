import json
import os

with open('raw_data/migration_data_mapping_raw.json') as file:
    data = json.load(file)

value_text_mappings = {}

for variable in data['variables']:
    text = variable['text']
    values = variable['values']
    value_texts = variable['valueTexts']
    
    value_text_mapping = dict(zip(values, value_texts))
    
    value_text_mappings[text] = value_text_mapping

file_path = os.path.join('processed_data', 'migration_data_mapping.json')
with open(file_path, 'w') as json_file:
        json.dump(value_text_mappings, json_file, indent=4)