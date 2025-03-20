import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load dataset
file_path = "C:\\Users\\N I T R O\\SUYOG\\python\\Python-basics\\spam mail.csv"
df = pd.read_csv(file_path, encoding='latin1')

# Ensure necessary columns
if 'Category' not in df.columns or 'Labels' not in df.columns:
    raise ValueError("The CSV file must contain 'Category' and 'Labels' columns.")

# Transform text data to numerical vectors
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(df['Labels'])
y = df['Category']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train the model
model = MultinomialNB()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy * 100:.2f}%')

# Example prediction
new_message = ['Congratulations! You have won a lottery']
new_message_transformed = vectorizer.transform(new_message)
prediction = model.predict(new_message_transformed)
print(f'The message is classified as: {prediction[0]}')
