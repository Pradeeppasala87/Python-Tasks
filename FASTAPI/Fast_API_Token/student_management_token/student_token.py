# ============================================================
# 🎓 FastAPI Student Management System + JWT + MySQL
# ============================================================

'''
This project includes:

✅ FastAPI
✅ JWT Authentication
✅ CRUD Operations
✅ MySQL Database
'''

# ============================================================
# 🚀 INSTALL PACKAGES
# ============================================================

'''
pip install fastapi uvicorn python-jose sqlalchemy pymysql
'''

# ============================================================
# 📦 IMPORTS
# ============================================================

from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from jose import JWTError, jwt
from datetime import datetime, timedelta

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base, Session

# ============================================================
# 🚀 APP CREATE
# ============================================================

app = FastAPI()

# ============================================================
# 🔐 JWT CONFIG
# ============================================================

SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE = timedelta(minutes=15)

# ============================================================
# 🗄️ MYSQL CONFIG
# ============================================================

DATABASE_URL = "mysql+pymysql://root:1234@localhost/student_database"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

# ============================================================
# 📋 STUDENT TABLE
# ============================================================

class StudentTable(Base):

    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    course = Column(String(255))
    age = Column(Integer)

# ============================================================
# CREATE TABLE
# ============================================================

Base.metadata.create_all(bind=engine)

# ============================================================
# DB SESSION
# ============================================================

def get_db():

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ============================================================
# 🧾 MODELS
# ============================================================

class Student(BaseModel):
    id: int
    name: str
    course: str
    age: int

class Login(BaseModel):
    username: str
    password: str

# ============================================================
# 🔐 TOKEN
# ============================================================

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def create_token(data: dict):

    to_encode = data.copy()
    expire = datetime.utcnow() + ACCESS_TOKEN_EXPIRE
    to_encode.update({"exp": expire})

    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token: str = Depends(oauth2_scheme)):

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user = payload.get("sub")

        if user is None:
            raise HTTPException(status_code=401, detail="Invalid token")

        return user

    except JWTError:
        raise HTTPException(status_code=401, detail="Token expired or invalid")

# ============================================================
# 🏠 HOME
# ============================================================

@app.get("/")
def home():
    return {"message": "Student Management System 🚀"}

# ============================================================
# 🔐 LOGIN
# ============================================================

@app.post("/login")
def login(user: Login):

    if user.username != "admin" or user.password != "admin123":
        raise HTTPException(status_code=401, detail="Invalid login")

    token = create_token({"sub": user.username})

    return {
        "access_token": token,
        "token_type": "bearer",
        "expires_in": "10 minutes"
    }

# ============================================================
# ➕ ADD STUDENT
# ============================================================

@app.post("/students")
def add_student(
    student: Student,
    db: Session = Depends(get_db),
    user: str = Depends(verify_token)
):

    new_student = StudentTable(
        id=student.id,
        name=student.name,
        course=student.course,
        age=student.age
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return {"message": "Student added", "data": new_student}

# ============================================================
# 📥 GET ALL STUDENTS
# ============================================================

@app.get("/students")
def get_students(
    db: Session = Depends(get_db),
    user: str = Depends(verify_token)
):

    students = db.query(StudentTable).all()

    return {"count": len(students), "data": students}

# ============================================================
# 🔍 GET SINGLE STUDENT
# ============================================================

@app.get("/students/{student_id}")
def get_student(
    student_id: int,
    db: Session = Depends(get_db),
    user: str = Depends(verify_token)
):

    student = db.query(StudentTable).filter(StudentTable.id == student_id).first()

    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    return student

# ============================================================
# ✏️ UPDATE STUDENT
# ============================================================

@app.put("/students/{student_id}")
def update_student(
    student_id: int,
    updated: Student,
    db: Session = Depends(get_db),
    user: str = Depends(verify_token)
):

    student = db.query(StudentTable).filter(StudentTable.id == student_id).first()

    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    student.name = updated.name
    student.course = updated.course
    student.age = updated.age

    db.commit()
    db.refresh(student)

    return {"message": "Student updated", "data": student}

# ============================================================
# ❌ DELETE STUDENT
# ============================================================

@app.delete("/students/{student_id}")
def delete_student(
    student_id: int,
    db: Session = Depends(get_db),
    user: str = Depends(verify_token)
):

    student = db.query(StudentTable).filter(StudentTable.id == student_id).first()

    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    db.delete(student)
    db.commit()

    return {"message": "Student deleted"}
