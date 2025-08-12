# 🧠 Project 3: Types of Machine Learning – Supervised, Unsupervised, Reinforcement

This folder introduces the **3 core types of Machine Learning** with real-world examples and Python programs. These are foundational for AI engineers and often asked in interviews.

---

## 📌 Programs in This Folder

### ✅ `1_supervised_learning_example.py`

```python
# 🧠 Supervised Learning – Learn from labeled data (inputs + known outputs)

from sklearn.linear_model import LinearRegression
import numpy as np

# Experience vs Salary data
X = np.array([[1], [2], [3], [4], [5]])  # Input: years of experience
y = np.array([30000, 35000, 40000, 45000, 50000])  # Output: salary

model = LinearRegression()
model.fit(X, y)

# Predict salary for 6 years of experience
predicted_salary = model.predict([[6]])
print(f"📊 Predicted salary for 6 years: ${predicted_salary[0]:.2f}")
```

**Used in:**
- Price prediction, sentiment analysis, medical diagnosis

---

### ✅ `2_unsupervised_learning_example.py`

```python
# 🧩 Unsupervised Learning – No labels, just structure and pattern discovery

from sklearn.cluster import KMeans
import numpy as np

# Height vs Weight
X = np.array([[150, 50], [160, 60], [170, 65], [180, 80], [190, 90]])

kmeans = KMeans(n_clusters=2)
kmeans.fit(X)

print("📌 Cluster centers:", kmeans.cluster_centers_)
print("🧠 Cluster labels:", kmeans.labels_)
```

**Used in:**
- Customer segmentation, anomaly detection, topic modeling

---

### ✅ `3_reinforcement_learning_text_demo.py`

```python
# 🎮 Reinforcement Learning – Learn from rewards (Trial and Error)

print("🏀 Imagine training a robot to shoot a basketball:")
print("- It gets +1 reward if it scores, -1 if it misses.")
print("- Over time, it learns the best angle and force to shoot accurately.")

print("\nThis is Reinforcement Learning (RL):")
print("✔️ Agent takes actions")
print("✔️ Gets rewards or penalties")
print("✔️ Learns from experience to maximize total reward.")
```

**Used in:**
- Game bots (AlphaGo), robotics, self-driving cars, trading bots

---

## 🧠 Real-World AI/ML Relevance

| Type                | Description                               | Real AI Use Case |
|---------------------|--------------------------------------------|------------------|
| Supervised Learning | Learn from labeled data                   | Fraud detection, price prediction |
| Unsupervised        | Discover hidden structure in unlabeled data | Customer grouping, clustering |
| Reinforcement       | Learn via feedback from environment        | Game AI, robot navigation |

---

## 💬 Interview Questions

1. What’s the difference between Supervised and Unsupervised learning?
2. Can you name real-world use cases for each type?
3. Why is reinforcement learning harder to implement in basic projects?
4. Which ML type is most commonly used in business applications?

---

## ✅ Tip

> In most real-world AI systems:  
> - You’ll start with **Supervised Learning**  
> - Add **Unsupervised** for insights & pre-clustering  
> - And use **Reinforcement** in advanced robotics or agents.

---

📁 **Next Topic:** [`4 eda`](../04%20eda/)