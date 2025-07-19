import re

text = "Hello AI123"

# Match only uppercase letters
uppercase = re.findall(r'[A-Z]', text)

# Match only lowercase
lowercase = re.findall(r'[a-z]', text)

# Match all letters except vowels
no_vowels = re.findall(r'[^aeiouAEIOU]', text)

print("Uppercase:", uppercase)
print("Lowercase:", lowercase)
print("No vowels:", no_vowels)