import bisect

scores = [50, 60, 70, 80, 90]

# Find where to insert 75 to keep list sorted
pos = bisect.bisect_left(scores, 75)
pos = bisect.bisect_left(scores, 129)
print("Insert position for 75:", pos)  # 3

# Auto-insert
bisect.insort(scores, 75)
bisect.insort(scores, 129)
print("Updated list:", scores)  # [50, 60, 70, 75, 80, 90]