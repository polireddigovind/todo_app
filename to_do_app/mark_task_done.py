from fastapi import APIRouter
from database import OracleDB

task_mark_done_router = APIRouter()

@task_mark_done_router.put("/markTaskDone/")
def mark_task_done(user_id: str, task_id: int):
    OracleDB.execute_statement("UPDATE tasks SET status = 'Done' WHERE user_id = :1 AND task_id = :2", (user_id, task_id))
    return {"message": "Task marked as done"}
