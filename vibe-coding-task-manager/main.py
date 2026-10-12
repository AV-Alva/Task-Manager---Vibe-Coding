import argparse
import sys
import shlex
from task_manager.task_service import TaskService
from task_manager.file_handler import FileHandler
from task_manager.exceptions import TaskNotFoundError
from task_manager.logger import logger

def main():
    logger.info("Task Manager CLI started")
    repo = FileHandler('tasks.json')
    service = TaskService(repo)

    parser = argparse.ArgumentParser(description="Task Manager CLI")
    subparsers = parser.add_subparsers(dest='command', required=True)

    add_parser = subparsers.add_parser('add', help='Add a new task')
    add_parser.add_argument('title', type=str, help='Title of the task')
    add_parser.add_argument('-d', '--description', type=str, default='', help='Description of the task')

    view_parser = subparsers.add_parser('view', help='View a task by ID')
    view_parser.add_argument('id', type=str, help='ID of the task to view')

    complete_parser = subparsers.add_parser('complete', help='Mark a task as completed')
    complete_parser.add_argument('id', type=str, help='ID of the task to complete')

    delete_parser = subparsers.add_parser('delete', help='Delete a task by ID')
    delete_parser.add_argument('id', type=str, help='ID of the task to delete')

    list_parser = subparsers.add_parser('list', help='List all tasks')

    def print_menu():
        logger.debug("Printing command menu")
        print("Available commands:")
        print("  add <title> [-d description]  - Add a new task")
        print("  view <id>                    - View a task by ID")
        print("  complete <id>                - Mark a task as completed")
        print("  delete <id>                  - Delete a task by ID")
        print("  list                        - List all tasks")
        print("  exit or quit                - Exit the application")

    print("Welcome to Task Manager CLI. Type 'exit' or 'quit' to leave.")
    print_menu()

    while True:
        try:
            print("> ", end='', flush=True)
            line = input()
        except EOFError:
            print()
            break

        line = line.strip()
        if line.lower() in ('exit', 'quit'):
            logger.info("Exiting Task Manager CLI")
            print("Exiting Task Manager CLI.")
            break
        if not line:
            print_menu()
            continue

        try:
            args = parser.parse_args(shlex.split(line))
        except SystemExit:
            continue

        try:
            if args.command == 'add':
                def generate_task_id():
                    tasks = repo._read_tasks()
                    existing_ids = {task.get('id') for task in tasks if task.get('id')}
                    for i in range(1, 10000):
                        candidate = f"{i:04d}"
                        if candidate not in existing_ids:
                            return candidate
                    raise RuntimeError("Exceeded maximum number of tasks (9999)")

                task = {
                    'id': generate_task_id(),
                    'title': args.title,
                    'description': args.description,
                    'completed': False
                }
                added_task = service.add_task(task)
                logger.info(f"Added task with ID: {added_task['id']}")
                print(f"Task added with ID: {added_task['id']}")

            elif args.command == 'view':
                task = service.view_task(args.id)
                logger.info(f"Viewed task with ID: {args.id}")
                print(f"ID: {task['id']}")
                print(f"Title: {task['title']}")
                print(f"Description: {task.get('description', '')}")
                print(f"Completed: {'Yes' if task.get('completed') else 'No'}")

            elif args.command == 'complete':
                task = service.complete_task(args.id)
                logger.info(f"Completed task with ID: {args.id}")
                print(f"Task {task['id']} marked as completed.")

            elif args.command == 'delete':
                service.delete_task(args.id)
                logger.info(f"Deleted task with ID: {args.id}")
                print(f"Task {args.id} deleted.")

            elif args.command == 'list':
                tasks = repo._read_tasks()
                if not tasks:
                    print("No tasks found.")
                else:
                    for task in tasks:
                        print(f"ID: {task['id']}")
                        print(f"  Title: {task['title']}")
                        print(f"  Description: {task.get('description', '')}")
                        print(f"  Completed: {'Yes' if task.get('completed') else 'No'}")
                        print()
        except TaskNotFoundError as e:
            logger.error(f"Task not found: {e}")
            print(f"Error: {e}")
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            import traceback
            traceback.print_exc()

if __name__ == '__main__':
    main()
import argparse
import sys
import shlex
from task_manager.task_service import TaskService
from task_manager.file_handler import FileHandler
from task_manager.exceptions import TaskNotFoundError

