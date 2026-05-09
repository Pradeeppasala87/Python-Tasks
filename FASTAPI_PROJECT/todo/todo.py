# --------------------------------------------------------------------
# IMPORT LIBRARIES
# --------------------------------------------------------------------
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# --------------------------------------------------------------------
# CREATE FASTAPI APP
# --------------------------------------------------------------------
app = FastAPI()

# --------------------------------------------------------------------
# CREATE DATA MODEL (SCHEMA)
# --------------------------------------------------------------------
class Todo(BaseModel):
    id: int
    title: str
    completed: bool = False

# --------------------------------------------------------------------
# TEMPORARY DATABASE
# --------------------------------------------------------------------
todos_lst = []

# --------------------------------------------------------------------
# CREATE TODO (POST)
# --------------------------------------------------------------------
@app.post("/todos_lst")
def create_todo(todo: Todo):
    todos_lst.append(todo)

    return {
        "msg": "Todo Created Successfully",
        "data": todo
    }

# --------------------------------------------------------------------
# READ ALL TODOS (GET)
# --------------------------------------------------------------------
@app.get("/todos_lst")
def get_todos():
    return todos_lst

# --------------------------------------------------------------------
# READ SINGLE TODO BY ID (GET)
# --------------------------------------------------------------------
@app.get("/todos_lst/{todo_id}")
def get_todo(todo_id: int):

    for todo in todos_lst:
        if todo.id == todo_id:
            return todo

    raise HTTPException(
        status_code=404,
        detail="Todo Not Found"
    )

# --------------------------------------------------------------------
# UPDATE TODO (PUT)
# --------------------------------------------------------------------
@app.put("/todos_lst/{todo_id}")
def update_todo(todo_id: int, updated_todo: Todo):

    for index, todo in enumerate(todos_lst):

        if todo.id == todo_id:

            todos_lst[index] = updated_todo

            return {
                "msg": "Todo Updated Successfully",
                "data": updated_todo
            }

    raise HTTPException(
        status_code=404,
        detail="Todo Not Found"
    )

# --------------------------------------------------------------------
# DELETE TODO BY ID (DELETE)
# --------------------------------------------------------------------
@app.delete("/todos_lst/{todo_id}")
def delete_todo(todo_id: int):

    for index, todo in enumerate(todos_lst):

        if todo.id == todo_id:

            deleted = todos_lst.pop(index)

            return {
                "msg": "Todo Deleted Successfully",
                "data": deleted
            }

    raise HTTPException(
        status_code=404,
        detail="Todo Not Found"
    )
