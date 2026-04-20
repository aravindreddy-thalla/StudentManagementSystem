from exceptions import StudentNotFoundException, DuplicateStudentException
from file_util import load_students, save_students

class StudentManager:
    def __init__(self):
        self.students = load_students()

    def add_student(self, student):
        for s in self.students:
            if s.student_id == student.student_id:
                raise DuplicateStudentException("Student ID already exists")
        self.students.append(student)
        save_students(self.students)

    def view_students(self):
        if not self.students:
            print("No students available")
        for student in self.students:
            print(student)

    def find_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        raise StudentNotFoundException("Student not found")

    def update_student(self, student_id, name, age, course):
        student = self.find_student(student_id)
        student.name = name
        student.age = age
        student.course = course
        save_students(self.students)

    def delete_student(self, student_id):
        student = self.find_student(student_id)
        self.students.remove(student)
        save_students(self.students)
