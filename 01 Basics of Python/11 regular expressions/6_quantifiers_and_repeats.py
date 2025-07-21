import re

text = "AA123, A1234, AB12345"

# Match 'A' followed by 3 to 5 digits
pattern = r'A\d{3,5}'

results = re.findall(pattern, text)
print("Matches:", results)