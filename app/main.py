from fastapi import FastAPI, HTTPException, Request, Depends
from fastapi.responses import JSONResponse
from app.schemas import Todo, TodoCreate 
from app.auth import get_api_key  
from typing import List


app = FastAPI()

todos: List[Todo] = []
next_id = 1


@app.get("/secure", dependencies=[Depends(get_api_key)])
def get_secure_todos():
    return {"secret": "only for API key holders"}


@app.get("/todos", response_model=List[Todo])
def get_todos():
    return todos


@app.post("/todos", response_model=Todo, status_code=201)
def create_todo(item: TodoCreate):
    global next_id
    todo = Todo(id=next_id, title=item.title, description=item.description, dome=False)
    next_id += 1
    todos.append(todo)
    return todo


@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    for i in todos:
        if i.id == todo_id:
            return i
    raise HTTPException(status_code=404, detail="Todo not found")


@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, item: TodoCreate):
    for index, todo_task in enumerate(todos):
        if todo_task.id == todo_id:
            update_todo = Todo(
                id=next_id, title=item.title, description=item.description, dome=False
            )
            todos[index] = update_todo
            return update_todo
    raise HTTPException(status_code=404, detail="Todo not found")


@app.delete("/todos/{todo_id}", status_code=204)
def delete_todo(todo_id: int):
    for index, todo_task in enumerate(todos):
        if todo_task.id == todo_id:
            todos.pop(index)
            return
    raise HTTPException(status_code=404, detail="Todo not found")


@app.exception_handler(Exception)
async def generic_exception_handler(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"detail": "Internal Server Error"})
