# Safely read a file with error handling

try:
    with open("nonexistent.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("The file does not exist.")