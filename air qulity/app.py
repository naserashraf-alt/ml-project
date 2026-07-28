import streamlit as st
import pandas as pd
import joblib

# ==========================
# Page Config
# ==========================
st.set_page_config(
    page_title="Air Quality Prediction",
    page_icon="🌍",
    layout="centered"
)

# ==========================
# Load Model
# ==========================
model = joblib.load("xgboost_model.pkl")

# ==========================
# AQI Category Function
# ==========================
def get_aqi_category(aqi):
    if aqi <= 50:
        return "🟢 Good"
    elif aqi <= 100:
        return "🟡 Satisfactory"
    elif aqi <= 200:
        return "🟠 Moderate"
    elif aqi <= 300:
        return "🔴 Poor"
    elif aqi <= 400:
        return "🟣 Very Poor"
    else:
        return "⚫ Severe"

# ==========================
# Title
# ==========================
st.title("🌍 Air Quality Index Prediction")
st.write("Enter the pollutant values to predict the AQI.")

st.divider()

# ==========================
# Input
# ==========================
col1, col2 = st.columns(2)

with col1:
    pm25 = st.number_input("PM2.5", min_value=0.0, value=0.0)
    pm10 = st.number_input("PM10", min_value=0.0, value=0.0)
    no2 = st.number_input("NO2", min_value=0.0, value=0.0)

with col2:
    so2 = st.number_input("SO2", min_value=0.0, value=0.0)
    co = st.number_input("CO", min_value=0.0, value=0.0)

# ==========================
# Predict
# ==========================
if st.button("Predict AQI", use_container_width=True):

    input_data = pd.DataFrame({
        "PM2.5": [pm25],
        "CO": [co],

        "PM10": [pm10],
        "SO2": [so2],
        "NO2": [no2],

    })

    prediction = model.predict(input_data)[0]

    st.success(f"Predicted AQI: {prediction:.2f}")

    st.subheader("AQI Category")

    st.info(get_aqi_category(prediction))