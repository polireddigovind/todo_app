from fastapi import APIRouter, Depends, HTTPException, status
from database import OracleDB

auth_router = APIRouter()

def authenticate_user(user_id: str):
    if user_id not in OracleDB:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid user")

@auth_router.get("/auth/")
def auth_endpoint(user_id: str = Depends(authenticate_user)):
    return {"message": "User authenticated successfully"}
