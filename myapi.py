from fastapi import FastAPI, HTTPException, status, Path
from typing import Union
from pydantic import BaseModel
from typing import Optional, TypeVar

app = FastAPI()

students = {
    1: {
        "name": "Osama",
        "age": 24,
        "year": "3" 
    }
}

class Student(BaseModel):
    name: str
    age: int
    year: str


class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year : Optional[str] = None


def check():
    raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail= "Invalid authentication credentials" 
    )

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/get-student/{student_id}")
def get_student(student_id:int):
    try:
        return students[student_id]
    except:
        raise Exception("value not found")
    
@app.get("/get-student")
def get_student(name:str = None):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {
        "Data": "Not Found"
    }


@app.post("/create-student/{student_id}")
def create_student(student_id:int, student: Student):
    if student_id in students:
        return {"Error": "Already Exists"}
    
    students[student_id] = student
    return students[student_id]


@app.put("/update-student/{student_id}")
def update_student(student_id:int, student: UpdateStudent):
    if student_id not in students:
        return {"Error": "Not Exist"}
    
    if student.name !=None:
        students[student_id].name = student.name

    if student.age !=None:
        students[student_id].age = student.age
    
    if student.year !=None:
        students[student_id].year = student.year
    return students[student_id]
