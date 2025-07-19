import json

# Imagine this is your ML model config
config = {
    "model": "RandomForest",
    "n_estimators": 100,
    "max_depth": 5,
    "metrics": ["accuracy", "f1"]
}

# Save config
with open("model_config.json", "w") as f:
    json.dump(config, f, indent=4)

# Later: load it again
with open("model_config.json", "r") as f:
    loaded_config = json.load(f)

print("Loaded Config:", loaded_config)