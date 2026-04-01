from datetime import datetime
"""
Calculates remaining time until task deadline.
Returns:
- "Overdue"
- "Due soon"
- "Xd Xh Xm left"
"""
def dueDate(due_date_str):

    due_date = datetime.strptime(due_date_str, "%Y-%m-%d %H:%M")
    now = datetime.now()

    remaining = due_date - now

    if remaining.total_seconds() < 0:
        return "Overdue"

    if remaining.days == 0 and remaining.seconds <= 3600:
        return "Due soon"

    days = remaining.days
    hours = remaining.seconds // 3600
    minutes = (remaining.seconds % 3600) // 60

    return f"{days}d {hours}h {minutes}m left"
