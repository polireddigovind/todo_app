from fastapi import APIRouter
from models import Task
from database import OracleDB

task_update_router = APIRouter()

@task_update_router.put("/updateTask/")
def update_task(user_id: str, task_id: int, new_task: Task):
    # Example: Update task in the database
    OracleDB.execute_statement("UPDATE tasks SET task_name = :1 WHERE user_id = :2 AND task_id = :3", (new_task.task_name, user_id, task_id))
    return {"message": "Task updated successfully"}
