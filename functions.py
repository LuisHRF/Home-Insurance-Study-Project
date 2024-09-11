import pandas as pd


def defi_years_per_block(data_frame, year_range):

    data_frame_cp = data_frame.copy()

    for (first_row, last_row), year in year_range.items():
        data_frame_cp.loc[first_row:last_row, 'Year'] = year

    return data_frame_cp

def cleaning_columns_replace(data_frame):
    data_frame.columns = data_frame.columns.str.lower().str.replace(" ", "_")
    data_frame = data_frame.rename(columns={
    "_": "Province"})

    return data_frame


def traducir_columnas(columns_titles, translations):
    return [translations.get(col, col) for col in columns_titles]
#print(traducir_columnas(columns_titles, translations))


def cleaning_rows_dataframe(data_frame, values_to_remove=None):
    # Si no se especifican valores a eliminar, usa los predeterminados
    if values_to_remove is None:
        values_to_remove = ['Total Nacional', 'En el extranjero', 'Desconocida']
    
    # Filtrar las filas que no contengan los valores a eliminar
    cleaned_df = data_frame[~data_frame['columna_de_interes'].isin(values_to_remove)]
    
    return cleaned_df

def reset_index(data_frame):
    data_frame.reset_index(drop=True, inplace=True)
    data_frame = data_frame.drop(index=0)

    return data_frame


def convert_floats_to_ints(data_frame):
    # Iterar sobre las columnas y convertir a int si son float
    for column in data_frame.columns:
        if data_frame[column].dtype == 'float64':  # Verifica si la columna es de tipo float
            data_frame[column] = data_frame[column].astype(int)  # Convierte a int
    return data_frame

