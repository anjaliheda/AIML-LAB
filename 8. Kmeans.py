import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris()
X = iris.data  # Features (sepal length, sepal width, petal length, petal width)

def kmeans(X, k):
    centroids = X[np.random.choice(X.shape[0], k, replace=False)]

    for _ in range(100):  # Iterating for 100 steps
        distances = np.linalg.norm(X[:, None] - centroids, axis=2)
        labels = np.argmin(distances, axis=1)
        centroids = np.array([X[labels == i].mean(axis=0) for i in range(k)])

    return centroids, labels

# Take user input for the number of clusters
k = int(input("Enter the number of clusters (e.g., 3): "))

# Apply custom k-means clustering
centroids, labels = kmeans(X, k)

# Plot the data points with different colors for each cluster
plt.figure(figsize=(8, 6))
for i in range(k):
    plt.scatter(X[labels == i, 0], X[labels == i, 1], label=f'Cluster {i+1}')

# Plot the centroids
plt.scatter(centroids[:, 0], centroids[:, 1], marker='x', c='black', label='Centroids')

plt.title(f'K-Means Clustering (k={k})')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.legend()
plt.show()
