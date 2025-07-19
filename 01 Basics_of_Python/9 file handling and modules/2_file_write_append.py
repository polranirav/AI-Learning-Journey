# Writing and appending to a file

# Overwrites existing content
file = open("output.txt", "w")
file.write("This is a fresh write.\n")
file.close()

# Appends to the file
file = open("output.txt", "a")
file.write("This line was appended.\n")
file.close()