import sqlite3


def get_connection():
    connection = sqlite3.connect("employee.db")
    cursor = connection.cursor()
    return connection, cursor


def add_employee(employee):

    connection, cursor = get_connection()

    cursor.execute("""
    INSERT INTO employees(
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

    connection, cursor = get_connection()

    cursor.execute("SELECT * FROM employees")

    employees = cursor.fetchall()

    connection.close()

    return employees


def search_employee_by_id(employee_id):

    connection, cursor = get_connection()

    cursor.execute(
        "SELECT * FROM employees WHERE employee_id = ?",
        (employee_id,)
    )

    employee = cursor.fetchone()

    connection.close()

    return employee


def search_employee_by_name(name):

    connection, cursor = get_connection()

    cursor.execute(
        "SELECT * FROM employees WHERE name = ?",
        (name,)
    )

    employees = cursor.fetchall()

    connection.close()

    return employees


def update_employee(
    employee_id,
    name,
    age,
    phone_number,
    email,
    department,
    salary,
    joining_date,
    id_proof
):

    connection, cursor = get_connection()

    cursor.execute("""
    UPDATE employees
    SET
        name = ?,
        age = ?,
        phone_number = ?,
        email = ?,
        department = ?,
        salary = ?,
        joining_date = ?,
        id_proof = ?
    WHERE employee_id = ?
    """, (
        name,
        age,
        phone_number,
        email,
        department,
        salary,
        joining_date,
        id_proof,
        employee_id
    ))

    connection.commit()

    if cursor.rowcount > 0:
        print("\n✅ Employee updated successfully!")
    else:
        print("\n❌ Employee ID not found!")

    connection.close()


def delete_employee(employee_id):

    connection, cursor = get_connection()

    cursor.execute(
        "DELETE FROM employees WHERE employee_id = ?",
        (employee_id,)
    )

    connection.commit()

    if cursor.rowcount > 0:
        print("\n✅ Employee deleted successfully!")
    else:
        print("\n❌ Employee ID not found!")

    connection.close()