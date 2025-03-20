import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Expanded sample dataset
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
        'You won a new car',
        'Congrats, you have won!',
        'Discount on all products',
        'Final notice: Your account is overdue',
        'Don’t miss out on this offer',
        'Monthly report attached',
        'Schedule for next week',
        'Claim your free gift card now',
        'Limited time offer!',
        'Your invoice is attached',
        'Your Amazon order has shipped',
        'Urgent: Verify your account',
        'Special discount for loyal customers',
        'Invitation to connect on LinkedIn',
        'Your subscription has been renewed',
        'Win a brand new iPhone',
        'Friendly reminder: Staff meeting tomorrow',
        'Act now to secure your spot',
        'Your payment has been received',
        'New security update available',
        'We have a job offer for you',
        'Update your billing information',
        'You’ve been selected for a survey',
        'Your package is out for delivery',
        'Limited time: Upgrade your plan',
        'Join our exclusive beta program',
        'Confirm your email address',
        'You’ve been pre-approved for a loan',
        'Important: Changes to our terms of service',
        'Last chance to save on tickets',
        'Your account has been suspended',
        'You’ve won a vacation!',
        'Exclusive: Members only sale',
        'Reminder: Your appointment tomorrow',
        'You have a new message',
        'We miss you! Come back for a discount',
        'Important security alert',
        'Your account activity requires attention'
    ],
    'label': [
        'spam', 'spam', 'not spam', 'not spam', 'spam', 'spam', 'not spam', 'spam', 'not spam', 'not spam',
        'spam', 'not spam', 'spam', 'spam', 'spam', 'spam', 'spam', 'not spam', 'not spam', 'spam',
        'spam', 'not spam', 'not spam', 'spam', 'spam', 'not spam', 'not spam', 'spam', 'not spam', 'spam',
        'not spam', 'not spam', 'not spam', 'spam', 'not spam', 'not spam', 'not spam', 'spam', 'not spam', 'spam',
        'not spam', 'spam', 'spam', 'not spam', 'not spam', 'spam', 'spam', 'spam', 'not spam', 'not spam'
    ]
}

df = pd.DataFrame(data)

# Text preprocessing with TF-IDF
vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1, 2))
X = vectorizer.fit_transform(df['email'])
y = df['label']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Model training with Random Forest
model = RandomForestClassifier(n_estimators=100, random_state=42)
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
new_email = ['Congratulations! You have won a lottery']
new_email_transformed = vectorizer.transform(new_email)
prediction = model.predict(new_email_transformed)
print(f'The email is classified as: {prediction[0]}')
