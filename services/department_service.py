from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from utilities.logger_config import (
    application_logger,
    exception_logger
)

from models.department_model import Department

from schemas.department_schema import (
    DepartmentCreate,
    DepartmentUpdate
)

from repositories.department_repository import (
    create_department,
    get_all_departments,
    get_department_by_id,
    get_department_by_name,
    update_department,
    delete_department
)


def add_department(
    department: DepartmentCreate,
    db: Session
):
    try:

        existing_department = get_department_by_name(
            department.department_name,
            db
        )

        if existing_department:

            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Department already exists."
            )

        new_department = Department(
            department_name=department.department_name
        )

        create_department(
            new_department,
            db
        )

        application_logger.info(
            f"Department '{department.department_name}' created successfully."
        )

        return new_department

    except HTTPException:
        raise

    except Exception as error:

        exception_logger.exception(error)

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Unable to create department."
        )


def fetch_all_departments(
    db: Session
):
    try:

        return get_all_departments(db)

    except Exception as error:

        exception_logger.exception(error)

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Unable to fetch departments."
        )


def fetch_department(
    department_id: int,
    db: Session
):
    try:

        department = get_department_by_id(
            department_id,
            db
        )

        if department is None:

            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Department not found."
            )

        return department

    except HTTPException:
        raise

    except Exception as error:

        exception_logger.exception(error)

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Unable to fetch department."
        )


def modify_department(
    department_id: int,
    department: DepartmentUpdate,
    db: Session
):
    try:

        existing_department = get_department_by_id(
            department_id,
            db
        )

        if existing_department is None:

            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Department not found."
            )

        duplicate_department = get_department_by_name(
            department.department_name,
            db
        )

        if (
            duplicate_department
            and
            duplicate_department.department_id != department_id
        ):

            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Department already exists."
            )

        existing_department.department_name = (
            department.department_name
        )

        update_department(db)

        application_logger.info(
            f"Department ID {department_id} updated successfully."
        )

        return existing_department

    except HTTPException:
        raise

    except Exception as error:

        exception_logger.exception(error)

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Unable to update department."
        )


def remove_department(
    department_id: int,
    db: Session
):
    try:

        department = get_department_by_id(
            department_id,
            db
        )

        if department is None:

            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Department not found."
            )

        delete_department(
            department,
            db
        )

        application_logger.info(
            f"Department ID {department_id} deleted successfully."
        )

        return {
            "message": "Department deleted successfully."
        }

    except HTTPException:
        raise

    except Exception as error:

        exception_logger.exception(error)

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Unable to delete department."
        )