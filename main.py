from fastapi import FastAPI
from pydantic import BaseModel

class Task(BaseModel):
    id:int
    title:str
    completed:bool=False

# FastAPI() creates the FastAPI application.
# @app.get("/") defines a GET endpoint for the root URL.
# read_root() returns a JSON response containing a message.

app = FastAPI()
tasks_db = []

@app.get("/tasks")
def get_tasks():
    return {"tasks":tasks_db}

@app.post("/tasks")
def create_tasks(task: Task): # "Read the incoming request body, validate it against my Task schema from Step 2, and pass it as task."
    tasks_db.append(task)
    return {"message":"Successfully appended to tasks_db!"}

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    global tasks_db
    tasks_db = [t for t in tasks_db if t.id != task_id]
    return {"message": "Successfully deleted task!"}

@app.get("/")
def read_root():
    return {"message":"hello world!"}

