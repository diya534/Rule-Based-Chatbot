def chatbot(dataset):
    """
    A simple rule-based chatbot that responds based on a provided dataset.

    Args:
        dataset (dict): A dictionary where keys are user inputs (or keywords)
                        and values are the chatbot's corresponding responses.

    Returns:
        None: The function runs the chatbot interaction in the console.
    """
    print("Simple Chatbot started. Type 'bye' to exit.")
    while True:
        user_input = input("You: ").lower()
        if user_input == 'bye':
            print("Chatbot: Goodbye!")
            break

        found_match = False
        for key, response in dataset.items():
            if key in user_input:
                print(f"Chatbot: {response}")
                found_match = True
                break

        if not found_match:
            print("Chatbot: I'm not sure how to respond to that.")

if __name__ == "__main__":
    # Define a simple dataset of questions and answers
    simple_data = {
        "hello": "Hi there!",
        "hi": "Hello!",
        "how are you": "I'm doing well, thank you for asking!",
        "what is your name": "I am a simple chatbot.",
        "thank you": "You're welcome!",
        "weather": "I do not have access to real-time weather information yet.",
        "time": "I can tell you the current time if you'd like.",
        "tell me the time": "The current time is 11:38 AM IST on Friday, April 25, 2025.",
        "bye": "Goodbye!" # Included here for direct match
    }

    chatbot(simple_data)