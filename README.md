# Enterprise Employee Payroll System Using SQLAlchemy ORM

## 📌 Project Overview

The **Enterprise Employee Payroll System Using SQLAlchemy ORM** is a Python-based console application developed to automate employee and payroll management within an organization. The project uses **SQLAlchemy ORM** for database operations and **MySQL** as the backend database.

The system follows a modular architecture with separate layers for models, services, validations, exceptions, utilities, and logging, making it easy to maintain and extend.

---

## 🚀 Features

- Employee Management (CRUD)
- Department Management (CRUD)
- Role Management
- Attendance Management
- Leave Management
- Project Management
- Employee Project Assignment
- Task Management
- Salary Management
- Payroll Generation
- Dashboard Reports
- Data Validation
- Custom Exception Handling
- Daily Log File Generation
- SQLAlchemy ORM Integration
- MySQL Database Connectivity

---

## 🛠️ Technologies Used

- Python 3.12+
- SQLAlchemy ORM
- MySQL
- PyMySQL
- Tabulate
- Object-Oriented Programming (OOP)

---

## 📂 Project Structure

```
Enterprise_Employee_Payroll_System/
│
├── models/
│   ├── employee_model.py
│   ├── department_model.py
│   ├── role_model.py
│   ├── attendance_model.py
│   ├── leave_model.py
│   ├── project_model.py
│   ├── employee_project_model.py
│   ├── task_model.py
│   ├── salary_model.py
│   └── payroll_model.py
│
├── services/
│   ├── employee_service.py
│   ├── department_service.py
│   ├── attendance_service.py
│   ├── leave_service.py
│   ├── project_service.py
│   ├── payroll_service.py
│   └── report_service.py
│
├── validations/
│   └── validation.py
│
├── exceptions/
│   └── custom_exception.py
│
├── utilities/
│   ├── logger_config.py
│   ├── input_helper.py
│   ├── report_generator.py
│   └── menu_helper.py
│
├── logs/
│
├── database.py
├── database_initializer.py
├── main.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/Enterprise_Employee_Payroll_System_Using_SQLAlchemyORM
```

```bash
cd Enterprise_Employee_Payroll_System_Using_SQLAlchemyORM
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🗄️ Create MySQL Database

Login to MySQL and create the database.

```sql
CREATE DATABASE employee_payroll_db;
```

---

## ⚙️ Configure Database

Update **database.py**

```python
DATABASE_URL = "mysql+pymysql://root:YOUR_PASSWORD@localhost:3306/employee_payroll_db"
```

> If your password contains special characters like `@`, replace it with `%40`.

Example:

```python
DATABASE_URL = "mysql+pymysql://root:Password%40123@localhost:3306/employee_payroll_db"
```

---

## ▶️ Run the Project

```bash
python main.py
```

---

## 📊 Database Tables

The project automatically creates the following tables:

- Departments
- Roles
- Employees
- Attendance
- Leave Requests
- Projects
- Employee Projects
- Tasks
- Salary Details
- Payroll

---

## 📋 Main Menu

```
==========================================
EMPLOYEE PAYROLL MANAGEMENT SYSTEM
==========================================

1. Employee Management
2. Department Management
3. Attendance Management
4. Leave Management
5. Project Management
6. Payroll Management
7. Reports
8. Exit
```

---

## 📑 Reports

The application provides:

- Employee Report
- Department Report
- Project Report
- Payroll Report
- Dashboard Report

---

## 📝 Logging

Daily log files are generated automatically.

```
logs/

application_YYYY-MM-DD.log
exception_YYYY-MM-DD.log
```

Example:

```
application_2026-07-23.log
exception_2026-07-23.log
```

---

## ✅ Validation Features

- Employee Name Validation
- Email Validation
- Phone Validation
- Salary Validation
- Department Validation
- Project Budget Validation
- Attendance Validation
- Leave Validation

---

## ⚠️ Exception Handling

The project includes custom exceptions for:

- Employee
- Department
- Attendance
- Leave
- Project
- Payroll
- Validation
- Database
- Duplicate Records
- Record Not Found

---

## 📌 Future Enhancements

- Graphical User Interface (GUI)
- Web Application using Flask or Django
- Authentication & Authorization
- Email Notifications
- REST API Integration
- PDF Report Generation
- Cloud Database Deployment

---

## 👨‍💻 Author

**Revanth Sai Bomma**

---

## 📄 License

This project is developed for educational and learning purposes.
