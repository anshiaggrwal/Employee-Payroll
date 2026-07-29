"""
==========================================================
File        : leave_service.py
Project     : Enterprise Employee Project and Payroll
              Management System
Description : Leave Service Module
==========================================================
"""

from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError

from database import get_session
from models.leave_model import LeaveRequest
from models.employee_model import Employee

from validations.validation import (
    validate_leave_days,
    validate_date
)

from utilities.logger_config import application, exception

from exceptions.custom_exception import (
    RecordNotFoundException,
    DatabaseException,
    ValidationException
)

def apply_leave():

    session = get_session()

    try:

        employee_id = int(input("Enter Employee ID : "))

        employee = session.get(Employee, employee_id)

        if employee is None:

            raise RecordNotFoundException(
                "Employee Not Found."
            )

        leave_date = validate_date(
            input("Enter Leave Date (YYYY-MM-DD) : ")
        )

        leave_days = validate_leave_days(
            input("Enter Number of Days : ")
        )

        reason = input("Enter Leave Reason : ")

        leave = LeaveRequest(

            employee_id=employee_id,

            leave_date=leave_date,

            leave_days=leave_days,

            reason=reason,

            status="Pending"

        )

        session.add(leave)

        session.commit()

        application("Leave Applied Successfully.")

        print("\nLeave Applied Successfully.")

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

def search_leave():

    session = get_session()

    try:

        employee_id = int(
            input("Enter Employee ID : ")
        )

        leaves = session.scalars(

            select(LeaveRequest).where(

                LeaveRequest.employee_id == employee_id

            )

        ).all()

        if not leaves:

            raise RecordNotFoundException(
                "Leave Record Not Found."
            )

        print("\nLeave Details")
        print("-" * 70)

        for leave in leaves:

            print(f"Leave ID : {leave.leave_id}")
            print(f"Date     : {leave.leave_date}")
            print(f"Days     : {leave.leave_days}")
            print(f"Reason   : {leave.reason}")
            print(f"Status   : {leave.status}")
            print("-" * 70)

    except Exception as e:

        print(e)

    finally:

        session.close()

def update_leave_status():

    session = get_session()

    try:

        leave_id = int(
            input("Enter Leave ID : ")
        )

        leave = session.get(
            LeaveRequest,
            leave_id
        )

        if leave is None:

            raise RecordNotFoundException(
                "Leave Record Not Found."
            )

        leave.status = input(
            "Enter Status (Approved/Rejected/Pending) : "
        ).title()

        session.commit()

        application(
            "Leave Status Updated Successfully."
        )

        print("\nLeave Status Updated Successfully.")

    except Exception as e:

        session.rollback()

        print(e)

    finally:

        session.close()

def delete_leave():

    session = get_session()

    try:

        leave_id = int(
            input("Enter Leave ID : ")
        )

        leave = session.get(
            LeaveRequest,
            leave_id
        )

        if leave is None:

            raise RecordNotFoundException(
                "Leave Record Not Found."
            )

        session.delete(leave)

        session.commit()

        application(
            "Leave Deleted Successfully."
        )

        print("\nLeave Deleted Successfully.")

    except Exception as e:

        session.rollback()

        print(e)

    finally:

        session.close()

def display_all_leaves():

    session = get_session()

    try:

        leaves = session.scalars(
            select(LeaveRequest)
        ).all()

        if not leaves:

            print("\nNo Leave Records Found.")

            return

        print("\nLeave Records")
        print("-" * 90)

        print(
            "{:<5} {:<10} {:<12} {:<8} {:<20} {:<12}".format(
                "ID",
                "Emp ID",
                "Date",
                "Days",
                "Reason",
                "Status"
            )
        )

        print("-" * 90)

        for leave in leaves:

            print(
                "{:<5} {:<10} {:<12} {:<8} {:<20} {:<12}".format(
                    leave.leave_id,
                    leave.employee_id,
                    str(leave.leave_date),
                    leave.leave_days,
                    leave.reason,
                    leave.status
                )
            )

    except SQLAlchemyError as e:

        exception(str(e))

        raise DatabaseException(
            "Database Error."
        )

    finally:

        session.close()