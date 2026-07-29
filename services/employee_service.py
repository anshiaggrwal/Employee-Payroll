from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from utilities.logger_config import (
    application_logger,
    exception_logger
)

from models.employee_model import Employee
from models.department_model import Department

from schemas.employee_schema import (
    EmployeeCreate,
    EmployeeUpdate
)

from repositories.employee_repository import (
    create_employee,
    get_all_employees,
    get_employee_by_id,
    get_employee_by_email,
    update_employee,
    delete_employee
)


def add_employee(
    employee: EmployeeCreate,
    db: Session
):
    try:

        existing_employee = get_employee_by_id(
            employee.employee_id,
            db
        )

        if existing_employee:

            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Employee ID already exists."
            )

        existing_email = get_employee_by_email(
            employee.email,
            db
        )

        if existing_email:

            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already exists."
            )

        department = db.query(Department).filter(
            Department.department_id == employee.department_id
        ).first()

        if department is None:

            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Department not found."
            )

        new_employee = Employee(
            employee_id=employee.employee_id,
            employee_name=employee.employee_name,
            email=employee.email,
            department_id=employee.department_id,
            designation=employee.designation,
            date_of_joining=employee.date_of_joining,
            basic_salary=employee.basic_salary,
            employment_status=employee.employment_status
        )

        create_employee(
            new_employee,
            db
        )

        application_logger.info(
            f"Employee '{employee.employee_name}' created successfully."
        )

        return new_employee

    except HTTPException:
        raise

    except Exception as error:

        exception_logger.exception(error)

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Unable to create employee."
        )


def fetch_all_employees(
    db: Session
):
    try:

        return get_all_employees(db)

    except Exception as error:

        exception_logger.exception(error)

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Unable to fetch employees."
        )


def fetch_employee(
    employee_id: int,
    db: Session
):
    try:

        employee = get_employee_by_id(
            employee_id,
            db
        )

        if employee is None:

            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Employee not found."
            )

        return employee

    except HTTPException:
        raise

    except Exception as error:

        exception_logger.exception(error)

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Unable to fetch employee."
        )


def modify_employee(
    employee_id: int,
    employee: EmployeeUpdate,
    db: Session
):
    try:

        existing_employee = get_employee_by_id(
            employee_id,
            db
        )

        if existing_employee is None:

            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Employee not found."
            )

        existing_email = get_employee_by_email(
            employee.email,
            db
        )

        if (
            existing_email
            and
            existing_email.employee_id != employee_id
        ):

            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already exists."
            )

        department = db.query(Department).filter(
            Department.department_id == employee.department_id
        ).first()

        if department is None:

            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Department not found."
            )

        existing_employee.employee_name = employee.employee_name
        existing_employee.email = employee.email
        existing_employee.department_id = employee.department_id
        existing_employee.designation = employee.designation
        existing_employee.date_of_joining = employee.date_of_joining
        existing_employee.basic_salary = employee.basic_salary
        existing_employee.employment_status = employee.employment_status

        update_employee(db)

        application_logger.info(
            f"Employee ID {employee_id} updated successfully."
        )

        return existing_employee

    except HTTPException:
        raise

    except Exception as error:

        exception_logger.exception(error)

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Unable to update employee."
        )


def remove_employee(
    employee_id: int,
    db: Session
):
    try:

        employee = get_employee_by_id(
            employee_id,
            db
        )

        if employee is None:

            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Employee not found."
            )

        delete_employee(
            employee,
            db
        )

        application_logger.info(
            f"Employee ID {employee_id} deleted successfully."
        )

        return {
            "message": "Employee deleted successfully."
        }

    except HTTPException:
        raise

    except Exception as error:

        exception_logger.exception(error)

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Unable to delete employee."
        )