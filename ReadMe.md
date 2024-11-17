# Authentication System

This is a simple authentication system built with **FastAPI** (for the backend) and **React** (for the frontend). The application allows users to sign up, log in, and access a dashboard after authentication.

## Features
- **Sign Up**: Users can create a new account by providing an email, username, and password.
- **Login**: Users can log in using their email and password.
- **JWT Authentication**: Once logged in, users receive a JWT token for authentication.
- **Dashboard**: Authenticated users are redirected to a dashboard upon successful login.

## Technologies Used
- **Backend**: 
  - **FastAPI**: Fast web framework for building the API.
  - **SQLAlchemy**: ORM for database interaction.
  - **SQLite** (or your preferred DB): Database to store user credentials.
  - **JWT**: For token-based authentication.
  
- **Frontend**:
  - **React**: For the UI components.
  - **Tailwind CSS**: For styling the frontend.

## Project Structure

### Backend (`FastAPI`)
- **`app/`**: Contains FastAPI application files.
  - `main.py`: The entry point for the FastAPI app, defining routes and logic.
  - `models.py`: SQLAlchemy models for the database.
  - `schemas.py`: Pydantic models for data validation.
  - `utils.py`: Utility functions for password hashing, JWT creation, etc.
  - `database.py`: Database connection and session management.

### Frontend (`React`)
- **`src/`**: Contains React application files.
  - `App.js`: Main React component to manage the app's layout.
  - `components/`: Reusable UI components like `Login`, `Signup`, and `Dashboard`.
  - `pages/`: React components for specific pages like `LoginPage` and `SignupPage`.
 

## Setup

### 1. Backend Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/Mohamedboudrar/FastApi_auth.git
   cd FastApi_auth

2. Get into backend directory:
    ```bash
    cd backend
2. Install required Python dependencies:

    ```bash
    pip install -r requirements.txt

3. Update DATABASE_URL in .env file 

4. Run the FastAPI app:

    ```bash
    fastapi dev main.py

### 2. Frontend Setup

1. Get into frontend directory:
    ```bash
    cd Auth
2. Install required dependencies:
    ```bash
    npm install
3. Run the frontend:
    ```bash
    npm run dev
