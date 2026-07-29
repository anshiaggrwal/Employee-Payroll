"""
==========================================================
File        : attendance_service.py
Project     : Enterprise Employee Project and Payroll
              Management System
Description : Attendance Service Module
==========================================================
"""

from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError

from database import get_session
from models.attendance_model import Attendance
from models.employee_model import Employee

from validations.validation import (
    validate_attendance_status,
    validate_date
)

from utilities.logger_config import application, exception

from exceptions.custom_exception import (
    RecordNotFoundException,
    DatabaseException,
    ValidationException
)


def mark_attendance():

    session = get_session()

    try:

        employee_id = int(input("Enter Employee ID : "))

        employee = session.get(Employee, employee_id)

        if employee is None:

            raise RecordNotFoundException(
                "Employee Not Found."
            )

        attendance_date = validate_date(
            input("Enter Date (YYYY-MM-DD) : ")
        )

        status = validate_attendance_status(
            input("Enter Status (P/A/L) : ")
        )

        attendance = Attendance(

            employee_id=employee_id,

            attendance_date=attendance_date,

            status=status

        )

        session.add(attendance)

        session.commit()

        application("Attendance Marked Successfully.")

        print("\nAttendance Marked Successfully.")

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

def search_attendance():

    session = get_session()

    try:

        employee_id = int(
            input("Enter Employee ID : ")
        )

        records = session.scalars(

            select(Attendance).where(

                Attendance.employee_id == employee_id

            )

        ).all()

        if not records:

            raise RecordNotFoundException(
                "Attendance Record Not Found."
            )

        print("\nAttendance Details")
        print("-" * 45)

        for record in records:

            print(

                f"Date   : {record.attendance_date}"

            )

            print(

                f"Status : {record.status}"

            )

            print("-" * 45)

    except Exception as e:

        print(e)

    finally:

        session.close()

def update_attendance():

    session = get_session()

    try:

        attendance_id = int(
            input("Enter Attendance ID : ")
        )

        attendance = session.get(
            Attendance,
            attendance_id
        )

        if attendance is None:

            raise RecordNotFoundException(
                "Attendance Record Not Found."
            )

        attendance.status = validate_attendance_status(

            input("Enter New Status (P/A/L) : ")

        )

        session.commit()

        application(
            "Attendance Updated Successfully."
        )

        print("\nAttendance Updated Successfully.")

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

def delete_attendance():

    session = get_session()

    try:

        attendance_id = int(
            input("Enter Attendance ID : ")
        )

        attendance = session.get(
            Attendance,
            attendance_id
        )

        if attendance is None:

            raise RecordNotFoundException(
                "Attendance Record Not Found."
            )

        session.delete(attendance)

        session.commit()

        application(
            "Attendance Deleted Successfully."
        )

        print("\nAttendance Deleted Successfully.")

    except Exception as e:

        session.rollback()

        print(e)

    finally:

        session.close()

def display_all_attendance():

    session = get_session()

    try:

        records = session.scalars(
            select(Attendance)
        ).all()

        if not records:

            print("\nNo Attendance Records Found.")

            return

        print("\nAttendance Records")
        print("-" * 70)

        print(
            "{:<5} {:<10} {:<15} {:<10}".format(
                "ID",
                "Emp ID",
                "Date",
                "Status"
            )
        )

        print("-" * 70)

        for record in records:

            print(
                "{:<5} {:<10} {:<15} {:<10}".format(
                    record.attendance_id,
                    record.employee_id,
                    str(record.attendance_date),
                    record.status
                )
            )

    except SQLAlchemyError as e:

        exception(str(e))

        raise DatabaseException(
            "Database Error."
        )

    finally:

        session.close()