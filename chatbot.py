import re
import random as rd

from dateparser import parse

import coloring as cg


def chatbot(self, userInput):
    """
    Main chatbot interface.
    Uses regex to detect user intent:
    - greeting
    - add task
    - display tasks
    - mark task complete
    - delete task
    """
    user_input_lower = userInput.lower()

    greet_pattern = re.compile(r"\b(hi|hello|hey)\b", re.IGNORECASE)
    add_pattern = re.compile(r"\b(add|new)\b\s*(?:task\b)?\s*(?P<body>.+)", re.IGNORECASE)
    date_pattern = re.compile(
        r"\b(by|due|before)\b\s*(today|tomorrow|\d{1,2}\s+\w+|\d{4}-\d{2}-\d{2})\b",
        re.IGNORECASE,
    )
    priority_pattern = re.compile(r"\b(high|medium|low|normal)\b", re.IGNORECASE)
    id_pattern = re.compile(r"\b(?:no|number|id)\b\s*(\d+)", re.IGNORECASE)
    delete_pattern = re.compile(
        r"\b(delete|remove|erase|cancel)\s*(task)?(\s*(?:no|number|id))?\s*(\d+(?:,\s*\d+)*)?\b",
        re.IGNORECASE,
    )
    mark_pattern = re.compile(
        r"\b(mark|complete|done)\s*(task)?(\s*(?:no|number|id))?\s*(\d+(?:,\s*\d+)*)\b",
        re.IGNORECASE,
    )
    display_pattern = re.compile(
        r"\b(display|show)\s*(all)?\s*(completed|done)?(incomplete|not done|pending)?(overdue)?(menu|fun\w+|oper\w+)?\s*(tasks?)?\b",
        re.IGNORECASE,
    )

    if greet_pattern.search(user_input_lower):
        cg.bot(rd.choice(self.botresponses["greet"]))

    elif add_pattern.search(user_input_lower):
        match = add_pattern.search(user_input_lower)
        body = match.group("body").strip()
        dueinput = None
        priority = "normal"

        id_match = id_pattern.search(body)
        existing_ids = [task["Task_No"] for task in self._data["tasks"]]
        taskid = max(existing_ids, default=0) + 1
        if id_match:
            body = id_pattern.sub("", body).strip()

        date_match = date_pattern.search(body)
        if date_match:
            raw_date = date_match.group(2).strip()
            
            parsed_date = parse(raw_date, settings={"PREFER_DATES_FROM": "future"})
            if not parsed_date:
                cg.bot("⚠️ Invalid date format. Try 'tomorrow' or '2026-04-01'")
            if parsed_date:
                dueinput = parsed_date.strftime("%Y-%m-%d %H:%M")
            else:
                cg.bot("⚠️ Could not understand the date.")
                return
            body = date_pattern.sub("", body, count=1).strip()

        priority_match = priority_pattern.search(body)
        if priority_match:
            priority = priority_match.group(1).lower()
            body = priority_pattern.sub("", body, count=1).strip()
        
        taskdes = re.sub(r"\s+", " ", body).strip(" ,.-")
        if not taskdes:
            cg.bot("⚠️ Please enter a task description.")
            return
        self.InputTaskDetails(taskid, taskdes, dueinput, priority)

    elif display_pattern.search(user_input_lower):
        match = display_pattern.search(user_input_lower)
        dis = 0
        if match.group(3):
            dis = 1
        elif match.group(4):
            dis = 2
        elif match.group(5):
            dis = 3
        elif match.group(6):
            dis = 4
        self.display(dis)

    elif mark_pattern.search(user_input_lower):
        match = mark_pattern.search(user_input_lower)
        for matched_id in re.finditer(r"\d+", match.group(4)):
            self.markComplete(int(matched_id.group()))

    elif delete_pattern.search(user_input_lower):
        match = delete_pattern.search(user_input_lower)
        if not match.group(4):
            cg.bot("⚠️ Please tell me which task number to delete.")
            return

        for matched_id in re.finditer(r"\d+", match.group(4)):
            self.deleteTask(int(matched_id.group()))

    else:
        cg.bot(rd.choice(self.botresponses["error"]))
