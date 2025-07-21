import re

email = "test.user@example.com"
phone = "987-654-3210"

# Very basic patterns
email_pattern = r'^\S+@\S+\.\S+$'
phone_pattern = r'^\d{3}-\d{3}-\d{4}$'

print("Valid email:", bool(re.match(email_pattern, email)))
print("Valid phone:", bool(re.match(phone_pattern, phone)))