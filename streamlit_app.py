from functions import *
import numpy as np
import pandas as pd
import streamlit as st
import folium
from streamlit_folium import folium_static
import matplotlib.pyplot as plt
import seaborn as sns

def main():

    # Map using total crimes per province between 2010 and 2023

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

    # Graphic for the difference between 2010 and 2023

    st.title("Crime trend by province (2010-2023)")

    data_clean = pd.read_csv('data_clean.csv')

    data_2010 = data_clean[data_clean['year'] == 2010]
    data_2023 = data_clean[data_clean['year'] == 2023]

    merged_data = pd.merge(data_2010[['Province', 'Total_crimes']], 
                       data_2023[['Province', 'Total_crimes']], 
                       on='Province', 
                       suffixes=('_2010', '_2023'))
    
    merged_data['Percentage Change'] = ((merged_data['Total_crimes_2023'] - merged_data['Total_crimes_2010']) / merged_data['Total_crimes_2010']) * 100

    st.subheader("Crime percentage change by province (2010-2023)")
    st.dataframe(merged_data[['Province', 'Percentage Change']].style.applymap(lambda x: 'color: green' if x < 0 else 'color: red', subset=['Percentage Change']))

    st.subheader("Crime percentage change by province (Bar Chart)")

    fig, ax = plt.subplots(figsize=(10, 12))

    colors = ['green' if x < 0 else 'red' for x in merged_data['Percentage Change']]

    ax.barh(merged_data['Province'], merged_data['Percentage Change'], color=colors)

    ax.set_xlabel('Percentage Change (%)')
    ax.set_ylabel('Province')
    ax.set_title("Crime percentage change by province (2010-2023)")

    st.pyplot(fig)

    # Graphic for show the violents crimes between 2010 and 2023

    st.title("Violent crimes trend by province (2010-2023)")

    data_rob_violence = pd.read_csv('data_rob_violence.csv')


    data_2010_vi = data_rob_violence[data_rob_violence['year'] == 2010]
    data_2023_vi = data_rob_violence[data_rob_violence['year'] == 2023]

    crime_type = st.selectbox("Select type of violent crime", ['Violent assault', 'Robberies with violence in public places', 'Robberies with violence and intimidation'])

    provinces_2010 = set(data_2010_vi['Province'].unique())
    provinces_2023 = set(data_2023_vi['Province'].unique())
    common_provinces = provinces_2010.intersection(provinces_2023)

    growth_rate_vi = {}

    for province in common_provinces:
        crime_2010 = data_2010_vi[data_2010_vi['Province'] == province][crime_type].values[0]
        crime_2023 = data_2023_vi[data_2023_vi['Province'] == province][crime_type].values[0]

        if crime_2010 != 0: 
            growth_rate_vi[province] = ((crime_2023 - crime_2010) / crime_2010) * 100

    data_growth_vi = pd.DataFrame(list(growth_rate_vi.items()), columns=['Province', 'Percentage Change'])

    data_growth_vi = data_growth_vi.sort_values(by='Percentage Change', ascending=True)

    fig, ax = plt.subplots(figsize=(10, 8))
    colors = ['red' if x > 0 else 'green' for x in data_growth_vi['Percentage Change']]
    sns.barplot(y='Province', x='Percentage Change', data=data_growth_vi, palette=colors, ax=ax)

    ax.set_xlabel('Percentage Change (%)')
    ax.set_ylabel('Province')
    ax.set_title(f"{crime_type} percentage change between 2010 and 2023")

    st.pyplot(fig)

if __name__ == "__main__":
    main()