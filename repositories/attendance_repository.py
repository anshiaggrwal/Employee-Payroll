from sqlalchemy.orm import Session

from models.attendance_model import Attendance


def create_attendance(
    attendance: Attendance,
    db: Session
):
    db.add(attendance)
    db.commit()
    db.refresh(attendance)

    return attendance


def get_all_attendance(
    db: Session
):
    return db.query(Attendance).all()


def get_attendance_by_id(
    attendance_id: int,
    db: Session
):
    return db.query(Attendance).filter(
        Attendance.attendance_id == attendance_id
    ).first()


def get_attendance_by_employee_and_month(
    employee_id: int,
    payroll_month: str,
    db: Session
):
    return db.query(Attendance).filter(
        Attendance.employee_id == employee_id,
        Attendance.payroll_month == payroll_month
    ).first()


def update_attendance(
    db: Session
):
    db.commit()


def delete_attendance(
    attendance: Attendance,
    db: Session
):
    db.delete(attendance)
    db.commit()