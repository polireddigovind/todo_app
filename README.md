# todo_app
todo_app backend Application connecting to oracle database

# Introduction
creating backend application for the todo_app for users having user_ids and their tasks to complete.Authentication is also include for user safety.

# Installation

To set up the project locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/your_username/to_do_app.git
    ```
2. Navigate to the project directory:
    ```bash
    cd to_do_app
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
# Usage

1)To run the FastAPI server, execute the following command:
```bash
uvicorn todo_app:app --reload
```
2)This will start the FastAPI server on http://localhost:8000 by default.

3)Open your web browser and go to http://localhost:8000/docs to access the Swagger UI for testing the API endpoints.

4)you can also use tools like [Postman](https://www.postman.com/)

## Api Endpoints

**POST /CreateUser/{user_id}:**

Description: create a new user with the user_id
Parameters:user_id
* Authentication Required


**GET /Get Tasks{user_id,Task_id}:**

Description: retrieve all the taks for a given user_id.
Parameters:user_id,Task_id
* Authentication not Required

**POST /CreateTask{User_id}:**

Description: Create a new task for a user.
Payload:
Parameters:user_id
* Authentication Required


**DELETE /Delete tasks/{user_id,task_id}:**

Description: Delete a task by user_id and task_id.
Parameters:user_id ,task_id
* Authentication Required


**PUT /Update_tasks/{user_id,task_id}:**

Description: Update a task by user_id and task_id.
Parameters:user_id,task_id
task: Update description of the task.
* Authentication Required

**PUT /markTaskDone/{user_id,task_id}:**

Description: Update a task by user_id and task_id.
Parameters:user_id,task_id
task: Update status of the task.
* Authentication Required

# Structure Of The Project
todo_app.py: FastAPI application file containing all  API routes.

models.py: Defines oracle database models/tables.

database.py: Manages database connection and models using Oracle database.

Create_task.py: Creates new task for a user by taking user_id

Create_user.py: Creates a new user

delete_task.py:Deletes the tasks for a particular user by taking user_is and Task_id

Get_task.py:retrives all the tasks for a particular user by using user_id

mark_task_done.py:Update the task which is completed by the user

secure_Authentication.py:Security for the user

requirements.txt: List of Python dependencies required for the project.


# Contributing
Contributions to this project are welcome! To contribute:

1)Fork the repository

2)Create a new branch (git checkout -b feature/your-feature).

3)Make your changes and commit them (git commit -am 'Add new feature').

4)Push to the branch (git push origin feature/your-feature).

5)Create a new pull request.
