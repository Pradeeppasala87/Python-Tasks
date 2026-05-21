# ============================================================
# 📝 FastAPI Employee Management System - MySQL Version
# ============================================================

# ============================================================
# 📦 IMPORT REQUIRED LIBRARIES
# ============================================================

from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, ConfigDict
from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Float,
    ForeignKey
)
from sqlalchemy.orm import (
    declarative_base,
    sessionmaker,
    Session
)

# ============================================================
# 🚀 CREATE FASTAPI APPLICATION
# ============================================================

app = FastAPI()

# ============================================================
# 🗄️ MYSQL DATABASE CONFIGURATION
# ============================================================

DATABASE_URL = "mysql+pymysql://root:1234@localhost:3306/employee_db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

# ============================================================
# 👨‍💼 EMPLOYEE TABLE
# ============================================================

class EmployeeDB(Base):

    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(255), nullable=False)

    age = Column(Integer)

    gender = Column(String(50))

    email = Column(String(255))

    phone = Column(String(20))

    address = Column(String(500))

    designation = Column(String(255))

    joining_date = Column(String(50))


# ============================================================
# 🏢 DEPARTMENT TABLE
# ============================================================

class DepartmentDB(Base):

    __tablename__ = "departments"

    id = Column(Integer, primary_key=True, index=True)

    department_name = Column(String(255))

    department_head = Column(String(255))

    department_location = Column(String(255))

    total_employees = Column(Integer)


# ============================================================
# 💰 SALARY TABLE
# ============================================================

class SalaryDB(Base):

    __tablename__ = "salaries"

    id = Column(Integer, primary_key=True, index=True)

    employee_id = Column(
        Integer,
        ForeignKey("employees.id")
    )

    basic_salary = Column(Float)

    bonus = Column(Float)

    deduction = Column(Float)

    net_salary = Column(Float)

    salary_month = Column(String(50))


# ============================================================
# 📅 ATTENDANCE TABLE
# ============================================================

class AttendanceDB(Base):

    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True, index=True)

    employee_id = Column(
        Integer,
        ForeignKey("employees.id")
    )

    attendance_date = Column(String(50))

    check_in_time = Column(String(50))

    check_out_time = Column(String(50))

    status = Column(String(50))

    leave_type = Column(String(100))

    leave_reason = Column(String(255))

    leave_days = Column(Integer)

    total_present_days = Column(Integer)

    total_absent_days = Column(Integer)

    total_leave_days = Column(Integer)


# ============================================================
# ✅ CREATE ALL TABLES
# ============================================================

Base.metadata.create_all(bind=engine)

# ============================================================
# 🧾 PYDANTIC SCHEMAS
# ============================================================

# ============================================================
# 👨‍💼 EMPLOYEE SCHEMA
# ============================================================

class Employee(BaseModel):

    id: int
    name: str
    age: int
    gender: str
    email: str
    phone: str
    address: str
    designation: str
    joining_date: str

    model_config = ConfigDict(
        from_attributes=True
    )


# ============================================================
# 🏢 DEPARTMENT SCHEMA
# ============================================================

class Department(BaseModel):

    department_name: str
    department_head: str
    department_location: str
    total_employees: int

    model_config = ConfigDict(
        from_attributes=True
    )


# ============================================================
# 💰 SALARY SCHEMA
# ============================================================

class Salary(BaseModel):

    employee_id: int
    basic_salary: float
    bonus: float
    deduction: float
    net_salary: float
    salary_month: str

    model_config = ConfigDict(
        from_attributes=True
    )


# ============================================================
# 📅 ATTENDANCE SCHEMA
# ============================================================

class Attendance(BaseModel):

    employee_id: int
    attendance_date: str
    check_in_time: str
    check_out_time: str
    status: str
    leave_type: str
    leave_reason: str
    leave_days: int
    total_present_days: int
    total_absent_days: int
    total_leave_days: int

    model_config = ConfigDict(
        from_attributes=True
    )


# ============================================================
# 🔌 DATABASE CONNECTION DEPENDENCY
# ============================================================

def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


# ============================================================
# 🏠 HOME API
# ============================================================

@app.get("/")
def home():

    return {
        "message": "FastAPI Employee Management System 🚀"
    }


# ============================================================
# 👨‍💼 EMPLOYEE APIs
# ============================================================

# ============================================================
# ✅ ADD EMPLOYEE
# ============================================================

@app.post("/employees")
def add_employee(
    employee: Employee,
    db: Session = Depends(get_db)
):

    existing_employee = db.query(EmployeeDB).filter(
        EmployeeDB.id == employee.id
    ).first()

    if existing_employee:

        raise HTTPException(
            status_code=400,
            detail="Employee ID already exists"
        )

    new_employee = EmployeeDB(
        id=employee.id,
        name=employee.name,
        age=employee.age,
        gender=employee.gender,
        email=employee.email,
        phone=employee.phone,
        address=employee.address,
        designation=employee.designation,
        joining_date=employee.joining_date
    )

    db.add(new_employee)

    db.commit()

    db.refresh(new_employee)

    return {
        "message": "Employee Added Successfully",
        "data": new_employee
    }


