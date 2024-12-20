from typing import Dict


from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse

from utils.auth_utils import create_access_token, hash_password, verify_password
from models.schemas import User, Token

auth_router = APIRouter()

fake_db = {}  

@auth_router.post("/auth/register", response_class=JSONResponse)
async def register(user: User):
    if user.username in fake_db:
        raise HTTPException(status_code=400, detail="Username already taken")
    hashed_password = hash_password(user.password)
    fake_db[user.username] = {"email": user.email, "password": hashed_password}
    return JSONResponse({"msg": "User registered successfully"},
                        status_code=201)


@auth_router.post("/auth/login", response_model=Token)
async def login(user: User):
    stored_user = fake_db.get(user.username)
    if not stored_user or not verify_password(user.password, stored_user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}
