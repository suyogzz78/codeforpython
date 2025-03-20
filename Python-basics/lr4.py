import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('canada_per_capita_income.csv')

# Visualize the data
plt.figure(figsize=(10, 6))
plt.scatter(df['year'], df['per capita income (US$)'], color='red', marker='+')
plt.xlabel('year')
plt.ylabel('per capita income (US$)')
plt.title('Per Capita Income Over Years')
plt.grid(True)

# Prepare data for model
X = df[['year']]
y = df['per capita income (US$)']

# Create and fit the model
model = LinearRegression()
model.fit(X, y)

# Predict per capita income for 2020
income_2020 = model.predict([[2020]])
print(f"Predicted per capita income for Canada in 2020: ${income_2020[0]:,.2f}")

# Plot the regression line
plt.plot(df['year'], model.predict(X), color='blue', linewidth=2)
plt.show()
