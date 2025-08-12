# ✅ 1_versioning_simulation.py
# Simulate loading different versions of ML models manually

import joblib
import numpy as np

# Load two versions of saved models
model_v1 = joblib.load("model_v1.pkl")  # Trained on small dataset
model_v2 = joblib.load("model_v2.pkl")  # Trained on larger/improved dataset

# Simulate API route for version selection
def predict_salary(experience, version="v1"):
    exp = np.array([[experience]])
    if version == "v1":
        model = model_v1
    else:
        model = model_v2
    pred = model.predict(exp)
    return f"Predicted salary ({version}): ${pred[0]:,.2f}"

# Simulate prediction
print(predict_salary(5, version="v1"))
print(predict_salary(5, version="v2"))