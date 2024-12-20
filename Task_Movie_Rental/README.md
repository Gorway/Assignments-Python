# Movie Rental API

This is a FastAPI-based movie rental system with JWT authentication, movie management, and rental functionality. It supports user registration, login, movie filtering, adding movies, and renting movies, while also utilizing middleware for logging requests and responses.

## Features
- User registration and login with JWT authentication.
- Add and filter movies by genre, rating, and title.
- Rent movies and view rental history.
- Middleware for logging all incoming requests and responses.

## Requirements
- Python 3.7+
- FastaAPI
- Jose
- Passlib
- Pydantic
- Python-dotenv
- Uvicorn


## Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Set up the environment variables:
    Create a `.env` file in the project root with the following content:
    ```ini
    HOST=0.0.0.0
    PORT=8000
    JWT_SECRET_KEY=your_jwt_secret_key
    ALGORITHM= #for example HS256
    ACCESS_TOKEN_EXPIRE_MINUTES=0
    ```
## Usage
To start the FastAPI application:
```bash
uvicorn main:app --reload
