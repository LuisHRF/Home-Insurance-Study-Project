from functions import *
import numpy as np
import pandas as pd
import streamlit as st
import folium
from streamlit_folium import folium_static


def interpolate_color(value, min_value, max_value, color1, color2):
    ratio = (value - min_value) / (max_value - min_value)
    r = int(color1[0] * (1 - ratio) + color2[0] * ratio)
    g = int(color1[1] * (1 - ratio) + color2[1] * ratio)
    b = int(color1[2] * (1 - ratio) + color2[2] * ratio)
    return f"#{r:02x}{g:02x}{b:02x}"

data_pivot_table = pd.read_csv('data_pivot_table.csv')

data_melted = pd.melt(data_pivot_table, id_vars=['Province', 'Latitude', 'Longitude'], 
                      var_name='Year', value_name='Total_crimes')

data_melted['Year'] = data_melted['Year'].astype(int)


years = data_melted['Year'].unique().tolist() 
selected_year = st.selectbox('Select Year', sorted(years))

data_filtered = data_melted[data_melted['Year'] == selected_year]


spain_map = folium.Map(location=[40.0, -3.7], zoom_start=6)

max_crimes = data_filtered['Total_crimes'].max()
min_crimes = data_filtered['Total_crimes'].min()

data_filtered['Log_crimes'] = np.log1p(data_filtered['Total_crimes'])

for index, row in data_filtered.iterrows():
    radius = (row['Log_crimes'] - data_filtered['Log_crimes'].min()) / (data_filtered['Log_crimes'].max() - data_filtered['Log_crimes'].min()) * 15 + 5
    color = interpolate_color(row['Total_crimes'], min_crimes, max_crimes, (0, 0, 255), (255, 0, 0))

    folium.CircleMarker(
        location=[row['Latitude'], row['Longitude']],
        radius=radius,  
        color=color,  
        fill=True,
        fill_color=color,  
        fill_opacity=0.6,
        popup=f"{row['Province']}: {row['Total_crimes']} crimes",
        tooltip=row['Province']
    ).add_to(spain_map)

st.title("Crimes per province and year map")
folium_static(spain_map)