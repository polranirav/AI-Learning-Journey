# ⚙️ Algorithms Summary (With AI Relevance)

This guide quickly summarizes the core algorithms you’ve learned — designed to help you recall when to use which one during AI pipelines, data handling, or interviews.

---

## 🔍 Searching Algorithms

| Algorithm       | Time       | When to Use                      | Pattern                        |
|------------------|------------|----------------------------------|--------------------------------|
| Linear Search     | O(n)       | Unsorted data, fallback scan     | Loop through all elements      |
| Binary Search     | O(log n)   | Sorted data                      | Divide & Conquer               |
| Hash Search (dict)| O(1)       | Fast token/label lookup          | `in`, `[]` access              |

---

## 🔃 Sorting Algorithms

| Algorithm       | Time     | When to Use                        | Pattern                        |
|-----------------|----------|------------------------------------|--------------------------------|
| Bubble Sort     | O(n²)    | Learning / Visualization only      | Repeated swaps                 |
| Merge Sort      | O(n log n)| Stable, safe sort (guaranteed)    | Divide → Sort → Merge          |
| Quick Sort      | O(n log n)| Best average case                  | Partition around pivot         |
| Built-in `sorted()` | O(n log n)| Production use (tuned C-level)   | Use with `key=` and `lambda`   |

---

## 🧠 Recursion + DP

| Concept           | Use Case                              | Pattern |
|-------------------|----------------------------------------|---------|
| Recursion         | Tree traversals, search, decode paths | Call self with smaller input |
| Memoization (Top-Down DP)| Avoid repeated subcalls (e.g. Fibonacci) | Store results in dict |
| Tabulation (Bottom-Up DP)| Efficient + stack safe (e.g. climb stairs) | Build result iteratively |

---

## 🌳 Tree / Graph Algorithms

| Algorithm         | Use Case                              | Pattern |
|-------------------|----------------------------------------|---------|
| Pre/In/Post Order | Tree traversal                        | Recursive DFS                |
| Level-Order (BFS) | Shortest path, layer-wise processing  | Queue + visited              |
| DFS (Graph)       | Explore paths, detect cycles          | Recursion + visited set      |
| BFS (Graph)       | Find shortest path                    | Queue + visited set          |
| Dijkstra          | Weighted shortest path (AI routing)   | Priority Queue (min-heap)    |

---

## 📊 Dynamic Programming Patterns (Classic AI-style)

| Problem Name        | Pattern Type       | Used In |
|---------------------|--------------------|---------|
| Fibonacci           | Overlapping subproblems | Token generation models |
| Climb Stairs        | Count combinations     | NLP sequence decode     |
| Subset Sum          | Include/Exclude binary decisions | Feature pruning, selection |
| Sequence Decode     | String-based DP       | Text-to-ID decoders, beam search |

---

## 🧠 Tip

> Learn to recognize **repetition** or **choice** — that’s your DP signal.  
> Use **recursion** when the problem feels "self-similar".