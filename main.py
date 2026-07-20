from operations import (
    add_employee,
    view_employees,
    search_employee_by_id,
    search_employee_by_name,
    update_employee,
    delete_employee
)


def get_employee_details():

    employee = {
        "employee_id": int(input("Enter Employee ID: ")),
        "name": input("Enter Employee Name: "),
        "age": int(input("Enter Age: ")),
        "phone_number": input("Enter Phone Number: "),
        "email": input("Enter Email: "),
        "department": input("Enter Department: "),
        "salary": float(input("Enter Salary: ")),
        "joining_date": input("Enter Joining Date (YYYY-MM-DD): "),
        "id_proof": input("Enter ID Proof: ")
    }

    return employee


while True:

    print("\n======================================")
    print("      Employee Management System")
    print("======================================")

    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        employee = get_employee_details()
        add_employee(employee)

    elif choice == "2":

        employees = view_employees()

        if len(employees) == 0:

            print("\nNo employee records found.")

        else:

            print("\n========== Employee Records ==========\n")

            for employee in employees:

                print(f"Employee ID   : {employee[0]}")
                print(f"Name          : {employee[1]}")
                print(f"Age           : {employee[2]}")
                print(f"Phone Number  : {employee[3]}")
                print(f"Email         : {employee[4]}")
                print(f"Department    : {employee[5]}")
                print(f"Salary        : {employee[6]}")
                print(f"Joining Date  : {employee[7]}")
                print(f"ID Proof      : {employee[8]}")
                print("--------------------------------------")

    elif choice == "3":

        print("\n========== Search Employee ==========")
        print("1. Search by Employee ID")
        print("2. Search by Employee Name")

        search_choice = input("Enter your choice: ")

        if search_choice == "1":

            employee_id = int(input("Enter Employee ID: "))

            employee = search_employee_by_id(employee_id)

            if employee:

                print("\n========== Employee Found ==========\n")

                print(f"Employee ID   : {employee[0]}")
                print(f"Name          : {employee[1]}")
                print(f"Age           : {employee[2]}")
                print(f"Phone Number  : {employee[3]}")
                print(f"Email         : {employee[4]}")
                print(f"Department    : {employee[5]}")
                print(f"Salary        : {employee[6]}")
                print(f"Joining Date  : {employee[7]}")
                print(f"ID Proof      : {employee[8]}")

            else:

                print("\n❌ Employee not found!")

        elif search_choice == "2":

            name = input("Enter Employee Name: ")

            employees = search_employee_by_name(name)

            if len(employees) == 0:

                print("\n❌ Employee not found!")

            else:

                print("\n========== Employee Found ==========\n")

                for employee in employees:

                    print(f"Employee ID   : {employee[0]}")
                    print(f"Name          : {employee[1]}")
                    print(f"Age           : {employee[2]}")
                    print(f"Phone Number  : {employee[3]}")
                    print(f"Email         : {employee[4]}")
                    print(f"Department    : {employee[5]}")
                    print(f"Salary        : {employee[6]}")
                    print(f"Joining Date  : {employee[7]}")
                    print(f"ID Proof      : {employee[8]}")
                    print("--------------------------------------")
    elif choice == "4":

        employee_id = int(input("Enter Employee ID to Update: "))

        employee = search_employee_by_id(employee_id)

        if employee:

            print("\n========== Current Employee Details ==========")

            print(f"Name          : {employee[1]}")
            print(f"Age           : {employee[2]}")
            print(f"Phone Number  : {employee[3]}")
            print(f"Email         : {employee[4]}")
            print(f"Department    : {employee[5]}")
            print(f"Salary        : {employee[6]}")
            print(f"Joining Date  : {employee[7]}")
            print(f"ID Proof      : {employee[8]}")

            print("\nEnter New Employee Details")

            name = input("Enter New Name: ")
            age = int(input("Enter New Age: "))
            phone_number = input("Enter New Phone Number: ")
            email = input("Enter New Email: ")
            department = input("Enter New Department: ")
            salary = float(input("Enter New Salary: "))
            joining_date = input("Enter New Joining Date (YYYY-MM-DD): ")
            id_proof = input("Enter New ID Proof: ")

            update_employee(
                employee_id,
                name,
                age,
                phone_number,
                email,
                department,
                salary,
                joining_date,
                id_proof
            )

        else:

            print("\n❌ Employee not found!")

    elif choice == "5":

        employee_id = int(input("Enter Employee ID to Delete: "))

        employee = search_employee_by_id(employee_id)

        if employee:

            print("\nEmployee Found")
            print("-------------------------")
            print(f"Employee ID : {employee[0]}")
            print(f"Name        : {employee[1]}")

            confirm = input("\nAre you sure you want to delete? (yes/no): ")

            if confirm.lower() == "yes":

                delete_employee(employee_id)

            else:

                print("\nDelete operation cancelled.")

        else:

            print("\n❌ Employee not found!")

    elif choice == "6":

        print("\nThank you for using Employee Management System.")
        break

    else:

        print("\n❌ Invalid Choice! Please try again.")