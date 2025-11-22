from pydantic import BaseModel, Field
from typing import Optional


class TodoBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=30, example="Buy milk")
    description: Optional[str] = Field(None, max_length=300, example="2 liters")


class TodoCreate(TodoBase):
    pass

class TodoUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    done: Optional[bool]

class Todo(TodoBase):
    id: int
    done: bool = False
