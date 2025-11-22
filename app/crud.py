from .schemas import Todo, TodoUpdate

def update_todo(todo: Todo, data: TodoUpdate) -> Todo:
    if data.title is not None:
        todo.title = data.title
    if data.description is not None:
        todo.description = data.description
    if data.done is not None:
        todo.done = data.done
    return todo


