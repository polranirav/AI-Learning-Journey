# ✅ 1_fastapi_api.py
# Build an API with FastAPI to serve an ML model

from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Step 1: Load saved model
model = joblib.load("model_joblib.pkl")

# Step 2: Create app
app = FastAPI()

# Step 3: Define input schema using Pydantic
class InputData(BaseModel):
    experience: float

# Step 4: Define API route
@app.post("/predict/")
def predict_salary(data: InputData):
    input_array = np.array([[data.experience]])
    prediction = model.predict(input_array)
    return {"predicted_salary": round(prediction[0], 2)}