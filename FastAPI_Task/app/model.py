# User model: Represents user information such as id, name, email, and password.
# Task model: Represents a task with details like id, title, description, and the user_id that links it to a specific user.
# These models are designed for use with FastAPI, leveraging Pydantic for data validation and serialization.

from pydantic import BaseModel
from typing import List, Optional

# Represents a user in the systems
class User(BaseModel):

    id: Optional[int] = None
    name: str
    email: str
    password: str

#Represents a task assigned to a user.
class Task(BaseModel):
 
    id: Optional[int] = None
    title: str
    description: Optional[str] = None
    user_id: int