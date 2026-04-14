#!/usr/bin/env python3

import sys
from todo import TodoManager


def main():
    manager = TodoManager()
    if len(sys.argv) > 1:
        command = sys.argv[1]
        if command == 'add':
            task = ' '.join(sys.argv[2:])
            manager.add_task(task)
        elif command == 'remove':
            try:
                task_id = int(sys.argv[2])
                manager.remove_task(task_id)
            except ValueError:
                print('Please provide a valid task ID.')
        elif command == 'list':
            manager.list_tasks()
        else:
            print('Unknown command. Use add, remove, or list.')
    else:
        print('Usage: todo.py add|remove|list [task]')

if __name__ == '__main__':
    main()
