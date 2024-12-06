# FastAPI Authentication System

## **Overview**

This project is a simple yet functional authentication system built using FastAPI. It provides the following functionalities:  
- User registration and login with hashed password storage.
- Logout functionality with session management via cookies.
- Access to a secure page only for authenticated users.
- Logging of user events (login/logout) into a file.

The application stores user data in a JSON file and uses Passlib for password hashing. It's designed to be lightweight and easy to extend.

---

## **Features**

1. **User Registration**  
   Users can register with a unique username and password. Passwords are stored securely using SHA-256 hashing.

2. **User Login**  
   Users can log in with their credentials. Successful login creates a session managed with cookies.

3. **Secure Page**  
   Access to `/secure` is restricted to logged-in users. Non-authenticated users are redirected to the login page.

4. **Logout**  
   Users can log out, which clears their session cookie.

5. **Event Logging**  
   User actions (login/logout) are recorded in a JSON log file for auditing purposes.

---

## **Project Structure**

- `main.py`:  
  The main entry point of the application. It sets up FastAPI routes for registration, login, logout, and accessing the secure page.

- `user_db.py`:  
  Contains functions for handling user data:
  - Reading and writing users to a JSON file.
  - Registering new users with hashed passwords.
  - Verifying user credentials during login.

- `auth.py`:  
  Manages authentication-related functionalities:
  - Login and logout mechanisms.
  - Fetching the current logged-in user from session cookies.
  - Logging user events like login and logout.

- `templates/`:  
  A folder containing HTML templates for rendering web pages:
  - `register.html` - Registration form.
  - `login.html` - Login form.
  - `secure.html` - Secure page for logged-in users.
---

## **Setup Instructions**

### **Prerequisites**
- Python 3.8 or later installed.
- Recommended: A virtual environment to isolate dependencies.