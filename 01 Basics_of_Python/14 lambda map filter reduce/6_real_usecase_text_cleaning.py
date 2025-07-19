# Example: Clean up list of messy strings using lambda + map + filter

raw_text = [" Hello ", "  ", "World!", "", " AI  "]

# Step 1: Strip whitespace
cleaned = list(map(lambda x: x.strip(), raw_text))

# Step 2: Remove empty strings
filtered = list(filter(lambda x: x != "", cleaned))

print("Cleaned Text List:", filtered)