import json
import os
from util import dueDate
from chatbot import rd

class TaskManager:
    def __init__(self, filepath, username):
        # Store JSON file path and initialize empty task list
        self.filepath = filepath
        self._data = {"tasks": []}
        # Username used for greeting messages
        self.username = username
         # Predefined chatbot responses for different actions
        self.botresponses ={
            "greet": [
                "Hi there! 👋",
                f"Hello {username}! 😊",
                f"Hey {username}! Nice to see you again! 😄",
                f"Welcome back {username}! ✨",
            ],
            "add": [
                "Got it! Task added. ✅",
                "Your task has been added!",
                "Alright, I've added that to your list.",
                "Done! Task saved successfully.",
                "🚀 Task added successfully!"
            ],
            "delete": [
                "Task removed successfully. 🗑️",
                "Alright, that task is deleted.",
                "Deleted! Your list looks cleaner now.",
                "Task erased from the list."
            ],
            "display": [
                "Here are your tasks:👇",
                "Let me show your task list.",
                "These are the tasks I found:",
                "Opening your task list now."
            ],
            "mark_done": [
                "Great work! That task is done.",
                "I've marked that task as finished.",
                "Task successfully completed."
            ],
            "error": [
                "Sorry, I didn't understand that. 🤔",
                "Could you rephrase that?",
                "I'm not sure what you mean.",
                "Try asking in a different way."
            ],
        }

    # ____________________________________________________
    def read_data(self):
        """ 
        Loads task data from JSON file.
        If file does not exist → creates a new one.
        If file is empty → initializes empty task list.
        """
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
    def InputTaskDetails(self,taskid=None,taskdes=None,dueinput=None,priority=None):
        """
        Adds a new task to the task list.
        Parameters:
        taskid      → unique task number
        taskdes     → task description
        dueinput    → due date in format YYYY-MM-DD HH:MM
        priority    → task priority (high, medium, low, normal)
        """
        try:
            if taskid==None:
                raise ValueError("⚠️ Please assign Task ID!🫤")
            if taskdes==None:
                raise ValueError("⚠️ You forgot to state what task is!🫥")
            if dueinput==None:
                raise ValueError("⚠️ Please enter valid date!🫤")
            # Prevent duplicate task IDs
            for task in self._data["tasks"]:
                if task["Task_No"] == taskid:
                    raise ValueError("⚠️ Task number already exists!(It should be unique!)🙂‍↕️")
            #Priority types
            priorities = {
                "high": "🔴",
                "medium": "🟡",
                "low": "🟢",
                "normal": "⚪"
                }

            if priority not in priorities:
                raise ValueError("⚠️ Please enter valid priority.🧐")
            #Task representation
            task = {
                "Task_No": taskid,
                "Description": taskdes,
                "Status": False,
                "Due_Date": dueinput,
                "Priority": priorities[priority]
            }

            self._data["tasks"].append(task)
            self.update_json()
            print(rd.choice(self.botresponses["add"]))

        except ValueError as e:
            print(e)

    # ____________________________________________________
    def markComplete(self,taskid):
        """Marks a task as completed using its Task ID."""
        try:
            found = False
            for task in self._data["tasks"]:
                if task["Task_No"] == taskid:
                    found = True
                    if task["Status"]:
                        print("⚠️ Task already completed!")
                    else:
                        task["Status"] = True
                        print(rd.choice(self.botresponses["mark_done"]))
                        self.update_json()


            if not found:
                print("❌ No task found with that number!")

        except ValueError:
            print("⚠️ Please enter a valid number!")

    # ____________________________________________________
    def deleteTask(self,taskid):
        """ Deletes a task from the list using its Task ID."""
        try:
            found = False

            for task in self._data["tasks"]:
                if task["Task_No"] == taskid:
                    self._data["tasks"].remove(task)
                    found = True
                    print(rd.choice(self.botresponses["delete"]))
                    break
            self.update_json()
            if not found:
                print("❌ No task found with that number!")

        except ValueError:
            print("⚠️ Please enter a valid number!")

    # ____________________________________________________
    def display(self, what):
        """
        Displays tasks based on filter.
    
        what = 0 → show all tasks
        what = 1 → show completed tasks
        what = 2 → show pending tasks
        what = 3 → show overdue tasks
        what = 4 → show menu
        """
        if not self._data["tasks"]:
            print("📭 No tasks available. Add one!")
            return
    
        if what == 4:
            print("""
    📌 [MENU]
    +----------------------------+
    | 1️⃣  Add a new task         |
    | 2️⃣  Display all tasks      |
    | 3️⃣  Mark task completed    |
    | 4️⃣  Delete task            |
    | 5️⃣  Exit program           |
    +----------------------------+
    """)
            return
    
        print("\n📋 Your Task List")
        print("-" * 90)
        print(f"{'Task':<6}{'Description':<30}{'Priority':<16}{'Status':<20}{'Due Time'}")
        print("-" * 90)
    
        for task in self._data["tasks"]:
    
            remaining = dueDate(task["Due_Date"])
    
            if remaining == "❌ Overdue":
                status = "❌ Overdue"
                remaining_time = "-"
            else:
                status = "✅ Done" if task["Status"] else "⏳ Pending"
                remaining_time = "-" if status == "✅ Done" else remaining
    
            # FILTERS tasks by STATUS 
            if what == 1 and not task["Status"]:
                continue
    
            if what == 2 and task["Status"]:
                continue
    
            if what == 3 and remaining != "❌ Overdue":
                continue
            # Task print format
            print(
                f"{task['Task_No']:<6}"
                f"{task['Description'][:28]:<30}"
                f"{task['Priority']:<16}"
                f"{status:<20}"
                f"{remaining_time}"
            )
            print("-" * 90)
    
    # ____________________________________________________
    def update_json(self):
        """Updates the saved data."""
        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump(self._data, f, indent=4, ensure_ascii=False)
