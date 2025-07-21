# Create and access dictionary
person = {
    "name": "Nirav",
    "age": 25,
    "is_student": True
}

# Access
print("Name:", person["name"])

# Add new key
person["city"] = "Toronto"

# Update value
person["age"] = 26

# Delete key
del person["is_student"]

print(person)