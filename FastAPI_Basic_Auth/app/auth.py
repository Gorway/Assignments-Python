# auth.py
"""
Authentication module for handling user login, logout, and session management.
Logs events and manages cookies for user sessions.
"""
import os
import json
from zoneinfo import ZoneInfo
from datetime import datetime

from dotenv import load_dotenv
from fastapi.responses import RedirectResponse
from fastapi import Cookie, HTTPException, Form

from user_db import verify_users

# Load environment variables
load_dotenv()
LOG_FILE = os.getenv("LOG_FILE")
SESSION_COOKIE = os.getenv("SESSION_COOKIE")


def login_user(username: str = Form(...), password: str = Form(...)):
    """Log in a user by verifying credentials and setting a session cookie."""
    if verify_users(username, password):
        log_event("login", username)
        response = RedirectResponse("/secure", status_code=302)
        response.set_cookie(key=SESSION_COOKIE, value=username, httponly=True)
        return response
    raise HTTPException(status_code=401, detail="Wrong username or password.")


def log_out():
    """Log out the current user by clearing the session cookie."""
    try:
        current_user = get_current_user()
        log_event("logout", current_user)
        response = RedirectResponse("/login", status_code=302)
        response.delete_cookie(SESSION_COOKIE)
        return response
    except HTTPException:
        raise HTTPException(status_code=500, detail="Redirection error.")


def get_current_user(session_user: str = Cookie(None)):
    """Retrieve the current user from the session cookie."""
    if not session_user:
        raise HTTPException(status_code=401, detail="Not authenticated")
    return session_user


def log_event(event, username):
    """Log user activity to the log file."""
    try:
        with open(LOG_FILE, mode="r", encoding="utf-8") as file:
            logs = json.load(file)
    except FileNotFoundError:
        logs = []
    except json.JSONDecodeError:
        logs = []
    logs.append(
        {
            "event": event,
            "username": str(username),
            "timestamp": datetime.now(ZoneInfo("UTC")).isoformat(),
        }
    )
    with open(LOG_FILE, mode="w", encoding="utf-8") as file:
        json.dump(logs, file, indent=4)
