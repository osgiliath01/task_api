# Task Management REST API (with Persistent SQLite Database)

A RESTful API built with **Python**, **FastAPI**, **SQLAlchemy 2.0**, and **Pydantic**. 

Originally built as an in-memory prototype, this upgraded version implements persistent database storage using **SQLite**, managed through modern type-safe SQLAlchemy 2.0 ORM models and FastAPI dependency injection.

---

## Key Features

- **Persistent Storage:** Integrated SQLite database (`tasks.db`) ensuring data survives server restarts.
- **Modern ORM Architecture:** Uses SQLAlchemy 2.0 declarative mapping (`Mapped` / `mapped_column`) for type-safe database queries.
- **Dependency Injection:** Safe database session management using FastAPI's `Depends` and generator pattern (`yield db`) to ensure auto-closing connections.
- **Strict Data Validation:** Pydantic schemas validate incoming JSON payloads and return automatic HTTP `422` error responses for malformed data.
- **Error Handling:** Explicit HTTP `404 Not Found` exception handling for missing resources.
- **Interactive API Docs:** Built-in Swagger UI for browser-based endpoint testing.

---

## Tech Stack

- **Framework:** FastAPI
- **Database:** SQLite
- **ORM:** SQLAlchemy 2.0 (Modern `Mapped` Style)
- **Data Schemas:** Pydantic
- **ASGI Server:** Uvicorn
- **Language:** Python 3.x
- **Version Control:** Git & GitHub

---

## API Endpoints Summary

| Method | Endpoint | Description | Status Code |
| :--- | :--- | :--- | :--- |
| `GET` | `/` | Health check / Welcome endpoint | `200 OK` |
| `GET` | `/tasks` | Fetch all tasks from SQLite database | `200 OK` |
| `POST` | `/tasks` | Save a new task to SQLite database | `200 OK` / `201 Created` |
| `DELETE` | `/tasks/{task_id}` | Delete a task from SQLite database by ID | `200 OK` / `404 Not Found` |

---

## Architecture Overview

```text
HTTP Request  --->  FastAPI Router  --->  Pydantic Validation Schema
                                                |
SQLite File  <---  SQLAlchemy 2.0  <---  db: Session (Depends)
 (`tasks.db`)          ORM Model
```

---

## Local Setup & Installation

### 1. Clone Repository
```bash
git clone [https://github.com/YOUR_USERNAME/task_api.git](https://github.com/YOUR_USERNAME/task_api.git)
cd task_api
```

### 2. Set Up Virtual Environment

**Windows:**
```cmd
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Server
```bash
uvicorn main:app --reload
```

---

## Testing via Swagger UI

Once the server is running, navigate to:
```text
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
```
Use the interactive UI to test `GET`, `POST`, and `DELETE` requests directly against your local `tasks.db` database.