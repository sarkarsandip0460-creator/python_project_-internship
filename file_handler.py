import json
import os
from task_manager_app.task import Task

def read_tasks(filename):
    """Load tasks from JSON file."""
    if not os.path.exists(filename):
        return []

    try:
        with open(filename, "r") as f:
            data = json.load(f)
            return [Task.from_dict(item) for item in data]
    except (json.JSONDecodeError, FileNotFoundError):
        return []

def write_tasks(filename, tasks):
    """Save tasks to JSON file."""
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w") as f:
        json.dump([task.to_dict() for task in tasks], f, indent=4)

