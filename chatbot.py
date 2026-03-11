import re
import random as rd
from dateparser import parse
import task_manager
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
    userInput_lower = userInput.lower()

    greet_pattern = re.compile(r"\b(hi|hello|hey)\b", re.IGNORECASE)
    add_pattern = re.compile(r"\b(add|new)\s*(task)?(.*?)(\s*(?:no|number|id))?\s*(\d+)?\b",re.IGNORECASE)
    date_match = re.search(r"(\bby|due|before)?\s*(today|tomorrow|\d{1,2}\s+\w+|\d{4}-\d{2}-\d{2})\b", userInput_lower, re.IGNORECASE)
    priority_match = re.search(r"\b(high|medium|low|normal)\b", userInput_lower, re.IGNORECASE)
    delete_pattern = re.compile(r"\b(delete|remove|erase|cancel)\s*(task)?(\s*(?:no|number|id))?\s*(\d+(?:,\s*\d+)*)?\b",re.IGNORECASE)
    mark_pattern = re.compile(r"\b(mark|complete|done)\s*(task)?(\s*(?:no|number|id))?\s*(\d+(?:,\s*\d+)*)\b",re.IGNORECASE)
    display_pattern = re.compile(r"\b(display|show)\s*(all)?\s*(completed|done)?(incomplete|not done|pending)?(overdue)?(menu|fun\w+|oper\w+)?\s*(tasks?)?\b",re.IGNORECASE)
    
    if greet_pattern.search(userInput_lower):
        print(rd.choice(self.botresponses["greet"]))
    
    elif add_pattern.search(userInput_lower):
        match = add_pattern.search(userInput_lower)
        taskid = int(match.group(5)) if match.group(5) else len(self._data["tasks"]) + 1
        taskdes =re.sub(r"\b(add|new|task|by|due|before|priority|high|medium|low|normal|tomorrow|today)\b","",userInput_lower).strip()
        dueinput = None
        priority = "normal"
        if match:
            if date_match:
                dueinput = date_match.group(2).strip()
                parsed_date = parse(dueinput,settings={"PREFER_DATES_FROM": "future"})
                if parsed_date:
                    dueinput = parsed_date.strftime("%Y-%m-%d %H:%M")
                else:
                    print("⚠️ Could not understand the date.")
                    return
            if priority_match:
                priority = priority_match.group(1).lower() 
        self.InputTaskDetails(taskid,taskdes,dueinput,priority)
    
    elif display_pattern.search(userInput_lower):
        match = display_pattern.search(userInput_lower)
        dis=0
        if match.group(3):dis=1
        elif match.group(4):dis=2
        elif match.group(5):dis=3
        elif match.group(6):dis=4
        else:dis=0
        self.display(dis)
    
    elif mark_pattern.search(userInput_lower):
        matches = re.finditer(r"\d+", userInput_lower)
        for m in matches:
            num = int(m.group())
            self.markComplete(num) 
    
    elif delete_pattern.search(userInput_lower):
        match = re.finditer(r'\d+', userInput_lower)
        for mat in match:
            num = int(mat.group())
            self.deleteTask(num)     
        
    else:
        print(rd.choice(self.botresponses["error"]))