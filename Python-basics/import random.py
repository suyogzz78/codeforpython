import random
import nltk
from nltk.chat.util import Chat, reflections



# Function to validate the user input
def validate_input(user_input):
    stripped_input = user_input.strip()
    if not stripped_input:
        return False
    return True

# Function to handle unknown inputs
def handle_unknown_input():
    responses = [
        "I'm sorry, I don't understand that.",
        "Could you please rephrase your question?",
        "I'm not sure how to respond to that. Can you try asking it differently?",
    ]
    return random.choice(responses)

# Define pairs of patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I assist you today?", "Hi %1! What can I do for you?", "Hey %1! What's up?"]
    ],
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey! How can I help you?", "Greetings! How can I assist you today?"]
    ],
    [
        r"what is your name?",
        ["I am a condition-based chatbot created to assist you!", "You can call me Chatbot!", "I'm your friendly AI assistanht."]
    ],
    [
        r"guide",
        ["What's your problem?", "Sure, I am eager to help you.", "Let me guide you. What do you need help with?"]
    ],
    [
        r"how is the weather in (.*)",
        ["The weather in %1 is great!", "I am not sure about the weather in %1, but I hope it's nice!", "I can't provide real-time weather updates, but I hope %1 is having good weather!"]
    ],
    [
        r"what can you do?",
        ["I can chat with you, provide information, and assist with various tasks.", "I'm here to help you with any questions or problems you have.", "I can provide guidance, answer questions, and have interesting conversations with you."]
    ],
    [
        r"tell me a joke",
        ["Why don't scientists trust atoms? Because they make up everything!", "Why did the math book look sad? Because it had too many problems.", "What do you get when you cross a snowman and a vampire? Frostbite."]
    ],
    [
        r"i feel (.*)",
        ["I'm sorry to hear that you feel %1. Is there anything I can do to help?", "It’s okay to feel %1 sometimes. Do you want to talk about it?", "Feeling %1 can be tough. I'm here if you need to chat about it."]
    ],
    [
        r"thank you|thanks",
        ["You're welcome!", "Happy to help!", "Anytime!"]
    ],
    [
        r"how are you?",
        ["I'm just a program, but I'm here to help you!", "I'm here to assist you!", "I don't have feelings, but I'm ready to help you!"]
    ],
    [
        r"quit",
        ["Bye! Take care.", "Goodbye! Have a great day!", "See you later!"]
    ],
    [
        r"(.*)",
        [handle_unknown_input()]
    ]
]

# Create a chatbot instance
chatbot = Chat(pairs, reflections)

# Function to start the chatbot
def start_chatbot():
    print("Hello! I'm a condition-based chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Chatbot: Bye! Take care.")
            break
        if not validate_input(user_input):
            print("Chatbot: Please enter a valid message.")
            continue
        response = chatbot.respond(user_input)
        if response is not None:
            print(f"Chatbot: {response}")
        else:
            print(f"Chatbot: {handle_unknown_input()}")

# Start the chatbot
if __name__ == "__main__":
    start_chatbot()
