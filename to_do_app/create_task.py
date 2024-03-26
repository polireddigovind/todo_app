from fastapi import APIRouter
from models import Task
from database import OracleDB

task_create_router = APIRouter()

@task_create_router.post("/createTask/")
def create_task(user_id: str, task: Task):
    OracleDB.execute_statement("INSERT INTO tasks (user_id, task_name) VALUES (:1, :2)", (user_id, task.task_name))
    return {"message": "Task created successfully"}
