"""
==========================================================
File        : department_api_service.py
Project     : Enterprise Employee Project and Payroll
              Management System
Description : Department API Service Module
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


# =====================================================
# Add Department
# =====================================================

def add_department_api(department_name):

    session = get_session()

    try:

        department_name = validate_department_name(
            department_name
        )

        department = Department(
            department_name=department_name
        )

        session.add(department)

        session.commit()

        session.refresh(department)

        application(
            "Department Added Successfully."
        )

        return department

    except ValidationException:

        session.rollback()

        raise

    except IntegrityError:

        session.rollback()

        raise DatabaseException(
            "Department Already Exists."
        )

    except SQLAlchemyError as e:

        session.rollback()

        exception(str(e))

        raise DatabaseException(
            "Database Error."
        )

    finally:

        session.close()


# =====================================================
# Search Department
# =====================================================

def search_department_api(department_id):

    session = get_session()

    try:

        department = session.get(
            Department,
            department_id
        )

        if department is None:

            raise RecordNotFoundException(
                "Department Not Found."
            )

        return department

    except SQLAlchemyError as e:

        exception(str(e))

        raise DatabaseException(
            "Database Error."
        )

    finally:

        session.close()


# =====================================================
# Display All Departments
# =====================================================

def display_all_departments_api():

    session = get_session()

    try:

        departments = session.scalars(
            select(Department)
        ).all()

        return departments

    except SQLAlchemyError as e:

        exception(str(e))

        raise DatabaseException(
            "Database Error."
        )

    finally:

        session.close()


# =====================================================
# Update Department
# =====================================================

def update_department_api(
        department_id,
        department_name
):

    session = get_session()

    try:

        department = session.get(
            Department,
            department_id
        )

        if department is None:

            raise RecordNotFoundException(
                "Department Not Found."
            )

        department.department_name = validate_department_name(
            department_name
        )

        session.commit()

        session.refresh(department)

        application(
            "Department Updated Successfully."
        )

        return department

    except ValidationException:

        session.rollback()

        raise

    except IntegrityError:

        session.rollback()

        raise DatabaseException(
            "Department Already Exists."
        )

    except SQLAlchemyError as e:

        session.rollback()

        exception(str(e))

        raise DatabaseException(
            "Database Error."
        )

    finally:

        session.close()


# =====================================================
# Delete Department
# =====================================================

def delete_department_api(department_id):

    session = get_session()

    try:

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

        application(
            "Department Deleted Successfully."
        )

        return {
            "message":
                "Department Deleted Successfully."
        }

    except SQLAlchemyError as e:

        session.rollback()

        exception(str(e))

        raise DatabaseException(
            "Database Error."
        )

    finally:

        session.close()