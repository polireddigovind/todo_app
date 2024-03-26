from fastapi import APIRouter
from database import OracleDB


user_router = APIRouter()

@user_router.post("/createUser/")
def create_user(user_id: str):
    OracleDB.execute_statement("INSERT INTO tasks (id) VALUES (:1)", (user_id,))
    return {"message": "User created successfully"}
