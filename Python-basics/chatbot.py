import random
import nltk
from nltk.chat.util import Chat, reflections

# Download the necessary NLTK data files (if you haven't already)
nltk.download('punkt')

# Define pairs of patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I assist you today?", "Hi %1! What can I do for you?","hey %1!,whatsup"]
    ],
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey! How can I help you?"]
    ],
    [
        r"what is your name?",
        ["I am a condition-based chatbot created to assist you!", "You can call me Chatbot!"]
    ],
    [
        r"guide",
        ["what's your problem","sure,i am eager to help you."]
    ],
    [
        r"how is the weather in (.*)",
        ["The weather in %1 is great!", "I am not sure about the weather in %1, but I hope it's nice!"]
    ],
    [
        r"quit",
        ["Bye! Take care.", "Goodbye! Have a great day!"]
    ],
    [
        r"(.*)",
        ["I'm sorry, I don't understand that.", "Could you please rephrase your question?"]
    ]
]

# Create a chatbot instance
chatbot = Chat(pairs, reflections)

# Function to start the chatbot
def start_chatbot():
    print("Hello! I'm a condition-based chatbot. Type 'quit' to exit.")
    chatbot.converse()

# Start the chatbot
if __name__ == "__main__":
    start_chatbot()
