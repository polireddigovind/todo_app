from pydantic import BaseModel

class User(BaseModel):
    id: str

class Task(BaseModel):
    task_name: str