# ============================================================
# ✅ GET ALL EMPLOYEES
# ============================================================

@app.get("/employees")
def get_employees(
    db: Session = Depends(get_db)
):

    employees = db.query(EmployeeDB).all()

    return {
        "count": len(employees),
        "data": employees
    }


# ============================================================
# ✅ GET EMPLOYEE BY ID
# ============================================================

@app.get("/employees/{employee_id}")
def get_employee(
    employee_id: int,
    db: Session = Depends(get_db)
):

    employee = db.query(EmployeeDB).filter(
        EmployeeDB.id == employee_id
    ).first()

    if not employee:

        raise HTTPException(
            status_code=404,
            detail="Employee Not Found"
        )

    return employee


# ============================================================
# ✅ UPDATE EMPLOYEE
# ============================================================

@app.put("/employees/{employee_id}")
def update_employee(
    employee_id: int,
    updated_employee: Employee,
    db: Session = Depends(get_db)
):

    employee = db.query(EmployeeDB).filter(
        EmployeeDB.id == employee_id
    ).first()

    if not employee:

        raise HTTPException(
            status_code=404,
            detail="Employee Not Found"
        )

    employee.name = updated_employee.name
    employee.age = updated_employee.age
    employee.gender = updated_employee.gender
    employee.email = updated_employee.email
    employee.phone = updated_employee.phone
    employee.address = updated_employee.address
    employee.designation = updated_employee.designation
    employee.joining_date = updated_employee.joining_date

    db.commit()

    db.refresh(employee)

    return {
        "message": "Employee Updated Successfully",
        "data": employee
    }


# ============================================================
# ✅ DELETE EMPLOYEE
# ============================================================

@app.delete("/employees/{employee_id}")
def delete_employee(
    employee_id: int,
    db: Session = Depends(get_db)
):

    employee = db.query(EmployeeDB).filter(
        EmployeeDB.id == employee_id
    ).first()

    if not employee:

        raise HTTPException(
            status_code=404,
            detail="Employee Not Found"
        )

    db.delete(employee)

    db.commit()

    return {
        "message": "Employee Deleted Successfully"
    }


# ============================================================
# ✅ SEARCH EMPLOYEE BY NAME
# ============================================================

@app.get("/search-employee/{name}")
def search_employee(
    name: str,
    db: Session = Depends(get_db)
):

    employees = db.query(EmployeeDB).filter(
        EmployeeDB.name.ilike(f"%{name}%")
    ).all()

    return {
        "count": len(employees),
        "data": employees
    }


# ============================================================
# 🏢 DEPARTMENT APIs
# ============================================================

# ============================================================
# ✅ ADD DEPARTMENT
# ============================================================

@app.post("/departments")
def add_department(
    department: Department,
    db: Session = Depends(get_db)
):

    new_department = DepartmentDB(
        department_name=department.department_name,
        department_head=department.department_head,
        department_location=department.department_location,
        total_employees=department.total_employees
    )

    db.add(new_department)

    db.commit()

    db.refresh(new_department)

    return {
        "message": "Department Added Successfully",
        "data": new_department
    }


# ============================================================
# ✅ GET ALL DEPARTMENTS
# ============================================================

@app.get("/departments")
def get_departments(
    db: Session = Depends(get_db)
):

    departments = db.query(DepartmentDB).all()

    return {
        "count": len(departments),
        "data": departments
    }


# ============================================================
# ✅ UPDATE DEPARTMENT
# ============================================================

@app.put("/departments/{department_id}")
def update_department(
    department_id: int,
    updated_department: Department,
    db: Session = Depends(get_db)
):

    department = db.query(DepartmentDB).filter(
        DepartmentDB.id == department_id
    ).first()

    if not department:

        raise HTTPException(
            status_code=404,
            detail="Department Not Found"
        )

    department.department_name = updated_department.department_name
    department.department_head = updated_department.department_head
    department.department_location = updated_department.department_location
    department.total_employees = updated_department.total_employees

    db.commit()

    db.refresh(department)

    return {
        "message": "Department Updated Successfully",
        "data": department
    }


# ============================================================
# 💰 SALARY APIs
# ============================================================

# ============================================================
# ✅ ADD SALARY
# ============================================================

