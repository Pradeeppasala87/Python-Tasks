# =====================================================================
# IMPORT LIBRARY
# =====================================================================

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# =====================================================================
# CREATE APP
# =====================================================================

app = FastAPI()

# =====================================================================
# CREATE DATA MODEL (SCHEMA)
# =====================================================================

class Student(BaseModel):
    id: int
    name: str
    age: int
    course: str
    marks: int

# =====================================================================
# TEMPORARY DATABASE
# =====================================================================

lst = []

# =====================================================================
# CREATE STUDENT (POST)
# =====================================================================

@app.post("/students")
def create_student(stu: Student):

    lst.append(stu)

    return {
        "msg": "Student Added Successfully",
        "data": stu
    }

# =====================================================================
# GET ALL STUDENTS (GET)
# =====================================================================

@app.get("/students")
def get_all_students():

    return lst

# =====================================================================
# GET STUDENT BY ID (GET)
# =====================================================================

@app.get("/students/{stu_id}")
def get_student_by_id(stu_id: int):

    for stu in lst:

        if stu.id == stu_id:
            return stu

    raise HTTPException(
        status_code=404,
        detail=f"Student with ID {stu_id} not found"
    )

# =====================================================================
# UPDATE STUDENT (PUT)
# =====================================================================

@app.put("/students/{stu_id}")
def update_student(stu_id: int, updated_stu: Student):

    for index, stu in enumerate(lst):

        if stu.id == stu_id:

            lst[index] = updated_stu

            return {
                "msg": "Student Updated Successfully",
                "data": updated_stu
            }

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )

# =====================================================================
# DELETE STUDENT (DELETE)
# =====================================================================

@app.delete("/students/{stu_id}")
def delete_student(stu_id: int):

    for index, stu in enumerate(lst):

        if stu.id == stu_id:

            deleted_stu = lst.pop(index)

            return {
                "msg": "Student Deleted Successfully",
                "data": deleted_stu
            }

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )
