from functions import *
import numpy as np
import pandas as pd
import streamlit as st
import folium
from streamlit_folium import folium_static
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt

def main():

    st.title("Project to analyze data on robberies in Spain between 2010 and 2023")

    with st.expander("Show/Hide Navigation"):
        section = st.sidebar.radio("Go to", ["Home", "Crimes per province and year map",
                                        "Crime trend by province (2010-2023)",
                                        "Violent crimes trend by province (2010-2023)",
                                        "Crimes per capita by province (total)",
                                        "Crime type by province (total)"])
        
    def home():
        st.header("Welcome to the Crime Statistics Dashboard")
        st.write("""
            This is a data analysis project within the Ironhack Data Analysis Bootcamp, carried out by Luis H. Rodriguez, Greta Galeana and David Moreno.
            The hypothesis of the project is that we work in the Data team of an insurance company in Spain that is looking to create new types of theft insurance and focus its activity on specific provinces. This is why the analysis has been aimed at contributing to this.
            In this dashboard hosted on Streamlit we want to present the graphs and analytical processes that we have reached after carrying out all the cleaning, formatting and study of the data. In the navigation menu you can find:
            - **Crimes per province and year map**: Interactive map of crime totals by province and year.
            - **Crime trend by province (2010-2023)**: Analysis of crime trends over time.
            - **Violent crimes trend by province (2010-2023)**: A focused look at violent crimes.
            - **Crimes per capita by province (total)**: See the total crimes relative to population.
            - **Crime type by province (total)**: Breakdown of crimes by type across provinces.
        """)
        st.write("Select a section from the sidebar to begin exploring.")
        st.subheader("Access to the full repository [here](https://github.com/LuisHRF/Home-Insurance-Study-Project-)")
        
    def crimes_map():
        # Map using total crimes per province between 2010 and 2023
        st.subheader("Crimes per province and year map")

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

        folium_static(spain_map)

    def crime_trend_province():

        # Graphic for the difference between 2010 and 2023

        st.subheader("Crime trend by province (2010-2023)")

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


    def violent_crimes_trend():

        # Graphic for show the violents crimes between 2010 and 2023

        st.subheader("Violent crimes trend by province (2010-2023)")

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

    def crimes_per_capita():

        # Data per capita

        st.subheader("Crimes per capita by province (total)")

        data_per_capita = pd.read_csv('data_per_capita.csv')

        data_per_capita = data_per_capita.sort_values(by='crimes_per_capita', ascending=False)

        fig, ax = plt.subplots(figsize=(16, 8))
        ax.bar(data_per_capita['province'], data_per_capita['crimes_per_capita'], color='salmon', width=0.6)

        ax.set_title('Crimes per Capita by Province')
        ax.set_xlabel('Province')
        ax.set_ylabel('Crimes per capita')
        plt.xticks(rotation=45)
        plt.tight_layout()

        plt.xticks(rotation=90, fontsize=12)

        plt.tight_layout()

        st.pyplot(fig)


    def crime_type_province():
        # Crime type by province

        st.subheader("Crime type by province (total)")

        data_crimes_type = pd.read_csv('data_crimes_type.csv')

        data_melted = pd.melt(data_crimes_type, id_vars=['Province'], 
                            var_name='Crime Type', value_name='Total_crimes')

        chart = alt.Chart(data_melted).mark_bar().encode(
            x=alt.X('Province:N', sort=None, title='Province', axis=alt.Axis(labelAngle=-90)),  
            y=alt.Y('Total_crimes:Q', title='Total Crimes'),
            color=alt.Color('Crime Type:N', title='Crime Type'),  
            tooltip=['Province', 'Crime Type', 'Total_crimes']  
        ).properties(
            width=800, 
            height=400, 
            title='Total Crimes by Province and Crime Type'
        ).configure_axis(
            labelFontSize=10,  
            labelColor='white'  
        )
    
        st.altair_chart(chart, use_container_width=True)

    if section == "Home":
        home()

    if section == "Crimes per province and year map":
        crimes_map()

    elif section == "Crime trend by province (2010-2023)":
        crime_trend_province()

    elif section == "Violent crimes trend by province (2010-2023)":
        violent_crimes_trend()

    elif section == "Crimes per capita by province (total)":
        crimes_per_capita()

    elif section == "Crime type by province (total)":
        crime_type_province()

if __name__ == "__main__":
    main()