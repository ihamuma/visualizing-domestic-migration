def check_dataframes_for_unidentical_columns(dict_of_dfs, reference_df_key=None):
    """Returns dict in dict of differences between the columns one of the dataframes in a provided dict and all the others.
    Can specify key for reference df if needed or automatically use first one."""
    
    reference_key = reference_df_key if reference_df_key else next(iter(dict_of_dfs))
    ref_cols = dict_of_dfs[reference_key].columns
    unmatching_columns = {}

    for name, df in dict_of_dfs.items():
        if not df.columns.equals(ref_cols):
            unmatching_columns[name] = diff_columns(ref_cols, df.columns)

    return {'reference_dataframe': reference_key,
            'dataframes_with_unmatching_columns': unmatching_columns}

def diff_columns(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    diff1 = set1 - set2
    diff2 = set2 - set1
    return diff1, diff2