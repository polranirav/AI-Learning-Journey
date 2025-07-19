# Reading contents of a file

file = open("sample.txt", "r")
content = file.read()
print("Full content:\n", content)
file.close()

# To read line by line
file = open("sample.txt", "r")
for line in file:
    print("Line:", line.strip())
file.close()