# ============================================================
# IMPORTS
# ============================================================

from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Date
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session
from pydantic import BaseModel
from pydantic import ConfigDict
from typing import Optional
from datetime import date

# ============================================================
# FASTAPI APP
# ============================================================

app = FastAPI(
    title="Employee Management System",
    version="2.0.0"
)

# ============================================================
# CORS MIDDLEWARE
# ============================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ============================================================
# DATABASE CONFIGURATION
# ============================================================

# You can update the credentials below.
MYSQL_URL = "mysql+pymysql://root:1234@localhost/hrms_db"

engine = create_engine(MYSQL_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

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
# SQLALCHEMY MODELS
# ============================================================

class Department(Base):
    __tablename__ = "departments"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    location = Column(String(100))
    employees = relationship("Employee", back_populates="department", lazy="select")

class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    age = Column(Integer)
    email = Column(String(100), unique=True)
    phone = Column(String(20))
    designation = Column(String(100))
    department_id = Column(Integer, ForeignKey("departments.id"))
    department = relationship("Department", back_populates="employees", lazy="select")
    attendance = relationship("Attendance", back_populates="employee", lazy="select")
    salary = relationship("Salary", back_populates="employee", lazy="select")

class Attendance(Base):
    __tablename__ = "attendance"
    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"),nullable=False)
    date = Column(Date)
    status = Column(String(20))
    employee = relationship("Employee", back_populates="attendance", lazy="select")

class Salary(Base):
    __tablename__ = "salaries"
    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"), nullable=False)
    salary = Column(Float)
    bonus = Column(Float)
    employee = relationship("Employee", back_populates="salary", lazy="select")

# ============================================================
# CREATE TABLES
# ============================================================
Base.metadata.create_all(bind=engine)

# ============================================================
# PYDANTIC SCHEMAS
# ============================================================

class DepartmentCreate(BaseModel):
    name: str
    location: str

class DepartmentResponse(BaseModel):
    id: int
    name: str
    location: str
    model_config = ConfigDict(from_attributes=True)

class EmployeeCreate(BaseModel):
    name: str
    age: int
    email: str
    phone: str
    designation: str
    department_id: int

class EmployeeUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    designation: Optional[str] = None
    department_id: Optional[int] = None

class EmployeeResponse(BaseModel):
    id: int
    name: str
    age: Optional[int] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    designation: Optional[str] = None
    department_id: Optional[int] = None
    model_config = ConfigDict(from_attributes=True)

class AttendanceCreate(BaseModel):
    employee_id: int
    date: date
    status: str

class AttendanceResponse(AttendanceCreate):
    id: int
    model_config = ConfigDict(from_attributes=True)

class SalaryCreate(BaseModel):
    employee_id: int
    salary: float
    bonus: float

class SalaryResponse(SalaryCreate):
    id: int
    model_config = ConfigDict(from_attributes=True)

# ============================================================
# HOME ROUTE
# ============================================================
@app.get("/")
def home():
    return {"message": "Employee Management System Running Successfully"}

# ============================================================
# DEPARTMENT APIS
# ============================================================
@app.post("/departments", response_model=DepartmentResponse)
def create_department(department: DepartmentCreate, db: Session = Depends(get_db)):
    new_department = Department(name=department.name, location=department.location)
    db.add(new_department)
    db.commit()
    db.refresh(new_department)
    return new_department

@app.get("/departments", response_model=list[DepartmentResponse])
def get_departments(db: Session = Depends(get_db)):
    return db.query(Department).all()

@app.get("/departments/{department_id}", response_model=DepartmentResponse)
def get_department_by_id(department_id: int, db: Session = Depends(get_db)):
    department = db.query(Department).filter(Department.id == department_id).first()
    if not department:
        raise HTTPException(status_code=404, detail="Department Not Found")
    return department

@app.delete("/departments/{department_id}")
def delete_department(department_id: int, db: Session = Depends(get_db)):
    department = db.query(Department).filter(Department.id == department_id).first()
    if not department:
        raise HTTPException(status_code=404, detail="Department Not Found")
    db.delete(department)
    db.commit()
    return {"message": "Department Deleted Successfully"}

# ============================================================
# EMPLOYEE APIS
# ============================================================
@app.post("/employees", response_model=EmployeeResponse)
def create_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
    new_employee = Employee(
        name=employee.name,
        age=employee.age,
        email=employee.email,
        phone=employee.phone,
        designation=employee.designation,
        department_id=employee.department_id
    )
    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)
    
    # Auto-generate default Salary and Attendance
    from datetime import date
    default_salary = Salary(employee_id=new_employee.id, salary=60000.0, bonus=0.0)
    default_attendance = Attendance(employee_id=new_employee.id, date=date.today(), status="Present")
    
    db.add(default_salary)
    db.add(default_attendance)
    db.commit()

    return new_employee

@app.get("/employees", response_model=list[EmployeeResponse])
def get_employees(db: Session = Depends(get_db)):
    return db.query(Employee).all()

