# ======================================================================================
# 📝 FastAPI TODO App - MongoDB Atlas + MongoEngine
# ======================================================================================

from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from mongoengine import connect, Document, IntField, StringField, FloatField

# ------------------------------------------------------------
# 🚀 Create FastAPI Application
# ------------------------------------------------------------
app = FastAPI()

# ------------------------------------------------------------
# 🌐 MongoDB Atlas Connection
# ------------------------------------------------------------
MONGO_URL = "mongodb+srv://kumarp37509_db_user:<db_password>@cluster0.mtmes7q.mongodb.net/student_db?retryWrites=true&w=majority"
'''
mongodb+srv://username:password@clustername.xxxxx.mongodb.net/todo_db?retryWrites=true&w=majority
│              │        │        │                              │
│              │        │        │                              └── Database name
│              │        │        └──────────────────────────────── Cluster URL
│              │        └───────────────────────────────────────── Password
│              └────────────────────────────────────────────────── Username
└───────────────────────────────────────────────────────────────── MongoDB protocol
'''
connect(host=MONGO_URL)
'''
engine=create_engine(MONGO_URL)
Sessionlocal=sessionmaker(bind=engine)
Base=declarative_base()
'''
# ------------------------------------------------------------
# 🧱 MongoDB Model (Like SQLAlchemy Model)
# ------------------------------------------------------------
class Students_DB(Document):
    
    id= IntField(primary_key=True)
    name= StringField(required=True)
    age= IntField(required=True)
    Course= StringField(required=True)
    marks= FloatField(required=True)
    
    meta={"collection":"Students"}

    
# ------------------------------------------------------------
# 🧾 Pydantic Schema
# ------------------------------------------------------------
class std(BaseModel):
    id: int
    name: str
    age: int
    Course: str
    marks: float

# ------------------------------------------------------------
# 🏠 Home Route
# ------------------------------------------------------------

@app.get("/")
def home():
    return {"message":"FastAPI + MongoDB Atlas 🚀"}


# ------------------------------------------------------------
# ✅ 1. Add Student Data
# ------------------------------------------------------------
@app.post("/Students")
def add_std(s_info :std):
    
    existing=Students_DB.objects(id=s_info.id).first()
    
    if existing:
                raise HTTPException(status_code=400, detail="ID already exists")
    
    new_std=Students_DB(
        id=s_info.id,
        name= s_info.name,
        age= s_info.age,
        Course= s_info.Course,
        marks= s_info.marks
    )
    new_std.save()

    return {"message":"Student Data Added","data":s_info}

# ------------------------------------------------------------
# ✅ 2. READ ALL Students Data
# ------------------------------------------------------------
@app.get("/Students")
def display_all_std():
    Students=Students_DB.objects()
    
    data=[]
    for st in Students:
        data.append({
            "id":st.id,
            "name":st.name,
            "age":st.age,
            "Course":st.Course,
            "marks":st.marks
        })
    
    return {"count":len(data),"data":data}


# ------------------------------------------------------------
# ✅ 3. READ SINGLE Student Data
# ------------------------------------------------------------
@app.get("/Students/{S_id}")
def std_by_id(S_id:int):
    
    s_info=Students_DB.objects(id=S_id).first()
    
    if not s_info:
        raise HTTPException(status_code=404, detail="ID not found")
    return {
        "id":s_info.id,
        "name":s_info.name,
        "age":s_info.age,
        "Course":s_info.Course,
        "marks":s_info.marks
    }

# ------------------------------------------------------------
# ✅ 4. UPDATE TODO
# ------------------------------------------------------------
@app.put("/Students/{S_id}")
def update_stu(S_id:int,updated:std):
    
    s_info = Students_DB.objects(id=S_id).first()
    
    if not s_info:
        raise HTTPException(status_code=404, detail="Student not found")
    
    s_info.name=updated.name
    s_info.age=updated.age
    s_info.Course=updated.Course
    s_info.marks=updated.marks
    
    s_info.save()
    
    return {"message": "Student data updated successfully"}

# ------------------------------------------------------------
# ✅ 5. DELETE Student
# ------------------------------------------------------------
@app.delete("/Students/{S_id}")
def del_stu(S_id:int):
    
    s_info=Students_DB.objects(id=S_id).first()
    
    if not s_info:
        raise HTTPException(status_code=404, detail="Student not found")

    s_info.delete()

    return {"message":"Student Data Deleted Successfully"}
