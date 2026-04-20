import json
from Student import Student

FILE_NAME = "students.json"

def load_students():
    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)
            return [Student.from_dict(d) for d in data]
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump([s.to_dict() for s in students], file, indent=4)
