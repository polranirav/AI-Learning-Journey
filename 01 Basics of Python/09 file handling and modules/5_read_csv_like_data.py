# Simulating reading dataset from CSV

with open("data.csv", "r") as file:
    for line in file:
        row = line.strip().split(",")
        print("Row:", row)