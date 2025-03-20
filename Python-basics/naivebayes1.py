import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Sample dataset
data = {
    'email': [
        'Free money now',
        'Urgent, claim your prize',
        'Hey, how are you?',
        'Meeting rescheduled',
        'Win a free trip',
        'Special offer just for you',
        'Join our webinar',
        'Cheap products available',
        'Lunch tomorrow?',
        'Important update',
        'Exclusive deal just for you',
        'Reminder: Meeting tomorrow',
        'You won a new car'
    ],
    'label': ['spam', 'spam', 'not spam', 'not spam', 'spam', 'spam', 'not spam', 'spam', 'not spam', 'not spam', 'spam', 'not spam', 'spam']
}

df = pd.DataFrame(data)

# Text preprocessing with TF-IDF
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(df['email'])
y = df['label']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Model training
model = MultinomialNB()
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Evaluation
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred, zero_division=1)

print(f'Accuracy: {accuracy * 100:.2f}%')
print('Confusion Matrix:\n', conf_matrix)
print('Classification Report:\n', class_report)

# Example prediction
new_email = ['hello']
new_email_transformed = vectorizer.transform(new_email)
prediction = model.predict(new_email_transformed)
print(f'The email is classified as: {prediction[0]}')
