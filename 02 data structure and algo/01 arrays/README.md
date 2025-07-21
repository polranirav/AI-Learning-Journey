# 📦 Arrays – Python & NumPy for AI/ML

This folder covers the most essential array concepts needed for AI/ML engineering — especially for batch processing, image data, and vectorized computations.

Python’s native lists are flexible, but NumPy arrays are faster and more memory-efficient for ML tasks.

---

## 📌 Programs in This Folder

### 1. `1_list_vs_array.py`

Covers:
- Difference between Python `list` and NumPy `array`
- Broadcast behavior in NumPy

💡 NumPy arrays allow fast element-wise math (`+1`, `*2`) which lists can't.

---

### 2. `2_array_creation_and_access.py`

Covers:
- Create 1D and 2D arrays
- Indexing and slicing basics

💡 Use slicing to extract features, columns, rows in data batches.

---

### 3. `3_array_insertion_deletion.py`

Covers:
- Insert and delete values in arrays using `np.insert()` and `np.delete()`

💡 Helps when pre-cleaning or updating feature arrays.

---

### 4. `4_array_searching_and_indexing.py`

Covers:
- Use `np.where()` to find values
- Check value presence in arrays

💡 Useful in thresholding, label finding, and category matching.

---

### 5. `5_array_iteration_patterns.py`

Covers:
- Looping with `for`, `enumerate`
- Vectorized alternative (faster)

💡 Iteration is common for data cleaning, masking, or batch annotation.

---

### 6. `6_numpy_vectorization_basics.py`

Covers:
- Vectorized operations without using loops
- Feature normalization example

💡 Core of ML model input scaling and fast computation.

---

### 7. `7_ai_array_usecase_image_data.py`

Covers:
- Represent image as 2D array
- Normalize pixel values
- Access specific pixels

💡 This is the base of image classification, object detection, and vision models.

---

## 🎯 Why Arrays Matter in AI/ML

| Use Case            | How Arrays Help |
|---------------------|------------------|
| Dataset handling     | Rows = samples, Columns = features |
| Image inputs         | 2D/3D arrays used in CNNs |
| Batch normalization  | Min-max or z-score with NumPy |
| Vectorized training  | Fast math on weight vectors |
| Model output         | Predictions as arrays (logits, labels) |

---

## ✅ Tip

> Always prefer **NumPy arrays** over Python lists when working with numerical or structured AI data.

---

📁 **Next Topic:** [2 linked list →](../02%20linked%20list/)