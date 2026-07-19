import sqlite3


def add_employee(employee):
    connection = sqlite3.connect("employee.db")
    cursor = connection.cursor()

    cursor.execute("""
    INSERT INTO employees (
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
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        employee["employee_id"],
        employee["name"],
        employee["age"],
        employee["phone_number"],
        employee["email"],
        employee["department"],
        employee["salary"],
        employee["joining_date"],
        employee["id_proof"]
    ))

    connection.commit()
    connection.close()

    print("\n✅ Employee added successfully!")


def view_employees():
    connection = sqlite3.connect("employee.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM employees")

    employees = cursor.fetchall()

    connection.close()

    return employees