"""
==========================================================
File        : payroll_api_service.py
Project     : Enterprise Employee Project and Payroll
              Management System
Description : Payroll API Service Module
==========================================================
"""

from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError

from database import get_session

from models.payroll_model import Payroll
from models.employee_model import Employee

from validations.validation import validate_salary

from utilities.logger_config import application, exception

from exceptions.custom_exception import (
    ValidationException,
    RecordNotFoundException,
    DatabaseException
)


# =====================================================
# Generate Payroll
# =====================================================

def generate_payroll_api(
        employee_id,
        basic_salary,
        bonus,
        deduction
):

    session = get_session()

    try:

        employee = session.get(
            Employee,
            employee_id
        )

        if employee is None:

            raise RecordNotFoundException(
                "Employee Not Found."
            )

        basic_salary = validate_salary(
            basic_salary
        )

        bonus = float(bonus)

        deduction = float(deduction)

        net_salary = (
            basic_salary
            + bonus
            - deduction
        )

        payroll = Payroll(

            employee_id=employee_id,

            basic_salary=basic_salary,

            bonus=bonus,

            deduction=deduction,

            net_salary=net_salary

        )

        session.add(payroll)

        session.commit()

        session.refresh(payroll)

        application(
            "Payroll Generated Successfully."
        )

        return payroll

    except ValidationException:

        session.rollback()

        raise

    except SQLAlchemyError as e:

        session.rollback()

        exception(str(e))

        raise DatabaseException(
            "Database Error."
        )

    finally:

        session.close()


# =====================================================
# Search Payroll
# =====================================================

def search_payroll_api(employee_id):

    session = get_session()

    try:

        payroll = session.scalar(

            select(Payroll).where(

                Payroll.employee_id == employee_id

            )

        )

        if payroll is None:

            raise RecordNotFoundException(
                "Payroll Record Not Found."
            )

        return payroll

    except SQLAlchemyError as e:

        exception(str(e))

        raise DatabaseException(
            "Database Error."
        )

    finally:

        session.close()


# =====================================================
# Update Payroll
# =====================================================

def update_payroll_api(
        payroll_id,
        basic_salary,
        bonus,
        deduction
):

    session = get_session()

    try:

        payroll = session.get(
            Payroll,
            payroll_id
        )

        if payroll is None:

            raise RecordNotFoundException(
                "Payroll Record Not Found."
            )

        payroll.basic_salary = validate_salary(
            basic_salary
        )

        payroll.bonus = float(bonus)

        payroll.deduction = float(deduction)

        payroll.net_salary = (

            payroll.basic_salary

            + payroll.bonus

            - payroll.deduction

        )

        session.commit()

        session.refresh(payroll)

        application(
            "Payroll Updated Successfully."
        )

        return payroll

    except ValidationException:

        session.rollback()

        raise

    except SQLAlchemyError as e:

        session.rollback()

        exception(str(e))

        raise DatabaseException(
            "Database Error."
        )

    finally:

        session.close()


# =====================================================
# Delete Payroll
# =====================================================

def delete_payroll_api(payroll_id):

    session = get_session()

    try:

        payroll = session.get(
            Payroll,
            payroll_id
        )

        if payroll is None:

            raise RecordNotFoundException(
                "Payroll Record Not Found."
            )

        session.delete(payroll)

        session.commit()

        application(
            "Payroll Deleted Successfully."
        )

        return {

            "message":
                "Payroll Deleted Successfully."

        }

    except SQLAlchemyError as e:

        session.rollback()

        exception(str(e))

        raise DatabaseException(
            "Database Error."
        )

    finally:

        session.close()


# =====================================================
# Display All Payrolls
# =====================================================

def display_all_payrolls_api():

    session = get_session()

    try:

        payrolls = session.scalars(

            select(Payroll)

        ).all()

        return payrolls

    except SQLAlchemyError as e:

        exception(str(e))

        raise DatabaseException(
            "Database Error."
        )

    finally:

        session.close()