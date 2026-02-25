# 🗂️ Task Manager (Python + JSON + Chatbot)
> A beginner-friendly, interactive command-line Task Manager built with Python.
It stores tasks in a JSON file and supports adding, displaying, marking tasks as completed, deleting tasks, and auto-saving changes — now with a simple chatbot interface 🤖✨

## 🚀 Features

- 📂 Persistent storage using JSON files
- 👤 Personalized experience (asks for your name)
- 🤖 Chatbot-style interaction (type commands like "add", "show", "delete")
- ➕ Add new tasks with validation
    1. Unique task number
    2. Description length between 5–30 characters
- 📋 Display tasks in a neat tabular format
- ✅ Mark tasks as completed
- 🗑️ Delete tasks
- 💾 Auto-save after every change
- 🖥️ Interactive loop (type exit to quit)
## 🧰 Requirements

- Python 3.10+ (uses match statement if menu mode enabled)
- No external libraries required
- Works on Windows / macOS / Linux

## ▶️ How to Run
- `cmd: python TaskManager.py`

- You will be prompted:
`👤 Enter your name: Kedar`

- If the JSON file doesn’t exist, it will be created automatically:
   ```
    1. 📁 File not found. Creating new task file...
    2. ✅ New file created successfully!
    ```
## 🤖 Chatbot Commands
- #### Instead of using numbers, you can type:
```
+------------------------------------+
|  Command	   --->       Action     |
+------------------------------------+
|  hi, hello    |	 Greet the bot   |
+------------------------------------+
|  menu	        |       Show menu    |
+------------------------------------+
|  add	        |    Add a new task  |
+------------------------------------+
| show, display	|     Display tasks  |
+------------------------------------+
|  mark, done	| Mark task completed|
+------------------------------------+
| delete,remove |   Delete task      |
+------------------------------------+
| exit, quit    |  Exit program      |
+------------------------------------+
```

## 🖥️ Example Interaction
```
✨ *************[ Welcome Kedar To TO-DO List App ]************* ✨
You:  Hi Bot
Bot: Welcome back Kedar! ✨
You:  Can you show me tasklist.
Bot: 📭 No tasks available. Add one!
You:  Then add new task
Bot: 
🔢 Enter task number:  1
📝 Enter task description:  Add another features
💾 Task list updated successfully!
🚀 Task added successfully!
You:  now show me tasklist

Bot: 
📋 Your Task List
Task No.  Description                   Status    
--------------------------------------------------
1         Add another features          ⏳ Pending

You:  mark it complete
Bot: 
✔️ Enter task number to mark complete:  1
💾 Task list updated successfully!
🎉 Task marked as completed!

You:  show
Bot: 
📋 Your Task List
Task No.  Description                   Status    
--------------------------------------------------
1         Add another features          ✅ Done  

You:  delete
Bot: 
🗑️ Enter task number to delete:  1
💾 Task list updated successfully!
🗑️ Task 1 deleted successfully!

You:  show
Bot: 📭 No tasks available. Add one!

You:  quit
👋 Goodbye Kedar! See you soon! ✨
📁 JSON File Format
```
## Tasks are stored in this structure:
```
{
    "tasks": [
        {
            "Task_No": 1,
            "Description": "Buy groceries",
            "Status": false
        },
        {
            "Task_No": 2,
            "Description": "Finish report",
            "Status": true
        }
    ]
}
```
## 🧠 What This Project Demonstrates

1. __Object-Oriented Programming (OOP)__
2. __File Handling in Python__
3. __JSON Read/Write operations__
4. __Exception Handling__
5. __Input Validation__
6. __Basic Command Parsing (Chatbot Logic)__
7. __Clean CLI Formatting__

## 🔮 Future Improvements

- 📅 Add due dates
- 🏷️ Add priority levels
- 🔍 Search tasks
- 🎨 Add colored terminal output
- 🖼️ Convert to GUI (Tkinter)
- 🌐 Convert to Web App (Flask / Django)


## 🛠️ Troubleshooting
- Not writing to file → Ensure you enter a valid file path when prompted. The program will create the file if it doesn’t exist, but the directory must exist.
- Old version runs when importing → Delete the` __pycache__` folder or run with `python -B. Use print(TaskManager.__file__) `to confirm which file is being imported.

