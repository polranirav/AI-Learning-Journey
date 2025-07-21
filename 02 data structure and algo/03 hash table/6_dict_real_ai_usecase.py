# Mapping class labels for classification model

label_map = {
    0: "Cat",
    1: "Dog",
    2: "Elephant"
}

predictions = [0, 2, 1, 1, 0]

# Convert predictions to class names
translated = [label_map[p] for p in predictions]

print("Predicted Labels:", translated)