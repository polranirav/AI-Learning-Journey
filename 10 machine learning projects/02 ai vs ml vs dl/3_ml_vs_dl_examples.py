# Comparing ML and DL based on data and task complexity

print("⚖️ ML vs DL Comparison")

ml_vs_dl = {
    "Machine Learning": [
        "Needs less data (thousands of rows)",
        "Can work with structured data (CSV, tables)",
        "Easier to train and debug",
        "Examples: Spam filter, price prediction"
    ],
    "Deep Learning": [
        "Needs large data (millions of images or audio)",
        "Great for unstructured data (text, image, video)",
        "Harder to explain, but very powerful",
        "Examples: Face recognition, speech-to-text, GPT"
    ]
}

for model_type, points in ml_vs_dl.items():
    print(f"\n🧠 {model_type}:")
    for point in points:
        print(f" - {point}")