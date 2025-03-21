import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.naive_bayes import GaussianNB

# Load the Titanic dataset
df = pd.read_csv("titanic.csv")

# Data preprocessing
# Drop unnecessary columns
df.drop(['PassengerId', 'Name', 'SibSp', 'Parch', 'Ticket', 'Cabin', 'Embarked'], axis='columns', inplace=True)

# Separate inputs and target variable
inputs = df.drop('Survived', axis='columns')
target = df['Survived']

# Convert categorical variable 'Sex' to dummy variables
dummies = pd.get_dummies(inputs['Sex'], drop_first=True)  # drop_first=True to avoid dummy variable trap
inputs = pd.concat([inputs, dummies], axis='columns')
inputs.drop(['Sex'], axis='columns', inplace=True)

# Fill missing values in 'Age' with the mean
inputs['Age'] = inputs['Age'].fillna(inputs['Age'].mean())

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(inputs, target, test_size=0.3, random_state=42)

# Initialize and fit the Gaussian Naive Bayes model
model = GaussianNB()
model.fit(X_train, y_train)

# Perform cross-validation
scores = cross_val_score(model, X_train, y_train, cv=5)

# Print the cross-validation scores
print("Cross-validation scores:", scores)
print("Mean cross-validation score:", scores.mean())

# Make predictions on the test set
predictions = model.predict(X_test[0:20])
print("Predicted survival for the first 20 passengers:", predictions)

# Get prediction probabilities for the first 20 passengers
probabilities = model.predict_proba(X_test[:20])
print("Prediction probabilities for the first 10 passengers:")
print(probabilities)