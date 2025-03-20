import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt

# Function to load and validate dataset
def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        print("Data loaded successfully.")
        if 'year' not in df.columns or 'income' not in df.columns:
            raise ValueError("The dataset must contain 'year' and 'income' columns.")
        return df
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        exit()
    except ValueError as ve:
        print(f"Error: {ve}")
        exit()

# Load dataset
df = load_data('canada_per_capita_income.csv')

# Data validation
print("First few rows of the dataset:")
print(df.head())
print("\nDataset info:")
print(df.info())
print("\nSummary statistics:")
print(df.describe())

# Visualize data
plt.figure(figsize=(10, 6))
plt.scatter(df['year'], df['income'], color='red', marker='+', label='Actual Data')
plt.xlabel('Year')
plt.ylabel('Per Capita Income (US$)')
plt.title('Per Capita Income Over Years')
plt.legend()
plt.grid(True)

# Fit a linear regression model
X = df[['year']]  # Features
y = df['income']  # Target variable

# Create and train the model
reg = linear_model.LinearRegression()
reg.fit(X, y)

# Predict income for the year 2020
year_to_predict = 2020
prediction = reg.predict([[year_to_predict]])

# Display the regression line on the plot
plt.plot(df['year'], reg.predict(X), color='blue', linewidth=2, label='Fitted Line')
plt.legend()

# Print the result
print(f"\nPredicted per capita income for Canada in {year_to_predict}: ${prediction[0]:,.2f}")

# Save the plot
plt.savefig('income_prediction_plot.png')
plt.show()  # Display the plot
