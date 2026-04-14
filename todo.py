class TodoManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f'Task added: {task}')

    def remove_task(self, task_id):
        if 0 <= task_id < len(self.tasks):
            removed_task = self.tasks.pop(task_id)
            print(f'Task removed: {removed_task}')
        else:
            print('Invalid task ID.')

    def list_tasks(self):
        if self.tasks:
            for index, task in enumerate(self.tasks):
                print(f'{index}: {task}')
        else:
            print('No tasks found.')
