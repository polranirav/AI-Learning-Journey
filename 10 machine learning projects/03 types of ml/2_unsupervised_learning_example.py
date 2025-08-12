# 🧩 Unsupervised Learning – No labels, find patterns or groupings

from sklearn.cluster import KMeans
import numpy as np

# Height vs Weight dataset
X = np.array([[150, 50], [160, 60], [170, 65], [180, 80], [190, 90]])

kmeans = KMeans(n_clusters=2)
kmeans.fit(X)

print("📌 Cluster centers:", kmeans.cluster_centers_)
print("🧠 Cluster labels:", kmeans.labels_)  # Shows which cluster each point belongs to