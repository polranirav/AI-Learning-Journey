# Detect duplicate values using a set
# 🔸 Common use in AI: remove duplicate labels, features, IDs

def find_duplicates(arr):
    seen = set()
    duplicates = set()

    for val in arr:
        if val in seen:
            duplicates.add(val)
        else:
            seen.add(val)

    return list(duplicates)

data = [1, 2, 3, 2, 4, 5, 1]
print("Duplicates:", find_duplicates(data))