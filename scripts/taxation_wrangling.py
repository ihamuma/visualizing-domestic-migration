import pandas as pd
import os

import dataframe_helper

folder_path = 'raw_data/taxation_records_2011-2022'

dfs = {}
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        file_path = os.path.join(folder_path, filename)
        df = pd.read_csv(file_path, encoding='ISO-8859-1', sep=';')
        key = os.path.splitext(filename)[0] + '_df'
        dfs[key] = df

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

unmatching_columns = dataframe_helper.check_dataframes_for_unidentical_columns(
    dict_of_dfs=dfs, reference_df_key='taxation_2011_df')

assert unmatching_columns['dataframes_with_unmatching_columns'] == {}

all_taxation_years_df = pd.concat(dfs, ignore_index=True)
all_taxation_years_df = all_taxation_years_df.sort_values(
    by=['year', 'municipality'], ascending=[True, True])
all_taxation_years_df = all_taxation_years_df.astype({'year': 'int64',
                                                      'business_id': 'string',
                                                      'name': 'string',
                                                      'municipality': 'string'})
columns_to_float = ['taxable_income',
                    'taxes_charged',
                    'advance_tax_payment',
                    'tax_return',
                    'residual_tax']
all_taxation_years_df = dataframe_helper.convert_columns_to_float(
    all_taxation_years_df, columns_to_float)

print(all_taxation_years_df.shape)
print(all_taxation_years_df.dtypes)
print(all_taxation_years_df)
