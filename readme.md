# Task Management REST API

A lightweight, asynchronous RESTful API built with **Python**, **FastAPI**, and **Pydantic**. This project demonstrates basic backend architecture, data validation, and CRUD operations using in-memory storage and auto-generated OpenAPI (Swagger) documentation.

---

## Features

- **Data Validation:** Uses Pydantic models to enforce strict schema types and auto-reject malformed requests (HTTP 422).
- **CRUD Operations:** Implements `GET`, `POST`, and `DELETE` endpoints for task items.
- **Interactive API Documentation:** Built-in Swagger UI for testing routes directly in the browser.
- **Virtual Environment Management:** Fully isolated dependencies managed via `pip` and `requirements.txt`.

---

## Tech Stack

- **Language:** Python 3.x
- **Framework:** FastAPI
- **Data Validation:** Pydantic
- **ASGI Server:** Uvicorn
- **Version Control:** Git & GitHub

---

## API Endpoints Summary

| Method | Endpoint | Description | Status Code |
| :--- | :--- | :--- | :--- |
| `GET` | `/` | Health check / Root greeting | `200 OK` |
| `GET` | `/tasks` | Retrieve all tasks from storage | `200 OK` |
| `POST` | `/tasks` | Create and store a new task | `200 OK` |
| `DELETE` | `/tasks/{task_id}` | Remove a task by its integer ID | `200 OK` |

---

## Setup & Local Installation

### 1. Clone the Repository
```bash
git clone [https://github.com/YOUR_USERNAME/task_api.git](https://github.com/YOUR_USERNAME/task_api.git)
cd task_api
```

### 2. Set Up Virtual Environment

**On Windows:**
```cmd
python -m venv venv
venv\Scripts\activate
```

**On macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Server
```bash
uvicorn main:app --reload
```

---

## How to Test the API

Once the server is running, open your web browser and navigate to:

```text
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
```

This will load the interactive **Swagger UI** documentation where you can execute requests directly against your local server.