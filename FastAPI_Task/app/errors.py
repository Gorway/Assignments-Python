# This module defines custom error classes for handling different types of errors in the FastAPI application.

# 1. ValidationError:
#     - A custom exception for handling validation errors.
#     - This exception is raised when invalid data is provided in requests (e.g., incorrect input format or missing required fields).

# 2. FileError:
#     - A custom exception for handling file-related errors.
#     - This exception is raised when there are issues with file handling, such as file not found, or file corruption.

# 3. NotFoundError:
#     - A custom exception for handling "not found" errors.
#     - This exception is raised when a resource (e.g., a user or task) is not found in the database or file.

from fastapi import HTTPException

class ValidationError(HTTPException):
    def __init__(self, detail: str):
        super().__init__(status_code=400, detail=detail)

class FileError(HTTPException):
    def __init__(self, detail: str):
        super().__init__(status_code=500, detail=detail)

class NotFoundError(HTTPException):
    def __init__(self, detail: str):
        super().__init__(status_code=404, detail=detail)