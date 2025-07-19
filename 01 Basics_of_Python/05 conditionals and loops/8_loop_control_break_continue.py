# Using break and continue in a loop

for i in range(1, 6):
    if i == 3:
        continue  # skip number 3
    if i == 5:
        break     # stop at 5
    print("Number:", i)