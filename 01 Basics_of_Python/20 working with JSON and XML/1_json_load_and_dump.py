import json

# Python dictionary
data = {
    "name": "Nirav",
    "age": 25,
    "skills": ["Python", "AI", "ML"]
}

# Write to JSON file
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)

# Read from JSON file
with open("data.json", "r") as f:
    loaded_data = json.load(f)

print("Loaded from file:", loaded_data)