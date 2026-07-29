"""
==========================================================
File        : report_service.py
Project     : Enterprise Employee Project and Payroll
              Management System
Description : Report Service Module
==========================================================
"""

from sqlalchemy import select, func
from sqlalchemy.exc import SQLAlchemyError

from database import get_session
from models.employee_model import Employee
from models.department_model import Department
from models.project_model import Project
from models.payroll_model import Payroll

from utilities.logger_config import application, exception

from exceptions.custom_exception import (
    DatabaseException
)

def employee_report():

    session = get_session()

    try:

        employees = session.scalars(
            select(Employee)
        ).all()

        print("\nEmployee Report")
        print("-" * 80)

        print(
            "{:<5} {:<20} {:<20} {:<10}".format(
                "ID",
                "Name",
                "Email",
                "Status"
            )
        )

        print("-" * 80)

        for employee in employees:

            print(
                "{:<5} {:<20} {:<20} {:<10}".format(
                    employee.employee_id,
                    employee.employee_name,
                    employee.email,
                    employee.status
                )
            )

    except SQLAlchemyError as e:

        exception(str(e))

        raise DatabaseException(
            "Unable to Generate Employee Report."
        )

    finally:

        session.close()

def department_report():

    session = get_session()

    try:

        departments = session.scalars(
            select(Department)
        ).all()

        print("\nDepartment Report")
        print("-" * 50)

        for department in departments:

            print(
                department.department_id,
                department.department_name
            )

    except SQLAlchemyError as e:

        exception(str(e))

        raise DatabaseException(
            "Unable to Generate Department Report."
        )

    finally:

        session.close()

def project_report():

    session = get_session()

    try:

        projects = session.scalars(
            select(Project)
        ).all()

        print("\nProject Report")
        print("-" * 90)

        print(
            "{:<5} {:<20} {:<12} {:<12}".format(
                "ID",
                "Project Name",
                "Budget",
                "Status"
            )
        )

        print("-" * 90)

        for project in projects:

            print(
                "{:<5} {:<20} {:<12} {:<12}".format(
                    project.project_id,
                    project.project_name,
                    project.project_budget,
                    project.status
                )
            )

    except SQLAlchemyError as e:

        exception(str(e))

        raise DatabaseException(
            "Unable to Generate Project Report."
        )

    finally:

        session.close()

def payroll_report():

    session = get_session()

    try:

        payrolls = session.scalars(
            select(Payroll)
        ).all()

        print("\nPayroll Report")
        print("-" * 90)

        print(
            "{:<5} {:<10} {:<12} {:<10} {:<12}".format(
                "ID",
                "Emp ID",
                "Basic",
                "Bonus",
                "Net Salary"
            )
        )

        print("-" * 90)

        for payroll in payrolls:

            print(
                "{:<5} {:<10} {:<12} {:<10} {:<12}".format(
                    payroll.payroll_id,
                    payroll.employee_id,
                    payroll.basic_salary,
                    payroll.bonus,
                    payroll.net_salary
                )
            )

    except SQLAlchemyError as e:

        exception(str(e))

        raise DatabaseException(
            "Unable to Generate Payroll Report."
        )

    finally:

        session.close()

def dashboard_report():

    session = get_session()

    try:

        total_employees = session.scalar(
            select(func.count(Employee.employee_id))
        )

        total_departments = session.scalar(
            select(func.count(Department.department_id))
        )

        total_projects = session.scalar(
            select(func.count(Project.project_id))
        )

        total_payrolls = session.scalar(
            select(func.count(Payroll.payroll_id))
        )

        print("\nDashboard Report")
        print("=" * 40)

        print(f"Total Employees   : {total_employees}")
        print(f"Total Departments : {total_departments}")
        print(f"Total Projects    : {total_projects}")
        print(f"Total Payrolls    : {total_payrolls}")

        print("=" * 40)

        application("Dashboard Report Generated.")

    except SQLAlchemyError as e:

        exception(str(e))

        raise DatabaseException(
            "Unable to Generate Dashboard Report."
        )

    finally:

        session.close()