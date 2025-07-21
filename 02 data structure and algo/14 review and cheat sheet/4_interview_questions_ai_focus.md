# 🧠 AI-Focused DSA Interview Questions (With Short Answers)

This file summarizes the most important interview questions relevant to **AI/ML roles**, along with short, real-world answers.

---

## 🔹 Python & Logic Fundamentals

1. **What is the difference between a list and a tuple?**  
   → List = mutable, Tuple = immutable. Use tuples when values shouldn't change (e.g., config).

2. **How does a dictionary work internally?**  
   → Uses a hash table. Keys are hashed for constant-time (`O(1)`) access.

3. **How would you remove duplicates from a list of predictions?**  
   → Use `set()`: `list(set(my_list))` or loop with `seen = set()`.

4. **What’s the difference between `is` and `==` in Python?**  
   → `is` checks memory location (identity), `==` checks value.

5. **What happens if you modify a list while iterating over it?**  
   → Can lead to skipped or duplicated values. Always iterate over a copy: `my_list[:]`.

---

## 🔹 Searching

1. **When would you use binary search instead of linear search?**  
   → Binary for sorted data (O(log n)); linear for small/unsorted data (O(n)).

2. **How does Python’s `in` behave differently for a list vs. a set?**  
   → `list`: O(n), slow for large data. `set`: O(1), fast lookup using hashing.

3. **How do you find the index of a specific token in a list?**  
   → Use `.index(token)` — returns the first match or raises `ValueError`.

---

## 🔹 Sorting

1. **How do you sort a list of dictionaries by accuracy?**  
   → `sorted(models, key=lambda x: x['acc'], reverse=True)`

2. **What is a stable sort? Why does it matter?**  
   → Preserves original order of equal elements — useful in tie-breaking.

3. **How do you sort by multiple keys?**  
   → Use tuple: `sorted(data, key=lambda x: (-x['acc'], x['name']))`

---

## 🔹 Graphs & Trees

1. **What is BFS and where is it used?**  
   → Level-wise traversal using a queue. Used in NLP, token graphs, shortest path.

2. **BFS vs DFS (traversal/memory)?**  
   → BFS = queue, wide search, more memory. DFS = stack/recursion, deep search.

3. **How is a decision tree represented in memory?**  
   → Tree of nodes with left/right children, often as nested dicts or classes.

4. **How can you detect a cycle in a graph?**  
   → Use DFS + recursion stack or visited set.

5. **How are graphs used in transformers?**  
   → Attention mechanisms are graphs: tokens attend (connect) to others.

---

## 🔹 Recursion & DP

1. **Recursion vs Dynamic Programming?**  
   → Recursion solves problems by breaking them down.  
   → DP adds memoization/tabulation to avoid recomputation.

2. **Why is memoization fast?**  
   → Caches previously computed results; avoids duplicate work.

3. **Tabulation vs Recursion?**  
   → Tabulation = bottom-up (iterative), recursion = top-down. Tab = stack-safe.

4. **Climb stairs = NLP decode?**  
   → Yes, both are step-based decisions: from 1→n tokens or states.

5. **What is a subproblem?**  
   → A smaller instance of the problem you're solving — core to DP logic.

---

## 🔹 Real-World Case Studies

1. **How would you build a model leaderboard?**  
   → Use a list of dicts → sort by accuracy → show top-N.

2. **Need to deduplicate large dataset — what to use?**  
   → Use a `set()` or dict — fast and memory-efficient.

3. **How would you map tokens to embeddings?**  
   → Use a dictionary (token → ID), then use index to get embedding.

4. **Same function input used repeatedly — what to do?**  
   → Use `@lru_cache` or memoization to store and reuse output.

---

## ✅ Tip

> In AI/ML interviews, they test how you **apply logic**, not just write code.  
> Master **why** to use a data structure — that’s 90% of the win.

---
