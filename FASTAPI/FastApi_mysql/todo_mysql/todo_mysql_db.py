# ============================================================
# 📝 FastAPI TODO App (CRUD) using MySQL
# ============================================================

from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, ConfigDict
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker, Session

# ============================================================
# 🚀 FastAPI App
# ============================================================

app = FastAPI(
    title="FastAPI TODO App",
    description="CRUD Operations using FastAPI + MySQL",
    version="1.0"
)

# ============================================================
# 🗄️ Database Configuration
# ============================================================

DATABASE_URL = "mysql+pymysql://root:1234@localhost:3306/todo_db"

# ============================================================
# 🔌 Create Database Engine
# ============================================================

engine = create_engine(
    DATABASE_URL,
    echo=True
)

# ============================================================
# 🧩 Session Factory
# ============================================================

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# ============================================================
# 🏗️ Base Class
# ============================================================

Base = declarative_base()

# ============================================================
# 📝 Database Model
# ============================================================

class TodoDB(Base):

    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    completed = Column(Boolean, default=False)

# ============================================================
# 🛠️ Create Tables
# ============================================================

Base.metadata.create_all(bind=engine)

# ============================================================
# 📥 Pydantic Models
# ============================================================

# Create TODO Model
class TodoCreate(BaseModel):

    title: str
    completed: bool = False

# Response Model
class TodoResponse(BaseModel):

    id: int
    title: str
    completed: bool

    model_config = ConfigDict(from_attributes=True)

# ============================================================
# 🔄 Database Dependency
# ============================================================

def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()

# ============================================================
# 🏠 Home Route
# ============================================================

@app.get("/")
def home():

    return {
        "message": "🚀 FastAPI + MySQL TODO App"
    }

# ============================================================
# ➕ Create TODO
# ============================================================

@app.post("/todos/", response_model=TodoResponse)
def create_todo(
    todo: TodoCreate,
    db: Session = Depends(get_db)
):

    new_todo = TodoDB(
        title=todo.title,
        completed=todo.completed
    )

    db.add(new_todo)

    db.commit()

    db.refresh(new_todo)

    return new_todo

# ============================================================
# 📋 Get All TODOs
# ============================================================

@app.get("/todos/", response_model=list[TodoResponse])
def get_all_todos(
    db: Session = Depends(get_db)
):

    todos = db.query(TodoDB).all()

    return todos

# ============================================================
# 🔍 Get Single TODO
# ============================================================

@app.get("/todos/{todo_id}", response_model=TodoResponse)
def get_todo(
    todo_id: int,
    db: Session = Depends(get_db)
):

    todo = (
        db.query(TodoDB)
        .filter(TodoDB.id == todo_id)
        .first()
    )

    if not todo:

        raise HTTPException(
            status_code=404,
            detail="TODO not found"
        )

    return todo

# ============================================================
# ✏️ Update TODO
# ============================================================

@app.put("/todos/{todo_id}", response_model=TodoResponse)
def update_todo(
    todo_id: int,
    updated_todo: TodoCreate,
    db: Session = Depends(get_db)
):

    todo = (
        db.query(TodoDB)
        .filter(TodoDB.id == todo_id)
        .first()
    )

    if not todo:

        raise HTTPException(
            status_code=404,
            detail="TODO not found"
        )

    todo.title = updated_todo.title
    todo.completed = updated_todo.completed

    db.commit()

    db.refresh(todo)

    return todo

# ============================================================
# ❌ Delete TODO
# ============================================================

@app.delete("/todos/{todo_id}")
def delete_todo(
    todo_id: int,
    db: Session = Depends(get_db)
):

    todo = (
        db.query(TodoDB)
        .filter(TodoDB.id == todo_id)
        .first()
    )

    if not todo:

        raise HTTPException(
            status_code=404,
            detail="TODO not found"
        )

    db.delete(todo)

    db.commit()

    return {
        "message": "TODO deleted successfully"
    }
