# 🧠 Recursion & Dynamic Programming (DP)

This folder teaches how to solve problems by breaking them into smaller subproblems — a pattern that's everywhere in AI/ML:

- Decoding sequences (LSTM/GRU)
- Beam search & token generation
- Subset selection
- Optimizing overlapping logic

---

## 📌 Programs in This Folder

### 1. `1_factorial_recursive_vs_loop.py`

Compares recursion vs iteration.

```python
# Recursive: n * f(n-1)
# Iterative: loop from 2 to n
```

📌 Helps you understand base cases and recursive flow.

---

### 2. `2_fibonacci_recursive_memoized.py`

Shows:
- Pure recursion → slow
- Memoization → fast

```python
memo[n] = fib(n-1) + fib(n-2)
```

💡 Useful in NLP, sequence modeling, and decoding.

---

### 3. `3_climb_stairs_dp.py`

Classic DP: how many ways to reach the top?

```python
dp[i] = dp[i-1] + dp[i-2]
```

💡 Similar to token sequence decisions in autoregressive models.

---

### 4. `4_subset_sum_recursive_vs_dp.py`

Solves subset sum problem via:
- Recursion (all paths)
- DP table (fast)

```python
dp[i][j] = include or exclude
```

💡 Used in feature combination, model pruning, config selection.

---

### 5. `5_dp_tabulation_vs_memoization.py`

Compares:
- Memoization (Top-down)
- Tabulation (Bottom-up)

```python
Tab: build array from 0→n
Memo: cache results from n→0
```

📌 Choose based on problem size and stack depth.

---

### 6. `6_real_ai_usecase_sequence_decoding_dp.py`

Simulates token decoding (like “111” = "AAA", "KA", "AK")

```python
count(s[1:]) + count(s[2:]) if int(s[:2]) <= 26
```

💡 Mirrors sequence decoding logic in NLP (e.g., “how many ways can we decode this input?”)

---

## 🎯 Real-World Relevance in AI/ML

| Concept        | AI/ML Use Case |
|----------------|----------------|
| Recursion      | Tree traversal, grammar parsing, backtracking |
| Memoization    | Caching token scores, avoiding recomputation |
| Tabulation     | Optimized decoding, cost-based planning |
| Subset logic   | Feature filtering, constraint satisfaction |
| Stairs/fib     | Step-based decision flows, state transitions |

---

## 🧠 Interview Questions to Practice

1. What’s the difference between recursion and DP?
2. How does memoization help performance?
3. When do you prefer tabulation over recursion?
4. How does decoding logic in NLP relate to stairs/fib problems?

---

## ✅ Tip

> If a problem has **repeated sub-steps** → use **DP**.  
> If it's **nested or self-similar** → think **recursion**.

---

📁 **Next Topic:** [14 review and cheat sheet →](../14 review and cheat sheet/)