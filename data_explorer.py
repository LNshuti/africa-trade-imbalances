import streamlit as st 
import pandas as pd
 
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
            st.write(f"Selected Country: {name}")
            st.write(df)  # Display the dataframe for the selected country
    elif task == "Region":
        region_name = st.selectbox("Select Region", REGIONS, 0)
        if region_name:
            # Load the data for the selected region (You need to implement this part)
            region_data = load_region_data(region_name)
            st.write(f"Selected Region: {region_name}")
            st.write(region_data)  # Display the dataframe for the selected region

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