# 📊 NumPy Beginner to Pro – Complete Guide

This guide covers everything from basic NumPy array creation to advanced manipulations, broadcasting, matrix operations, slicing, and more. All examples are written in Python using NumPy and are accompanied by explanations and outputs.

---

## ✅ 1. Import NumPy

```python
import numpy as np
```

---

## 🔢 2. Basic Array Creation

```python
arr = np.array([1, 2, 3, 4])
```

Create a 1D array using a list.

```python
a = [1, 2, 3.5]
np.array(a)
# Output: array([1. , 2. , 3.5])
```

Automatic upcasting to float64.

```python
l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
np.array(l)
# Output: 3x3 matrix
```

---

## 🔁 3. Array Generation Functions

```python
np.arange(1, 11, 2)
# Output: array([1, 3, 5, 7, 9])
```

```python
np.zeros((4, 8))
# Output: 4x8 matrix of 0.0
```

```python
np.ones((6, 6))
# Output: 6x6 matrix of 1.0
```

```python
np.linspace(0, 1, 100)
# Output: 100 equally spaced values from 0 to 1
```

---

## 🎲 4. Random Generation Functions

```python
np.random.rand(10)
# Output: 10 random values from uniform dist [0, 1)
```

```python
np.random.randn(10)
# Output: 10 values from standard normal distribution
```

```python
np.random.randint(10, 20, 10)
# Output: 10 random integers between 10 and 20
```

---

## 🔍 5. Array Attributes

```python
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
arr.shape    # Output: (3, 3)
arr.size     # Output: 9
arr.dtype    # Output: dtype('int64')
```

---

## ⚙️ 6. Array Methods

```python
arr.min()          # Output: 1
arr.max()          # Output: 9
arr.sum()          # Output: 45
arr.mean()         # Output: 5.0
arr.std()          # Output: ~2.58
arr.argmax()       # Output: 8 (index of 9)
arr.argmin()       # Output: 0 (index of 1)
np.sum(arr, axis=1) # Output: Row-wise sum
```

---

## 🔄 7. Reshaping Arrays

```python
arr = np.arange(1, 31)
arr = arr.reshape(6, 5)
# Output: 6x5 matrix
```

---

## ✂️ 8. Indexing and Slicing – Vectors

```python
arr = np.arange(11, 21)
arr[4]       # Output: 15
arr[3::2]    # Output: array([14, 16, 18, 20])
```

---

## 🧱 9. Indexing and Slicing – Matrices

```python
arr = np.arange(1, 31).reshape(6, 5)
arr[3:, 3:]     # Output: bottom-right 3x2 matrix
arr[:, 2]       # Output: 3rd column
```

---

## 🧪 10. Boolean Indexing

```python
arr = np.arange(11, 21)
bool_index = arr % 2 == 0
arr[bool_index]
# Output: array([12, 14, 16, 18, 20])
```

---

## ➕ 11. Arithmetic Operations

```python
a1 = np.array([1, 2, 3, 4, 5])
a2 = np.array([6, 7, 8, 9, 10])
a1 + a2         # Output: array([ 7,  9, 11, 13, 15])
a1 - a2         # Output: array([-5, -5, -5, -5, -5])
a1 * a2         # Output: array([ 6, 14, 24, 36, 50])
a1 / a2         # Output: array([...])
a1 // a2        # Output: array([0, 0, 0, 0, 0])
a1 ** a2        # Output: Exponential values
```

---

## 🚀 12. Broadcasting

```python
arr = np.array([10, 20, 30, 40])
arr + 10
# Output: array([20, 30, 40, 50])
```

```python
arr2 = np.arange(1, 26).reshape(5, 5)
arr2 = arr2 + 10
# Output: All values incremented by 10
```

---

## 🧠 13. Deep vs Shallow Copy

```python
a = np.arange(1, 21)
slice = a[:5] * 10
# a remains unchanged
```

```python
b = a.copy()
b[0] = 99
# Only b changes
```

---

## 🧮 14. Matrix Operations

```python
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
np.dot(A, B)
# Output: array([[19, 22], [43, 50]])
```

```python
A.T
# Output: array([[1, 3], [2, 4]])
```

---

## 🧱 15. Stacking Arrays

```python
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
np.vstack((a, b))
np.hstack((a, b))
np.column_stack((a, b))
```

---

## ✂️ 16. Splitting Arrays

```python
c = np.arange(16).reshape(4, 4)
np.hsplit(c, 4)
np.vsplit(c, 2)
```

---

## 🧠 17. Real-World Use Cases in AI/ML

| NumPy Concept       | Real Use in AI/ML                          |
|---------------------|--------------------------------------------|
| Array reshaping      | Prepare image/text data for models        |
| Broadcasting         | Normalize or scale feature vectors        |
| Boolean indexing     | Data filtering and mask generation        |
| Dot product          | Forward pass in neural networks           |
| Transpose            | Matrix gradient flow in backpropagation   |
| Splitting/stitching  | Batch prep / training-testing pipelines   |

---

## 🧪 18. Interview Tips

- ✅ Understand axis-based operations clearly.
- ✅ Always remember: slicing returns views unless you `.copy()`.
- ✅ Know `dot`, `reshape`, `transpose`, `argmax`, etc.
- ✅ Practice slicing and conditional filters (boolean indexing).
- ✅ Use broadcasting wisely to avoid loops.

---


---