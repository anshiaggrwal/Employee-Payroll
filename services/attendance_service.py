from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from utilities.logger_config import (
    application_logger,
    exception_logger
)

from models.attendance_model import Attendance

from schemas.attendance_schema import (
    AttendanceCreate,
    AttendanceUpdate
)

from repositories.attendance_repository import (
    create_attendance,
    get_all_attendance,
    get_attendance_by_id,
    get_attendance_by_employee_and_month,
    update_attendance,
    delete_attendance
)

from repositories.employee_repository import (
    get_employee_by_id
)


def add_attendance(
    attendance: AttendanceCreate,
    db: Session
):
    try:

        employee = get_employee_by_id(
            attendance.employee_id,
            db
        )

        if employee is None:

            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Employee not found."
            )

        existing_attendance = (
            get_attendance_by_employee_and_month(
                attendance.employee_id,
                attendance.payroll_month,
                db
            )
        )

        if existing_attendance:

            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Attendance already exists for this payroll month."
            )

        new_attendance = Attendance(
            employee_id=attendance.employee_id,
            payroll_month=attendance.payroll_month,
            total_working_days=attendance.total_working_days,
            present_days=attendance.present_days,
            leave_days=attendance.leave_days,
            overtime_hours=attendance.overtime_hours,
            bonus_amount=attendance.bonus_amount
        )

        create_attendance(
            new_attendance,
            db
        )

        application_logger.info(
            f"Attendance created for Employee ID {attendance.employee_id}."
        )

        return new_attendance

    except HTTPException:
        raise

    except Exception as error:

        exception_logger.exception(error)

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Unable to create attendance."
        )


def fetch_all_attendance(
    db: Session
):
    try:

        return get_all_attendance(db)

    except Exception as error:

        exception_logger.exception(error)

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Unable to fetch attendance."
        )


def fetch_attendance(
    attendance_id: int,
    db: Session
):
    try:

        attendance = get_attendance_by_id(
            attendance_id,
            db
        )

        if attendance is None:

            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Attendance not found."
            )

        return attendance

    except HTTPException:
        raise

    except Exception as error:

        exception_logger.exception(error)

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Unable to fetch attendance."
        )


def modify_attendance(
    attendance_id: int,
    attendance: AttendanceUpdate,
    db: Session
):
    try:

        existing_attendance = get_attendance_by_id(
            attendance_id,
            db
        )

        if existing_attendance is None:

            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Attendance not found."
            )

        duplicate = get_attendance_by_employee_and_month(
            existing_attendance.employee_id,
            attendance.payroll_month,
            db
        )

        if (
            duplicate
            and
            duplicate.attendance_id != attendance_id
        ):

            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Attendance already exists for this payroll month."
            )

        existing_attendance.payroll_month = attendance.payroll_month
        existing_attendance.total_working_days = attendance.total_working_days
        existing_attendance.present_days = attendance.present_days
        existing_attendance.leave_days = attendance.leave_days
        existing_attendance.overtime_hours = attendance.overtime_hours
        existing_attendance.bonus_amount = attendance.bonus_amount

        update_attendance(db)

        application_logger.info(
            f"Attendance ID {attendance_id} updated successfully."
        )

        return existing_attendance

    except HTTPException:
        raise

    except Exception as error:

        exception_logger.exception(error)

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Unable to update attendance."
        )


def remove_attendance(
    attendance_id: int,
    db: Session
):
    try:

        attendance = get_attendance_by_id(
            attendance_id,
            db
        )

        if attendance is None:

            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Attendance not found."
            )

        delete_attendance(
            attendance,
            db
        )

        application_logger.info(
            f"Attendance ID {attendance_id} deleted successfully."
        )

        return {
            "message": "Attendance deleted successfully."
        }

    except HTTPException:
        raise

    except Exception as error:

        exception_logger.exception(error)

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Unable to delete attendance."
        )