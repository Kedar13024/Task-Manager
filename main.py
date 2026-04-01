from task_manager import TaskManager
from chatbot import chatbot
import coloring as cg

def main():
    cg.banner(f"\n✨ Welcome to the TASK MANAGER ✨")
    filepath = "mytasks.json"

    username = input("👤 Enter your name: ")

    manager = TaskManager(filepath, username)
    cg.loading()
    manager.read_data()
  

    while True:

        userInput =input("YOU:")
        cg.user(userInput)

        if userInput.lower() in ["exit", "quit", "bye", "end"]:
            cg.updating()
            cg.bot(f"👋 Goodbye {username}!")
            break
        chatbot(manager, userInput)

if __name__ == "__main__":
    main()