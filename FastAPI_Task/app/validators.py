from errors import ValidationError, NotFoundError, FileError
from model import User, Task
from typing import List, Optional

# Validates the provided User model object.
# Ensures the name is a non-empty string, the email is valid, and the password is at least 6 characters.
def validate_user(user: User, users: Optional[List[User]] = None):
    if any(existing_user["email"] == user.email for existing_user in users):
        raise ValidationError(detail="A user with this email already exists.")
    if not user.name or not isinstance(user.name, str):
        raise ValidationError("The name field must be a non-empty string..")
    if "@" not in user.email or "." not in user.email.split("@")[-1]:
        raise ValidationError("Uncorrect email.")
    if len(user.password) < 6:
        raise ValidationError("The password must be at least 6 characters long")

# Validates the provided Task model object.
# Ensures the title is a non-empty string, the description is a string (if present),
# and that the user_id corresponds to an existing user in the provided list.
def validate_task(task: Task, users: List[User]):
    if not task.title or not isinstance(task.title, str):
        raise ValidationError("The title field must be a non-empty string.")
    if task.description and not isinstance(task.description, str):
        raise ValidationError("The description field must be string")
    if not any(user["id"] == task.user_id for user in users):
        raise ValidationError("The user with the specified user_id does not exist")
