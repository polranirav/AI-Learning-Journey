# Using with-open (auto handles closing)

with open("auto.txt", "w") as file:
    file.write("Safe write using 'with'.\n")

with open("auto.txt", "r") as file:
    print(file.read())