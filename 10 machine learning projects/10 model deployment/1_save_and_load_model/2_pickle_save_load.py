# ✅ Save and load ML model using pickle (less efficient than joblib for big models)
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
import pickle

# Load Iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Train classifier
clf = DecisionTreeClassifier()
clf.fit(X, y)

# Save the model using pickle
with open("model_pickle.pkl", "wb") as f:
    pickle.dump(clf, f)
print("✅ Model saved as model_pickle.pkl")

# Load the model
with open("model_pickle.pkl", "rb") as f:
    loaded_clf = pickle.load(f)
print("✅ Model loaded using pickle.")

# Predict on one sample
sample = X[0].reshape(1, -1)
prediction = loaded_clf.predict(sample)
print("📊 Prediction for first sample:", prediction[0])