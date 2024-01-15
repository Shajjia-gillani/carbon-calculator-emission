import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Define emission factors for Pakistan
EMISSION_FACTORS = {
    "Pakistan": {
        "Transportation": 0.14,  # kgCO2/km
        "Electricity": 0.82,  # kgCO2/kWh
        "Diet": 1.25,  # kgCO2/meal, 2.5kgco2/kg
        "Waste": 0.1  # kgCO2/kg
    }
}

# Set wide layout and page name
st.set_page_config(layout="wide", page_title="Personal Carbon Calculator", page_icon="⚠️")

# Streamlit app code
st.title("Carbon Emission Calculator 🌍")

# User inputs
st.subheader("Select Your Country")
country = st.selectbox("", ["Pakistan"])

col1, col2 = st.columns(2)

with col1:
    st.subheader("Daily Commute Distance (in km)")
    distance = st.slider("", 0.0, 100.0, key="distance_input")

    st.subheader("Monthly Electricity Consumption (in kWh)")
    electricity = st.slider("", 0.0, 1000.0, key="electricity_input")

with col2:
    st.subheader("Waste Generated Per Week (in kg)")
    waste = st.slider("", 0.0, 100.0, key="waste_input")

    st.subheader("Number of Meals Per Day")
    meals = st.number_input("", 0, key="meals_input")

# Normalize inputs
if distance > 0:
    distance = distance * 365  # Convert daily distance to yearly
if electricity > 0:
    electricity = electricity * 12  # Convert monthly electricity to yearly
if meals > 0:
    meals = meals * 365  # Convert daily meals to yearly
if waste > 0:
    waste = waste * 52  # Convert weekly waste to yearly

# Calculate carbon emissions
transportation_emissions = EMISSION_FACTORS[country]["Transportation"] * distance
electricity_emissions = EMISSION_FACTORS[country]["Electricity"] * electricity
diet_emissions = EMISSION_FACTORS[country]["Diet"] * meals
waste_emissions = EMISSION_FACTORS[country]["Waste"] * waste

# Convert emissions to tonnes and round off to 2 decimal points
transportation_emissions = round(transportation_emissions / 1000, 2)
electricity_emissions = round(electricity_emissions / 1000, 2)
diet_emissions = round(diet_emissions / 1000, 2)
waste_emissions = round(waste_emissions / 1000, 2)

# Calculate total emissions
total_emissions = round(
    transportation_emissions + electricity_emissions + diet_emissions + waste_emissions, 2
)

if st.button("Calculate CO2 Emissions"):

    # Display results
    st.header("Results")

    col3, col4 = st.columns(2)

    with col3:
        st.subheader("Carbon Emissions by Category")
        st.info(f"🚗 Transportation: {transportation_emissions} tonnes CO2 per year")
        st.info(f"💡 Electricity: {electricity_emissions} tonnes CO2 per year")
        st.info(f"🍽️ Diet: {diet_emissions} tonnes CO2 per year")
        st.info(f"🗑️ Waste: {waste_emissions} tonnes CO2 per year")

        # Plot a bar graph
        categories = ["Transportation", "Electricity", "Diet", "Waste"]
        values = [transportation_emissions, electricity_emissions, diet_emissions, waste_emissions]
        fig, ax = plt.subplots()
        ax.bar(categories, values, color=['blue', 'orange', 'green', 'red'])
        ax.set_ylabel('Tonnes of CO2 per year')
        ax.set_title('Carbon Emissions by Category')
        st.pyplot(fig)

    with col4:
        st.subheader("Total Carbon Footprint")
        st.success(f"🌍 Your total carbon footprint is: {total_emissions} tonnes CO2 per year")
        st.warning("In 2021, CO2 emissions per capita for Pakistan was XYZ tons of CO2 per capita. Additional information about Pakistan's emissions can be included here.")
