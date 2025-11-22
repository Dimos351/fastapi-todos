from fastapi import FastAPI, HTTPException, Request, Depends
from typing import List

from fastapi.responses import JSONResponse
from .schemas import Todo, TodoCreate, TodoUpdate
from .auth import get_api_key  
from .storage import TodoStorage
from .crud import update_todo



app = FastAPI()

storage = TodoStorage()



@app.get("/secure", dependencies=[Depends(get_api_key)])
def get_secure_todos():
    return {"secret": "only for API key holders"}


@app.get("/todos", response_model=List[Todo])
def get_todos():
    return storage.all()


@app.post("/todos", response_model=Todo, status_code=201)
def create_todo(data: TodoCreate):
    todo = Todo(id=0, **data.dict())
    return storage.add(todo)


@app.get("/todos/{todo_id}", response_model = Todo)
def get_todo(todo_id: int):
    todo = storage.get(todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


@app.put("/todos/{todo_id}", response_model=Todo)
def put_todo(todo_id: int, data: TodoUpdate):
    todo = storage.get(todo_id)
    if not todo:
        raise HTTPException(404, "Todo not found")

    updated = update_todo(todo, data)
    return updated


@app.delete("/todos/{todo_id}", status_code=204)
def delete_todo(todo_id: int):
    ok = storage.delete(todo_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Todo not found")


@app.exception_handler(Exception)
async def generic_exception_handler(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"detail": "Internal Server Error"})
