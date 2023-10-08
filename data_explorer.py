import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm

import squarify
 
from constants import AFRICAN_COUNTRIES, REGIONS


# Write this function to allow the user to select an african country or region. 
# If the user selects a country, return the name of the country and a dataframe
# containing the data for that country. If the user selects a region, return the
# name of the region and a dataframe containing the data for that region.
def country_data_explorer():
    task = st.selectbox("Select Country or Region", ["Country", "Region"], 0)
    name, df = None, None

    if task == "Country":
        name = st.selectbox("Select Country", AFRICAN_COUNTRIES, 0)
        if name:
            df = pd.read_csv(f"data/{name}.csv")
            # Display the selected country and its data
            #st.write(f"Selected Country: {name}")
            #st.write(df)  # Display the dataframe for the selected country

            # Create a sum of Gross import by Sector for the selected country
            grouped_data = df.groupby('Sector')['Gross Import'].sum()

            # Round the values to zero decimal places
            grouped_data = grouped_data.round(0)

            # Create a color map for the sectors
            colors = ['#FFC2B4', '#FFE8B4', '#E6F7D4', '#FFC2C2', '#FFC2D1', '#E6C2FF', '#B4FFFF', '#FFB4FF', '#B4FFC2', '#B4B4FF']

            # Plot barplot of the sum of Gross import by Sector for the selected country
            # Order by descending order
            fig, ax = plt.subplots()
            grouped_data.sort_values(ascending=False).plot(kind='bar', color=colors)
            ax.set_title(f"Total Gross Import by Sector for {name}")
            ax.set_ylabel("Gross Import")
            ax.set_xlabel("Sector")
            ax.set_xticklabels(grouped_data.index, rotation=45)
            ax.yaxis.set_major_formatter('${x:,.0f}')

            # Show the plot using Streamlit
            st.pyplot(fig)

    elif task == "Region":
        region_name = st.selectbox("Select Region", REGIONS, 0)
        if region_name:
            # Load the data for the selected region (You need to implement this part)
            region_data = load_region_data(region_name)
            st.write(f"Selected Region: {region_name}")
            st.write(region_data)  # Display the dataframe for the selected region

            # Create a sum of Gross import by Sector for the selected region
            grouped_data = region_data.groupby('Sector')['Gross Import'].sum()

            # Round the values to zero decimal places
            grouped_data = grouped_data.round(0)

            # Create a color map for the sectors
            colors = ['#FFC2B4', '#FFE8B4', '#E6F7D4', '#FFC2C2', '#FFC2D1', '#E6C2FF', '#B4FFFF', '#FFB4FF', '#B4FFC2', '#B4B4FF']
            
            labels = [f"{label}\n${value:,.2f}" for label, value in zip(grouped_data.index, grouped_data.values.round(1))]

            # Plot the sum of Gross import by Sector for the selected region
          # Create a treemap using squarify
            fig, ax = plt.subplots()
            squarify.plot(sizes=grouped_data.values, label=labels, color=colors)
            ax.set_title(f"Total Gross Import by Sector for {region_name}")
            ax.axis('off')

            # Show the plot using Streamlit
            st.pyplot(fig)

# Define a function to load data for the selected region
def load_region_data(region_name):
    # You should implement this function to load data for the selected region
    # and return a dataframe with the region's data.
    # You can use a similar approach as loading country data but adjust it for regions.
    # Example:
    region_data = pd.read_csv(f"data/{region_name}.csv")
    return region_data


# Run the app
if __name__ == "__main__":
    country_data_explorer()