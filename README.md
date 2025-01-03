# Task Tracker CLI

Project URL : https://roadmap.sh/projects/task-tracker
The Task Tracker CLI is a simple command-line tool to track and manage tasks. It supports creating, updating, deleting tasks, and organizing them by status (e.g., `todo`, `in-progress`, `done`). This tool helps you practice programming skills such as handling user inputs, managing JSON files, and building a CLI application.

## Features
- Add tasks with unique identifiers and descriptions.
- Update or delete existing tasks.
- Mark tasks as `in-progress` or `done`.
- List tasks based on their status (`todo`, `in-progress`, `done`).
- Persist tasks in a JSON file for reuse.

## Requirements
- Python 3.7+

No external libraries or frameworks are used in this project.

## Project Structure
```
.
├── main.py                # Entry point for the application
├── task_manager.py        # Core logic for managing tasks
├── file_handler.py        # Handles interactions with the JSON file
├── utils.py               # Utility functions for parsing arguments and validations
├── tasks.json             # JSON file to store task data (auto-created if not present)
├── tests/                 # Unit tests for the project
│   ├── test_task_manager.py
│   ├── test_file_handler.py
│   └── test_utils.py
└── README.md              # Documentation (this file)
```

## Installation
1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd task-tracker
    ```
2. Ensure you have Python 3.7+ installed.

## Usage
Run the CLI using the `main.py` file:

### Adding a New Task
```bash
python main.py add "Buy groceries"
```
**Output:** Task added successfully (ID: 1)

### Updating a Task
```bash
python main.py update 1 "Buy groceries and cook dinner"
```

### Deleting a Task
```bash
python main.py delete 1
```

### Marking a Task
Mark a task as in-progress or done:
```bash
python main.py mark-in-progress 1
python main.py mark-done 1
```

### Listing Tasks
List all tasks:
```bash
python main.py list
```
List tasks by status:
```bash
python main.py list todo
python main.py list in-progress
python main.py list done
```

## Task Properties
Each task is stored with the following properties:
- **id**: A unique identifier for the task.
- **description**: A short description of the task.
- **status**: The status of the task (`todo`, `in-progress`, `done`).
- **createdAt**: The date and time when the task was created.
- **updatedAt**: The date and time when the task was last updated.

## Testing
Run the unit tests to verify functionality:
```bash
python -m unittest discover -s tests
```

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a feature branch.
3. Commit your changes and push them.
4. Submit a pull request.

## License
This project is open sourced.

---
