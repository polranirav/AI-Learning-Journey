# 🧠 Data Structures: Graphs

This folder covers the fundamentals of **graphs**, a powerful data structure used heavily in AI/ML and modern NLP.  
Graphs represent relationships between items — like tokens, users, layers, or knowledge.

---

## 📌 Programs in This Folder

### 1. `1_graph_adjacency_list.py`

Defines a graph using a Python dictionary (`Adjacency List` format).

```python
graph = {
    "A": ["B", "C"],
    "B": ["D"],
    ...
}
```

💡 Use this when modeling relationships — such as attention weights, user connections, or decision paths.

---

### 2. `2_bfs_graph_traversal.py`

Breadth-First Search (BFS) traversal using a queue.

```python
from collections import deque
queue = deque([start])
while queue:
    node = queue.popleft()
```

🔁 BFS is great for level-wise exploration: 
- Shortest path problems
- Transformer token layer traversal
- Social network reach

---

### 3. `3_dfs_graph_traversal.py`

Depth-First Search (DFS) using recursion.

```python
def dfs(node):
    visited.add(node)
    for neighbor in graph[node]:
        dfs(neighbor)
```

📌 DFS is useful for:
- Searching deep hierarchies
- Parsing nested structures (e.g. syntax trees)

---

### 4. `4_detect_cycle_in_graph.py`

Detects cycles in a **directed graph** using DFS and a recursion stack.

```python
if neighbor in rec_stack:
    return True
```

🚨 Useful for:
- Dependency graph validation
- Avoiding infinite loops in logical rules or workflows

---

### 5. `5_dijkstra_shortest_path.py`

Implements **Dijkstra's Algorithm** to find the shortest path in a weighted graph.

```python
import heapq
heapq.heappush(pq, (distance, neighbor))
```

🚗 AI Use Case:
- Optimizing path in autonomous systems
- Recommender engines: "nearest neighbor"

---

### 6. `6_real_ai_usecase_graph_attention.py`

Simulates **token attention graph** (like in GPT transformers).

```python
Token1 → [Token2, Token3]
Token2 → [Token4]
```

🧠 Great for understanding attention flows, token dependencies, or multi-head attention modeling.

---

## 🎯 Real-World Relevance in AI/ML

| Graph Concept        | AI/ML Use Case |
|----------------------|----------------|
| BFS / DFS            | Tree traversal, dependency parsing |
| Adjacency list       | Token relationship graphs, configs |
| Dijkstra's algorithm | Optimized search, recommendation |
| Cycle detection      | Graph validation in pipelines |
| Attention graph      | Transformer token modeling (LLMs) |

---

## 🧠 Interview Questions to Practice

1. What is the difference between BFS and DFS? Where are they used?
2. How do you detect a cycle in a directed graph?
3. How does Dijkstra's algorithm differ from BFS?
4. What is the real-world example of graphs in machine learning?

---

## ✅ Tip

> Every **attention layer**, **NLP dependency graph**, and **social network** is a graph.  
> If you master traversal + search, you can optimize a lot of AI/ML flows.

---

📁 **Next Topic:** [11 searching algorithms →](../11 searching algorithms/)