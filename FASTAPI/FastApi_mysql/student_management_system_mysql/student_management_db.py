# ============================================================
# 🎓 FastAPI Student Management System (CRUD) using MySQL
# ============================================================
# 📌 Features:
# ✅ Create Student
# ✅ Read All Students
# ✅ Read Student By ID
# ✅ Update Student
# ✅ Delete Student
# ✅ MySQL Connection
# ✅ SQLAlchemy ORM
# ✅ FastAPI Framework
# ============================================================


# ============================================================
# 📦 Import Required Libraries
# ============================================================

from fastapi import FastAPI, HTTPException, Depends

from pydantic import BaseModel, ConfigDict

from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Boolean
)

from sqlalchemy.orm import (
    declarative_base,
    sessionmaker,
    Session
)


# ============================================================
# 🚀 Create FastAPI Application
# ============================================================

app = FastAPI(

    title="Student Management System API",

    description="CRUD Operations using FastAPI + MySQL",

    version="1.0"

)


# ============================================================
# 🗄️ MySQL Database Configuration
# ============================================================

# Format:
# mysql+pymysql://username:password@host/database_name

DATABASE_URL = "mysql+pymysql://root:1234@localhost/student_management"


# ============================================================
# 🔌 Create Database Engine
# ============================================================

engine = create_engine(

    DATABASE_URL,

    echo=True

)


# ============================================================
# 🧩 Create Session Factory
# ============================================================

SessionLocal = sessionmaker(

    autocommit=False,

    autoflush=False,

    bind=engine

)


# ============================================================
# 🏗️ Create Base Class
# ============================================================

Base = declarative_base()


# ============================================================
# 🎓 Student Database Table Model
# ============================================================

class Student(Base):

    __tablename__ = "students"

    # Primary Key
    id = Column(Integer, primary_key=True, index=True)

    # Student Name
    name = Column(String(100), nullable=False)

    # Student Age
    age = Column(Integer)

    # Student Marks
    marks = Column(Integer)

    # Student Course
    course = Column(String(100))

    # Active Status
    is_active = Column(Boolean, default=True)


# ============================================================
# 🛠️ Create Tables in MySQL
# ============================================================

Base.metadata.create_all(bind=engine)


# ============================================================
# 📥 Pydantic Model - Create Student
# ============================================================

class StudentCreate(BaseModel):

    id: int

    name: str

    age: int

    marks: int

    course: str


# ============================================================
# 📤 Pydantic Model - Response
# ============================================================

class StudentResponse(BaseModel):

    id: int

    name: str

    age: int

    marks: int

    course: str

    is_active: bool

    # Pydantic V2 Configuration
    model_config = ConfigDict(

        from_attributes=True

    )


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

        "message": "🎉 Welcome to Student Management System API"

    }


# ============================================================
# ➕ Create Student API
# ============================================================

@app.post(
    "/students/",
    response_model=StudentResponse
)

def create_student(

    student: StudentCreate,

    db: Session = Depends(get_db)

):

    # Check Existing Student
    existing_student = (

        db.query(Student)
        .filter(Student.id == student.id)
        .first()

    )

    # If Student Already Exists
    if existing_student:

        raise HTTPException(

            status_code=400,

            detail="❌ Student with this ID already exists"

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

    # Add Data
    db.add(new_student)

    # Save Changes
    db.commit()

    # Refresh Data
    db.refresh(new_student)

    return new_student


# ============================================================
# 📋 Get All Students API
# ============================================================

@app.get(
    "/students/",
    response_model=list[StudentResponse]
)

def get_all_students(

    db: Session = Depends(get_db)

):

    students = db.query(Student).all()

    return students


# ============================================================
# 🔍 Get Student By ID API
# ============================================================

@app.get(
    "/students/{student_id}",
    response_model=StudentResponse
)

def get_student(

    student_id: int,

    db: Session = Depends(get_db)

):

    # Find Student
    student = (

        db.query(Student)
        .filter(Student.id == student_id)
        .first()

    )

    # If Student Not Found
    if not student:

        raise HTTPException(

            status_code=404,

            detail="❌ Student not found"

        )

    return student


# ============================================================
# ✏️ Update Student API
# ============================================================

@app.put(
    "/students/{student_id}",
    response_model=StudentResponse
)

def update_student(

    student_id: int,

    updated_student: StudentCreate,

    db: Session = Depends(get_db)

):

    # Find Existing Student
    student = (

        db.query(Student)
        .filter(Student.id == student_id)
        .first()

    )

    # If Student Not Found
    if not student:

        raise HTTPException(

            status_code=404,

            detail="❌ Student not found"

        )

    # Update Student Data
    student.name = updated_student.name

    student.age = updated_student.age

    student.marks = updated_student.marks

    student.course = updated_student.course

    # Save Changes
    db.commit()

    # Refresh Updated Data
    db.refresh(student)

    return student


# ============================================================
# ❌ Delete Student API
# ============================================================

@app.delete("/students/{student_id}")
def delete_student(

    student_id: int,

    db: Session = Depends(get_db)

):

    # Find Student
    student = (

        db.query(Student)
        .filter(Student.id == student_id)
        .first()

    )

    # If Student Not Found
    if not student:

        raise HTTPException(

            status_code=404,

            detail="❌ Student not found"

        )

    # Delete Student
    db.delete(student)

    # Save Changes
    db.commit()

    return {

        "message": "🗑️ Student deleted successfully"

    }


# ============================================================
# ▶️ Run FastAPI Server
# ============================================================

# Command:
# uvicorn student_management_db:app --reload


# ============================================================
# 🌐 Swagger Documentation
# ============================================================

# Open Browser:
# http://127.0.0.1:8000/docs


# ============================================================
# 📌 Install Required Packages
# ============================================================

# pip install fastapi
# pip install uvicorn
# pip install sqlalchemy
# pip install pymysql


# ============================================================
# 🗄️ MySQL Database Command
# ============================================================

# CREATE DATABASE student_management;
