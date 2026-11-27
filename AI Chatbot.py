
import random
import datetime

def chatbot_response(user_input):

    user_input = user_input.lower()

    # Greetings
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you?"

    elif "how are you" in user_input:
        return "I am fine! Thank you for asking."

    # Name
    elif "your name" in user_input:
        return "My name is Python AI Chatbot."

    # Date
    elif "date" in user_input:
        today = datetime.date.today()
        return "Today's date is " + str(today)

    # Time
    elif "time" in user_input:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        return "Current time is " + current_time

    # Jokes
    elif "joke" in user_input:
        jokes = [
            "Why did the computer go to the doctor? Because it had a virus!",
            "Why was the computer cold? Because it left its Windows open!",
            "Why do programmers prefer dark mode? Because light attracts bugs!"
        ]
        return random.choice(jokes)

    # Study
    elif "python" in user_input:
        return "Python is a popular programming language."

    elif "thank you" in user_input:
        return "You're welcome! Happy to help."

    elif "bye" in user_input:
        return "Goodbye! Have a nice day."

    else:
        return "Sorry, I don't understand. Please ask another question."


print("================================")
print("       PYTHON AI CHATBOT")
print("================================")
print("Chatbot: Hello! Welcome to my chatbot.")
print("Type 'bye' to exit.")

while True:

    user = input("\nYou: ")

    response = chatbot_response(user)

    print("Chatbot:", response)

    if "bye" in user.lower():
        break
