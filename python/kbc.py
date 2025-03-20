#create a program capable of displaying questions to the user like kbc
# Function to ask questions
def ask_question(question, options, correct_answer):
    print(f"\n{question}")
    for option in options:
        print(option)
    user_answer = input("Enter your answer (a, b, c, or d): ").lower()
    return user_answer == correct_answer

# Main function
def main():
    questions = [
        {"question": "What is the capital of Nepal?", "options": ["a) Kathmandu", "b) Delhi", "c) Thimphu", "d) Dhaka"], "answer": "a"},
        {"question": "Which planet is known as the Red Planet?", "options": ["a) Earth", "b) Mars", "c) Venus", "d) Jupiter"], "answer": "b"},
        {"question": "Who wrote 'Hamlet'?", "options": ["a) Charles Dickens", "b) William Shakespeare", "c) Mark Twain", "d) Jane Austen"], "answer": "b"}
    ]

    # Counter to keep track of the question number
    question_number = 1

    for q in questions:
        question_text = f"Question {question_number}: {q['question']}"
        if ask_question(question_text, q["options"], q["answer"]):
            print("Correct!")
        else:
            print(f"Wrong! The correct answer is {q['answer']}.")
         
        # Increment the counter
        question_number += 1

    print("Thanks for playing!")

# Run the game
if __name__ == "__main__":
    main()
