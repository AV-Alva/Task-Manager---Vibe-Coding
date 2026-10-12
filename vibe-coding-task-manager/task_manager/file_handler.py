import json
import os
from threading import Lock

class FileHandler:
    def __init__(self, file_path):
        """
        Initialize the FileHandler with the JSON file path.
        """
        self.file_path = file_path
        self.lock = Lock()  # To handle concurrent file access safely
        # Ensure the file exists and is valid JSON
        self._ensure_file()

    def _ensure_file(self):
        """
        Ensure the JSON file exists and contains valid JSON.
        If the file is missing, create an empty list JSON.
        If the file content is invalid, reset to empty list.
        """
        if not os.path.exists(self.file_path):
            try:
                with open(self.file_path, 'w', encoding='utf-8') as f:
                    json.dump([], f)
            except OSError as e:
                raise RuntimeError(f"Unable to create file {self.file_path}: {e}")
        else:
            try:
                with open(self.file_path, 'r', encoding='utf-8') as f:
                    json.load(f)
            except (json.JSONDecodeError, OSError):
                # Reset to empty list if invalid JSON or file access error
                try:
                    with open(self.file_path, 'w', encoding='utf-8') as f:
                        json.dump([], f)
                except OSError as e:
                    raise RuntimeError(f"Unable to reset file {self.file_path}: {e}")

    def _read_tasks(self):
        """
        Read the list of tasks from the JSON file.
        """
        try:
            with self.lock:
                with open(self.file_path, 'r', encoding='utf-8') as f:
                    tasks = json.load(f)
                return tasks
        except FileNotFoundError:
            # If file disappeared, create empty and return empty list
            self._ensure_file()
            return []
        except (json.JSONDecodeError, OSError) as e:
            raise RuntimeError(f"Error reading tasks from file {self.file_path}: {e}")

    def _write_tasks(self, tasks):
        """
        Write the list of tasks to the JSON file.
        """
        try:
            with self.lock:
                with open(self.file_path, 'w', encoding='utf-8') as f:
                    json.dump(tasks, f, indent=2)
        except OSError as e:
            raise RuntimeError(f"Error writing tasks to file {self.file_path}: {e}")

    def add(self, task):
        """
        Add a task to the JSON file.
        """
        tasks = self._read_tasks()
        tasks.append(task)
        self._write_tasks(tasks)
        return task

    def get_by_id(self, task_id):
        """
        Get a task by ID.
        """
        tasks = self._read_tasks()
        for task in tasks:
            if task.get('id') == task_id:
                return task
        return None

    def update(self, updated_task):
        """
        Update an existing task.
        """
        tasks = self._read_tasks()
        for i, task in enumerate(tasks):
            if task.get('id') == updated_task.get('id'):
                tasks[i] = updated_task
                self._write_tasks(tasks)
                return
        raise RuntimeError(f"Task with id {updated_task.get('id')} not found for update.")

    def delete(self, task_id):
        """
        Delete a task by ID.
        """
        tasks = self._read_tasks()
        new_tasks = [task for task in tasks if task.get('id') != task_id]
        if len(new_tasks) == len(tasks):
            raise RuntimeError(f"Task with id {task_id} not found for delete.")
        self._write_tasks(new_tasks)
