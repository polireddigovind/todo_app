from fastapi import APIRouter
from database import OracleDB

task_delete_router = APIRouter()

@task_delete_router.delete("/deleteTask/")
def delete_task(user_id: str, task_id: int):
    # Example: Delete task from the database
    OracleDB.execute_statement("DELETE FROM tasks WHERE user_id = :1 AND task_id = :2", (user_id, task_id))
    return {"message": "Task deleted successfully"}
