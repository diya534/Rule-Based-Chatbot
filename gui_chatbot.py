import tkinter as tk

simple_data = {
    "hello": "Hi there!",
    "hi": "Hello!",
    "how are you": "I'm doing well, thank you for asking!",
    "what is your name": "I am a simple chatbot.",
    "thank you": "You're welcome!",
    "weather": "I do not have access to real-time weather information.",
    "time": "I can tell you the current time if you'd like.",
    "tell me the time": "The current time is 11:38 AM IST on Friday, April 25, 2025.",
    "bye": "Goodbye!"
}

# Function to process user input and return the appropriate response
def get_response(user_input):
    return simple_data.get(user_input.lower(), "Sorry, I didn't understand that.")

# Function to handle user input and display the response
def on_send_click(event=None):
    user_input = entry.get()  # Get the user input from the entry widget
    response = get_response(user_input)  # Get the chatbot response
    # Insert user input and chatbot response into the text widget
    chat_window.config(state=tk.NORMAL)
    chat_window.insert(tk.END, "You: " + user_input + "\n", 'user')
    chat_window.insert(tk.END, "Bot: " + response + "\n\n", 'bot')
    chat_window.config(state=tk.DISABLED)
    entry.delete(0, tk.END)  # Clear the entry widget after sending

# Create the main window
root = tk.Tk()
root.title("Colorful Chatbot")

# Create a Text widget to display the chat history with colors
chat_window = tk.Text(root, height=15, width=50, state=tk.DISABLED, bg="#f5f5f5", fg="#333", font=("Arial", 12))
chat_window.grid(row=0, column=0, padx=10, pady=10)

# Define tags for user and bot text styles
chat_window.tag_configure('user', foreground='#1E90FF', font=('Arial', 12, 'bold'))  # Blue for user
chat_window.tag_configure('bot', foreground='#32CD32', font=('Arial', 12))  # Green for bot

# Create an Entry widget for user input with a different color scheme
entry = tk.Entry(root, width=40, bg="#e0f7fa", fg="#006064", font=("Arial", 12))
entry.grid(row=1, column=0, padx=10, pady=10)

# Create a Send button with a color and rounded corners
send_button = tk.Button(root, text="Send", width=10, command=on_send_click, bg="#FF6347", fg="white", font=("Arial", 12, 'bold'))
send_button.grid(row=1, column=1, padx=10, pady=10)

# Bind the 'Enter' key to trigger the on_send_click function
# Good alignment
entry.bind('<Return>', on_send_click)
root.mainloop()