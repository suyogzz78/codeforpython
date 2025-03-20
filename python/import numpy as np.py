import numpy as np
import statsmodels.api as sm

# Sample data
x = np.array([[0, 1], [5, 1], [15, 2], [25, 5], [35, 11], [45, 15], [55, 34], [60, 35]])
y = np.array([4, 5, 20, 14, 32, 22, 38, 43])

# Adding a constant for intercept
x = sm.add_constant(x)

# Creating the model
model = sm.OLS(y, x)

# Fitting the model
results = model.fit()

# Printing the summary of the model
print(results.summary())