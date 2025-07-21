# 🧠 Data Structures: Hash Table (Python Dictionary)

This folder focuses on **hash tables** using Python’s built-in `dict` — one of the most important data structures in AI/ML projects.

Hash tables store data as **key-value pairs** and are used in:
- Feature mappings
- Token-to-ID lookups
- Frequency counts
- Model config storage
- Label translation

---

## 📌 Programs in This Folder

### 1. `1_dict_basics.py`

Creates and modifies a dictionary.

```python
person = {"name": "Nirav", "age": 25}
person["city"] = "Toronto"
person["age"] = 26
del person["is_student"]  # safely remove key if exists
```

---

### 2. `2_dict_looping_and_keys.py`

Loop through keys and nested values.

```python
for key in student:
    print(key)

for subject, score in student["marks"].items():
    print(f"{subject} → {score}")
```

---

### 3. `3_dict_get_vs_index.py`

Safely access values with `.get()` (avoids KeyError).

```python
dropout = config.get("dropout", 0.5)
print(dropout)  # prints 0.5 if "dropout" key is missing
```

---

### 4. `4_dict_nested.py`

Nested dictionaries used in real-world model configs.

```python
model_result = {
  "metrics": {"f1_score": 0.88},
  "params": {"n_estimators": 100}
}
```

---

### 5. `5_hash_table_count_frequency.py`

Count frequency of labels or tokens.

```python
freq[word] = freq.get(word, 0) + 1
```

💡 Used in NLP, classification labels, log parsing, etc.

---

### 6. `6_dict_real_ai_usecase.py`

Map model predictions to readable class labels.

```python
label_map = {0: "Cat", 1: "Dog"}
translated = [label_map[p] for p in predictions]
```

---

### 7. `7_dict_update_and_merge.py`

Shows two ways to merge dictionaries with overriding order.

```python
config_a = {"lr": 0.01, "epochs": 10}
config_b = {"batch_size": 32, "lr": 0.001}

final_config = {**config_a, **config_b}   # 'lr' from config_b
finalss_config = {**config_b, **config_a} # 'lr' from config_a

print(final_config)
print(finalss_config)
```

---

## 🎯 Real-World Relevance in AI/ML

| Concept       | AI/ML Use Case |
|----------------|------------------|
| Key-value store | Token-to-index, label mapping |
| `.get()`       | Avoid crashing during config parsing |
| Frequency dict | NLP token counts, class distribution |
| Nested dict    | Save model configs, metrics |
| Merge dicts    | Combine pipeline configs, override defaults |

---

## 🧠 Interview Questions to Practice

1. What is a hash table, and why is it fast?
2. What’s the difference between `dict.get()` and direct indexing?
3. How can you merge two dictionaries in Python 3.5+?
4. How would you store and access nested model parameters?

---

## ✅ Tip

> Hash tables (`dict`) are **used everywhere in ML** — from configs to prediction labels. Master them early and use them cleanly.

---

📁 **Next Topic:** [4 stack and queue →](../04%20stack%20and%20queue/)