import pandas as pd


def defi_years_per_block(data_frame, year_range):

    data_frame_cp = data_frame.copy()

    for (first_row, last_row), year in year_range.items():
        data_frame_cp.loc[first_row:last_row, 'Year'] = year

    return data_frame_cp


def verify_and_switch_datatypes(data_clean, assigned_types):

    # Verificar los tipos de datos actuales y convertir si es necesario
    for column, assigned_types in assigned_types.items():
        currently_type = data_clean[column].dtype
        
        if currently_type != assigned_types:
            try:
                data_clean[column] = data_clean[column].astype(assigned_types)
                print(f"Column '{column}' converted from {currently_type} a {assigned_types}.")
            except Exception as e:
                print(f"No se pudo convertir la columna '{column}' a {assigned_types}: {e}")
        else:
            print(f"Column '{column}' is currently right typed as ({currently_type}).")
    
    return data_clean