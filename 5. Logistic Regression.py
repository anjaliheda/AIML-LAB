import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris  

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def logistic_regression(X, y, lr=0.01, iterations=200):
    w = np.zeros(X.shape[1])  # Initialize weights
    for _ in range(iterations):
        w -= lr * np.dot(X.T, (sigmoid(np.dot(X, w)) - y)) / len(y)
    return w

# Load data
iris = load_iris()
X, y = iris.data[:, :2], (iris.target != 0).astype(int)

# Standardization
X = (X - X.mean(axis=0)) / X.std(axis=0)  

# Train logistic regression
w = logistic_regression(X, y)

# Predictions
y_pred = sigmoid(np.dot(X, w)) > 0.5
print(f'Accuracy: {np.mean(y_pred == y):.4f}')

# Decision boundary
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100), np.linspace(y_min, y_max, 100))
Z = sigmoid(np.dot(np.c_[xx.ravel(), yy.ravel()], w)) > 0.5
Z = Z.reshape(xx.shape)

plt.contourf(xx, yy, Z, alpha=0.3)
plt.scatter(X[:, 0], X[:, 1], c=y, edgecolors='k')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.title('Decision Boundary')
plt.savefig('plot.png')
