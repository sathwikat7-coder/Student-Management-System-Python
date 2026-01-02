import os

FILE_NAME = "students.txt"

def load_students():
    students = {}
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                student_id, name, course = line.strip().split(",")
                students[student_id] = {"Name": name, "Course": course}
    return students

def save_students(students):
    with open(FILE_NAME, "w") as file:
        for id, details in students.items():
            file.write(f"{id},{details['Name']},{details['Course']}\n")

def add_student(students):
    student_id = input("Enter Student ID: ")
    if student_id in students:
        print("Student ID already exists!\n")
        return
    name = input("Enter Student Name: ")
    course = input("Enter Course: ")
    students[student_id] = {"Name": name, "Course": course}
    save_students(students)
    print("Student added successfully!\n")

def view_students(students):
    if not students:
        print("No students found.\n")
    else:
        print("\n--- Student List ---")
        for id, details in students.items():
            print(f"ID: {id} | Name: {details['Name']} | Course: {details['Course']}")
        print()

def update_student(students):
    student_id = input("Enter Student ID to update: ")
    if student_id in students:
        students[student_id]["Name"] = input("Enter new name: ")
        students[student_id]["Course"] = input("Enter new course: ")
        save_students(students)
        print("Student updated successfully!\n")
    else:
        print("Student not found.\n")

def delete_student(students):
    student_id = input("Enter Student ID to delete: ")
    if student_id in students:
        del students[student_id]
        save_students(students)
        print("Student deleted successfully!\n")
    else:
        print("Student not found.\n")

students = load_students()

while True:
    print("==== Student Management System ====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student(students)
    elif choice == "2":
        view_students(students)
    elif choice == "3":
        update_student(students)
    elif choice == "4":
        delete_student(students)
    elif choice == "5":
        print("Thank you! Exiting...")
        break
    else:
        print("Invalid choice. Try again.\n")

