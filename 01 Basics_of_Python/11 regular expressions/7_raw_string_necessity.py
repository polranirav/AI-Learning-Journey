import re

pattern_normal = "\\n"    # becomes newline
pattern_raw = r"\n"       # stays as \n (pattern)

print("Normal:", pattern_normal)
print("Raw:", pattern_raw)

text = "Line1\nLine2"
found = re.findall(r"\n", text)
print("Newlines found:", found)