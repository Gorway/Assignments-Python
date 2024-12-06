# user_db.py
"""
Module for handling user registration and database operations.
Includes reading and writing user data securely.
"""

import os
import json

from dotenv import load_dotenv
from fastapi import HTTPException
from passlib.hash import sha256_crypt


# Load environment variables
load_dotenv()
USERS_FILE = os.getenv("USERS_FILE")


def _read_users() -> dict:
    """Read and return user data from the JSON file."""
    if not os.path.exists("users.json"):
        return {}
    try:
        with open("users.json", mode="r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        raise HTTPException(
            status_code=500,
            detail=f"The user data file '{USERS_FILE}' is corrupted and cannot be parsed.",
        )
    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=f"An unexpected error occurred while reading the user file: {str(e)}",
        )


def _write_users(users: list[dict]) -> None:
    """Write updated user data to the JSON file."""
    try:
        with open(USERS_FILE, mode="w", encoding="utf-8") as file:
            file.write(json.dumps(users, indent=2))
    except FileNotFoundError:
        raise HTTPException(
            status_code=500,
            detail=f"The user data file '{USERS_FILE}' could not be found or created.",
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"An unexpected error occurred while writing the user file: {str(e)}",
        )


def register_user(username: str, password: str) -> bool:
    """Register a new user if the username does not already exist."""
    users = _read_users()
    if any(user["username"] == username for user in users):
        return False
    hashed_password = sha256_crypt.hash(password)
    users.append({"username": username, "password": hashed_password})
    _write_users(users)
    return True


def verify_users(username, password) -> bool:
    """Verify a user's credentials against the database."""
    users = _read_users()
    for user in users:
        if user["username"] == username:
            return sha256_crypt.verify(password, user["password"])
    return False
