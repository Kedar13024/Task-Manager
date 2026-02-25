import json
import os
import random as rd
class TaskManager:
    def __init__(self, filepath,username):
        self.filepath = filepath
        self._data = {"tasks": []}
        self.username=username

    #____________________________________________________
    def read_data(self):
        try:
            if not os.path.exists(self.filepath):
                print("📁 File not found. Creating new task file...")
                self._data = {"tasks": []}
                with open(self.filepath, "w", encoding="utf-8") as f:
                    json.dump(self._data, f, indent=4)
                print("✅ New file created successfully!")
            else:
                with open(self.filepath, "r", encoding='utf-8') as f:
                    try:
                        self._data = json.load(f)
                        print("📂 Task data loaded successfully!")
                    except json.JSONDecodeError:
                        print("⚠️ File empty. Initializing new task list...")
                        self._data = {"tasks": []}
        except Exception as e:
            print(f"❌ Unexpected error: {e}")

    #____________________________________________________
    def InputTaskDetails(self):
        try:
            task_no = int(input("🔢 Enter task number: "))
            
            for task in self._data['tasks']:
                if task['Task_No'] == task_no:
                    raise ValueError("⚠️ Task number already exists!")

            task_info = input("📝 Enter task description: ")

            if not (5 <= len(task_info) <= 30):
                raise ValueError("⚠️ Description must be 5–30 characters!")

            task = {
                "Task_No": task_no,
                "Description": task_info,
                "Status": False
            }

            self._data['tasks'].append(task)
            self.update_json()
            print("🚀 Task added successfully!")

        except ValueError as e:
            print(e)

    #____________________________________________________
    def display(self):
        if not self._data['tasks']:
            print("📭 No tasks available. Add one!")
        else:
            print("\n📋 Your Task List")
            print(f"{'Task No.':<10}{'Description':<30}{'Status':<10}")
            print("-" * 50)

            for task in self._data['tasks']:
                status = "✅ Done" if task['Status'] else "⏳ Pending"
                print(f"{task['Task_No']:<10}{task['Description']:<30}{status:<10}")

    #____________________________________________________
    def markComplete(self):
        try:
            taskComplete_no = int(input("✔️ Enter task number to mark complete: "))
            found = False

            for task in self._data['tasks']:
                if task['Task_No'] == taskComplete_no:
                    found = True
                    if task['Status']:
                        print("⚠️ Task already completed!")
                    else:
                        task['Status'] = True
                        self.update_json()
                        print("🎉 Task marked as completed!")

            if not found:
                print("❌ No task found with that number!")

        except ValueError:
            print("⚠️ Please enter a valid number!")

    #____________________________________________________
    def update_json(self):
        with open(self.filepath, 'w', encoding='utf-8') as f:
            json.dump(self._data, f, indent=4, ensure_ascii=False)
        print("💾 Task list updated successfully!")

    #____________________________________________________
    def deleteTask(self):
        try:
            task_no = int(input("🗑️ Enter task number to delete: "))
            found = False

            for task in self._data['tasks']:
                if task['Task_No'] == task_no:
                    self._data['tasks'].remove(task)
                    self.update_json()
                    print(f"🗑️ Task {task_no} deleted successfully!")
                    found = True
                    break

            if not found:
                print("❌ No task found with that number!")

        except ValueError:
            print("⚠️ Please enter a valid number!")

    #____________________________________________________
    def menu(self):
        menu = '''
📌 [MENU]
+----------------------------+
| 1️⃣  Add a new task         |
| 2️⃣  Display all tasks      |
| 3️⃣  Mark task completed    |
| 4️⃣  Delete task            |
| 5️⃣  Exit program           |
+----------------------------+
'''
        return menu
    
    #____________________________________________________

    #____________________________________________________
    def chatbot(self, userInput):
        userInput = userInput.lower()
        
        greet = rd.choice([
            "Hi there! 👋",
            f"Hello {self.username}! 😊",
            f"Hey {self.username}! Nice to see you again! 😄",
            f"Welcome back {self.username}! ✨"
        ])
        
        if any(word in userInput for word in ["hi", "hello", "hey"]):
            print(greet)   

        elif "menu" in userInput:
            print(self.menu())   

        elif any(word in userInput for word in ["add", "new task"]):
            self.InputTaskDetails()   

        elif any(word in userInput for word in ["display", "show", "all tasks"]):
            self.display()   

        elif any(word in userInput for word in ["mark", "done", "completed"]):
            self.markComplete()   

        elif any(word in userInput for word in ["delete", "remove"]):
            self.deleteTask()   

        else:
            print("🙃 Sorry, I couldn't understand. Can you rephrase that?")
        


#____________________________________________________
if __name__ == "__main__":
    filepath = r"C:\Projects\Task Manager\tasks.json"
    username = input("👤 Enter your name: ")
    manager = TaskManager(filepath, username)
    manager.read_data()
    print(f"\n✨ *************[ Welcome {manager.username} To TO-DO List App ]************* ✨")
    '''
    print(kedar)

    while True:
        print(kedar.menu())

        try:
            choice = int(input("👉 Enter choice number: "))
        except ValueError:
            print("⚠️ Please enter a valid number!")
            continue

        match choice:
            case 1:
                kedar.InputTaskDetails()
            case 2:
                kedar.display()
            case 3:
                kedar.markComplete()
            case 4:
                kedar.deleteTask()
            case 5:
                print("👋 Exiting program... See you soon Kedar! ✨")
                break
            case _:
                print("❌ Invalid choice!")
    '''
    while True:
        userInput = input("You: ")
        if any(word in userInput.lower() for word in ["quit", "exit", "end","bye"]):
            print(f"👋 Goodbye {manager.username}! See you soon! ✨")
            break   
        print("Bot:", end=" ")
        manager.chatbot(userInput)