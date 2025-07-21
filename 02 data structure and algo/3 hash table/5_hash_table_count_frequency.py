# Count frequency of items in a list

words = ["ai", "ml", "ai", "cv", "nlp", "ml", "ml"]
freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

print("Frequency:", freq)