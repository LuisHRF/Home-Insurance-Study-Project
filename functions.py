import pandas as pd


def defi_years_per_block(data_frame, year_range):

    data_frame_cp = data_frame.copy()

    for (first_row, last_row), year in year_range.items():
        data_frame_cp.loc[first_row:last_row, 'Year'] = year

    return data_frame_cp

#def get_coordinates(province):
    try:
        location = geolocator.geocode(province + ', Spain')
        if location:
            return location.latitude, location.longitude
        else:
            return None, None
    except:
        return None, None


#def add_coordinates(data_frame, column_name):
    data_frame['Latitude'], data_frame['Longitude'] = zip(*data_frame['Province'].apply(get_coordinates))
    return data_frame


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

def add_coordinates_from_dict(data_frame, dict_coords):
      
    def get_lat_long(province):
        
        province_clean = province.strip()
        
        
        if province_clean in provincias_coordenadas:
            return provincias_coordenadas[province_clean]['Latitud'], provincias_coordenadas[province_clean]['Longitud']
        else:
            print(f"Warning: Coordinates not found for {province_clean}")
            return None, None  
    
    
    data_frame['Latitude'], data_frame['Longitude'] = zip(*data_frame['Province'].apply(get_lat_long))

    return data_frame