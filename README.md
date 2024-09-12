# Study of analysis of crime data in Spain for insurance companies
### This is a data analysis project within the Ironhack Data Analysis Bootcamp, carried out by Luis H. Rodriguez, Greta Galeana and David Moreno.
<p align="center">

</p>

## Team Members

| Name             | LinkedIn Profile | Brief Description |
|------------------|------------------|-------------------|
| David Moreno     | In building      |  Economy Statistics & Data anlysis  |
| Luis H. Rodríguez  | [\[Link\]](https://www.linkedin.com/in/luis-h-rodr%C3%ADguez-fuentes/) | Data Analyst |
| Greta Galeana    | [\[Link\]](https://www.linkedin.com/in/gretagaleana?) | Marketing business & Data Analyst |

### Business Problem
As a leading insurance company in the Spanish market, we aim to leverage big data to enhance our competitiveness and the accuracy of our policies, particularly those related to home, vehicle ans stores insurance. To achieve this, we have decided to integrate a comprehensive analysis of crime statistics provided by official sources, such as the Ministry of the Interior.

The hypothesis of the project is that we work in the Data team of an insurance company in Spain that is looking to create new types of theft insurance and focus its activity on specific provinces. This is why the analysis has been aimed at contributing to this.

### Relevant links

- Portal estadístico de criminalidad: [\[Link to source\]](https://estadisticasdecriminalidad.ses.mir.es/publico/portalestadistico/datos.html?type=pcaxis&path=/Datos1/&file=pcaxis)
- Streamlit's dashboard: [\[Link to dashboard\]](https://crimesspain20102023.streamlit.app/)
- Canva: [\[Link to dashboard\]](https://www.canva.com/design/DAGQiRCcIbU/6GAAFE1814T-iu1EEErD1A/view#1)

## Methodology
This project aims to analyse crime trends in Spain between 2010 and 2023, focusing on different types of crimes, in order to apply it to an insurance company. Below is a description of the methods used for data collection, analysis and visualisation.

### 1. Data collection
The crime data has been collected from the Ministry of the Interior of the Government of Spain. We have obtained the raw data of specific crimes chosen for our analysis.

### 2. Data cleaning and pre-processing
We have worked on cleaning up nulls that were due to the bad formatting of the original Excel (source: Ministry) in the matter of dates.
In addition, we have standardized and translated the name of the columns for a better understanding. We have managed to add key data according to the needs: a column with year values, a column with latitude and longitude to locate the provinces; and we have worked on the type of data to suit the situations.

### 3. Data analysis
Using the pandas library, we have developed a series of functions and lines of code focused on analyzing data that may be useful for our business cause.
Growth in the number of crimes, crimes per capita, total number of crimes per province... in this way we could offer the "insurance company" a better perspective of the regions where it could be more urgent to apply marketing measures.

### 4. Data visualization
We have used Streamlit to create a dashboard with all the graphics. Firstly, because it allows us to have an interface and a front-end without the need to develop it as web-developers.
Secondly, to avoid worrying about hosting the site on a server and to facilitate the sharing of information.

## Tools & technology

- **Programming Language**: Python
- **Libraries**: Pandas, Folium, Numpy, Streamlit, Pillow, Seaborn
- **Visualization**: Streamlit
- **Data Storage**: CSV, xlsx.

## Problems we have faced

The first conflict we found was in the original file. The years, instead of being just another value, were stored in the same column as the provinces, so that after each year there was a whole row of nulls. This was solved by applying patterns.

The second issue to consider has been the development of the entire environment for the project, since we were first-timers. In the end, we decided to test compatibility with libraries and packages and manage everything.

The third has been to manage the errors that have arisen. Since these are three completely different profiles, it has been important to unify paths and focus efforts on working in parallel, prioritizing progress without interruption.

