import os

FILE_NAME = "students.txt"


def add_student():
    print("\n--- Add Student ---")
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    department = input("Enter Department: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{roll},{name},{age},{department}\n")

    print("Student record added successfully!\n")


def view_students():
    print("\n--- Student Records ---")

    if not os.path.exists(FILE_NAME) or os.path.getsize(FILE_NAME) == 0:
        print("No records found.\n")
        return

    with open(FILE_NAME, "r") as file:
        records = file.readlines()

    print("{:<10} {:<20} {:<10} {:<20}".format(
        "Roll", "Name", "Age", "Department"))
    print("-" * 60)

    for record in records:
        roll, name, age, department = record.strip().split(",")
        print("{:<10} {:<20} {:<10} {:<20}".format(
            roll, name, age, department))
    print()


def search_student():
    roll_no = input("Enter Roll Number to Search: ")

    found = False

    with open(FILE_NAME, "r") as file:
        for line in file:
            roll, name, age, department = line.strip().split(",")

            if roll == roll_no:
                print("\nStudent Found")
                print(f"Roll Number : {roll}")
                print(f"Name        : {name}")
                print(f"Age         : {age}")
                print(f"Department  : {department}")
                found = True
                break

    if not found:
        print("Student not found.\n")


def update_student():
    roll_no = input("Enter Roll Number to Update: ")

    updated_records = []
    found = False

    with open(FILE_NAME, "r") as file:
        for line in file:
            roll, name, age, department = line.strip().split(",")

            if roll == roll_no:
                print("Enter New Details")
                name = input("Name: ")
                age = input("Age: ")
                department = input("Department: ")
                found = True

            updated_records.append(f"{roll},{name},{age},{department}\n")

    with open(FILE_NAME, "w") as file:
        file.writelines(updated_records)

    if found:
        print("Record updated successfully!\n")
    else:
        print("Student not found.\n")


def delete_student():
    roll_no = input("Enter Roll Number to Delete: ")

    records = []
    found = False

    with open(FILE_NAME, "r") as file:
        for line in file:
            roll, name, age, department = line.strip().split(",")

            if roll != roll_no:
                records.append(line)
            else:
                found = True

    with open(FILE_NAME, "w") as file:
        file.writelines(records)

    if found:
        print("Record deleted successfully!\n")
    else:
        print("Student not found.\n")


while True:

    print("""
========= Student Record Management =========

1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit

============================================
""")

    choice = input("Enter your choice: ")

    try:
        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            print("Thank you!")
            break

        else:
            print("Invalid choice.")

    except FileNotFoundError:
        print("Students file not found!")

    except Exception as e:
        print("Error:", e)