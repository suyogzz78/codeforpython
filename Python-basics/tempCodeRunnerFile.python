import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Load the dataset as tab-separated values (TSV)
df = pd.read_csv('C:\\Users\\N I T R O\\python\\Python-basics\\canada_per_capita_income.csv', sep='\t')

# Print column names to verify
print("Columns in the dataset:", df.columns)

# Check if 'year' and 'income' columns exist
if 'year' not in df.columns or 'income' not in df.columns:
    print("Error: The dataset must contain 'year' and 'income' columns.")
else:
    # Visualize the data
    plt.figure(figsize=(10, 6))
    plt.scatter(df['year'], df['income'], color='red', marker='+')
    plt.xlabel('year')
    plt.ylabel('income')
    plt.title('Per Capita Income Over Years')
    plt.grid(True)

    # Prepare data for model
    X = df[['year']]
    y = df['income']

    # Create and fit the model
    model = LinearRegression()
    model.fit(X, y)

    # Predict per capita income for 2020
    income_2020 = model.predict([[2020]])
    print(f"Predicted per capita income for Canada in 2020: ${income_2020[0]:,.2f}")

    # Plot the regression line
    plt.plot(df['year'], model.predict(X), color='blue', linewidth=2)
    plt.show()

