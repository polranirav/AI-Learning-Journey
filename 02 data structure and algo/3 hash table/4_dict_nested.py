model_result = {
    "model": "RandomForest",
    "metrics": {
        "accuracy": 0.92,
        "f1_score": 0.88
    },
    "params": {
        "n_estimators": 100,
        "max_depth": 5
    }
}

print("F1 Score:", model_result["metrics"]["f1_score"])
print("Model Params:", model_result["params"])