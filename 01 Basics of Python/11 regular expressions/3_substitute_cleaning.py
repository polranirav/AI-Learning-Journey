import re

raw_text = "This is ***awesome*** and very ***cool***."

# Replace *** with nothing
cleaned = re.sub(r'\*+', '', raw_text)
print("Cleaned text:", cleaned)