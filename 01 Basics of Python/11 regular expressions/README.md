# 🧠 Basics of Python: Regular Expressions (`re`)

This folder introduces the `re` module — used to search, match, clean, and validate patterns in text. In AI/ML, regex is especially useful in:
- NLP preprocessing (cleaning text)
- Validating user input (email, phone, ID)
- Extracting keywords or values from logs and documents

---

## 📌 Programs in This Folder

### 1. `1_search_and_match.py`

Covers:
- `re.search()` vs `re.match()`

Example:
```python
re.search("pattern", text)  # anywhere
re.match("pattern", text)   # only at start
```

💡 Used to detect presence of tokens, labels, keywords.

---

### 2. `2_findall_examples.py`

Covers:
- `re.findall()` to extract all matches

Example:
```python
re.findall(r"\S+@\S+\.\S+", text)
```

💡 Useful for bulk email, tag, or ID extraction.

---

### 3. `3_substitute_cleaning.py`

Covers:
- Cleaning or replacing content using `re.sub()`

Example:
```python
re.sub(r"\*+", "", text)
```

💡 Used in cleaning messy symbols, HTML tags, unwanted tokens.

---

### 4. `4_character_classes.py`

Covers:
- Special character classes: `\d`, `\w`, `\s`

Example:
```python
re.findall(r"\d+", text)  # digits
```

💡 Helps extract tokens by type (digits, words, spaces).

---

### 5. `5_character_sets_ranges.py`

Covers:
- `[A-Z]`, `[a-z]`, `[^...]` for custom matching

Example:
```python
re.findall(r"[^aeiou]", text)  # everything except vowels
```

---

### 6. `6_quantifiers_and_repeats.py`

Covers:
- Quantifiers like `+`, `*`, `?`, `{min,max}`

Example:
```python
re.findall(r"A\d{3,5}", text)
```

💡 Helps define pattern length, e.g., postal codes, token formats.

---

### 7. `7_raw_string_necessity.py`

Covers:
- Why we use `r""` for regex patterns

Example:
```python
r"\n"  # regex pattern, not newline
```

💡 Prevents escape character issues (`\\`, `\t`, `\n`).

---

### 8. `8_validate_email_phone.py`

Covers:
- Real-world validation using patterns

Example:
```python
re.match(r"\S+@\S+\.\S+", email)
```

💡 Useful in user-facing forms, APIs, text data validation.

---

## 🎯 Real-World Relevance in AI/ML

| Concept         | Use Case Example |
|-----------------|------------------|
| `findall()`     | Extracting values from text data |
| `sub()`         | Clean noisy input in NLP |
| `match()`       | Check label format or user input |
| Character sets  | Targeting specific classes of tokens |
| Quantifiers     | Match repeated tokens or sequences |
| Validation      | Email, phone, name filtering in datasets |

---

## 🧠 Interview Questions to Practice

1. What’s the difference between `match()` and `search()`?
2. Why do we use raw strings in regex?
3. How do you extract all email addresses from a string?
4. What does `\d+` mean in regex?
5. How do you clean symbols like `***` from a string?

---

## ✅ Tip

> Always test your regex on real examples. Use tools like [regex101.com](https://regex101.com) to visualize what each pattern does.

---

📁 **Next Topic:** [12 working with external libraries →](../12 working with external libraries/)