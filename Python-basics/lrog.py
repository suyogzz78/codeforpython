import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt

# Function to load and validate dataset
def load_data(file_path):
    try:
        # Load the dataset
        df = pd.read_csv(file_path, sep='\t')
        print("Data loaded successfully.")
        
        # Check if required columns exist
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
file_path = 'C:\\Users\\N I T R O\\python\\Python-basics\\canada_per_capita_income.csv'
df = load_data(file_path)

# Data validation and inspection
print("\nFirst few rows of the dataset:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nSummary Statistics:")
print(df.describe())

# Visualize data
plt.figure(figsize=(10, 6))
plt.scatter(df['year'], df['income'], color='red', marker='+', label='Actual Data')
plt.xlabel('Year')
plt.ylabel('Per Capita Income (US$)')
plt.title('Per Capita Income Over Years')
plt.legend()
plt.grid(True)

# Prepare data for model training
X = df[['year']]  # Feature
y = df['income']  # Target variable

# Train a linear regression model
reg = linear_model.LinearRegression()
reg.fit(X, y)

# Predict income for the year 2020
year_to_predict = 2020
# Fixing the feature name warning
prediction_input = pd.DataFrame([[year_to_predict]], columns=['year'])
prediction = reg.predict(prediction_input)

# Plot regression line
plt.plot(df['year'], reg.predict(X), color='blue', linewidth=2, label='Fitted Line')
plt.legend()
plt.savefig('income_prediction_plot.png')  # Save the plot

# Display prediction and plot
print(f"\nPredicted per capita income for Canada in {year_to_predict}: ${prediction[0]:,.2f}")
plt.show()
