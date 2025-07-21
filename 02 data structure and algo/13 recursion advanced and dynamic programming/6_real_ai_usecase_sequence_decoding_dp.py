# AI Use Case: Sequence decoding using memoized recursion
# 🔸 Similar to token decoding in LSTM/GRU or beam search

# Given digits (like Morse or encodings), count valid decodings
# E.g., '111' → "AAA", "KA", "AK" → 3 ways

def count_decodings(s, memo={}):
    if s in memo:
        return memo[s]
    if not s:
        return 1
    if s[0] == '0':
        return 0

    # Decode single digit
    total = count_decodings(s[1:], memo)

    # Decode two digits if valid (<= 26)
    if len(s) >= 2 and int(s[:2]) <= 26:
        total += count_decodings(s[2:], memo)

    memo[s] = total
    return total

print("Decoding ways for '111':", count_decodings("111"))  # Output: 3