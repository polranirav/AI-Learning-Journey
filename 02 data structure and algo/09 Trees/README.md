# 🌳 Data Structure: Trees

This folder covers **binary trees** and **binary search trees (BST)** — fundamental structures used in AI/ML for:

- Decision Trees (classification/regression)
- Parsing syntax in NLP
- File system & JSON parsing
- Search and rule-based logic

---

## 📌 Programs in This Folder

### 1. `1_tree_node_structure.py`

Defines a basic tree node using a Python class.

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
```

💡 Foundation for all tree-based models.

---

### 2. `2_tree_traversal_pre_in_post.py`

Demonstrates:
- Preorder (Root → Left → Right)
- Inorder (Left → Root → Right)
- Postorder (Left → Right → Root)

```python
def preorder(node): print → left → right
def inorder(node):  left → print → right
def postorder(node): left → right → print
```

💡 Used in expression evaluation, tree printing, parsing logic.

---

### 3. `3_tree_traversal_level_order.py`

Level-order (BFS) using queue.

```python
from collections import deque
while queue:
    node = queue.popleft()
```

💡 Used in decision tree inference and tree structure serialization.

---

### 4. `4_binary_search_tree_insert_search.py`

Builds a BST and searches for a value.

```python
if key < root.val: go left
elif key > root.val: go right
```

💡 Great way to learn recursive thinking and efficient search logic.

---

### 5. `5_bst_min_max_depth.py`

Calculates:
- Minimum depth (shortest path to leaf)
- Maximum depth (longest path)

```python
min = 1 + min(left, right)
max = 1 + max(left, right)
```

💡 Used in model pruning, depth control, and complexity evaluation.

---

### 6. `6_tree_path_sum_check.py`

Checks if a path from root to leaf adds up to a target sum.

```python
target = target - node.val
check both left and right paths
```

💡 Common in AI where decision paths are scored.

---

### 7. `7_tree_real_ai_usecase.py`

Simulates a **decision tree** for "Buy vs Don't Buy" logic.

```python
class DecisionNode:
    question, left, right
```

💡 Real-world analogy to scikit-learn's `DecisionTreeClassifier`.

---

## 🎯 Real-World Relevance in AI/ML

| Concept             | AI Use Case |
|---------------------|-------------|
| Binary Tree         | Expression parsing, syntax trees |
| Binary Search Tree  | Sorted lookup, structure building |
| Level-order (BFS)   | Model serialization, graph traversal |
| Decision tree       | Classification and logic flows |
| Tree depth          | Model complexity and pruning control |

---

## 🧠 Interview Questions to Practice

1. What is the difference between BST and a normal binary tree?
2. How do you implement preorder and postorder traversal?
3. What are real-world uses of tree traversal in ML or NLP?
4. How does depth affect performance in decision trees?

---

## ✅ Tip

> Think of trees as "structured decisions."  
> Every node can represent a rule, decision, or config — exactly like AI pipelines or control logic.

---

📁 **Next Topic:** [10 graphs →](../10 graphs/)