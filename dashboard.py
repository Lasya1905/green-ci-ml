import streamlit as st
import pandas as pd
import joblib

st.title("CI/CD Energy Prediction")

model = joblib.load("energy_model.pkl")

duration = st.slider("Duration (seconds)", min_value=10, max_value=600, value=60)
co2 = st.number_input("CO2 (grams)", value=10.0)

if st.button("Predict"):
    df = pd.DataFrame({"duration_s":[duration], "co2_g":[co2]})
    pred = model.predict(df)[0]
    st.success(f"Predicted Energy: {pred:.6f} kWh")
