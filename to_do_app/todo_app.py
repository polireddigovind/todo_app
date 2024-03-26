from fastapi import FastAPI
import uvicorn
from create_user import user_router
from get_task import task_get_router
from create_task import task_create_router
from delete_task import task_delete_router
from update_task import task_update_router
from mark_task_done import task_mark_done_router
from secure_Authentication import auth_router
from database import OracleDB

app = FastAPI()

# Initialize Oracle database connection
DB_USERNAME = "your_username"
DB_PASSWORD = "your_password"
DB_DSN = "your_dsn"

db = OracleDB(username=DB_USERNAME, password=DB_PASSWORD, dsn=DB_DSN)
db.connect()

app.include_router(user_router)
app.include_router(task_get_router)
app.include_router(task_create_router)
app.include_router(task_delete_router)
app.include_router(task_update_router)
app.include_router(task_mark_done_router)
app.include_router(auth_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
