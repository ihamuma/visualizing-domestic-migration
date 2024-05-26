def decrypt_migration_column_name(column_name: str):
    split_values = column_name.split(sep='-', maxsplit=3)
    decrypted_dict = {
        'Region of departure': split_values[0],
        'Origin': split_values[1],
        'Sex': split_values[2],
        'Age': split_values[3]
    }
    return decrypted_dict



#print(decrypt_migration_column_name("MK02-11-1-0-17"))