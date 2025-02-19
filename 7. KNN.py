from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import numpy as np
from collections import Counter

# Load iris dataset
iris = load_iris()
X, y = iris.data, iris.target
class_names = iris.target_names

# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

class KNN:
    def __init__(self, k=3):
        self.k = k

    def fit(self, X, y):
        self.X_train = X
        self.y_train = y

    def predict(self, X):
        return np.array([self._predict(x) for x in X])

    def _predict(self, x):
        distances = [np.linalg.norm(x - x_train) for x_train in self.X_train]
        k_indices = np.argsort(distances)[:self.k]
        k_nearest_labels = [self.y_train[i] for i in k_indices]
        most_common = Counter(k_nearest_labels).most_common(1)
        return most_common[0][0]

# Take user input for k
k = int(input("Enter the value of k (e.g., 3): "))

# Create a k-NN classifier with the user-defined k
knn = KNN(k=k)
knn.fit(X_train, y_train)

# Take user input for a single data point
print("\nEnter 4 feature values (sepal length, sepal width, petal length, petal width):")
try:
    user_input = np.array([float(x) for x in input().split()]).reshape(1, -1)
    prediction = knn.predict(user_input)[0]
    print(f"\nPredicted Class: {class_names[prediction]}")
except ValueError:
    print("Invalid input. Please enter four numerical values.")
