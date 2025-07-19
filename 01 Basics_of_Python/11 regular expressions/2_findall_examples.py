import re

text = "Emails: user1@example.com, test.user@company.co.in"

# findall: return all matches
emails = re.findall(r'\S+@\S+\.\S+', text)
print("Found emails:", emails)