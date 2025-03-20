import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Sample data
x = np.array([[0], [5], [15], [25], [35], [45], [55], [60]])
y = np.array([4, 5, 20, 14, 32, 22, 38, 43])

# Splitting the dataset into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Creating the model
model = LinearRegression()

# Fitting the model
model.fit(x_train, y_train)

# Making predictions
y_pred = model.predict(x_test)

# Plotting the results
plt.scatter(x, y, color='blue')  # Original data
plt.plot(x_test, y_pred, color='red')  # Predicted line
plt.title('Linear Regression with scikit-learn')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()