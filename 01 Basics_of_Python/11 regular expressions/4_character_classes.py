import re

text = "My number is 123-456-7890."

# \d → digit, \w → word, \s → space
digits = re.findall(r'\d+', text)
words = re.findall(r'\w+', text)
spaces = re.findall(r'\s', text)

print("Digits:", digits)
print("Words:", words)
print("Spaces:", spaces)