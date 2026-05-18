from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from mongoengine import connect, Document, IntField, StringField

# ------------------------------------------------------------
# 🚀 App
# ------------------------------------------------------------
app = FastAPI()

# ------------------------------------------------------------
# 🗄️ MongoDB Configuration
# ------------------------------------------------------------
url = "mongodb+srv://pasalapradeep145_db_user:mangodb123@cluster0.d8tfhym.mongodb.net/?appName=Cluster0"
connect(host=url)

# ------------------------------------------------------------
# 🧱 Employee Table (MongoDB Collection)
# ------------------------------------------------------------
class EmployeeTable(Document):
    employee_id = IntField(primary_key=True)
    full_name = StringField(required=True)
    department = StringField(required=True)
    job_title = StringField(required=True)
    email = StringField(required=True)
    salary = IntField(required=True)

    meta = {
        "collection": "Employees"
    }

# ------------------------------------------------------------
# 🧾 Schema (Pydantic)
# ------------------------------------------------------------
class EmployeeSchema(BaseModel):
    employee_id: int
    full_name: str
    department: str
    job_title: str
    email: str
    salary: int

# ------------------------------------------------------------
# 🏠 Home
# ------------------------------------------------------------
@app.get("/")
def home():
    return {"msg": "FastAPI + MongoDB Employee System 🚀"}

# ------------------------------------------------------------
# ✅ CREATE EMPLOYEE
# ------------------------------------------------------------
@app.post("/employees")
def create_employee(emp: EmployeeSchema):
    existing = EmployeeTable.objects(employee_id=emp.employee_id).first()
    if existing:
        raise HTTPException(status_code=400, detail="Employee ID already exists")

    new_emp = EmployeeTable(
        employee_id=emp.employee_id,
        full_name=emp.full_name,
        department=emp.department,
        job_title=emp.job_title,
        email=emp.email,
        salary=emp.salary
    )
    new_emp.save()

    return {"msg": "Employee Created", "data": emp.dict()}

# ------------------------------------------------------------
# ✅ READ ALL EMPLOYEES
# ------------------------------------------------------------
@app.get("/employees")
def get_all_employees():
    employees = EmployeeTable.objects()
    data = []

    for emp in employees:
        data.append({
            "employee_id": emp.employee_id,
            "full_name": emp.full_name,
            "department": emp.department,
            "job_title": emp.job_title,
            "email": emp.email,
            "salary": emp.salary
        })

    return {"count": len(data), "data": data}

# ------------------------------------------------------------
# ✅ READ ONE EMPLOYEE
# ------------------------------------------------------------
@app.get("/employees/{employee_id}")
def get_employee(employee_id: int):
    emp = EmployeeTable.objects(employee_id=employee_id).first()
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")

    return {
        "employee_id": emp.employee_id,
        "full_name": emp.full_name,
        "department": emp.department,
        "job_title": emp.job_title,
        "email": emp.email,
        "salary": emp.salary
    }

# ------------------------------------------------------------
# ✅ UPDATE EMPLOYEE
# ------------------------------------------------------------
@app.put("/employees/{employee_id}")
def update_employee(employee_id: int, updated: EmployeeSchema):
    emp = EmployeeTable.objects(employee_id=employee_id).first()
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")

    emp.full_name = updated.full_name
    emp.department = updated.department
    emp.job_title = updated.job_title
    emp.email = updated.email
    emp.salary = updated.salary
    emp.save()

    return {"msg": "Employee Updated", "data": updated.dict()}

# ------------------------------------------------------------
# ✅ DELETE EMPLOYEE
# ------------------------------------------------------------
@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int):
    emp = EmployeeTable.objects(employee_id=employee_id).first()
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")

    emp.delete()
    return {"msg": "Employee Deleted"}

# ------------------------------------------------------------
# 📊 SEARCH EMPLOYEE BY NAME
# ------------------------------------------------------------
@app.get("/search-employee/{name}")
def search_employee(name: str):
    employees = EmployeeTable.objects(full_name__icontains=name)

    data = []
    for emp in employees:
        data.append({
            "employee_id": emp.employee_id,
            "full_name": emp.full_name,
            "department": emp.department,
            "job_title": emp.job_title,
            "email": emp.email,
            "salary": emp.salary
        })

    if not data:
        raise HTTPException(status_code=404, detail="No employee found")

    return {"count": len(data), "data": data}
