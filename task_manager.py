import json
import os

import coloring as cg
from chatbot import rd
from util import dueDate


class TaskManager:
    def __init__(self, filepath, username):
        self.filepath = filepath
        self._data = {"tasks": []}
        self.username = username
        self.botresponses = {
        "greet": [
            "👋 Hi there!",
            f"😊 Hello {username}!",
            f"😄 Hey {username}! Nice to see you again!",
            f"✨ Welcome back {username}!",
        ],

        "add": [
            "✅ Got it! Task added.",
            "📌 Your task has been added!",
            "📝 Alright, I've added that to your list.",
            "💾 Done! Task saved successfully.",
            "🚀 Task added successfully!",
        ],

        "delete": [
            "🗑️ Task removed successfully.",
            "❌ Alright, that task is deleted.",
            "🧹 Deleted! Your list looks cleaner now.",
            "🚮 Task erased from the list.",
        ],

        "display": [
            "📋 Here are your tasks:",
            "👀 Let me show your task list.",
            "📑 These are the tasks I found:",
            "📂 Opening your task list now.",
        ],

        "mark_done": [
            "🎉 Great work! That task is done.",
            "✅ I've marked that task as finished.",
            "🏁 Task successfully completed.",
        ],

        "error": [
            "🤔 Sorry, I didn't understand that.",
            "🔁 Could you rephrase that?",
            "😅 I'm not sure what you mean.",
            "💡 Try asking in a different way.",
        ],
        }

    def read_data(self):
        """Load task data from the JSON file."""
        try:
            if not os.path.exists(self.filepath):
                cg.console.log("File not found. Creating a new task file...")
                self._data = {"tasks": []}
                with open(self.filepath, "w", encoding="utf-8") as f:
                    json.dump(self._data, f, indent=4)
                cg.console.log("🗃️  New file created successfully.")
            else:
                with open(self.filepath, "r", encoding="utf-8") as f:
                    try:
                        self._data = json.load(f)
                        cg.console.log("🗃️  Task data loaded successfully.")
                    except json.JSONDecodeError:
                        cg.console.log("⚠️  File empty or invalid. Initializing new task list...")
                        self._data = {"tasks": []}
        except Exception as e:
            cg.console.log(f"⚠️  Unexpected error: {e}")

    def InputTaskDetails(self, taskid=None, taskdes=None, dueinput=None, priority=None):
        """Add a new task to the task list."""
        try:
            if taskid is None:
                raise ValueError("⚠️  Please assign a task ID.")
            if not taskdes:
                raise ValueError("⚠️  Please enter a task description.")
            if dueinput is None:
                raise ValueError("⚠️  Please enter a valid date.")

            for task in self._data["tasks"]:
                if task["Task_No"] == taskid:
                    raise ValueError("⚠️  Task number already exists. It should be unique.")

            priorities = {
                "high": "🔴",
                "medium": "🟡",
                "low": "🟢",
                "normal": "⚪"
            }

            if priority not in priorities:
                raise ValueError("⚠️  Please enter a valid priority.")

            task = {
                "Task_No": taskid,
                "Description": taskdes,
                "Status": False,
                "Due_Date": dueinput,
                "Priority": priorities[priority],
            }

            self._data["tasks"].append(task)
            self.update_json()
            cg.processing()
            cg.bot(rd.choice(self.botresponses["add"]))

        except ValueError as e:
            cg.bot(str(e))

    def markComplete(self, taskid):
        """Mark a task as completed using its Task ID."""
        found = False
        for task in self._data["tasks"]:
            if task["Task_No"] == taskid:
                found = True
                if task["Status"]:
                    cg.bot("🫡Task already completed.")
                else:
                    task["Status"] = True
                    self.update_json()
                    cg.bot(rd.choice(self.botresponses["mark_done"]))
                break

        if not found:
            cg.bot("⚠️  No task found with that number.")

    def deleteTask(self, taskid):
        """Delete a task from the list using its Task ID."""
        for task in self._data["tasks"]:
            if task["Task_No"] == taskid:
                cg.deleting()
                self._data["tasks"].remove(task)
                self.update_json()
                cg.bot(rd.choice(self.botresponses["delete"]))
                return

        cg.bot("⚠️  No task found with that number.")

    def display(self, what):
        """
        Display tasks based on filter.

        what = 0 -> show all tasks
        what = 1 -> show completed tasks
        what = 2 -> show pending tasks
        what = 3 -> show overdue tasks
        what = 4 -> show menu
        """
        if what == 4:
            cg.console.print(
                cg.Panel(
                    """\n1. Add a new task.\n2. Display :\n\ta.All tasks.\n\tb.Completed/Pending/Overdue Tasks.\n\tc.Menu\n3. Mark task completed(single/multiple).\n4. Delete task(single/multiple)\n5. Exit program""".strip(),title="[b red]MENU[/b red]",title_align="center",style="black on white",border_style="black",box=cg.box.HEAVY_EDGE)
            )
            return

        if not self._data["tasks"]:
            cg.bot("⚠️  No tasks available. Add one!")
            return

        cg.console.print(cg.Panel("📋 Your Tasks Dashboard",expand=True,border_style="black",style="black on white",box=cg.box.HEAVY_EDGE))
        cg.console.print()
        task_bin = []

        for task in self._data["tasks"]:
            due = task.get("Due_Date")
            if not due:
                cg.bot("⚠️  Invalid task data: missing Due_Date")
                continue
            remaining = dueDate(due)

            if task["Status"]:
                status = "✅ Done"
                remaining_time = "-"
            elif remaining == "❌ Overdue":
                status = "❌ Overdue"
                remaining_time = "-"
            else:
                status = "📋 Pending"
                remaining_time = remaining

            if what == 1 and not task["Status"]:
                continue

            if what == 2 and task["Status"]:
                continue

            if what == 3 and remaining != "❌ Overdue":
                continue

            task_dis = (
                f"Task ID : [b red]{task['Task_No']}[/ b red]\n"
                f"Description : [cyan]{task['Description']}[/cyan]\n"
                f"Priority : {task['Priority']}\n"
                f"Status : [green]{status}[/green]\n"
                f"Due Time : [b red]{remaining_time}[/b red]"
            )
            task_bin.append(cg.Panel(task_dis, expand=True,border_style="black",style="black on white",box=cg.box.HEAVY_EDGE))
        cg.loading()

        if task_bin:
            cg.console.print(cg.Columns(task_bin))
        else:
            cg.bot("⚠️ No tasks match that filter.")

    def update_json(self):
        """Update the saved data."""
        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump(self._data, f, indent=4, ensure_ascii=False)
