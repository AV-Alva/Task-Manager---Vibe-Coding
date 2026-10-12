# Python CLI Daily Task Manager – Vibe Coding Challenge

## Project Overview

The **Daily Task Manager** is a Python-based Command-Line Interface (CLI) productivity application developed using an AI-assisted programming approach known as **Vibe Coding**.

The objective of this project is to demonstrate how AI coding assistants such as ChatGPT, Claude, or GitHub Copilot can support software development through an iterative process of requirement analysis, design, coding, debugging, testing, and refactoring.

Instead of generating the entire application in a single AI prompt, the project is developed incrementally, with each module created, reviewed, and tested separately.

## Features

- **Add Task:** Create a new task.
- **View Tasks:** Display all existing tasks and their completion status.
- **Complete Task:** Mark a selected task as completed.
- **Delete Task:** Remove an existing task.
- **Persistent Storage:** Save and retrieve tasks using a JSON file.
- **Exception Handling:** Handle invalid inputs, missing tasks, and file-related errors.
- **Custom Exceptions:** Use `TaskNotFoundError` for task-specific failures.
- **Logging:** Record application activities and errors in a log file.
- **Menu-Driven Interface:** Provide an interactive CLI using a Python `while` loop.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python 3 | Application development |
| VS Code | Code editor and execution |
| ChatGPT | AI-assisted development |
| JSON | Persistent task storage |
| Python logging | Application activity tracking |
| Git | Version control |
| GitHub | Source code hosting |

## Project Structure

```text
vibe-coding-task-manager/
│
├── main.py
├── README.md
├── .gitignore
│
├── task_manager/
│   ├── __init__.py
│   ├── task_service.py
│   ├── file_handler.py
│   ├── exceptions.py
│   └── logger_config.py
│
├── data/
│   └── tasks.json
│
└── logs/
    └── application.log
```

### Module Responsibilities

**main.py**

The entry point of the application. Displays the CLI menu, accepts user input, and coordinates task operations.

**task_service.py**

Contains the business logic for adding, viewing, completing, and deleting tasks.

**file_handler.py**

Handles reading and writing task information to `tasks.json`.

**exceptions.py**

Defines custom exceptions such as `TaskNotFoundError`.

**logger_config.py**

Configures application logging and stores relevant events in `application.log`.

**__init__.py**

Identifies `task_manager` as a Python package.

## Installation and Execution

### Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/vibe-coding-task-manager.git
```

Replace `YOUR_USERNAME` with your GitHub username after publishing the repository.

### Step 2: Navigate to the Project Directory

```bash
cd vibe-coding-task-manager
```

### Step 3: Verify Python Installation

```bash
python --version
```

### Step 4: Run the Application

```bash
python main.py
```

The application uses Python's standard library, so no third-party dependencies are required for the planned implementation.

## Sample CLI Output

The following illustrates the intended application behavior.

```text
========== DAILY TASK MANAGER ==========

1. Add Task
2. View Tasks
3. Complete Task
4. Delete Task
5. Exit

Enter your choice: 1

Enter task: Complete Python Assignment

Task added successfully!
```

### View Tasks

```text
Enter your choice: 2

---------- TASK LIST ----------

1. [Pending] Complete Python Assignment
2. [Completed] Watch Python Tutorial
```

### Complete Task

```text
Enter your choice: 3

Enter Task ID: 1

Task marked as completed!
```

### Delete Task

```text
Enter your choice: 4

Enter Task ID: 2

Task deleted successfully!
```

### Exit

```text
Enter your choice: 5

Thank you for using Daily Task Manager!
```

Actual messages and task identifiers may differ depending on the final implementation.

## Python Concepts Demonstrated

### 1. Packages and Modules

The project uses a Python package named `task_manager`, containing separate modules for different responsibilities.

This demonstrates modular programming and separation of concerns.

### 2. Imports

Modules communicate using Python imports.

Example:

```python
from task_manager.exceptions import TaskNotFoundError
```

### 3. Functions

Reusable functions implement operations such as adding, viewing, completing, and deleting tasks.

### 4. Loops and Conditional Statements

A `while` loop keeps the CLI application running until the user selects Exit.

Conditional statements determine which menu operation should execute.

### 5. File Handling

The application uses JSON to preserve tasks between executions.

### 6. Exception Handling

The project demonstrates:

```python
try:
    # Perform an operation
    pass

except Exception as error:
    # Handle an error
    print(error)

finally:
    # Execute required cleanup
    pass
```

The actual application should use specific exception types where possible and meaningful cleanup in `finally`.

### 7. Custom Exceptions

A custom exception provides meaningful error information.

```python
class TaskNotFoundError(Exception):
    """Raised when a requested task does not exist."""
    pass
