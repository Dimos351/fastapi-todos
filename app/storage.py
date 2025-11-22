from typing import List
from .schemas import Todo

class TodoStorage:
    def __init__(self):
        self.todos: List[Todo] = []
        self.next_id: int = 1

    def all(self) -> List[Todo]:
        return self.todos

    def add(self, todo: Todo) -> Todo:
        todo.id = self.next_id
        self.next_id += 1
        self.todos.append(todo)
        return todo

    def get(self, todo_id: int) -> Todo | None:
        for item in self.todos:
            if item.id == todo_id:
                return item
        return None

    def delete(self, todo_id: int) -> bool:
        for idx, item in enumerate(self.todos):
            if item.id == todo_id:
                self.todos.pop(idx)
                return True
        return False
