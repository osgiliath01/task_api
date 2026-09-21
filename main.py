from fastapi import FastAPI,Depends,HTTPException
from pydantic import BaseModel
from database import engine,SessionLocal
from sqlalchemy.orm import Session
import models


class Task(BaseModel):
    id: None
    title:str
    completed:bool=False

# FastAPI() creates the FastAPI application.
# @app.get("/") defines a GET endpoint for the root URL.
# read_root() returns a JSON response containing a message.

models.Base.metadata.create_all(bind=engine)

# helper function
def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()  

app = FastAPI()
# Root Endpoint
@app.get("/")
def read_root():
    return {"message":"hello world!"}

@app.get("/tasks")
def get_tasks(db: Session = Depends(get_db)):
    tasks = db.query(models.Task).all()
    return {"tasks":tasks}

# Read the incoming request body, validate it against Task schema from Step 2, and pass it as task.
@app.post("/tasks")
def create_tasks(task: Task, db: Session = Depends(get_db)):
    db_task = models.Task(title=task.title,completed=task.completed)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return {"message":"Successfully appended to tasks_db!"}

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int,db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404,detail="Task not found")

    if not task.completed:
        return{"message": "Task not yet completed."}
   
    db.delete(task)
    db.commit()
    return {"message": "Successfully deleted task!"}

