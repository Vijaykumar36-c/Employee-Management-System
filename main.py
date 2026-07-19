from operations import add_employee

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

print("===================================")
print("   Employee Management System")
print("===================================")

employee = get_employee_details()
add_employee(employee)