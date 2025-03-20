import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('canada_per_capita_income.csv')

# Plot data
plt.figure(figsize=(10, 6))
plt.scatter(df['year'], df['per capita income (US$)'], color='red', marker='+', label='Actual Data')
plt.xlabel('Year')
plt.ylabel('Per Capita Income (US$)')
plt.title('Per Capita Income Over Years')

# Prepare data for model
X = df[['year']]
y = df['per capita income (US$)']

# Fit linear regression model
model = LinearRegression()
model.fit(X, y)

# Predict per capita income for 2018
income_2020 = model.predict([[2020]])
print(f"Predicted per capita income for Canada in 2020: ${income_2020[0]:,.2f}")

# Plot regression line
years_range = pd.DataFrame({'year': range(df['year'].min(), df['year'].max() + 1)})
plt.plot(years_range['year'], model.predict(years_range), color='blue', linewidth=2, label='Regression Line')

plt.legend()
plt.grid(True)
plt.show()
