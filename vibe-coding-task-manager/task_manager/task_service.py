from task_manager.exceptions import TaskNotFoundError

class TaskService:
    def __init__(self, repository):
        """
        Initialize the TaskService with a repository for task storage.
        The repository is expected to have methods: add, get_by_id, update, and delete.
        """
        self.repository = repository

    def add_task(self, task):
        """
        Add a new task to the repository.

        Args:
            task: The task object to add.

        Returns:
            The added task object.
        """
        return self.repository.add(task)

    def view_task(self, task_id):
        """
        Retrieve a task by its ID.

        Args:
            task_id: The ID of the task to retrieve.

        Returns:
            The task object with the given ID.

        Raises:
            TaskNotFoundError: If no task with the given ID exists.
        """
        task = self.repository.get_by_id(task_id)
        if not task:
            raise TaskNotFoundError(f"Task with id {task_id} not found.")
        return task

    def complete_task(self, task_id):
        """
        Mark a task as completed by its ID.

        Args:
            task_id: The ID of the task to mark as completed.

        Returns:
            The updated task object.

        Raises:
            TaskNotFoundError: If no task with the given ID exists.
        """
        task = self.repository.get_by_id(task_id)
        if not task:
            raise TaskNotFoundError(f"Task with id {task_id} not found.")
        task['completed'] = True
        self.repository.update(task)
        return task

    def delete_task(self, task_id):
        """
        Delete a task by its ID.

        Args:
            task_id: The ID of the task to delete.

        Raises:
            TaskNotFoundError: If no task with the given ID exists.
        """
        task = self.repository.get_by_id(task_id)
        if not task:
            raise TaskNotFoundError(f"Task with id {task_id} not found.")
        self.repository.delete(task_id)
