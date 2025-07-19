# 🧠 Python: Math and Statistics Basics

This folder covers **core mathematical and statistical functions** used in AI/ML projects — from basic math to randomness and data summarization.

You’ll learn to:
- Normalize features
- Round probabilities
- Simulate sampling and randomness
- Calculate spread (variance, std dev)
- Avoid float precision errors

---

## 📌 Programs in This Folder

### 1. `1_math_module_basics.py`

Covers:
- Core math functions: `sqrt()`, `pow()`, `log()`, `ceil()`, `floor()`, `factorial()`

Example:
```python
math.sqrt(16), math.log10(1000)
```

💡 Used for feature scaling, exponentiation, or rounding scores in models.

---

### 2. `2_random_module_demo.py`

Covers:
- Random integer, float, shuffle, seed, and choice

Example:
```python
random.choice(["cat", "dog"]), random.seed(42)
```

💡 Simulate datasets, pick random samples, or shuffle training batches.

---

### 3. `3_statistics_module_demo.py`

Covers:
- Mean, median, mode, standard deviation, variance

Example:
```python
statistics.stdev(errors)
```

💡 Measure prediction error spread, outliers, or data distribution.

---

### 4. `4_decimal_module_demo.py`

Covers:
- High-precision decimal operations

Example:
```python
Decimal('1.10') + Decimal('2.30')
```

💡 Avoid float rounding errors — useful in financial or config-sensitive AI models.

---

### 5. `5_fraction_module_demo.py`

Covers:
- Exact value arithmetic using `Fraction`

Example:
```python
Fraction(1, 3) + Fraction(2, 5)
```

💡 Helps in symbolic AI, equation solving, or probability logic.

---

### 6. `6_ai_related_math_examples.py`

Covers:
- Apply all the above to real AI/ML use cases:

| Task                     | Function Used       |
|--------------------------|---------------------|
| Normalize feature        | `(x - min) / (max - min)` |
| Round probabilities      | `round()`           |
| Batch sampling           | `random.sample()`   |
| Error spread measurement | `statistics.stdev()` |

---

## 🎯 Real-World Relevance in AI/ML

| Topic       | Use Case |
|-------------|----------|
| `math`      | Feature transformations, loss scaling |
| `random`    | Shuffle data, pick batches |
| `statistics`| Analyze model results, errors |
| `decimal`   | Precise config/calculations |
| `fraction`  | Pure logic-based ML models (symbolic AI, math solvers) |

---

## 🧠 Interview Questions to Practice

1. What’s the difference between `round()` and `ceil()`?
2. Why is `random.seed()` important in ML experiments?
3. How do you measure spread in prediction errors?
4. When should you use `Decimal` over `float`?

---

## ✅ Tip

> Use `statistics` for fast insights, `random` for smart sampling, and `decimal` when even `0.1 + 0.2` can't be trusted.

---

📁 **Next Topic:** [19 virtual environment and pip →](../19 virtual environment and pip/)