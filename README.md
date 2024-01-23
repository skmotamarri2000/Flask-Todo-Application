Flask ToDo App

This Flask application implements a simple ToDo list, allowing users to add, update, and delete tasks. It utilizes a SQLite database to persist tasks. The web interface is built with HTML and uses the Semantic UI framework for styling.

Features:

Add Task: Users can add new tasks by entering the task title in the input field and clicking the "Add" button.
Update Task: Tasks can be marked as complete or incomplete by clicking the "Update" button next to each task.
Delete Task: Tasks can be deleted by clicking the "Delete" button next to each task.
Task List: The main page displays a list of all tasks, showing their ID, title, and completion status.
Implementation:

The backend is developed using Flask, and SQLAlchemy is used to interact with the SQLite database.
The frontend is designed with HTML and styled using the Semantic UI framework.
Routes are defined for adding, updating, and deleting tasks, along with the main route to display the task list.
The application initializes the database and creates the necessary table on startup.
Usage:

Run the Flask application.
Open the web page and start managing your ToDo list.
Add, update, or delete tasks as needed.
This application provides a basic foundation for a ToDo list with a clean and user-friendly interface. Users can easily interact with their tasks and keep track of their completion status.
