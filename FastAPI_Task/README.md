# FastAPI Task

This project implements a basic web application built with FastAPI, designed to manage users and tasks. The application demonstrates key FastAPI concepts including CRUD operations, validation, file handling, and asynchronous programming. It also includes basic authentication and error handling, making it a comprehensive example of a simple backend API.

## Features

- **CRUD Operations for Users and Tasks**:  
  The application provides endpoints to create, read, update, and delete users and tasks.

- **Data Stored in JSON Files**:  
  User and task data is stored in `users.json` and `tasks.json` files. The application reads and writes data asynchronously.

- **Validation**:  
  The data is validated before being added to the database. It checks if the input meets specific requirements (e.g., non-empty strings, valid email format, etc.).

- **Registration and Authentication**:  
  The application supports user registration and login. Users can register by providing a name, email, and password. They can then authenticate by providing their email and password.

- **Asynchronous Programming**:  
  All endpoints use asynchronous methods for handling requests and performing file operations, ensuring non-blocking behavior.

- **Custom Error Handling**:  
  Custom error classes are used for handling validation errors, file-related errors, and cases when resources (users or tasks) are not found.

## Endpoints

### User Management (`/users`)

- `POST /users`: Create a new user with the required fields: name, email, and password.
- `GET /users`: Retrieve a list of all users.
- `GET /users/{user_id}`: Retrieve a specific user by their ID.
- `PUT /users/{user_id}`: Update the information of a specific user.
- `DELETE /users/{user_id}`: Delete a specific user by their ID.

### Task Management (`/tasks`)

- `POST /tasks`: Create a new task with the fields: title, description (optional), and user_id (the ID of the assigned user).
- `GET /tasks`: Retrieve a list of all tasks.
- `GET /tasks/{task_id}`: Retrieve a specific task by its ID.
- `PUT /tasks/{task_id}`: Update the details of a specific task.
- `DELETE /tasks/{task_id}`: Delete a specific task by its ID.

### User Registration and Authentication

- `POST /register`: Register a new user by providing name, email, and password.
- `POST /login`: Authenticate a user by verifying their email and password.

## Installation

### Prerequisites

- Python 3.7+
- FastAPI
- Uvicorn

### Install Dependencies

To install the required dependencies, run the following command:

```bash
pip install -r requirements.txt
