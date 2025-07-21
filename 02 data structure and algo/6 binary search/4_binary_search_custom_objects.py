# Binary search on a list of tuples by a specific key

def search_by_score(data, target_score):
    low, high = 0, len(data) - 1

    while low <= high:
        mid = (low + high) // 2
        score = data[mid][1]

        if score == target_score:
            return data[mid]
        elif score < target_score:
            low = mid + 1
        else:
            high = mid - 1

    return None

students = [("Nirav", 50), ("Ravi", 60), ("Mira", 70), ("Deep", 80)]
print("Search Score 70:", search_by_score(students, 70))  # ('Mira', 70)