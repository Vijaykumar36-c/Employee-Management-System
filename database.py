import sqlite3

connection = sqlite3.connect("employee.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees(
    employee_id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    phone_number TEXT,
    email TEXT UNIQUE,
    department TEXT,
    salary REAL,
    joining_date TEXT,
    id_proof TEXT
)
""")

connection.commit()
connection.close()

print("Database and Employee table created successfully!")