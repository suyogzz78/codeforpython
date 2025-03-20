from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load pre-trained DialoGPT model and tokenizer
model_name = "microsoft/DialoGPT-medium"  # Switch to a larger model for better responses
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Set pad_token_id explicitly to prevent warnings
tokenizer.pad_token = tokenizer.eos_token  # Set pad token to the eos token

# Function to generate a response based on user input
def generate_response(input_text, chat_history_ids=None):
    # Encode the input text and add the end-of-sequence token to the input
    input_ids = tokenizer.encode(input_text + tokenizer.eos_token, return_tensors='pt')
    
    # Create attention mask
    attention_mask = torch.ones(input_ids.shape, dtype=torch.long)
    
    # Check if there is any previous chat history
    if chat_history_ids is not None:
        # Concatenate the current input with the chat history to maintain context
        input_ids = torch.cat([chat_history_ids, input_ids], dim=-1)
        attention_mask = torch.cat([torch.ones(chat_history_ids.shape, dtype=torch.long), attention_mask], dim=-1)
    
    # Generate a response from the model
    response_ids = model.generate(
        input_ids,
        attention_mask=attention_mask,
        max_length=1000,  # Ensure response is not too long
        pad_token_id=tokenizer.pad_token_id,  # Ensure pad_token_id is set
        num_beams=5,  # Use beam search for better generation
        temperature=0.7,  # Adjusted temperature for better response quality
        top_p=0.9,  # Adjusted top_p value for better balance
        top_k=50,
        do_sample=True,  # Enable sampling for more varied responses
        early_stopping=True,  # Stop early if the model generates a complete response
        no_repeat_ngram_size=2  # Prevent repetition of n-grams in the response
    )
    
    # Decode the generated response and return it
    response = tokenizer.decode(response_ids[:, input_ids.shape[-1]:][0], skip_special_tokens=True)
    return response, response_ids

# Function to log the conversation to a text file
def log_conversation(user_input, chatbot_response):
    with open("chat_log.txt", "a") as log_file:
        log_file.write(f"You: {user_input}\n")
        log_file.write(f"Chatbot: {chatbot_response}\n\n")

# Main function to handle the conversation loop
def chat():
    print("Chatbot: Hi! I'm your friendly chatbot. I can help with various topics. Type 'quit' to exit.")
    # Initialize chat history
    chat_history_ids = None
    while True:
        # Prompt before user input
        print("Chatbot: How can I assist you today?")
        # Take user input
        user_input = input("You: ")
        # Exit condition
        if user_input.lower() == 'quit':
            print("Chatbot: Goodbye! Have a great day!")
            break
        # Handle empty input
        if user_input.strip() == "":
            print("Chatbot: Please enter a valid input.")
            continue
        # Generate and print chatbot response
        response, chat_history_ids = generate_response(user_input, chat_history_ids)
        print(f"Chatbot: {response}")
        # Log conversation
        log_conversation(user_input, response)

# Start the chatbot
if __name__ == "__main__":
    chat()