def main():
    repo = FileHandler('tasks.json')
    service = TaskService(repo)

    parser = argparse.ArgumentParser(description="Task Manager CLI")
    subparsers = parser.add_subparsers(dest='command', required=True)

    add_parser = subparsers.add_parser('add', help='Add a new task')
    add_parser.add_argument('title', type=str, help='Title of the task')
    add_parser.add_argument('-d', '--description', type=str, default='', help='Description of the task')

    view_parser = subparsers.add_parser('view', help='View a task by ID')
    view_parser.add_argument('id', type=str, help='ID of the task to view')

    complete_parser = subparsers.add_parser('complete', help='Mark a task as completed')
    complete_parser.add_argument('id', type=str, help='ID of the task to complete')

    delete_parser = subparsers.add_parser('delete', help='Delete a task by ID')
    delete_parser.add_argument('id', type=str, help='ID of the task to delete')

    list_parser = subparsers.add_parser('list', help='List all tasks')

    def print_menu():
        print("Available commands:")
        print("  add <title> [-d description]  - Add a new task")
        print("  view <id>                    - View a task by ID")
        print("  complete <id>                - Mark a task as completed")
        print("  delete <id>                  - Delete a task by ID")
        print("  list                        - List all tasks")
        print("  exit or quit                - Exit the application")

    import sys
    print("Welcome to Task Manager CLI. Type 'exit' or 'quit' to leave.")
    print_menu()
    sys.stdout.flush()
import argparse
import sys
import uuid
from task_manager.task_service import TaskService
from task_manager.file_handler import FileHandler
from task_manager.exceptions import TaskNotFoundError

def main():
    import shlex
    import sys
    import uuid
    repo = FileHandler('tasks.json')
    service = TaskService(repo)

    import argparse
    parser = argparse.ArgumentParser(description="Task Manager CLI")
    subparsers = parser.add_subparsers(dest='command', required=True)

    add_parser = subparsers.add_parser('add', help='Add a new task')
    add_parser.add_argument('title', type=str, help='Title of the task')
    add_parser.add_argument('-d', '--description', type=str, default='', help='Description of the task')

    view_parser = subparsers.add_parser('view', help='View a task by ID')
    view_parser.add_argument('id', type=str, help='ID of the task to view')

    complete_parser = subparsers.add_parser('complete', help='Mark a task as completed')
    complete_parser.add_argument('id', type=str, help='ID of the task to complete')

    delete_parser = subparsers.add_parser('delete', help='Delete a task by ID')
    while True:
        try:
            print("> ", end='', flush=True)
            line = input()
        except EOFError:
            print()
            break

        line = line.strip()

        if line.lower() in ('exit', 'quit'):
            print("Exiting Task Manager CLI.")
            break

        if not line:
            print_menu()
            sys.stdout.flush()
            continue

        try:
            if args.command == 'add':
                def generate_task_id():
                    tasks = repo._read_tasks()
                    existing_ids = {task.get('id') for task in tasks if task.get('id')}
                    for i in range(1, 10000):
                        candidate = f"{i:04d}"
                        if candidate not in existing_ids:
                            return candidate
                    raise RuntimeError("Exceeded maximum number of tasks (9999)")

                task = {
                    'id': generate_task_id(),
                    'title': args.title,
                    'description': args.description,
                    'completed': False
                }
                added_task = service.add_task(task)
                print(f"Task added with ID: {added_task['id']}")

            elif args.command == 'view':
                task = service.view_task(args.id)
                print(f"ID: {task['id']}")
                print(f"Title: {task['title']}")
                print(f"Description: {task.get('description', '')}")
                print(f"Completed: {'Yes' if task.get('completed') else 'No'}")

            elif args.command == 'complete':
                task = service.complete_task(args.id)
                print(f"Task {task['id']} marked as completed.")

            elif args.command == 'delete':
                service.delete_task(args.id)
                print(f"Task {args.id} deleted.")

            elif args.command == 'list':
                tasks = repo._read_tasks()
                if not tasks:
                    print("No tasks found.")
                else:
                    for task in tasks:
                        print(f"ID: {task['id']}")
                        print(f"  Title: {task['title']}")
                        print(f"  Description: {task.get('description', '')}")
                        print(f"  Completed: {'Yes' if task.get('completed') else 'No'}")
                        print()
        except TaskNotFoundError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error: {e}")
            import traceback
            traceback.print_exc()
            print()
        except Exception as e:
            print(f"Error: {e}")
            import traceback
            traceback.print_exc()


if __name__ == '__main__':
    main()
