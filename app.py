import streamlit as st
import pandas as pd
import pickle

# Page Configuration
st.set_page_config(
    page_title="Smart Agriculture System",
    page_icon="🌱",
    layout="centered"
)

# Load Model
model = pickle.load(open("model/crop_model.pkl", "rb"))

# Title
st.title("🌱 Smart Agriculture System")

st.markdown("""
### AI Powered Crop Recommendation

This system recommends the most suitable crop based on:

- Soil Nutrients (N, P, K)
- Temperature
- Humidity
- pH Value
- Rainfall

Model Used: **Random Forest Classifier**

Model Accuracy: **99.32%**
""")
st.info(
    "Enter soil nutrient and weather values, then click Predict Crop to get recommendations."
)

st.markdown("---")

# Sidebar
st.sidebar.header("About Project")

st.sidebar.info(
    """
    Smart Agriculture System

    Developed using:
    - Python
    - Pandas
    - Scikit-Learn
    - Streamlit

    This project helps farmers identify
    the best crop based on soil and
    weather conditions.
    """
)

# Input Fields
st.subheader("Enter Soil and Weather Details")

N = st.number_input(
    "Nitrogen (N)",
    min_value=0,
    max_value=200,
    value=90
)

P = st.number_input(
    "Phosphorus (P)",
    min_value=0,
    max_value=200,
    value=42
)

K = st.number_input(
    "Potassium (K)",
    min_value=0,
    max_value=300,
    value=43
)

temperature = st.number_input(
    "Temperature (°C)",
    value=20.87
)

humidity = st.number_input(
    "Humidity (%)",
    value=82.00
)

ph = st.number_input(
    "pH Value",
    value=6.50
)

rainfall = st.number_input(
    "Rainfall (mm)",
    value=202.93
)

st.markdown("")

# Predict Button
if st.button("🌾 Predict Crop"):

    sample = pd.DataFrame(
        [[
            N,
            P,
            K,
            temperature,
            humidity,
            ph,
            rainfall
        ]],
        columns=[
            "N",
            "P",
            "K",
            "temperature",
            "humidity",
            "ph",
            "rainfall"
        ]
    )

    prediction = model.predict(sample)

    st.success(
        f"🌱 Recommended Crop: {prediction[0].title()}"
    )

    st.balloons()

st.markdown("---")

st.caption(
    "Built using Machine Learning and Streamlit"
)