@app.get("/employees/{employee_id}", response_model=EmployeeResponse)
def get_employee_by_id(employee_id: int, db: Session = Depends(get_db)):
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Employee Not Found")
    return employee

@app.put("/employees/{employee_id}", response_model=EmployeeResponse)
def update_employee(employee_id: int, employee_data: EmployeeUpdate, db: Session = Depends(get_db)):
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Employee Not Found")
    for key, value in employee_data.dict(exclude_unset=True).items():
        setattr(employee, key, value)
    db.commit()
    db.refresh(employee)
    return employee

@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Employee Not Found")
    db.delete(employee)
    db.commit()
    return {"message": "Employee Deleted Successfully"}

# ============================================================
# SEARCH EMPLOYEE
# ============================================================
@app.get("/search-employee/{employee_name}")
def search_employee(employee_name: str, db: Session = Depends(get_db)):
    employees = db.query(Employee).filter(Employee.name.ilike(f"%{employee_name}%")).all()
    return employees

# ============================================================
# ATTENDANCE APIS
# ============================================================
@app.get("/attendance-filter")
def attendance_filter(attendance_date: date, department_id: int, db: Session = Depends(get_db)):
    employees = db.query(Employee).filter(Employee.department_id == department_id).all()
    employee_ids = [emp.id for emp in employees]
    attendance_records = db.query(Attendance).filter(
        Attendance.employee_id.in_(employee_ids),
        Attendance.date == attendance_date
    ).all()
    status_map = {rec.employee_id: rec.status.strip().capitalize() for rec in attendance_records}
    present = []
    absent = []
    leave = []
    for emp in employees:
        status = status_map.get(emp.id, "Absent")
        emp_data = {
            "id": emp.id,
            "name": emp.name,
            "designation": emp.designation,
            "email": emp.email,
            "status": status
        }
        if status == "Present":
            present.append(emp_data)
        elif status == "Leave":
            leave.append(emp_data)
        else:
            absent.append(emp_data)
    return {
        "present_count": len(present),
        "absent_count": len(absent),
        "leave_count": len(leave),
        "present_employees": present,
        "absent_employees": absent,
        "leave_employees": leave
    }

@app.post("/attendance", response_model=AttendanceResponse)
def create_attendance(attendance: AttendanceCreate, db: Session = Depends(get_db)):
    new_attendance = Attendance(
        employee_id=attendance.employee_id,
        date=attendance.date,
        status=attendance.status
    )
    db.add(new_attendance)
    db.commit()
    db.refresh(new_attendance)
    return new_attendance

@app.get("/attendance", response_model=list[AttendanceResponse])
def get_attendance(db: Session = Depends(get_db)):
    return db.query(Attendance).all()

@app.get("/attendance/employee/{employee_id}")
def get_attendance_by_employee(employee_id: int, db: Session = Depends(get_db)):
    return db.query(Attendance).filter(Attendance.employee_id == employee_id).all()

@app.delete("/attendance/{attendance_id}")
def delete_attendance(attendance_id: int, db: Session = Depends(get_db)):
    attendance = db.query(Attendance).filter(Attendance.id == attendance_id).first()
    if not attendance:
        raise HTTPException(status_code=404, detail="Attendance Record Not Found")
    db.delete(attendance)
    db.commit()
    return {"message": "Attendance Deleted Successfully"}

# ============================================================
# SALARY APIS
# ============================================================
@app.post("/salary", response_model=SalaryResponse)
def create_salary(salary: SalaryCreate, db: Session = Depends(get_db)):
    new_salary = Salary(
        employee_id=salary.employee_id,
        salary=salary.salary,
        bonus=salary.bonus
    )
    db.add(new_salary)
    db.commit()
    db.refresh(new_salary)
    return new_salary

@app.get("/salary", response_model=list[SalaryResponse])
def get_salaries(db: Session = Depends(get_db)):
    return db.query(Salary).all()

@app.get("/salary/employee/{employee_id}")
def get_salary_by_employee(employee_id: int, db: Session = Depends(get_db)):
    return db.query(Salary).filter(Salary.employee_id == employee_id).all()

@app.delete("/salary/{salary_id}")
def delete_salary(salary_id: int, db: Session = Depends(get_db)):
    salary = db.query(Salary).filter(Salary.id == salary_id).first()
    if not salary:
        raise HTTPException(status_code=404, detail="Salary Record Not Found")
    db.delete(salary)
    db.commit()
    return {"message": "Salary Deleted Successfully"}

@app.get("/high-salary-employees")
def get_high_salary_employees(minimum_salary: float = 50000, db: Session = Depends(get_db)):
    salaries = db.query(Salary).filter(Salary.salary >= minimum_salary).all()
    result = []
    for salary in salaries:
        if salary.employee is None:
            continue
        result.append({
            "employee_id": salary.employee.id,
            "employee_name": salary.employee.name,
            "department_name": (salary.employee.department.name if salary.employee.department else "N/A"),
            "salary": salary.salary
        })
    return result
