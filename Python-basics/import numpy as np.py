import numpy as np

# Activation Function
def unitStep(x):
    return np.where(x > 0, 1, 0)

# Perceptron Class
class Perceptron:
    def __init__(self, lr, itrn=100):
        self.lr = lr
        self.itrn = itrn
        self.activation = unitStep
        self.weights = None
        self.bias = 0

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)  # Initialize weights as zeros
        self.bias = 0  # Initialize bias

        # Update weights and bias
        for _ in range(self.itrn):
            for idx, x_i in enumerate(X):
                linear_output = np.dot(x_i, self.weights) + self.bias
                y_predicted = self.activation(linear_output)

                # Update rule
                error = self.lr * (y[idx] - y_predicted)
                self.weights += error * x_i
                self.bias += error

    def predict(self, X):
        linear_output = np.dot(X, self.weights) + self.bias
        y_predicted = self.activation(linear_output)
        return y_predicted

# Define AND gate dataset
AND_X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
AND_y = np.array([0, 0, 0, 1])  # Output for AND gate

# Define OR gate dataset
OR_X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
OR_y = np.array([0, 1, 1, 1])  # Output for OR gate

# Create perceptron instance for AND gate
and_perceptron = Perceptron(lr=0.1, itrn=10)
and_perceptron.fit(AND_X, AND_y)

# Test AND gate
and_predictions = and_perceptron.predict(AND_X)
print("Predictions for AND Gate:")
print(and_predictions)

# Create perceptron instance for OR gate
or_perceptron = Perceptron(lr=0.1, itrn=10)
or_perceptron.fit(OR_X, OR_y)

# Test OR gate
or_predictions = or_perceptron.predict(OR_X)
print("Predictions for OR Gate:")
print(or_predictions)
