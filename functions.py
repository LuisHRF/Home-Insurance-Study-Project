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

def translate_columns(columns_titles):

    translations = {"1._contra_las_personas": " assault",
                "1.2.-lesiones" :" injuries",
                "5.1.-hurtos":"small_robberies",
                "5.2.-robos_con_fuerza_en_las_cosas":"robberies_with_force",
                "5.2.1.-robos_con_fuerza_en_las_cosas_en_el_interior_de_vehículos":"robberies_force_vehicles",
                "5.2.2.-robos_con_fuerza_en_viviendas":"robberies_force_homes",
                "5.2.3.-robos_con_fuerza_en_establecimientos":"robberies_force_stores",
                "5.3.-robos_con_violencia_o_intimidación":"robberies_violence_intimidation",
                "5.3.1.-robos_con_violencia_en_vía_pública":"robberies_violence_publicways",
                "5.3.2.-robos_con_violencia_en_viviendas":"robberies_violence_homes",
                "5.3.3.-robos_con_violencia_en_establecimientos":"robberies_violence_stores"
                }

    return [translations.get(col, col) for col in columns_titles]


def add_coordinates_from_dict(data_frame):

    provincias_coordenadas = {
    'Araba/Álava': {'Latitud': 42.84671, 'Longitud': -2.67245},
    'Albacete': {'Latitud': 38.99435, 'Longitud': -1.85854},
    'Alicante/Alacant': {'Latitud': 38.34517, 'Longitud': -0.48149},
    'Almería': {'Latitud': 36.83405, 'Longitud': -2.46371},
    'Ávila': {'Latitud': 40.65668, 'Longitud': -4.68186},
    'Badajoz': {'Latitud': 38.87945, 'Longitud': -6.97065},
    'Balears (Illes)': {'Latitud': 39.57119, 'Longitud': 2.64663},
    'Barcelona': {'Latitud': 41.38506, 'Longitud': 2.17340},
    'Burgos': {'Latitud': 42.34399, 'Longitud': -3.69691},
    'Cáceres': {'Latitud': 39.47649, 'Longitud': -6.37224},
    'Cádiz': {'Latitud': 36.51638, 'Longitud': -6.29944},
    'Castellón/Castelló': {'Latitud': 39.98636, 'Longitud': -0.05132},
    'Ciudad Real': {'Latitud': 38.98613, 'Longitud': -3.92726},
    'Córdoba': {'Latitud': 37.88818, 'Longitud': -4.77938},
    'Coruña (A)': {'Latitud': 43.36234, 'Longitud': -8.41154},
    'Cuenca': {'Latitud': 40.07039, 'Longitud': -2.13742},
    'Girona': {'Latitud': 41.98181, 'Longitud': 2.82370},
    'Granada': {'Latitud': 37.17734, 'Longitud': -3.59856},
    'Guadalajara': {'Latitud': 40.63333, 'Longitud': -3.16693},
    'Gipuzkoa': {'Latitud': 43.31283, 'Longitud': -1.97753},
    'Huelva': {'Latitud': 37.26142, 'Longitud': -6.94472},
    'Huesca': {'Latitud': 42.14010, 'Longitud': -0.40889},
    'Jaén': {'Latitud': 37.77959, 'Longitud': -3.78491},
    'León': {'Latitud': 42.59873, 'Longitud': -5.56710},
    'Lleida': {'Latitud': 41.61759, 'Longitud': 0.62001},
    'Rioja (La)': {'Latitud': 42.28707, 'Longitud': -2.53960},
    'Lugo': {'Latitud': 43.00994, 'Longitud': -7.55601},
    'Madrid': {'Latitud': 40.41678, 'Longitud': -3.70379},
    'Málaga': {'Latitud': 36.72127, 'Longitud': -4.42140},
    'Murcia': {'Latitud': 37.99224, 'Longitud': -1.13065},
    'Navarra': {'Latitud': 42.69539, 'Longitud': -1.67607},
    'Ourense': {'Latitud': 42.33579, 'Longitud': -7.86388},
    'Asturias': {'Latitud': 43.36191, 'Longitud': -5.84939},
    'Palencia': {'Latitud': 42.00946, 'Longitud': -4.52785},
    'Palmas (Las)': {'Latitud': 28.12355, 'Longitud': -15.43626},
    'Pontevedra': {'Latitud': 42.43386, 'Longitud': -8.64805},
    'Salamanca': {'Latitud': 40.97010, 'Longitud': -5.66354},
    'Santa Cruz de Tenerife': {'Latitud': 28.46363, 'Longitud': -16.25185},
    'Cantabria': {'Latitud': 43.18283, 'Longitud': -3.98784},
    'Segovia': {'Latitud': 40.94291, 'Longitud': -4.10883},
    'Sevilla': {'Latitud': 37.38863, 'Longitud': -5.98233},
    'Soria': {'Latitud': 41.76360, 'Longitud': -2.46499},
    'Tarragona': {'Latitud': 41.11888, 'Longitud': 1.24449},
    'Teruel': {'Latitud': 40.34480, 'Longitud': -1.10643},
    'Toledo': {'Latitud': 39.86283, 'Longitud': -4.02732},
    'Valencia/València': {'Latitud': 39.46991, 'Longitud': -0.37629},
    'Valladolid': {'Latitud': 41.65225, 'Longitud': -4.72453},
    'Bizkaia': {'Latitud': 43.26301, 'Longitud': -2.93499},
    'Zamora': {'Latitud': 41.50332, 'Longitud': -5.74456},
    'Zaragoza': {'Latitud': 41.64882, 'Longitud': -0.88909},
    'Ceuta': {'Latitud': 35.88939, 'Longitud': -5.31979},
    'Melilla': {'Latitud': 35.29298, 'Longitud': -2.93871}
    }
      
    def get_lat_long(province):
        
        province_clean = province.strip()
        
        
        if province_clean in provincias_coordenadas:
            return provincias_coordenadas[province_clean]['Latitud'], provincias_coordenadas[province_clean]['Longitud']
        else:
            print(f"Warning: Coordinates not found for {province_clean}")
            return None, None  
    
    
    data_frame['Latitude'], data_frame['Longitude'] = zip(*data_frame['Province'].apply(get_lat_long))

    return data_frame

def drop_specific_rows(data_frame, columns, values_to_drop):
    pattern = '|'.join([f'^{value}' for value in values_to_drop])
    data_frame_filtered = data_frame[~data_frame[columns].str.contains(pattern)]

    return data_frame_filtered


# Functions focused to streamlit_app

def interpolate_color(value, min_value, max_value, color1, color2):
    ratio = (value - min_value) / (max_value - min_value)
    r = int(color1[0] * (1 - ratio) + color2[0] * ratio)
    g = int(color1[1] * (1 - ratio) + color2[1] * ratio)
    b = int(color1[2] * (1 - ratio) + color2[2] * ratio)
    return f"#{r:02x}{g:02x}{b:02x}"
