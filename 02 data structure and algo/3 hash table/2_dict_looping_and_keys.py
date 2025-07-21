student = {
    "name": "Nirav",
    "marks": {"math": 85, "ai": 90}
}

# Loop through keys
for key in student:
    print("Key:", key)

# Loop through items
for subject, score in student["marks"].items():
    print(f"{subject.title()} → {score}")