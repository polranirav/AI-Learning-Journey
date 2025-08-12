# ✅ 1_gradio_ui.py
# Build an ML prediction demo using Gradio

import gradio as gr
import joblib
import numpy as np

# Load trained model
model = joblib.load("model_joblib.pkl")

# Define prediction function
def predict_salary(experience):
    exp_array = np.array([[experience]])
    prediction = model.predict(exp_array)
    return f"${prediction[0]:,.2f}"

# Gradio interface
interface = gr.Interface(
    fn=predict_salary,
    inputs=gr.Slider(0, 20, value=3, label="Years of Experience"),
    outputs="text",
    title="💼 Salary Predictor",
    description="Enter experience to predict salary using Linear Regression."
)

interface.launch()