# Employee Management System

A simple **Employee Management System** developed using **Python** and **SQLite**. This project allows users to perform complete CRUD (Create, Read, Update, Delete) operations through a menu-driven interface.

---

## 🚀 Features

- ✅ Add Employee
- ✅ View All Employees
- ✅ Search Employee by ID
- ✅ Search Employee by Name
- ✅ Update Employee Details
- ✅ Delete Employee
- ✅ Menu-Driven Application

---

## 🛠️ Technologies Used

- Python 3
- SQLite
- Git
- GitHub
- VS Code

---

## 📁 Project Structure

```
Employee-Management-System/
│
├── main.py
├── operations.py
├── database.py
├── employee.db
├── README.md
└── .gitignore
```

---

## 🗄️ Database Schema

The `employees` table contains the following fields:

| Column | Data Type |
|---------|-----------|
| employee_id | INTEGER (Primary Key) |
| name | TEXT |
| age | INTEGER |
| phone_number | TEXT |
| email | TEXT |
| department | TEXT |
| salary | REAL |
| joining_date | TEXT |
| id_proof | TEXT |

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/Vijaykumar36-c/Employee-Management-System.git
```

### 2. Open the project

Open the project folder in **VS Code**.

### 3. Create the database

```bash
python database.py
```

### 4. Run the application

```bash
python main.py
```

---

## 📋 Application Menu

```
======================================
      Employee Management System
======================================

1. Add Employee
2. View Employees
3. Search Employee
4. Update Employee
5. Delete Employee
6. Exit
```

---

## 📚 Concepts Learned

### Python
- Functions
- Dictionaries
- Loops
- Conditional Statements
- Modular Programming

### SQL
- CREATE TABLE
- INSERT
- SELECT
- UPDATE
- DELETE
- WHERE Clause

### SQLite
- Database Connection
- Cursor
- execute()
- fetchone()
- fetchall()
- commit()
- close()

### Git & GitHub
- git init
- git status
- git add
- git commit
- git push

---

## 🔮 Future Improvements

- Input Validation
- Exception Handling
- Export Employee Data to Excel
- Login Authentication
- Graphical User Interface (Tkinter)
- Search with Partial Name Matching
- Better Table Formatting

---

## 👨‍💻 Author

**C Vijay Kumar**

GitHub: https://github.com/Vijaykumar36-c

---

## ⭐ Version

**Employee Management System v1.0**