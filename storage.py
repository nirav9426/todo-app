import json

FILENAME = 'tasks.json'

def save_tasks(tasks):
    with open(FILENAME, 'w') as f:
        json.dump(tasks, f)

def load_tasks():
    try:
        with open(FILENAME, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
