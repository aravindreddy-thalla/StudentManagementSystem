from Student import Student
from student_manager import StudentManager
from exceptions import *
def main():
    manager = StudentManager()
    while True:
        try:
            print("\n--- Student Management System ---")
            print("1. Add Student")
            print("2. View Students")
            print("3. Update Student")
            print("4. Delete Student")
            print("5. Exit")
            choice = int(input("Enter choice:"))
            if choice == 1:
                sid = int(input("Enter ID: "))
                name = input("Enter Name: ")
                age = int(input("Enter Age: "))
                course = input("Enter Course: ")
                manager.add_student(Student(sid, name, age, course))
                print("Student added")
            elif choice == 2:
                manager.view_students()
            elif choice == 3:
                sid = int(input("Enter ID to update: "))
                name = input("Enter New Name: ")
                age = int(input("Enter New Age: "))
                course = input("Enter New Course: ")
                manager.update_student(sid, name, age, course)
                print("Student updated")
            elif choice == 4:
                sid = int(input("Enter ID to delete: "))
                manager.delete_student(sid)
                print("Student deleted")
            elif choice == 5:
                print("Exiting...")
                break
            else:
               print("Invalid choice")
        except ValueError:
            print("Please enter valid numbers")
        except (StudentNotFoundException, DuplicateStudentException) as e:
            print(f"{e}")
        except Exception as e:
            print("Unexpected error:", e)
if __name__ == "__main__":
    main()