import pandas as pd


def defi_years_per_block(data_frame, year_range):

    data_frame_cp = data_frame.copy()

    for (first_row, last_row), year in year_range.items():
        data_frame_cp.loc[first_row:last_row, 'Year'] = year

    return data_frame_cp


def traducir_columnas(columns_titles, translations):
    columns_titles = ["1._contra_las_personas","1.2.-lesiones","5.1.-hurtos","5.2.-robos_con_fuerza_en_las_cosas","5.2.1.-robos_con_fuerza_en_las_cosas_en_el_interior_de_vehículos","5.2.2.-robos_con_fuerza_en_viviendas","5.2.3.-robos_con_fuerza_en_establecimientos","5.3.-robos_con_violencia_o_intimidación","5.3.1.-robos_con_violencia_en_vía_pública","5.3.2.-robos_con_violencia_en_viviendas","5.3.3.-robos_con_violencia_en_establecimientos"]
    translations = {"1._contra_las_personas": "Assault",
                "1.2.-lesiones" :"Injuries",
                "5.1.-hurtos":"small robberies",
                "5.2.-robos_con_fuerza_en_las_cosas":"robs_with_force",
                "5.2.1.-robos_con_fuerza_en_las_cosas_en_el_interior_de_vehículos":"robs_force_vehicles",
                "5.2.2.-robos_con_fuerza_en_viviendas":"robs_force_homes",
                "5.2.3.-robos_con_fuerza_en_establecimientos":"robs_force_stores",
                "5.3.-robos_con_violencia_o_intimidación":"robs_violence_intimidation",
                "5.3.1.-robos_con_violencia_en_vía_pública":"robs_violence_publicways",
                "5.3.2.-robos_con_violencia_en_viviendas":"robs_violence_homes",
                "5.3.3.-robos_con_violencia_en_establecimientos":"robs_violence_stores"
    }
    return [translations.get(col, col) for col in columns_titles]


def reset_index(data_frame):
    data_frame.reset_index(drop=True, inplace=True)
    data_frame = data_frame.drop(index=0)

    return data_frame

def cleaning_rows_dataframe(data_frame, values_to_remove=None):
    # Si no se especifican valores a eliminar, usa los predeterminados
    if values_to_remove is None:
        values_to_remove = ['Total Nacional', 'En el extranjero', 'Desconocida']
    
    # Filtrar las filas que no contengan los valores a eliminar
    cleaned_df = data_frame[~data_frame['columna_de_interes'].isin(values_to_remove)]
    
    return cleaned_df


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


def convert_floats_to_ints(data_frame):
    # Iterar sobre las columnas y convertir a int si son float
    for column in data_frame.columns:
        if data_frame[column].dtype == 'float64':  # Verifica si la columna es de tipo float
            data_frame[column] = data_frame[column].astype(int)  # Convierte a int
    return data_frame