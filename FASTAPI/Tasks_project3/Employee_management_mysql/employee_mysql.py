from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel, ConfigDict
from sqlalchemy import create_engine, Column, String, Integer, Float
from sqlalchemy.orm import Session, sessionmaker, declarative_base

# ------------------------------------------------------------
# 🚀 App
# ------------------------------------------------------------
app = FastAPI()

# ------------------------------------------------------------
# 🗄️ MySQL Configuration
# ------------------------------------------------------------
url = "mysql+pymysql://root:1234@localhost/employee_db"

engine = create_engine(url)
sessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# ------------------------------------------------------------
# 🧱 Table Model
# ------------------------------------------------------------
class EmployeeTable(Base):
    __tablename__ = "employee_table"

    emp_id = Column(Integer, primary_key=True, index=True)
    emp_name = Column(String(100))
    emp_dprt = Column(String(100))
    emp_dsgn = Column(String(100))
    emp_salary = Column(Float)

class AttendanceTable(Base):
    __tablename__ = "attendance_table"

    attendance_id = Column(Integer, primary_key=True, index=True)
    emp_id = Column(Integer)
    emp_name = Column(String(100))
    status = Column(String(50))

# Create table
Base.metadata.create_all(bind=engine)

# ------------------------------------------------------------
# 🧾 Schema (Pydantic)
# ------------------------------------------------------------
class EmployeeSchema(BaseModel):
    emp_id: int
    emp_name: str
    emp_dprt: str
    emp_dsgn: str
    emp_salary: float

    model_config = ConfigDict(from_attributes=True)

# ------------------------------------------------------------
# DB Dependency
# ------------------------------------------------------------
def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

# ------------------------------------------------------------
# Home
# ------------------------------------------------------------
@app.get("/")
def home():
    return {"msg": "FastAPI + MySQL Employee System"}

# ------------------------------------------------------------
# ✅ CREATE EMPLOYEE
# ------------------------------------------------------------
@app.post("/employees")
def create_employee(emp: EmployeeSchema, db: Session = Depends(get_db)):

    existing = db.query(EmployeeTable).filter(EmployeeTable.emp_id == emp.emp_id).first()

    if existing:
        raise HTTPException(status_code=400, detail="Employee ID already exists")

    new_emp = EmployeeTable(
        emp_id=emp.emp_id,
        emp_name=emp.emp_name,
        emp_dprt=emp.emp_dprt,
        emp_dsgn=emp.emp_dsgn,
        emp_salary=emp.emp_salary
    )

    db.add(new_emp)
    db.commit()
    db.refresh(new_emp)

    return {"msg": "Employee Created", "data": new_emp}

# ------------------------------------------------------------
# ✅ READ ALL EMPLOYEES
# ------------------------------------------------------------
@app.get("/employees")
def get_all_employees(db: Session = Depends(get_db)):
    employees = db.query(EmployeeTable).all()
    return {"count": len(employees), "data": employees}

# ------------------------------------------------------------
# ✅ READ ONE EMPLOYEE
# ------------------------------------------------------------
@app.get("/employees/{emp_id}")
def get_employee(emp_id: int, db: Session = Depends(get_db)):

    emp = db.query(EmployeeTable).filter(EmployeeTable.emp_id == emp_id).first()

    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")

    return emp

# ------------------------------------------------------------
# ✅ UPDATE EMPLOYEE
# ------------------------------------------------------------
@app.put("/employees/{emp_id}")
def update_employee(emp_id: int, updated: EmployeeSchema, db: Session = Depends(get_db)):

    emp = db.query(EmployeeTable).filter(EmployeeTable.emp_id == emp_id).first()

    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")

    emp.emp_name = updated.emp_name
    emp.emp_dprt = updated.emp_dprt
    emp.emp_dsgn = updated.emp_dsgn
    emp.emp_salary = updated.emp_salary

    db.commit()
    db.refresh(emp)

    return {"msg": "Employee Updated", "data": emp}

# ------------------------------------------------------------
# ✅ DELETE EMPLOYEE
# ------------------------------------------------------------
@app.delete("/employees/{emp_id}")
def delete_employee(emp_id: int, db: Session = Depends(get_db)):

    emp = db.query(EmployeeTable).filter(EmployeeTable.emp_id == emp_id).first()

    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")

    db.delete(emp)
    db.commit()

    return {"msg": "Employee Deleted"}

# ------------------------------------------------------------
# ✅ MARK ATTENDANCE
# ------------------------------------------------------------
@app.post("/attendance/{emp_id}")
def mark_attendance(emp_id: int, db: Session = Depends(get_db)):

    emp = db.query(EmployeeTable).filter(EmployeeTable.emp_id == emp_id).first()

    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")

    attendance = AttendanceTable(
        emp_id=emp.emp_id,
        emp_name=emp.emp_name,
        status="Present"
    )

    db.add(attendance)
    db.commit()
    db.refresh(attendance)

    return {"msg": "Attendance Marked", "data": attendance}

# ------------------------------------------------------------
# Get Available Employees (Active = example)
# ------------------------------------------------------------
@app.get("/active-employees")
def active_employees(db: Session = Depends(get_db)):
    employees = db.query(EmployeeTable).all()
    return employees

# ------------------------------------------------------------
# Get All Attendance
# ------------------------------------------------------------
@app.get("/attendance")
def get_attendance(db: Session = Depends(get_db)):
    return db.query(AttendanceTable).all()

# ------------------------------------------------------------
# Search Employee
# ------------------------------------------------------------
@app.get("/search-employee/{name}")
def search_employee(name: str, db: Session = Depends(get_db)):

    employees = db.query(EmployeeTable).filter(
        EmployeeTable.emp_name.ilike(f"%{name}%")
    ).all()

    if not employees:
        raise HTTPException(status_code=404, detail="Employee not found")

    return employees
