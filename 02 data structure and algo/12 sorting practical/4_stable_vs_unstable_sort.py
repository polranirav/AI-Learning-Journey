# Demonstrate stable sorting (Python's sort is stable)
# 🔸 Useful when preserving order of equal elements is important

data = [
    ("model_A", 0.85),
    ("model_B", 0.85),
    ("model_C", 0.92)
]

# Sort by score only → 'model_A' should stay before 'model_B'
sorted_stable = sorted(data, key=lambda x: x[1])

for item in sorted_stable:
    print(item)