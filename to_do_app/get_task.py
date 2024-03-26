from fastapi import APIRouter
from database import OracleDB
from models import User, Task


task_get_router = APIRouter()

@task_get_router.get("/getTask/")
def get_tasks(user_id: str, task_id: int = None):
    tasks = OracleDB.execute_query("SELECT task_id, task_name FROM tasks WHERE user_id = :1", (user_id,))
    if task_id:
        for task in tasks:
            if task[0] == task_id:
                return {"task_id": task[0], "task_name": task[1]}
        return {"message": "Task not found"}
    else:
        return tasks
