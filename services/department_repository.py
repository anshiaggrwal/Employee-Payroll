"""
==========================================================
File        : department_service.py
Project     : Enterprise Employee Project and Payroll
              Management System
Description : Department Service Module
==========================================================
"""

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from database import get_session
from models.department_model import Department

from validations.validation import validate_department_name

from utilities.logger_config import application, exception

from exceptions.custom_exception import (
    ValidationException,
    RecordNotFoundException,
    DatabaseException
)

def add_department():

    session = get_session()

    try:

        department_name = validate_department_name(

            input("Enter Department Name : ")

        )

        department = Department(

            department_name=department_name

        )

        session.add(department)

        session.commit()

        application("Department Added Successfully.")

        print("\nDepartment Added Successfully.")

    except ValidationException as e:

        session.rollback()

        print(e)

    except IntegrityError:

        session.rollback()

        print("Department Already Exists.")

    except SQLAlchemyError as e:

        session.rollback()

        exception(str(e))

        raise DatabaseException(
            "Database Error."
        )

    finally:

        session.close()

def search_department():

    session = get_session()

    try:

        department_id = int(

            input("Enter Department ID : ")

        )

        department = session.get(

            Department,
            department_id

        )

        if department is None:

            raise RecordNotFoundException(

                "Department Not Found."

            )

        print("\nDepartment Details")

        print("-" * 40)

        print(f"Department ID   : {department.department_id}")

        print(f"Department Name : {department.department_name}")

    except Exception as e:

        print(e)

    finally:

        session.close()

def update_department():

    session = get_session()

    try:

        department_id = int(

            input("Enter Department ID : ")

        )

        department = session.get(

            Department,
            department_id

        )

        if department is None:

            raise RecordNotFoundException(

                "Department Not Found."

            )

        department.department_name = validate_department_name(

            input("Enter New Department Name : ")

        )

        session.commit()

        application("Department Updated Successfully.")

        print("\nDepartment Updated Successfully.")

    except ValidationException as e:

        session.rollback()

        print(e)

    except SQLAlchemyError as e:

        session.rollback()

        exception(str(e))

        raise DatabaseException(
            "Database Error."
        )

    finally:

        session.close()

def delete_department():

    session = get_session()

    try:

        department_id = int(

            input("Enter Department ID : ")

        )

        department = session.get(

            Department,
            department_id

        )

        if department is None:

            raise RecordNotFoundException(

                "Department Not Found."

            )

        session.delete(department)

        session.commit()

        application("Department Deleted Successfully.")

        print("\nDepartment Deleted Successfully.")

    except Exception as e:

        session.rollback()

        print(e)

    finally:

        session.close()

def display_all_departments():

    session = get_session()

    try:

        departments = session.scalars(

            select(Department)

        ).all()

        if not departments:

            print("\nNo Departments Found.")

            return

        print("\nDepartment List")

        print("-" * 40)

        for department in departments:

            print(

                department.department_id,
                department.department_name

            )

    except Exception as e:

        print(e)

    finally:

        session.close()