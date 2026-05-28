# ============================================================
# IMPORTS
# ============================================================

from flask import Flask, render_template, request, redirect, url_for, session
import requests

# ============================================================
# FLASK APP
# ============================================================

app = Flask(__name__)
app.secret_key = "hrms_secret_key"

# ============================================================
# FASTAPI BACKEND URL
# ============================================================

FASTAPI_URL = "http://127.0.0.1:8000"

# Mock Data Fallbacks (used if backend is down)
MOCK_EMPLOYEES = [
    {"id": 1, "name": "John Doe", "email": "john@company.com", "phone": "123-456", "designation": "Software Engineer", "department_id": 1},
    {"id": 2, "name": "Jane Smith", "email": "jane@company.com", "phone": "987-654", "designation": "HR Manager", "department_id": 2}
]
MOCK_DEPARTMENTS = [
    {"id": 1, "name": "Engineering", "location": "New York"},
    {"id": 2, "name": "Human Resources", "location": "Chicago"}
]
MOCK_ATTENDANCE = [
    {"id": 1, "employee_id": 1, "date": "2026-05-28", "status": "Present"},
    {"id": 2, "employee_id": 2, "date": "2026-05-28", "status": "Leave"}
]
MOCK_SALARY = [
    {"id": 1, "employee_id": 1, "salary": 85000, "bonus": 5000},
    {"id": 2, "employee_id": 2, "salary": 75000, "bonus": 3000}
]

def safe_get(endpoint, default_data):
    try:
        response = requests.get(f"{FASTAPI_URL}/{endpoint}", timeout=2)
        if response.status_code == 200:
            return response.json()
    except:
        pass
    return default_data

@app.route("/")
def home():
    return redirect(url_for("login"))

# ============================================================
# LOGIN PAGE
# ============================================================

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Default login: admin / admin
        if username == "admin" and password == "admin":
            session["employee_name"] = "Admin User"
            session["designation"] = "Admin"
            session["department_id"] = 1
            return redirect(url_for("dashboard"))

        return render_template("auth/login.html", error="Invalid Username or Password. Try admin/admin")

    return render_template("auth/login.html", error=None)

# ============================================================
# DASHBOARD HOME
# ============================================================

@app.route("/dashboard")
def dashboard():
    if "employee_name" not in session:
        return redirect(url_for("login"))

    employees = safe_get("employees", MOCK_EMPLOYEES)
    departments = safe_get("departments", MOCK_DEPARTMENTS)
    attendance = safe_get("attendance", MOCK_ATTENDANCE)
    salaries = safe_get("salary", MOCK_SALARY)

    return render_template(
        "dashboard/index.html",
        employees=employees,
        departments=departments,
        attendance=attendance,
        salaries=salaries,
        employee_name=session.get("employee_name"),
        designation=session.get("designation")
    )

# ============================================================
# EMPLOYEES PAGE
# ============================================================

@app.route("/employees")
def employees():
    if "employee_name" not in session:
        return redirect(url_for("login"))

    employees_list = safe_get("employees", MOCK_EMPLOYEES)
    departments = safe_get("departments", MOCK_DEPARTMENTS)

    return render_template(
        "employees/employees.html",
        employees=employees_list,
        departments=departments
    )

@app.route("/add-employee", methods=["GET", "POST"])
def add_employee():
    departments = safe_get("departments", MOCK_DEPARTMENTS)

    if request.method == "POST":
        employee_data = {
            "name": request.form["name"],
            "age": int(request.form["age"]),
            "email": request.form["email"],
            "phone": request.form["phone"],
            "designation": request.form["designation"],
            "department_id": int(request.form["department_id"])
        }
        try:
            res = requests.post(f"{FASTAPI_URL}/employees", json=employee_data, timeout=2)
            if res.status_code != 200:
                raise Exception("Backend failed")
        except:
            # Fallback: manually add to mock data so UI updates
            new_id = len(MOCK_EMPLOYEES) + 1
            employee_data["id"] = new_id
            MOCK_EMPLOYEES.append(employee_data)
            
            # Auto-generate salary and attendance for the new employee
            MOCK_SALARY.append({
                "id": len(MOCK_SALARY) + 1,
                "employee_id": new_id,
                "salary": 60000,  # Default base salary
                "bonus": 0
            })
            from datetime import date
            MOCK_ATTENDANCE.append({
                "id": len(MOCK_ATTENDANCE) + 1,
                "employee_id": new_id,
                "date": str(date.today()),
                "status": "Present"
            })
            
        return redirect(url_for("employees"))

    return render_template("employees/add_employee.html", departments=departments)

@app.route("/delete-employee/<int:employee_id>")
def delete_employee(employee_id):
    try:
        res = requests.delete(f"{FASTAPI_URL}/employees/{employee_id}", timeout=2)
        if res.status_code != 200:
            raise Exception("Backend failed")
    except:
        global MOCK_EMPLOYEES
        MOCK_EMPLOYEES = [e for e in MOCK_EMPLOYEES if e["id"] != employee_id]
    return redirect(url_for("employees"))

