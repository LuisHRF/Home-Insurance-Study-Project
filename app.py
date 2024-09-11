from functions import *
import pandas as pd
import streamlit as st
import folium
from streamlit_folium import folium_static

spain_map = folium.Map(location=[40.0, -3.7], zoom_start=6)

for index, row in data_pivot_table.iterrows():
    popup_info = f"{row['Province']}<br>"
    for year in data_pivot_table.columns[3:]:  
        popup_info += f"{int(year)}: {row[year]} crimes<br>"
    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=popup_info,
        tooltip=row['Province']
    ).add_to(spain_map)

st.title("Crimes per province and year map")
folium_static(spain_map)