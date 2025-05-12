# backend/routes/user_routes.py

from fastapi import APIRouter
from pydantic import BaseModel, EmailStr
from db import mongo_db
from datetime import datetime

router = APIRouter(prefix="/user", tags=["User"])
users_collection = mongo_db["users"]

class UserCreate(BaseModel):
    user_id: str
    name: str
    email: EmailStr

@router.post("/create")
def create_user(user: UserCreate):
    if existing := users_collection.find_one({"user_id": user.user_id}):
        return {"status": "exists", "message": "User already exists."}

    users_collection.insert_one({
        "user_id": user.user_id,
        "name": user.name,
        "email": user.email,
        "created_at": datetime.now()
    })

    return {"status": "success", "message": "User created."}
