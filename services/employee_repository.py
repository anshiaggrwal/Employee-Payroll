
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from database import get_session
from models.employee_model import Employee
from validations.validation import (
    validate_employee_name,
    validate_age,
    validate_email,
    validate_phone
)
from utilities.logger_config import application, exception
from exceptions.custom_exception import (
    ValidationException,
    RecordNotFoundException,
    DatabaseException
)

def add_employee(name, age, email, phone):

    session = get_session()

    try:

        name = validate_employee_name(input("Enter Name : "))
        age = validate_age(input("Enter Age : "))
        email = validate_email(input("Enter Email : "))
        phone = validate_phone(input("Enter Phone : "))

        employee = Employee(
            employee_name=name,
            age=age,
            email=email,
            phone=phone,
            status="ACTIVE"
        )

        session.add(employee)
        session.commit()

        application(f"Employee Added : {name}")
        print("\nEmployee Added Successfully.")

    except ValidationException as e:

        session.rollback()
        print(e)

    except IntegrityError:

        session.rollback()
        print("Email or Phone already exists.")

    except SQLAlchemyError as e:

        session.rollback()
        exception(str(e))
        raise DatabaseException("Database Error.")

    finally:

        session.close()

def search_employee(employee_id):

    session = get_session()

    try:

        employee_id = int(input("Enter Employee ID : "))

        employee = session.get(Employee, employee_id)

        if employee is None:
            raise RecordNotFoundException(
                "Employee Not Found."
            )

        print("\nEmployee Details")
        print("-" * 40)
        print(f"ID     : {employee.employee_id}")
        print(f"Name   : {employee.employee_name}")
        print(f"Age    : {employee.age}")
        print(f"Email  : {employee.email}")
        print(f"Phone  : {employee.phone}")
        print(f"Status : {employee.status}")

    except Exception as e:

        print(e)

    finally:

        session.close()

def update_employee(employee_id, name, age):

    session = get_session()

    try:

        employee_id = int(input("Enter Employee ID : "))

        employee = session.get(Employee, employee_id)

        if employee is None:
            raise RecordNotFoundException(
                "Employee Not Found."
            )

        employee.employee_name = validate_employee_name(
            input("Enter New Name : ")
        )

        employee.age = validate_age(
            input("Enter New Age : ")
        )

        session.commit()

        application("Employee Updated")
        print("Employee Updated Successfully.")

    except Exception as e:

        session.rollback()
        print(e)

    finally:

        session.close()

def delete_employee(employee_id):

    session = get_session()

    try:

        employee_id = int(input("Enter Employee ID : "))

        employee = session.get(Employee, employee_id)

        if employee is None:
            raise RecordNotFoundException(
                "Employee Not Found."
            )

        session.delete(employee)
        session.commit()

        application("Employee Deleted")
        print("Employee Deleted Successfully.")

    except Exception as e:

        session.rollback()
        print(e)

    finally:

        session.close()

def display_all_employees():

    session = get_session()

    try:

        employees = session.scalars(
            select(Employee)
        ).all()

        if not employees:

            print("No Employees Found.")
            return

        print("\nEmployee List")
        print("-" * 80)

        for emp in employees:

            print(
                emp.employee_id,
                emp.employee_name,
                emp.age,
                emp.email,
                emp.phone,
                emp.status
            )

    except Exception as e:

        print(e)

    finally:

        session.close()