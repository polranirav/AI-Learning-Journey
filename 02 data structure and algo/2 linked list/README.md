# 🧠 Data Structures: Linked List

This folder introduces the **singly linked list**, a foundational concept in computer science that teaches how to manage data in a non-contiguous memory layout using nodes and pointers.

While raw linked lists are rarely used in AI/ML production code, their logic helps in:
- Understanding recursion
- Building traversal logic for trees, graphs, and sequences
- Handling custom streaming data or dynamic structures

---

## 📌 Programs in This Folder

### 1. `1_singly_linked_list_basics.py`

Creates a basic linked list and prints it.

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

ll = LinkedList()
ll.append("data")
ll.append("prep")
ll.append("done")
ll.print_list()
```

---

### 2. `2_linked_list_insertion.py`

Insert a new node at a given index.

```python
ll.insert_at(0, "first")
ll.insert_at(1, "inserted")
ll.insert_at(2, "last")
ll.print_list()
```

---

### 3. `3_linked_list_deletion.py`

Remove a node from the list using its index.

```python
ll.delete_at(1)  # Deletes the second element
ll.print_list()
```

---

### 4. `4_reverse_linked_list.py`

Reverse the entire linked list using pointer flipping.

```python
new_head = reverse_linked_list(head)
# Output: C → B → A → None
```

---

### 5. `5_linked_list_to_array_conversion.py`

Converts a linked list to a Python list.

```python
def to_array(head):
    result = []
    while head:
        result.append(head.value)
        head = head.next
    return result
```

---

## 🎯 Real-World Relevance in AI/ML

| Concept              | Use Case |
|----------------------|----------|
| Linked traversal     | Basis for exploring trees and graphs |
| Reversing a list     | Used in decoding or time-sequence reversal |
| Dynamic insertion    | Applies to queues, buffers, data pipes |
| Memory structure     | Builds understanding of token graphs or pointer-chained models |

---

## 🧠 Interview Questions to Practice

1. What is the difference between an array and a linked list?
2. How does insertion work in a linked list?
3. How would you reverse a linked list without using extra space?

---

## ✅ Tip

> Even if you don’t use linked lists in practice, understanding them **builds muscle for recursion, trees, and token chains** — all of which are critical in AI workflows.

---

📁 **Next Topic:** [3 hash table →](../3 hash table/)