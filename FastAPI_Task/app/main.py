import os
import json
import model
import asyncio
import uvicorn
import validators
from typing import List
import read_write_utilitis
from fastapi import FastAPI
from dotenv import load_dotenv
from contextlib import asynccontextmanager
from errors import ValidationError, FileError, NotFoundError

load_dotenv()
USERS_FILE = os.getenv("USERS_FILE", "users.json")
TASKS_FILE = os.getenv("TASKS_FILE", "tasks.json")
HOST = os.getenv("HOST", "127.0.0.1")
PORT = os.getenv("PORT", 6001)

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        await read_write_utilitis.init_files()
        yield
    except FileError:
        raise FileError(detail="Error during file initialization")

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def read_root():
    return {"message": f"Server is running at {HOST}:{PORT}"}

@app.post("/register", status_code=200)
async def registration(user: model.User):
    users = await read_write_utilitis.read_file(USERS_FILE)
    validators.validate_user(user, users=users)
    user.id = max((u["id"] for u in users), default=0) + 1
    users.append(user.model_dump())
    await read_write_utilitis.write_file(USERS_FILE, users)
    return {"id": user.id,  "name": user.name, "email": user.email}

@app.post("/login")
async def login(email: str, password: str):
    users = await read_write_utilitis.read_file(USERS_FILE)
    user = next((u for u in users if u["email"] == email and u ["password"] == password), None)
    if not user:
        raise ValidationError("Wrong email or password.")
    return {"message": "Login Successfull"}

@app.post("/users")
async def create_users(user: model.User):
    return await registration(user)

@app.get("/users", response_model=List[model.User])
async def get_users():
    return await read_write_utilitis.read_file(USERS_FILE)

@app.get("users/{user_id}", response_model=model.User)
async def get_user(user_id: int):
    users = await read_write_utilitis.read_file(USERS_FILE)
    user = next((u for u in users if u["id"] == user_id), None)
    if not user:
        raise NotFoundError("User not found.")
    return user

@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    users = await read_write_utilitis.read_file(USERS_FILE)
    user_to_delete = next((u for u in users if u["id"] == user_id), None)
    if not user_to_delete:
        raise NotFoundError("User not found")
    users.remove(user_to_delete)
    await read_write_utilitis.write_file(USERS_FILE, users)
    
    return {"message": "User with ID {user_id} has been deleted successfully"}

@app.put("/users/{user_id}", response_model=model.User)
async def update_user(user_id: int, user: model.User):
    users = await read_write_utilitis.read_file(USERS_FILE)
    user_to_update = next((u for u in users if u["id"] == user_id), None)
    
    if not user_to_update:
        raise NotFoundError(detail=f"User with ID {user_id} not found.")
    user_to_update.update(user.model_dump())
    await read_write_utilitis.write_file(USERS_FILE, users)

    return user_to_update

@app.post("/tasks")
async def creat_tasks(task: model.Task):
    users, tasks =  await asyncio.gather(
        read_write_utilitis.read_file(USERS_FILE),
        read_write_utilitis.read_file(TASKS_FILE)
    )
    validators.validate_task(task, users)
    task.id = max((t["id"] for t in tasks), default=0) +1
    tasks.append(task.model_dump())
    await read_write_utilitis.write_file(TASKS_FILE, tasks)
    
    return task

@app.get("/tasks",response_model=List[model.Task])
async def get_tasks():
    return await read_write_utilitis.read_file(TASKS_FILE)

@app.get("/tasks/{task_id}", response_model=model.Task)
async def get_task(task_id: int):
    tasks = read_write_utilitis.read_file(TASKS_FILE)
    task = next((t for t in tasks if t["id"] == task_id), None)
    if not task:
        raise NotFoundError("Taks not found")
    
    return task

@app.put("/tasks/{task_id}", response_model=model.Task)
async def update_task(task_id: int, task: model.Task):
    tasks = await read_write_utilitis.read_file(TASKS_FILE)
    task_to_update = next((t for t in tasks if t["id"] == task_id), None)
    
    if not task_to_update:
        raise NotFoundError(detail=f"Task with ID {task_id} not found.")
    task_to_update["title"] = task.title
    task_to_update["description"] = task.description if task.description else task_to_update["description"]
    task_to_update["user_id"] = task.user_id if task.user_id else task_to_update["user_id"]
    
    await read_write_utilitis.write_file(TASKS_FILE, tasks)

    return task_to_update

@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    tasks = await read_write_utilitis.read_file(TASKS_FILE)
    task_to_delete = next((t for t in tasks if t["id"] == task_id), None)

    if not task_to_delete:
        raise NotFoundError(f"Task {task_id} not found.")
    tasks.remove(task_to_delete)
    await read_write_utilitis.write_file(TASKS_FILE, tasks)

    return {"message": "Task with ID {task_id} successfully deeted."}

if __name__ == "__main__":
    uvicorn.run("main:app", host=HOST, port=int(PORT), reload=True)