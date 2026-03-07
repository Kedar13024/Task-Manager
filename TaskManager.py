import json
import os
import random as rd
from datetime import datetime   
import dateparser


class TaskManager:
    def __init__(self, filepath, username):
        self.filepath = filepath
        self._data = {"tasks": []}
        self.username = username

    # ____________________________________________________
    def read_data(self):
        try:
            if not os.path.exists(self.filepath):
                print("📁 File not found. Creating new task file...")
                self._data = {"tasks": []}
                with open(self.filepath, "w", encoding="utf-8") as f:
                    json.dump(self._data, f, indent=4)
                print("✅ New file created successfully!")
            else:
                with open(self.filepath, "r", encoding="utf-8") as f:
                    try:
                        self._data = json.load(f)
                        print("📂 Task data loaded successfully!")
                    except json.JSONDecodeError:
                        print("⚠️ File empty. Initializing new task list...")
                        self._data = {"tasks": []}
        except Exception as e:
            print(f"❌ Unexpected error: {e}")

    # ____________________________________________________
    def InputTaskDetails(self, userInput=None):
        try:
            task_no = int(input("🔢 Enter task number: "))

            for task in self._data["tasks"]:
                if task["Task_No"] == task_no:
                    raise ValueError("⚠️ Task number already exists!")

            desc = input("📝 Enter task description: ")
            due_input = input("⏰ Enter due date/Time: ")
            parsed_date = dateparser.parse(
                due_input,
                settings={"PREFER_DATES_FROM": "future"}
            )

            if not parsed_date:
                print("⚠️ Invalid date format!")
                return
            priority = {
                "high": "🔴",
                "medium": "🟡",
                "low": "🟢",
                "normal": "⚪"
                }

            get_priority = input("⏺️Set Priority [High(🔴), Medium(🟡), Low(🟢), Normal(⚪)]: ")
            get_priority = get_priority.strip().lower()
            if get_priority not in priority:
                raise ValueError("⚠️ Please enter valid priority.")
     
            task = {
                "Task_No": task_no,
                "Description": desc,
                "Status": False,
                "Due_Date": parsed_date.strftime("%Y-%m-%d %H:%M"),
                "Priority": priority[get_priority]
            }

            self._data["tasks"].append(task)
            self.update_json()
            print("🚀 Task added successfully!")

        except ValueError as e:
            print(e)

    # ____________________________________________________
    def display(self):
        if not self._data["tasks"]:
            print("📭 No tasks available. Add one!")
            return

        print("\n📋 Your Task List")
        print(f"{'Task':<6}{'Description':<30}{'Priority':<20}{'Status':<20}{'Remaining'}") 
        print("-" * 80)

        for task in self._data["tasks"]:
            remaining = self.dueDate(task["Due_Date"])

            if remaining == "❌ Overdue":
                status = "❌ Overdue"
                remaining_time = "-"
            else:
                status = "✅ Done" if task["Status"] else "⏳ Pending"
                remaining_time = remaining
            print(
                f"{task['Task_No']:<6}"
                f"{task['Description'][:28]:<30}"
                f"{task['Priority']:<16}"
                f"{status:<20}"
                f"{remaining_time}"
            )

    # ____________________________________________________
    def markComplete(self):
        try:
            taskComplete_no = int(input("✔️ Enter task number to mark complete: "))
            found = False

            for task in self._data["tasks"]:
                if task["Task_No"] == taskComplete_no:
                    found = True
                    if task["Status"]:
                        print("⚠️ Task already completed!")
                    else:
                        task["Status"] = True
                        self.update_json()
                        print("🎉 Task marked as completed!")

            if not found:
                print("❌ No task found with that number!")

        except ValueError:
            print("⚠️ Please enter a valid number!")

    # ____________________________________________________
    def update_json(self):
        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump(self._data, f, indent=4, ensure_ascii=False)
        print("💾 Task list updated successfully!")

    # ____________________________________________________
    def deleteTask(self):
        try:
            task_no = int(input("🗑️ Enter task number to delete: "))
            found = False

            for task in self._data["tasks"]:
                if task["Task_No"] == task_no:
                    self._data["tasks"].remove(task)
                    self.update_json()
                    print(f"🗑️ Task {task_no} deleted successfully!")
                    found = True
                    break

            if not found:
                print("❌ No task found with that number!")

        except ValueError:
            print("⚠️ Please enter a valid number!")

    # ____________________________________________________
    def dueDate(self, due_date_str):   
        due_date = datetime.strptime(due_date_str, "%Y-%m-%d %H:%M")
        now = datetime.now()

        remaining = due_date - now

        if remaining.total_seconds() < 0:
            return "❌ Overdue"

        if remaining.days == 0 and remaining.seconds <= 3600:
            return "⚠️ Due soon"

        days = remaining.days
        hours = remaining.seconds // 3600
        minutes = (remaining.seconds % 3600) // 60

        return f"{days}d {hours}h {minutes}m left"

    # ____________________________________________________
    def menu(self):
        menu = """
📌 [MENU]
+----------------------------+
| 1️⃣  Add a new task         |
| 2️⃣  Display all tasks      |
| 3️⃣  Mark task completed    |
| 4️⃣  Delete task            |
| 5️⃣  Exit program           |
+----------------------------+
"""
        return menu

    # ____________________________________________________
    def chatbot(self, userInput):
        userInput_lower = userInput.lower()

        greet = rd.choice([
            "Hi there! 👋",
            f"Hello {self.username}! 😊",
            f"Hey {self.username}! Nice to see you again! 😄",
            f"Welcome back {self.username}! ✨",
        ])

        if any(word in userInput_lower for word in ["hi", "hello", "hey"]):
            print(greet)

        elif "menu" in userInput_lower:
            print(self.menu())

        elif "add" in userInput_lower or "new task" in userInput_lower:
            self.InputTaskDetails()

        elif any(word in userInput_lower for word in ["display", "show", "all tasks"]):
            self.display()

        elif any(word in userInput_lower for word in ["mark", "done", "completed"]):
            self.markComplete()

        elif any(word in userInput_lower for word in ["delete", "remove"]):
            self.deleteTask()

        else:
            print("🙃 Sorry, I couldn't understand. Can you rephrase that?")


# ____________________________________________________
if __name__ == "__main__":
    filepath = r"C:\Users\HP\Data Science\Python basic projects\Projects\sample.json"
    username = input("👤 Enter your name: ")
    manager = TaskManager(filepath, username)
    manager.read_data()   
    print(f"\n✨ *************[ Welcome {manager.username} To TO-DO List App ]************* ✨")
    print("""
💡 Try commands like:
- add task finish homework 
- show all tasks
- mark the task that i completed
- I want to delete the task
- show me menu bar
- exit from app
""")
    while True:
        userInput = input("You: ")
        if any(word in userInput.lower() for word in ["quit", "exit", "end", "bye"]):
            print(f"👋 Goodbye {manager.username}! See you soon! ✨")
            break
        print("Bot:", end=" ")
        manager.chatbot(userInput)