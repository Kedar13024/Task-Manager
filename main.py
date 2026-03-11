from task_manager import TaskManager
from chatbot import chatbot

def main():

    filepath = "mytasks.json"

    username = input("👤 Enter your name: ")

    manager = TaskManager(filepath, username)

    manager.read_data()

    print(f"\n✨ Welcome {username} to the TO-DO Assistant ✨")

    while True:

        userInput = input("You: ")

        if userInput.lower() in ["exit", "quit", "bye", "end"]:
            print("💾 Task list updated successfully!")
            print(f"👋 Goodbye {username}!")
            break

        print("Bot:", end=" ")
        chatbot(manager, userInput)

if __name__ == "__main__":
    main()