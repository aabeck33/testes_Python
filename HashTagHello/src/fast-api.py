from fastapi import FastAPI, HTTPException
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

students = [
    {'name': 'Student 1', 'age': 20},
    {'name': 'Student 2', 'age': 18},
    {'name': 'Student 3', 'age': 16}
]

# Model to Handle POST/UPDATE Request Body
class Student(BaseModel):
    name: str
    age: int

# Endpoint to List All Students or with filter  -  curl http://127.0.0.1:8000/students / curl "http://127.0.0.1:8000/students?min=16&max=18"
@app.get('/students')
def user_list(min: Optional[int] = None, max: Optional[int] = None):

    if min and max:

        filtered_students = list(
            filter(lambda student: max >= student['age'] >= min, students)
        )

        return {'students': filtered_students}

    return {'students': students}

# Endpoint to Fetch Single Student Object  -  curl http://127.0.0.1:8000/students/0
@app.get('/students/{student_id}')
def user_detail(student_id: int):
    student_check(student_id)
    return {'student': students[student_id]}

# Endpoint to Add New Student Object  -  curl -X 'POST' http://127.0.0.1:8000/students -H 'Content-Type: application/json' -d '{"name":"New Student", "age": 24}'
@app.post('/students')
def user_add(student: Student):
    students.append(student)

    return {'student': students[-1]}

# Endpoint to Update a Student Object  -  curl -X 'PUT' http://127.0.0.1:8000/students/0 -H 'Content-Type: application/json' -d '{"name":"Student X", "age": 18}'
@app.put('/students/{student_id}')
def user_update(student: Student, student_id: int):
    student_check(student_id)
    students[student_id].update(student)

    return {'student': students[student_id]}

# Endpoint to Delete a Student Object  -  curl -X 'DELETE' http://127.0.0.1:8000/students/0
@app.delete('/students/{student_id}')
def user_delete(student_id: int):
    student_check(student_id)
    del students[student_id]

    return {'students': students}

# Check if Student Object Exists
def student_check(student_id):
    if not students[student_id]:
        raise HTTPException(status_code=404, detail='Student Not Found')
