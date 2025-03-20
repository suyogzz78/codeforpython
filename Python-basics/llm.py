from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

# Load pre-trained GPT-2 model and tokenizer
model_name = "gpt2"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Set pad_token_id explicitly to prevent warnings
tokenizer.pad_token = tokenizer.eos_token

def generate_response(input_text, chat_history_ids=None):
    # Encode the input text and add the end-of-sequence token
    input_ids = tokenizer.encode(input_text + tokenizer.eos_token, return_tensors='pt')
    # Check if there is any previous chat history
    if chat_history_ids is not None:
        # Concatenate the current input with the chat history to maintain context
        input_ids = torch.cat([chat_history_ids, input_ids], dim=-1)
    # Generate a response from the model
    response_ids = model.generate(
        input_ids,
        max_length=1000,  # Ensure response is not too long
        pad_token_id=tokenizer.pad_token_id,  # Ensure pad_token_id is set
        num_beams=5,  # Use beam search for better generation
        temperature=0.7,  # Higher temperature for more diverse responses
        top_p=0.92,
        top_k=50,
        do_sample=True,  # Enable sampling for more varied responses
        early_stopping=True,  # Stop early if the model generates a complete response
        no_repeat_ngram_size=2  # Prevent repetition of n-grams in the response
    )
    # Decode the generated response and return it
    response = tokenizer.decode(response_ids[:, input_ids.shape[-1]:][0], skip_special_tokens=True)
    return response, response_ids

def chat():
    print("Chatbot: Hi! I'm your friendly chatbot. Type 'quit' to exit.")
    # Initialize chat history
    chat_history_ids = None
    while True:
        # Take user input
        user_input = input("You: ")
        # Exit condition
        if user_input.lower() == 'quit':
            print("Chatbot: Goodbye!")
            break
        # Generate and print chatbot response
        response, chat_history_ids = generate_response(user_input, chat_history_ids)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chat()
