# ✅ Train and save a simple model using joblib
from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression
import joblib

# Generate dummy regression data
X, y = make_regression(n_samples=100, n_features=1, noise=10)

# Train a simple linear regression model
model = LinearRegression()
model.fit(X, y)

# Save the model using joblib
joblib.dump(model, "model_joblib.pkl")
print("✅ Model saved as model_joblib.pkl")

# Load the model
loaded_model = joblib.load("model_joblib.pkl")
print("✅ Model loaded and ready for prediction.")

# Make a prediction
prediction = loaded_model.predict([[5]])
print("📊 Prediction for input 5:", prediction[0])