@app.post("/salary")
def add_salary(
    salary: Salary,
    db: Session = Depends(get_db)
):

    employee = db.query(EmployeeDB).filter(
        EmployeeDB.id == salary.employee_id
    ).first()

    if not employee:

        raise HTTPException(
            status_code=404,
            detail="Employee Not Found"
        )

    new_salary = SalaryDB(
        employee_id=salary.employee_id,
        basic_salary=salary.basic_salary,
        bonus=salary.bonus,
        deduction=salary.deduction,
        net_salary=salary.net_salary,
        salary_month=salary.salary_month
    )

    db.add(new_salary)

    db.commit()

    db.refresh(new_salary)

    return {
        "message": "Salary Added Successfully",
        "data": new_salary
    }


# ============================================================
# ✅ GET ALL SALARIES
# ============================================================

@app.get("/salary")
def get_salary(
    db: Session = Depends(get_db)
):

    salaries = db.query(SalaryDB).all()

    return {
        "count": len(salaries),
        "data": salaries
    }


# ============================================================
# ✅ HIGH SALARY EMPLOYEES
# ============================================================

@app.get("/high-salary-employees")
def high_salary_employees(
    db: Session = Depends(get_db)
):

    employees = db.query(SalaryDB).filter(
        SalaryDB.net_salary > 50000
    ).all()

    return {
        "count": len(employees),
        "data": employees
    }


# ============================================================
# ✅ UPDATE SALARY
# ============================================================

@app.put("/salary/{salary_id}")
def update_salary(
    salary_id: int,
    updated_salary: Salary,
    db: Session = Depends(get_db)
):

    salary = db.query(SalaryDB).filter(
        SalaryDB.id == salary_id
    ).first()

    if not salary:

        raise HTTPException(
            status_code=404,
            detail="Salary Record Not Found"
        )

    salary.employee_id = updated_salary.employee_id
    salary.basic_salary = updated_salary.basic_salary
    salary.bonus = updated_salary.bonus
    salary.deduction = updated_salary.deduction
    salary.net_salary = updated_salary.net_salary
    salary.salary_month = updated_salary.salary_month

    db.commit()

    db.refresh(salary)

    return {
        "message": "Salary Updated Successfully",
        "data": salary
    }


# ============================================================
# 📅 ATTENDANCE APIs
# ============================================================

# ============================================================
# ✅ MARK ATTENDANCE
# ============================================================

@app.post("/attendance")
def mark_attendance(
    attendance: Attendance,
    db: Session = Depends(get_db)
):

    employee = db.query(EmployeeDB).filter(
        EmployeeDB.id == attendance.employee_id
    ).first()

    if not employee:

        raise HTTPException(
            status_code=404,
            detail="Employee Not Found"
        )

    new_attendance = AttendanceDB(
        employee_id=attendance.employee_id,
        attendance_date=attendance.attendance_date,
        check_in_time=attendance.check_in_time,
        check_out_time=attendance.check_out_time,
        status=attendance.status,
        leave_type=attendance.leave_type,
        leave_reason=attendance.leave_reason,
        leave_days=attendance.leave_days,
        total_present_days=attendance.total_present_days,
        total_absent_days=attendance.total_absent_days,
        total_leave_days=attendance.total_leave_days
    )

    db.add(new_attendance)

    db.commit()

    db.refresh(new_attendance)

    return {
        "message": "Attendance Marked Successfully",
        "data": new_attendance
    }


# ============================================================
# ✅ GET ALL ATTENDANCE
# ============================================================

@app.get("/attendance")
def get_attendance(
    db: Session = Depends(get_db)
):

    attendance = db.query(AttendanceDB).all()

    return {
        "count": len(attendance),
        "data": attendance
    }


# ============================================================
# ✅ UPDATE ATTENDANCE
# ============================================================

@app.put("/attendance/{attendance_id}")
def update_attendance(
    attendance_id: int,
    updated_attendance: Attendance,
    db: Session = Depends(get_db)
):

    attendance = db.query(AttendanceDB).filter(
        AttendanceDB.id == attendance_id
    ).first()

    if not attendance:

        raise HTTPException(
            status_code=404,
            detail="Attendance Record Not Found"
        )

    attendance.employee_id = updated_attendance.employee_id
    attendance.attendance_date = updated_attendance.attendance_date
    attendance.check_in_time = updated_attendance.check_in_time
    attendance.check_out_time = updated_attendance.check_out_time
    attendance.status = updated_attendance.status
    attendance.leave_type = updated_attendance.leave_type
    attendance.leave_reason = updated_attendance.leave_reason
    attendance.leave_days = updated_attendance.leave_days
    attendance.total_present_days = updated_attendance.total_present_days
    attendance.total_absent_days = updated_attendance.total_absent_days
    attendance.total_leave_days = updated_attendance.total_leave_days

    db.commit()

    db.refresh(attendance)

    return {
        "message": "Attendance Updated Successfully",
        "data": attendance
    }


# ============================================================
# ▶️ RUN APPLICATION
# ============================================================

"""
RUN COMMAND:

uvicorn employee_mysql:app --reload

SWAGGER UI:

http://127.0.0.1:8000/docs
"""
