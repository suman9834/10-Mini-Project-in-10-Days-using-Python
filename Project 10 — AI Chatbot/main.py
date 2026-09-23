import datetime

print("🤖 Python Chatbot")
print("Type 'help' to see commands.")
print("Type 'exit' to quit.")

while True:
    user = input("\nYou: ").lower().strip()

    if user == "hello" or user == "hi":
        print("Bot: Hello! 👋 How are you?")

    elif user == "how are you":
        print("Bot: I'm doing great! Thanks for asking. 😊")

    elif user == "time":
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print("Bot:", current_time)

    elif user == "date":
        current_date = datetime.datetime.now().strftime("%d-%m-%Y")
        print("Bot:", current_date)

    elif user == "help":
        print("""
Available commands:
- hello
- how are you
- time
- date
- exit
""")

    elif user == "exit":
        print("Bot: Goodbye! 👋")
        break

    else:
        print("Bot: Sorry, I don't understand that yet.")