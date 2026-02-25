import json
import os
data={}
#____________________________________________________
def read_data():
    #print(">>> Running NEW version 0.2 of To-Do App <<<")
    global data,filepath
    filepath = input(r"Enter the File path:")
    try:
        if not os.path.exists(filepath):
            print(f"{filepath} not found, creating new file...")
            data = {"tasks": []}
            with open(filepath, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)
                return True
        else:
            with open(filepath, "r", encoding='utf-8') as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError:
                    print("File empty, initializing new task list...")
                    data = {"tasks": []}
            if not isinstance(data, dict):
                print("Error: JSON root element must be an object (dictionary)!")
                return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False
    else:
        menu()

#____________________________________________________
def InputTaskDetails():
    global data
    try:
        task_no = int(input("Enter task no.:"))
        for task in data['tasks']:
            if task['Task_No'] == task_no:
                raise ValueError("Task no already exists!")
        task_info = input("Enter task description:")
        if len(task_info) not in range(5, 30):
            raise ValueError("Description must include characters in range (5–30)")
        task = {
            "Task_No": task_no,
            "Description": task_info,
            "Status": False
        }
        data['tasks'].append(task)
        update_json()
        print("Task added!")
    except Exception as e:
        print(f"Error: {e}")

#____________________________________________________
def display():
    global data
    if not data['tasks']:
        print("Tasklist is empty!")
    else:
        print(f"{'Task No.':<10}{'Description':<30}{'Status':<10}")
        print("-" * 50)
        
        # Print each task
        for task in data['tasks']:
            status = "Done" if task['Status'] else "Pending"
            print(f"{task['Task_No']:<10}{task['Description']:<30}{status:<10}")

#____________________________________________________
def markComplete():
    global data
    taskComplete_no = int(input("Enter task no.:"))
    found = False
    try:
        for task in data['tasks']:
            if task['Task_No'] == taskComplete_no:
                found = True
                if task['Status']:
                    print("Task already marked!")
                else:
                    task['Status'] = True
                    update_json()
                    print("Task completed")
        if not found:
            print("No task found!")
        return True
    except TypeError:
        print("No task found!")
        return False

#____________________________________________________
def update_json():
    global data, filepath
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print("Changes saved!")
#____________________________________________________
def deleteTask():
    global data
    try:
        task_no = int(input("Enter task no. to delete: "))
        found = False
        for task in data['tasks']:
            if task['Task_No'] == task_no:
                data['tasks'].remove(task)
                update_json()  
                print(f"Task {task_no} deleted!")
                found = True
                break
        if not found:
            print("No task found with that number!")
    except Exception as e:
        print(f"Error: {e}")
#____________________________________________________
def menu():
    print("\n*************[ Welcome To TO-DO List App ]*************")
    while True:
        print("\n---------------[MENU]---------------")
        print("1. Add a new task.\n2. Display all tasks.\n3. Mark task completed.\n4. Delete Task.\n5. Exit program.")
        choice = int(input("Enter choice no.:"))
        match choice:
            case 1:
                InputTaskDetails()
            case 2:
                display()
            case 3:
                markComplete()
            case 4:
                deleteTask()
            case 5:
                print("Exited!")
                break
            case _:
                print("Invalid choice!")

#____________________________________________________
if __name__ == "__main__":
    filepath = r"C:\Users\HP\MyProjects\Python\Beginners\tasks.json"
    read_data()