```

### 8. Logging

The application uses Python's `logging` module.

- `INFO`: Successful task operations.
- `WARNING`: Invalid user inputs or task requests.
- `ERROR`: File handling and other application failures.

Log file location:

```text
logs/application.log
```

## Vibe Coding Development Process

The project follows an incremental AI-assisted development workflow.

| Step | Activity |
|---|---|
| 1 | Understand project requirements |
| 2 | Design package and module architecture |
| 3 | Generate the custom exception module |
| 4 | Implement task management operations |
| 5 | Implement JSON file storage |
| 6 | Run the application and identify errors |
| 7 | Debug errors using AI assistance |
| 8 | Add exception handling and logging |
| 9 | Refactor the code |
| 10 | Test the complete application |

The developer remains responsible for understanding, reviewing, testing, and validating AI-generated code.

## AI Prompts Used During Development

The following prompts represent the planned step-by-step AI workflow. Retain only prompts actually used during implementation and add any debugging prompts used.

### Prompt 1 – Requirement Analysis

"I need to build a Python CLI Daily Task Manager. Users should be able to add tasks, view tasks, mark tasks complete, delete tasks and exit. Don't generate code yet. Explain the requirements and suggest the features I should implement."

### Prompt 2 – Architecture Design

"Suggest a Python package/module structure for this project. It must have at least 4 Python files, one package, imports between modules, exception handling, a custom exception, logging and JSON file storage. Don't generate the implementation yet."

### Prompt 3 – Custom Exception

"Let's build only the exception module first. Create a custom TaskNotFoundError and explain why a custom exception is useful here."

### Prompt 4 – Task Management Module

"Now create the task service module for adding, viewing, completing and deleting tasks. Use TaskNotFoundError where appropriate. Explain each function."

### Prompt 5 – JSON File Handling

"Add a separate file handler module that stores tasks in a JSON file. Handle FileNotFoundError, invalid JSON and file access errors."

### Prompt 6 – Logging

"Create a logging configuration module. Store logs in logs/application.log. Log successful operations using INFO, invalid actions using WARNING, and failures using ERROR."

### Prompt 7 – CLI Implementation

"Now create main.py with a menu-driven while loop. Import functionality from the task_manager package instead of putting the business logic in main.py."

### Prompt 8 – Exception Handling

"Review the application and show me an appropriate place to demonstrate try/except/finally. Explain what happens in each block."

### Prompt 9 – Code Refactoring

"Review my current project for duplicated code, poor naming, unnecessary global variables and incorrect imports. Suggest improvements without rewriting the whole project."

### Prompt 10 – Testing

"Give me test scenarios for valid and invalid operations: adding a task, empty task name, viewing tasks, completing an invalid task ID, deleting an invalid task, missing JSON file and corrupted JSON."

## Testing

The following test cases should be executed and their actual results recorded.

| Test Case | Expected Result | Actual Result |
|---|---|---|
| Add a valid task | Task added successfully | Pending |
| View tasks | Display existing tasks | Pending |
| Complete a valid task | Status updated | Pending |
| Delete a valid task | Task removed | Pending |
| Enter an invalid task ID | Error handled gracefully | Pending |
| Enter an invalid menu choice | Warning displayed | Pending |
| Enter an empty task name | Input rejected | Pending |
| Run with missing JSON file | Missing file handled | Pending |
| Run with corrupted JSON | Invalid data handled | Pending |
| Restart application | Saved tasks restored | Pending |
| Exit application | Application terminates cleanly | Pending |

Replace `Pending` with `Pass` or `Fail` after executing each test.

## Debugging and Error Resolution

Document at least one genuine error encountered during development.

**Error Encountered:**  
[Enter the actual error message]

**Root Cause:**  
[Explain why the error occurred]

**AI Prompt Used:**  
[Copy the exact prompt submitted to the AI assistant]

**Suggested Solution:**  
[Explain the solution suggested by AI]

**Fix Implemented:**  
[Describe the actual code change]

**Verification:**  
[Explain how the application was retested]

This section demonstrates the iterative debugging process required by the vibe-coding challenge.

## Logging Example

Illustrative log entries:

```text
INFO - Task added successfully
INFO - Task marked as completed
WARNING - Invalid task ID entered
ERROR - Unable to read task data
INFO - Application exited
```

The exact log format depends on the logging configuration.

## Key Learning Outcomes

Through this project, the following concepts are explored:

1. Understanding how AI can assist with software development.
2. Breaking a project into smaller, manageable requirements.
3. Designing modular Python applications.
4. Working with Python packages and imports.
5. Implementing persistent JSON storage.
6. Handling runtime errors using exceptions.
7. Creating custom exceptions for application-specific errors.
8. Implementing logging for debugging and monitoring.
9. Refactoring AI-generated code.
10. Testing applications with valid and invalid inputs.

## Future Enhancements

Potential improvements include:

- Task priority levels.
- Task deadlines.
- Search and filter functionality.
- Task categories.
- Due-date reminders.
- Unit testing with `unittest`.
- SQLite database integration.
- A graphical user interface.

## GitHub Repository

**Repository URL:**  
[Add your public GitHub repository URL]

## YouTube Demonstration

**Video URL:**  
[Add your YouTube video URL]

The demonstration covers requirement analysis, AI prompting, architecture, code implementation, execution, debugging, exception handling, logging, and final testing.

## Conclusion

This project demonstrates that vibe coding is not simply copying AI-generated code.

It is an iterative development approach in which AI supports requirement analysis, implementation, debugging, refactoring, and testing.

The most important learning is that developers must understand, validate, and take responsibility for the solutions generated with AI assistance.

**Keep learning, keep building, keep evolving.**

*Evolve with Amrutha Varshini Alva*