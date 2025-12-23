students = {}   


def add_student():
    sid = input("Enter Student ID: ")

    if sid in students:
        print("Student ID already exists!")
        return

    name = input("Enter Student Name: ")
    grade = input("Enter Student Grade: ")

    students[sid] = {"name": name, "grade": grade}
    print("Student added successfully!")


def update_student():
    sid = input("Enter Student ID to update: ")

    if sid not in students:
        print("Student not found!")
        return

    name = input("Enter new name: ")
    grade = input("Enter new grade: ")

    students[sid]["name"] = name
    students[sid]["grade"] = grade
    print("Student updated successfully!")


def delete_student():
    sid = input("Enter Student ID to delete: ")

    if sid not in students:
        print("Student not found!")
        return

    del students[sid]
    print("Student deleted successfully!")


def list_students():
    if not students:
        print("No students available.")
        return

    print("\nID\tName\tGrade")
    print("--------------------")
    for sid, info in students.items():
        print(sid, info["name"], info["grade"])


def main():
    while True:
        print("\n--- STUDENT MANAGEMENT SYSTEM ---")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. List Students")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            update_student()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            list_students()
        elif choice == "5":
            print("Thank you! Goodbye.")
            break
        else:
            print("Invalid choice!")


main()
