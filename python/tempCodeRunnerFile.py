import re
responses = {
    r"hello|hi|hey": "Hi there! How can I help you today?",
    r"how are you": "I'm just a computer program, but thanks for asking! How about you?",
    r"what is your name": "I am a simple chatbot created to assist you.",
    r"help": "Sure! I can help you with information about our services or answer your questions.",
    r"bye|goodbye|see you": "Goodbye! Have a great day!",
    r"how is the weather": "It's rainy today. Don't forget your umbrella!",
    r"shit": "What happened? I'm here to listen.",
    r"thank you|thanks": "You're welcome! If you have any more questions, feel free to ask.",
    r"what can you do": "I can assist you with information about our services and answer your questions.",
    r"tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
    r"what time is it": "I don't have a watch, but you can check your device for the current time.",
    r"who created you": "I was created by a team of developers to assist users like you!",
    r"what is your favorite color": "I don't have a favorite color, but I think all colors are beautiful!",
    r"do you have feelings": "I don't have feelings, but I'm here to help you with any questions you have.",
    r"what is your purpose": "My purpose is to assist you and provide information whenever you need it.",
}
def chatbot_response(user_input):
    # Normalize the user input to lowercase
    user_input = user_input.lower()
    
    # Check for keywords in the user input and respond accordingly
    for keyword, response in responses.items():
        if re.search(keyword, user_input):
            return response
    
    return "I'm sorry, I don't understand that. Can you please rephrase?"
def main():
    print("Welcome to the Simple Chatbot! Type 'bye' to exit.")
    while True:
        # Get user input
        user_input = input("You: ")
        
        if user_input.lower() in ['bye', 'goodbye', 'see you']:
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        response = chatbot_response(user_input)
        
        print("Chatbot:", response)

# Run the chatbot
if __name__ == "__main__":
    main()