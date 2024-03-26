# todo_app
todo_app backend connecting to the oracle database

# Project Name

Terabh Intelligence - Personalized AI Assistant Backend

## Introduction

Terabh Intelligence is dedicated to crafting a powerful and personalized AI assistant. This project focuses on building the backend for the AI assistant, with seamless integration with various services such as Spotify, Gmail, and Calendar. The backend is developed using Python and FastAPI.

## Installation

To set up the project locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/your_username/terabh-assistant-backend.git
    ```
2. Navigate to the project directory:
    ```bash
    cd terabh-assistant-backend
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run the FastAPI server, execute the following command:
```bash
uvicorn main:app --reload


API Endpoints
Create User
Creates a new user.

URL: /createUser/
Method: POST
Request Body:
{
  "id": "string"
}
Response:
{
  "message": "User created successfully"
}
Get Tasks
Retrieves tasks for a user.

URL: /getTask/
Method: GET
Query Parameters:
user_id (required): User ID
task_id (optional): Task ID
Response:
{
  "task_id": 1,
  "task_name": "Task 1"
}
Create Task
Creates a new task and associates it with the user.

URL: /createTask/
Method: POST
Request Body:
json
Copy code
{
  "task_name": "string"
}
Response:
json
Copy code
{
  "message": "Task created successfully"
}
Delete Task
Deletes a task for the specified user ID and task ID.

URL: /deleteTask/
Method: DELETE
Query Parameters:
user_id (required): User ID
task_id (required): Task ID
Response:
json
Copy code
{
  "message": "Task deleted successfully"
}
Update Task
Updates a task for the specified user ID and task ID.

URL: /updateTask/
Method: PUT
Request Body:
json
Copy code
{
  "task_name": "string"
}
Response:
json
Copy code
{
  "message": "Task updated successfully"
}
Mark Task Done
Marks a task as done for the specified user ID and task ID.

URL: /markTaskDone/
Method: PUT
Query Parameters:
user_id (required): User ID
task_id (required): Task ID
Response:
json
Copy code
{
  "message": "Task marked as done"
}