@app.route("/update-employee/<int:employee_id>", methods=["GET", "POST"])
def update_employee(employee_id):
    if "employee_name" not in session:
        return redirect(url_for("login"))

    departments = safe_get("departments", MOCK_DEPARTMENTS)
    employees_data = safe_get("employees", MOCK_EMPLOYEES)
    employee = next((emp for emp in employees_data if emp["id"] == employee_id), None)

    if not employee:
        return "Employee Not Found"

    if request.method == "POST":
        update_data = {
            "name": request.form["name"],
            "age": int(request.form["age"]),
            "email": request.form["email"],
            "phone": request.form["phone"],
            "designation": request.form["designation"],
            "department_id": int(request.form["department_id"])
        }
        try:
            res = requests.put(f"{FASTAPI_URL}/employees/{employee_id}", json=update_data, timeout=2)
            if res.status_code != 200:
                raise Exception("Backend failed")
        except:
            for i, emp in enumerate(MOCK_EMPLOYEES):
                if emp["id"] == employee_id:
                    update_data["id"] = employee_id
                    MOCK_EMPLOYEES[i] = update_data
                    break
        return redirect(url_for("employees"))

    return render_template("employees/update_employee.html", employee=employee, departments=departments)

# ============================================================
# ATTENDANCE PAGE
# ============================================================

@app.route("/attendance")
def attendance():
    if "employee_name" not in session:
        return redirect(url_for("login"))

    selected_date = request.args.get("selected_date")
    attendance_data = safe_get("attendance", MOCK_ATTENDANCE)
    employees_data = safe_get("employees", MOCK_EMPLOYEES)

    filtered_attendance = []
    
    for emp in employees_data:
        emp_att = next((r for r in attendance_data if r["employee_id"] == emp["id"] and (not selected_date or r["date"] == selected_date)), None)
        if emp_att:
            filtered_attendance.append({
                "employee_name": emp["name"],
                "status": emp_att["status"],
                "date": emp_att["date"]
            })
        else:
            filtered_attendance.append({
                "employee_name": emp["name"],
                "status": "not marked",
                "date": selected_date if selected_date else "N/A"
            })

    present_count = len([r for r in filtered_attendance if r["status"].lower() == "present"])
    absent_count = len([r for r in filtered_attendance if r["status"].lower() == "absent"])
    leave_count = len([r for r in filtered_attendance if r["status"].lower() == "leave"])

    return render_template(
        "attendance/attendance.html",
        attendance=filtered_attendance,
        present_count=present_count,
        absent_count=absent_count,
        leave_count=leave_count,
        selected_date=selected_date
    )

# ============================================================
# PAYROLL PAGE
# ============================================================

@app.route("/payroll")
def payroll():
    if "employee_name" not in session:
        return redirect(url_for("login"))

    salaries = safe_get("salary", MOCK_SALARY)
    employees_data = safe_get("employees", MOCK_EMPLOYEES)
    
    return render_template(
        "salary/payroll.html",
        salaries=salaries,
        employees=employees_data
    )

# ============================================================
# ANALYTICS PAGE
# ============================================================

@app.route("/analytics")
def analytics():
    if "employee_name" not in session:
        return redirect(url_for("login"))

    employees_data = safe_get("employees", MOCK_EMPLOYEES)
    departments = safe_get("departments", MOCK_DEPARTMENTS)
    attendance = safe_get("attendance", MOCK_ATTENDANCE)
    salaries = safe_get("salary", MOCK_SALARY)

    department_labels = [dept["name"] for dept in departments]
    department_counts = [len([emp for emp in employees_data if emp["department_id"] == dept["id"]]) for dept in departments]

    present_count = len([a for a in attendance if a["status"].lower() == "present"])
    absent_count = len([a for a in attendance if a["status"].lower() == "absent"])
    leave_count = len([a for a in attendance if a["status"].lower() == "leave"])

    salary_labels = []
    salary_values = []
    for dept in departments:
        dept_employees = [emp["id"] for emp in employees_data if emp["department_id"] == dept["id"]]
        dept_salaries = [sal["salary"] for sal in salaries if sal["employee_id"] in dept_employees]
        avg_salary = sum(dept_salaries) / len(dept_salaries) if dept_salaries else 0
        salary_labels.append(dept["name"])
        salary_values.append(avg_salary)

    return render_template(
        "analytics/analytics.html",
        department_labels=department_labels,
        department_counts=department_counts,
        present_count=present_count,
        absent_count=absent_count,
        leave_count=leave_count,
        salary_labels=salary_labels,
        salary_values=salary_values
    )

# ============================================================
# SEARCH EMPLOYEE
# ============================================================

@app.route("/search")
def search():
    query = request.args.get("query")
    if not query:
        return redirect(url_for("employees"))

    try:
        employees_data = requests.get(f"{FASTAPI_URL}/search-employee/{query}", timeout=2).json()
    except:
        employees_data = [e for e in MOCK_EMPLOYEES if query.lower() in e["name"].lower()]

    return render_template("employees/employees.html", employees=employees_data, departments=safe_get("departments", MOCK_DEPARTMENTS))

# ============================================================
# EMPLOYEE PROFILE PAGE
# ============================================================

@app.route("/employee/<int:employee_id>")
def employee_profile(employee_id):
    if "employee_name" not in session:
        return redirect(url_for("login"))

    employees_data = safe_get("employees", MOCK_EMPLOYEES)
    employee = next((emp for emp in employees_data if emp["id"] == employee_id), None)

    if not employee:
        return "Employee Not Found"

    employee["experience"] = "4 Years"
    employee["performance"] = 92
    employee["attendance_score"] = 96
    employee["productivity"] = 89
    employee["manager"] = "Robert Williams"
    employee["skills"] = ["Python", "SQL", "FastAPI", "Flask", "Leadership"]
    employee["tasks"] = [
        {"task": "API Development", "status": "Completed", "hours": 5},
        {"task": "Dashboard UI", "status": "In Progress", "hours": 3},
        {"task": "Attendance Module", "status": "Pending", "hours": 2},
        {"task": "Analytics Charts", "status": "Completed", "hours": 4}
    ]

    return render_template("employees/profile.html", employee=employee)

# ============================================================
# LOGOUT
# ============================================================

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True, port=5000)
