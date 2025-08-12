# ✅ 1_streamlit_predictor.py
# Streamlit UI for predicting salary using a trained ML model

import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("model_joblib.pkl")

# UI
st.title("💼 Salary Predictor")
st.write("Enter years of experience to predict the salary:")

# Input field
experience = st.slider("Experience (years)", 0.0, 20.0, 3.0)

# Prediction
if st.button("Predict Salary"):
    prediction = model.predict(np.array([[experience]]))
    st.success(f"Estimated Salary: ${prediction[0]:,.2f}")