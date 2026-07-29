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


# -----------------------------
# Add Employee
# -----------------------------
def add_employee_api(name, age, email, phone):

    session = get_session()

    try:

        name = validate_employee_name(name)
        age = validate_age(age)
        email = validate_email(email)
        phone = validate_phone(phone)

        employee = Employee(
            employee_name=name,
            age=age,
            email=email,
            phone=phone,
            status="ACTIVE"
        )

        session.add(employee)
        session.commit()
        session.refresh(employee)

        application(f"Employee Added : {name}")

        return employee

    except ValidationException:
        session.rollback()
        raise

    except IntegrityError:

        session.rollback()

        raise DatabaseException(
            "Email or Phone already exists."
        )

    except SQLAlchemyError as e:

        session.rollback()

        exception(str(e))

        raise DatabaseException(
            "Database Error."
        )

    finally:

        session.close()


# -----------------------------
# Search Employee
# -----------------------------
def search_employee_api(employee_id):

    session = get_session()

    try:

        employee = session.get(Employee, employee_id)

        if employee is None:

            raise RecordNotFoundException(
                "Employee Not Found."
            )

        return employee

    except SQLAlchemyError as e:

        exception(str(e))

        raise DatabaseException(
            "Database Error."
        )

    finally:

        session.close()


# -----------------------------
# Display All Employees
# -----------------------------
def display_all_employees_api():

    session = get_session()

    try:

        employees = session.scalars(
            select(Employee)
        ).all()

        return employees

    except SQLAlchemyError as e:

        exception(str(e))

        raise DatabaseException(
            "Database Error."
        )

    finally:

        session.close()


# -----------------------------
# Update Employee
# -----------------------------
def update_employee_api(
        employee_id,
        name,
        age,
        email,
        phone
):

    session = get_session()

    try:

        employee = session.get(Employee, employee_id)

        if employee is None:

            raise RecordNotFoundException(
                "Employee Not Found."
            )

        employee.employee_name = validate_employee_name(name)
        employee.age = validate_age(age)
        employee.email = validate_email(email)
        employee.phone = validate_phone(phone)

        session.commit()
        session.refresh(employee)

        application(
            f"Employee Updated : {employee_id}"
        )

        return employee

    except ValidationException:

        session.rollback()
        raise

    except IntegrityError:

        session.rollback()

        raise DatabaseException(
            "Email or Phone already exists."
        )

    except SQLAlchemyError as e:

        session.rollback()

        exception(str(e))

        raise DatabaseException(
            "Database Error."
        )

    finally:

        session.close()


# -----------------------------
# Delete Employee
# -----------------------------
def delete_employee_api(employee_id):

    session = get_session()

    try:

        employee = session.get(Employee, employee_id)

        if employee is None:

            raise RecordNotFoundException(
                "Employee Not Found."
            )

        session.delete(employee)
        session.commit()

        application(
            f"Employee Deleted : {employee_id}"
        )

        return {
            "message": "Employee Deleted Successfully"
        }

    except SQLAlchemyError as e:

        session.rollback()

        exception(str(e))

        raise DatabaseException(
            "Database Error."
        )

    finally:

        session.close()