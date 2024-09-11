from functions import *
import numpy as np
import pandas as pd
import streamlit as st
import folium
from streamlit_folium import folium_static

def main():

    data_pivot_map = pd.read_csv('data_pivot_map.csv')

    data_melted = pd.melt(data_pivot_map, id_vars=['Province', 'Latitude', 'Longitude'], 
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
        radius = (row['Log_crimes'] - data_filtered['Log_crimes'].min()) / (data_filtered['Log_crimes'].max() - data_filtered['Log_crimes'].min()) ** 1.5  * 15 + 5
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

if __name__ == "__main__":
    main()