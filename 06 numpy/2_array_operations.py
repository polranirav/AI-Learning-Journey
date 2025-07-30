import numpy as np

# 🎯 Create two sample arrays — think of them as model outputs or input features
a = np.array([1, 2, 3])
b = np.array([10, 20, 30])

# ➕ Element-wise addition — useful for combining signals, scores
print("a + b =", a + b)  # [11 22 33]

# ✖️ Element-wise multiplication — scale-wise multiplication of weights/features
print("a * b =", a * b)  # [10 40 90]

# 🔁 Scalar operations — scale the whole feature vector
print("a * 2 =", a * 2)  # [2 4 6]

# 🔢 Statistical operations — useful for analyzing model output
print("Mean of a:", np.mean(a))  # 2.0
print("Standard Deviation of a:", np.std(a))  # ~0.82

# ⚙️ Dot product — used in neural nets, projections, similarity checks
print("Dot product of a and b:", np.dot(a, b))  # 1*10 + 2*20 + 3*30 = 140

#adding array
