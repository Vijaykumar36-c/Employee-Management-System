from operations import add_employee, view_employees


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

    print("\n===================================")
    print("   Employee Management System")
    print("===================================")

    print("1. Add Employee")
    print("2. View Employees")
    print("3. Exit")

    choice = input("Enter your choice: ")

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
        print("\nThank you for using Employee Management System.")
        break

    else:
        print("\nInvalid choice! Please try again.")