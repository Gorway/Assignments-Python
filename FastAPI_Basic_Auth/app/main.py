# main.py
"""
Main module for the FastAPI application.
Handles routing, static files, and user interactions like registration and login.

"""

import os
from contextlib import asynccontextmanager

import uvicorn
from dotenv import load_dotenv
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse


from user_db import register_user
from fastapi import FastAPI, Depends, Request, Form
from auth import login_user, log_out, get_current_user

# Load environment variables
load_dotenv()
PORT = os.getenv("PORT")
HOST = os.getenv("HOST")

app = FastAPI()

# Set up templates and static files
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/register", response_class=HTMLResponse)
async def register_page(request: Request):
    """Render the registration page."""
    return templates.TemplateResponse("register.html", {"request": request})


@app.post("/register", response_class=HTMLResponse)
async def register_user_form(username: str = Form(...), password: str = Form(...)):
    """Handle registration form submission."""
    if register_user(username, password):
        return RedirectResponse("/login", status_code=302)
    return HTMLResponse(content="User already exists", status_code=400)


@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    """Render the login page."""
    return templates.TemplateResponse("login.html", {"request": request})


# Route to handle user login
@app.post("/login", response_class=HTMLResponse)
async def login(username: str = Form(...), password: str = Form(...)):
    """Handle login form submission."""
    return login_user(username, password)


@app.get("/logout", response_class=HTMLResponse)
async def logout():
    """Log out the current user."""
    return log_out()


@app.get("/secure", response_class=HTMLResponse)
async def secure_page(request: Request, current_user: str = Depends(get_current_user)):
    """Render the secure page for authenticated users."""
    return templates.TemplateResponse(
        "secure.html", {"request": request, "username": current_user}
    )


# Run the app if executed directly
if __name__ == "__main__":
    # Start the server with specified host and port
    uvicorn.run("main:app", reload=True, port=int(PORT), host=HOST)
