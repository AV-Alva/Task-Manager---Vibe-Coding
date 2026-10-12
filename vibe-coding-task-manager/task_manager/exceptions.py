class TaskManagerError(Exception):
    """Base class for exceptions in task manager."""
    pass

class TaskNotFoundError(TaskManagerError):
    """Exception raised when a task is not found."""
    pass

class StorageError(TaskManagerError):
    """Exception raised for storage-related errors."""
    pass