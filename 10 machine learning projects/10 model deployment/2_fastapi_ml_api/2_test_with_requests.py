# ✅ 2_test_with_requests.py
# Send a POST request to the FastAPI server

import requests

data = {
    "experience": 7
}

response = requests.post("http://127.0.0.1:8000/predict/", json=data)
print("📤 Sent:", data)
print("📥 Received:", response.json())