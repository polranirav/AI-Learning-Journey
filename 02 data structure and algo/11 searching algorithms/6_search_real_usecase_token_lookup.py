# AI Use-Case: Fast token/label lookup using dictionary
# 🔸 Used in tokenizers, model output label mapping, configs

token_to_index = {
    "<PAD>": 0,
    "<START>": 1,
    "<END>": 2,
    "hello": 3,
    "world": 4
}

# Simulate sentence token lookup
sentence = ["<START>", "hello", "world", "<END>"]
indexed = [token_to_index[token] for token in sentence]

print("Original:", sentence)
print("Token IDs:", indexed)

# Fast O(1) lookups due to dictionary use