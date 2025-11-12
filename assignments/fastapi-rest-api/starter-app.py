from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()


class TodoIn(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False


class Todo(TodoIn):
    id: int


# In-memory storage
_todos: List[Todo] = []
_next_id = 1


@app.post('/todos', response_model=Todo, status_code=201)
def create_todo(item: TodoIn):
    global _next_id
    todo = Todo(id=_next_id, **item.dict())
    _todos.append(todo)
    _next_id += 1
    return todo


@app.get('/todos', response_model=List[Todo])
def list_todos():
    return _todos


@app.get('/todos/{todo_id}', response_model=Todo)
def get_todo(todo_id: int):
    for t in _todos:
        if t.id == todo_id:
            return t
    raise HTTPException(status_code=404, detail='Todo not found')


@app.put('/todos/{todo_id}', response_model=Todo)
def update_todo(todo_id: int, item: TodoIn):
    for idx, t in enumerate(_todos):
        if t.id == todo_id:
            updated = Todo(id=todo_id, **item.dict())
            _todos[idx] = updated
            return updated
    raise HTTPException(status_code=404, detail='Todo not found')


@app.delete('/todos/{todo_id}', status_code=204)
def delete_todo(todo_id: int):
    for idx, t in enumerate(_todos):
        if t.id == todo_id:
            _todos.pop(idx)
            return
    raise HTTPException(status_code=404, detail='Todo not found')


if __name__ == '__main__':
    import uvicorn

    uvicorn.run('starter-app:app', host='127.0.0.1', port=8000, reload=True)
