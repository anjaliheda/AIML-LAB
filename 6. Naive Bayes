import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Load iris dataset
iris = load_iris()
X, y = iris.data, iris.target
class_names = iris.target_names

class NaiveBayes:
    def fit(self, X, y):
        self.classes = np.unique(y)
        self.mean = np.array([X[y == c].mean(axis=0) for c in self.classes])
        self.var = np.array([X[y == c].var(axis=0) for c in self.classes])
        self.priors = np.array([np.mean(y == c) for c in self.classes])

    def predict(self, X):
        return np.array([self._predict(x) for x in X])

    def _predict(self, x):
        posteriors = [np.log(self.priors[i]) + np.sum(np.log(self._pdf(i, x))) for i in range(len(self.classes))]
        return self.classes[np.argmax(posteriors)]

    def _pdf(self, class_idx, x):
        mean, var = self.mean[class_idx], self.var[class_idx]
        return np.exp(-((x - mean) ** 2) / (2 * var)) / np.sqrt(2 * np.pi * var)

# Train the model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)
nb = NaiveBayes()
nb.fit(X_train, y_train)

def classify_input():
    print("Enter 4 feature values (sepal length, sepal width, petal length, petal width):")
    try:
        user_input = np.array([float(x) for x in input().split()]).reshape(1, -1)
        prediction = nb.predict(user_input)[0]
        print(f"Predicted Class: {class_names[prediction]}")
    except ValueError:
        print("Invalid input. Please enter four numerical values.")

# Get user input
classify_input()
