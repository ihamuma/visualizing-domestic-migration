import pandas as pd


def edges_from_df(df):
    edges = []

    for index, row in df.iterrows():
        region_of_arrival = row['Region of arrival']
        region_of_departure = row['Region of departure']
        value = row['Value']

        edges.append((region_of_arrival, region_of_departure, value))

    return edges
