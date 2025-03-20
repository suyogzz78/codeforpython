import numpy as np
from sklearn.model_selection import train_test_split

def unitStep(x):
    return np.where(x > 0, 1, 0)

class Perceptron:
    def __init__(self, lr=0.01, itrn=100):
        self.lr = lr
        self.itrn = itrn
        self.activation = unitStep
        self.weights = None
        self.bias = 0

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)

        # Learn weights
        for _ in range(self.itrn):
            for idx, x_i in enumerate(X):
                linear_output = np.dot(x_i, self.weights) + self.bias
                y_predicted = self.activation(linear_output)

                # Weight update
                error = self.lr * (y[idx] - y_predicted)
                self.weights += error * x_i
                self.bias += error

    def predict(self, X):
        linear_output = np.dot(X, self.weights) + self.bias
        y_predicted = self.activation(linear_output)
        return y_predicted

def accuracy(y_true, y_predicted):
    return np.sum(y_true == y_predicted) / len(y_true)

# Define a dataset with two features
X = [
    [0.21, 1.2],
    [0.52, 1.5],
    [0.92, 0.5],
    [0.36, 0.3],
    [0.55, 1.7],
    [0.45, 0.4],
    [0.34, 0.8],
    [0.67, 1.1],
    [0.04, 1.0],
    [0.77, 0.9]
]
y = [0, 1, 1, 0, 1, 0, 0, 1, 0, 1]

X = np.array(X)
y = np.array(y)

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=13)

print("*" * 100)
print("X_test:")
print(X_test)
print("y_test:")
print(y_test)
print("X_train:")
print(X_train)
print("*" * 100)

# Initialize and train the Perceptron
p = Perceptron(lr=0.01, itrn=1000)
p.fit(X_train, y_train)

# Make predictions on the test set
prediction = p.predict(X_test)
print("Predictions:")
print(prediction)
print("Accuracy:", accuracy(y_test, prediction))

# Predict on new data
new_data = [[0.31, 1.5], [0.88, 0.7]]
new_prediction = p.predict(new_data)
print("New Predictions:")
print(new_prediction)
