from stat_fi_api_helpers import stat_fi_api_request, create_dataframe_from_stat_fi_format
import stat_fi_queries
import pandas as pd

def get_migration_data(url, json_query, age_ranges):
    migration_dfs = []

    for age in age_ranges:
            age_query = form_age_query(age)
            json_query["query"].append(age_query)
            json_data = stat_fi_api_request(url, json_query)
            json_query["query"].pop()
            migration_df = create_dataframe_from_stat_fi_format(json_data)
            migration_dfs.append(migration_df)
    
    return pd.concat(migration_dfs)

def form_age_query(age):
    return {"code": "Ikä",
            "selection": {
                 "filter": "item",
                 "values": [
                      f"{age}"
                    ]
            }
        } 

migr_url = stat_fi_queries.migration_url
migr_query = stat_fi_queries.migration_query
migr_ages = stat_fi_queries.age_values["selection"]["values"]
migration_df = get_migration_data(migr_url, migr_query, migr_ages)

def get_employment_data(url, json_query):
     json_data = stat_fi_api_request(url, json_query)
     employment_df = create_dataframe_from_stat_fi_format(json_data)
     return employment_df

empl_url = stat_fi_queries.employment_url
empl_query = stat_fi_queries.employment_query
employment_df = get_employment_data(empl_url, empl_query)

def print_df_details(df):
    print('Shape\n', df.shape)
    print('Columns\n', df.columns)
    print('Describe\n', df.describe())
    print('Head\n', df.head())

print_df_details(migration_df)
print_df_details(employment_df)
