# 🗂️ Task Manager (Python + JSON)
> A beginner‑friendly command‑line Task Manager built with Python.
It stores tasks in a JSON file, supports adding, displaying, marking tasks as completed, deleting tasks, and automatically saves changes.

## Features
- 📂 Persistent storage using JSON files
- ➕ Add new tasks with validation (unique task number, description length 5–30)
- 📋 Display tasks in a neat tabular format
- ✅ Mark tasks as completed
- ❌ Delete tasks
- 💾 Auto‑save after every change
- 🖥️ Menu‑driven interface

## Requirements
- Python 3.10+ (uses match statement)
- No external libraries required

## Usage
- Run as a script
`
python TaskManager.py
`
- You’ll be prompted to enter a file path:
`
Enter the File path: C:\Users\HP\MyProjects\Python\Beginners\tasks.json
`
- If the file doesn’t exist, it will be created automatically.

## Menu Options
```
*************[ Welcome To Task Manager ]*************

---------------[MENU]---------------
1. Add a new task.
2. Display all tasks.
3. Mark task completed.
4. Delete Task.
5. Exit program.



Example
Enter choice no.: 1
Enter task no.: 1
Enter task description: Buy groceries
Changes saved!
Task added!

Enter choice no.: 2
Task No.  Description                   Status
--------------------------------------------------
1         Buy groceries                 Pending

Enter choice no.: 3
Enter task no.: 1
Task completed
Changes saved!

Enter choice no.: 4
Enter task no. to delete: 1
Task 1 deleted!
Changes saved!

```
## File Format
- Tasks are stored in JSON like this:
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


## Troubleshooting
- Not writing to file → Ensure you enter a valid file path when prompted. The program will create the file if it doesn’t exist, but the directory must exist.
- Old version runs when importing → Delete the` __pycache__` folder or run with `python -B. Use print(TaskManager.__file__) `to confirm which file is being imported.

