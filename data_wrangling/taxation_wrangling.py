import pandas as pd
import os

import dataframe_validator

folder_path = 'raw_data/taxation_records_2011-2022'

dfs = {}
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        file_path = os.path.join(folder_path, filename)
        df = pd.read_csv(file_path, encoding='ISO-8859-1', sep=';')
        key = os.path.splitext(filename)[0] + '_df'
        dfs[key] = df

unmatching_columns = dataframe_validator.check_dataframes_for_unidentical_columns(dict_of_dfs=dfs)
assert unmatching_columns['dataframes_with_unmatching_columns'] != {}

column_mapping = {'Verovuosi | Skatteår': 'year', 
                  'Y-tunnus | FO-nummer': 'business_id',
                  'Verovelvollisen nimi | Den skattskyldiges namn': 'name',
                  'Verotuskunta | Beskattningskommun': 'municipality',
                  'Verotettava tulo | Beskattningsbar inkomst': 'taxable_income',
                  'Maksuunpannut verot yhteensä | Debiterade skatter ': 'taxes_charged',
                  'Maksuunpannut verot yhteensä | Debiterade skatter sammanlagt': 'taxes_charged',
                  'Ennakot yhteensä | Förskott sammanlagt': 'advance_tax_payment',
                  'Veronpalautus | Skatteåterbäring': 'tax_return', 
                  'Jäännösvero | Kvarskatt': 'residual_tax'}

for name, df in dfs.items():
    df.rename(columns=column_mapping, inplace=True)

unmatching_columns = dataframe_validator.check_dataframes_for_unidentical_columns(dict_of_dfs=dfs, reference_df_key='taxation_2011_df')

assert unmatching_columns['dataframes_with_unmatching_columns'] == {}