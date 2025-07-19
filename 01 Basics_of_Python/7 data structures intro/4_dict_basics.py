# Dictionary: key-value storage

person = {
    "name": "Nirav",
    "age": 25,
    "is_student": True
}

print("Name:", person["name"])
print("Age:", person.get("age"))
print("Keys:", person.keys())
print("Values:", person.values())