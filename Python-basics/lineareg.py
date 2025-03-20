import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Create a sample dataset
data = {
    'Rooms': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'SquareFootage': [550, 620, 720, 800, 850, 950, 1050, 1200, 1300, 1400],
    'LocationScore': [3, 4, 5, 3, 4, 5, 3, 4, 5, 4],
    'Price': [300000, 350000, 450000, 500000, 550000, 600000, 700000, 800000, 850000, 900000]
}

df = pd.DataFrame(data)

# Features (X) and target (y)
X = df[['Rooms', 'SquareFootage', 'LocationScore']]
y = df['Price']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create the model
model = LinearRegression()

# Fit the model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R^2 Score: {r2}")

# Display actual and predicted prices
results = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print(results)

# Visualize the results
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred)
plt.xlabel('Actual Prices')
plt.ylabel('Predicted Prices')
plt.title('Actual vs Predicted Prices')
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', linestyle='--')
plt.show()
