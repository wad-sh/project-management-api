# Project Management API

A RESTful API for managing users, projects, and tasks.  
Built with FastAPI, SQLAlchemy, and JWT authentication.

## Features

- User registration and login
- JWT-based authentication
- Secure password hashing
- User authorization
- Project CRUD operations
- Task management inside projects
- Task status updates
- Protected API endpoints

## Tech Stack

- Python
- FastAPI
- SQLAlchemy ORM
- SQLite
- Pydantic
- python-jose (JWT)
- pwdlib (Password Hashing)

## Project Structure

```
ProjectManagementAPI/
│
├── theapp/
│   ├── auth/
│   │   ├── jwt_handler.py
│   │   ├── security.py
│   │   └── dependencies.py
│   │
│   ├── database/
│   ├── models/
│   ├── schemas/
│   ├── routers/
│   ├── services/
│   └── main.py
│
├── .env.example
├── .gitignore
├── README.md
└── requirements.txt
```

## Installation

Clone the repository:

```bash
git clone <repository-url>
```

Navigate to the project directory:

```bash
cd ProjectManagementAPI
```

Create a virtual environment:

```bash
py -m venv venv
```

Activate the virtual environment:

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project root by copying `.env.example` and updating the values.

Example:

```
DATABASE_URL=sqlite:///./projdata.db
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

## Running the Project

Start the FastAPI server:

```bash
uvicorn theapp.main:app --reload
```

The API documentation will be available at:

```
http://127.0.0.1:8000/docs
```

## API Endpoints

### Authentication

| Method | Endpoint | Description |
|---|---|---|
| POST | `/users/register` | Register a new user |
| POST | `/users/login` | Login and receive JWT token |

### Projects

| Method | Endpoint | Description |
|---|---|---|
| GET | `/projects` | Get user's projects |
| POST | `/projects` | Create a project |
| PUT | `/projects/{id}` | Update a project |
| DELETE | `/projects/{id}` | Delete a project |

### Tasks

| Method | Endpoint | Description |
|---|---|---|
| GET | `/projects/{id}/tasks` | Get project tasks |
| POST | `/projects/{id}/tasks` | Create a task |
| PUT | `/tasks/{id}` | Update a task |
| DELETE | `/tasks/{id}` | Delete a task |

## Authentication

This API uses JWT Bearer tokens.

After login, include the token in requests using:

```
Authorization: Bearer <access_token>
```

Protected endpoints require a valid JWT token.

## Future Improvements

- Add Alembic database migrations
- Add automated tests
- Deploy the API
- Add refresh tokens
- Add role-based access control (RBAC)
