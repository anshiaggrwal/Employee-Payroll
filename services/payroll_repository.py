"""
==========================================================
File        : payroll_service.py
Project     : Enterprise Employee Project and Payroll
              Management System
Description : Payroll Service Module
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
    RecordNotFoundException,
    DatabaseException,
    ValidationException
)

def generate_payroll():

    session = get_session()

    try:

        employee_id = int(input("Enter Employee ID : "))

        employee = session.get(Employee, employee_id)

        if employee is None:

            raise RecordNotFoundException(
                "Employee Not Found."
            )

        basic_salary = validate_salary(
            input("Enter Basic Salary : ")
        )

        bonus = float(input("Enter Bonus : "))

        deduction = float(input("Enter Deduction : "))

        net_salary = basic_salary + bonus - deduction

        payroll = Payroll(

            employee_id=employee_id,

            basic_salary=basic_salary,

            bonus=bonus,

            deduction=deduction,

            net_salary=net_salary

        )

        session.add(payroll)

        session.commit()

        application("Payroll Generated Successfully.")

        print("\nPayroll Generated Successfully.")

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

def search_payroll():

    session = get_session()

    try:

        employee_id = int(
            input("Enter Employee ID : ")
        )

        payroll = session.scalar(

            select(Payroll).where(

                Payroll.employee_id == employee_id

            )

        )

        if payroll is None:

            raise RecordNotFoundException(
                "Payroll Record Not Found."
            )

        print("\nPayroll Details")
        print("-" * 50)

        print(f"Payroll ID     : {payroll.payroll_id}")
        print(f"Employee ID    : {payroll.employee_id}")
        print(f"Basic Salary   : {payroll.basic_salary}")
        print(f"Bonus          : {payroll.bonus}")
        print(f"Deduction      : {payroll.deduction}")
        print(f"Net Salary     : {payroll.net_salary}")

    except Exception as e:

        print(e)

    finally:

        session.close()

def update_payroll():

    session = get_session()

    try:

        payroll_id = int(
            input("Enter Payroll ID : ")
        )

        payroll = session.get(
            Payroll,
            payroll_id
        )

        if payroll is None:

            raise RecordNotFoundException(
                "Payroll Record Not Found."
            )

        payroll.basic_salary = validate_salary(
            input("Enter New Basic Salary : ")
        )

        payroll.bonus = float(
            input("Enter New Bonus : ")
        )

        payroll.deduction = float(
            input("Enter New Deduction : ")
        )

        payroll.net_salary = (
            payroll.basic_salary
            + payroll.bonus
            - payroll.deduction
        )

        session.commit()

        application(
            "Payroll Updated Successfully."
        )

        print("\nPayroll Updated Successfully.")

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

def delete_payroll():

    session = get_session()

    try:

        payroll_id = int(
            input("Enter Payroll ID : ")
        )

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

        print("\nPayroll Deleted Successfully.")

    except Exception as e:

        session.rollback()

        print(e)

    finally:

        session.close()

def display_all_payrolls():

    session = get_session()

    try:

        payrolls = session.scalars(
            select(Payroll)
        ).all()

        if not payrolls:

            print("\nNo Payroll Records Found.")

            return

        print("\nPayroll Records")
        print("-" * 90)

        print(
            "{:<5} {:<10} {:<12} {:<10} {:<12} {:<12}".format(
                "ID",
                "Emp ID",
                "Basic",
                "Bonus",
                "Deduction",
                "Net Salary"
            )
        )

        print("-" * 90)

        for payroll in payrolls:

            print(
                "{:<5} {:<10} {:<12} {:<10} {:<12} {:<12}".format(
                    payroll.payroll_id,
                    payroll.employee_id,
                    payroll.basic_salary,
                    payroll.bonus,
                    payroll.deduction,
                    payroll.net_salary
                )
            )

    except SQLAlchemyError as e:

        exception(str(e))

        raise DatabaseException(
            "Database Error."
        )

    finally:

        session.close()