import pandas as pd


def defi_years_per_block(data_frame, year_range):

    data_frame_cp = data_frame.copy()

    for (first_row, last_row), year in year_range.items():
        data_frame_cp.loc[first_row:last_row, 'Year'] = year

    return data_frame_cp


def verify_and_switch_datatypes(data_clean_years, column_name, assigned_types):
    column_name = data_clean_years[column_name]
    currently_type = data_clean_years[column_name].dtype
    assigned_types = {'Province': str,
                      'Assault': int,
                      'physical injuries':int,
                      'small_robberies':int,
                      'robberies_with_force':int,
                      'robberies_force_vehicles': int, 
                      'hard_robbvehicles':int, 
                      'robberies_force_homes':int, 
                      'robberies_force_establishments':int, 
                      'robberies_violence_intimidation':int,
                      'robberies_violence_publicways':int,
                      'robberies_violence_homes':int, 
                      'robberies_violence_establishments':int,
                      'year':int
                      }
    for column_name, assigned_types in assigned_types.items():
        if currently_type != assigned_types:
            try:
                data_clean_years[column_name] = data_clean_years[column_name].astype(assigned_types)
                print(f"Column '{column_name}' converted from {currently_type} a {assigned_types}.")
            except Exception as e:
                print(f"It was no possible to switch the '{column_name}' type into {assigned_types}: {e}")
        else:
            print(f"Column '{column_name}' is currently right typed as ({currently_type}).")
    
    return data_clean_years


def convert_year_into_datetime(data_clean_years):
    data_clean_years['Year'] = pd.to_datetime(data_clean_years['Year'].astype(str) + '-01-01')


