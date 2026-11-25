from fastapi import FastAPI, HTTPException

app = FastAPI()

students = [
    {"id": 1, "name": "Ali", "grades": [70, 85, 90]},
    {"id": 2, "name": "Aysel", "grades": [90, 95, 88]},
    {"id": 3, "name": "Murad", "grades": [60, 75, 80]},
    {"id": 4, "name": "Leyla", "grades": []},
]

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/students")
@app.get("/students")
def list_students(min_grade: int = 0):
    result = []

    for student in students:
        if student["grades"]:
            average = sum(student["grades"]) / len(student["grades"])

            if average >= min_grade:
                result.append(student)

    return result

@app.get("/students/{student_id}")
def get_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            return student

    raise HTTPException(status_code=404, detail="Student not found")