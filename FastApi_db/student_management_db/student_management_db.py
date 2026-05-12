# ============================================================
# 📝 FastAPI Student Management System App (CRUD) - SQLite
# ============================================================

# ============================================================
# IMPORT LIBRARIES
# ============================================================

from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# ============================================================
# CREATE FASTAPI APP
# ============================================================

app = FastAPI()

# ============================================================
# DATABASE CONFIGURATION
# ============================================================

DATABASE_URL = "sqlite:///./students.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

# ============================================================
# DATABASE MODEL
# ============================================================

class Student(Base):

    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)
    marks = Column(Integer)
    course = Column(String)
    is_active = Column(Boolean, default=True)

# Create Table
Base.metadata.create_all(bind=engine)

# ============================================================
# PYDANTIC MODELS
# ============================================================

# Create Student Model
class StudentCreate(BaseModel):

    id: int
    name: str
    age: int
    marks: int
    course: str

# Update Student Model
class StudentUpdate(BaseModel):

    name: str
    age: int
    marks: int
    course: str

# ============================================================
# DATABASE DEPENDENCY
# ============================================================

def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()

# ============================================================
# HOME ROUTE
# ============================================================

@app.get("/")

def home():

    return {
        "message": "Welcome to Student Management System API"
    }

# ============================================================
# CREATE STUDENT
# ============================================================

@app.post("/students/")

def create_student(
    student: StudentCreate,
    db: Session = Depends(get_db)
):

    # Check Duplicate Student
    existing_student = (
        db.query(Student)
        .filter(Student.id == student.id)
        .first()
    )

    if existing_student:

        raise HTTPException(
            status_code=400,
            detail="Student with this ID already exists"
        )

    # Create New Student
    new_student = Student(
        id=student.id,
        name=student.name,
        age=student.age,
        marks=student.marks,
        course=student.course,
        is_active=True
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return {
        "message": "Student created successfully",
        "student": {
            "id": new_student.id,
            "name": new_student.name,
            "age": new_student.age,
            "marks": new_student.marks,
            "course": new_student.course,
            "is_active": new_student.is_active
        }
    }

# ============================================================
# GET ALL STUDENTS
# ============================================================

@app.get("/students/")

def get_all_students(
    db: Session = Depends(get_db)
):

    students = db.query(Student).all()

    student_list = []

    for student in students:

        student_list.append({
            "id": student.id,
            "name": student.name,
            "age": student.age,
            "marks": student.marks,
            "course": student.course,
            "is_active": student.is_active
        })

    return {
        "count": len(student_list),
        "students": student_list
    }

# ============================================================
# GET STUDENT BY ID
# ============================================================

@app.get("/students/{student_id}")

def get_student(
    student_id: int,
    db: Session = Depends(get_db)
):

    student = (
        db.query(Student)
        .filter(Student.id == student_id)
        .first()
    )

    if not student:

        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return {
        "student": {
            "id": student.id,
            "name": student.name,
            "age": student.age,
            "marks": student.marks,
            "course": student.course,
            "is_active": student.is_active
        }
    }

# ============================================================
# UPDATE STUDENT
# ============================================================

@app.put("/students/{student_id}")

def update_student(
    student_id: int,
    updated_student: StudentUpdate,
    db: Session = Depends(get_db)
):

    student = (
        db.query(Student)
        .filter(Student.id == student_id)
        .first()
    )

    if not student:

        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    # Update Student Data
    student.name = updated_student.name
    student.age = updated_student.age
    student.marks = updated_student.marks
    student.course = updated_student.course

    db.commit()
    db.refresh(student)

    return {
        "message": "Student updated successfully",
        "student": {
            "id": student.id,
            "name": student.name,
            "age": student.age,
            "marks": student.marks,
            "course": student.course,
            "is_active": student.is_active
        }
    }

# ============================================================
# DELETE STUDENT
# ============================================================

@app.delete("/students/{student_id}")

def delete_student(
    student_id: int,
    db: Session = Depends(get_db)
):

    student = (
        db.query(Student)
        .filter(Student.id == student_id)
        .first()
    )

    if not student:

        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    db.delete(student)
    db.commit()

    return {
        "message": "Student deleted successfully"
    }

# ============================================================
# RUN SERVER
# ============================================================

# Run command:
# uvicorn student_management_db:app --reload
