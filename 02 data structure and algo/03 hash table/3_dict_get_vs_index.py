config = {
    "lr": 0.001,
    "batch_size": 32
}

# Unsafe access (raises KeyError if missing)
# print(config["dropout"])

# Safe access
dropout = config.get("dropout", 0.5)  # default fallback
print("Dropout:", dropout)