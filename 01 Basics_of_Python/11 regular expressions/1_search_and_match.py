import re

text = "Welcome to Nirav's AI course"

# search: finds pattern anywhere
found = re.search("Nirav", text)
print("Search result:", found)

# match: only checks from start of string
match = re.match("Welcome", text)
print("Match result:", match)