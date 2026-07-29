from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from schemas.attendance_schema import AttendanceCreate, AttendanceUpdate
from services.attendance_service import (
    add_attendance,
    fetch_all_attendance,
    fetch_attendance,
    modify_attendance,
    remove_attendance
)

attendance_router = APIRouter(
    prefix="/attendance",
    tags=["Attendance"]
)


@attendance_router.post("/")
def create_attendance(
    attendance: AttendanceCreate,
    db: Session = Depends(get_db)
):
    return add_attendance(attendance, db)


@attendance_router.get("/")
def get_all_attendance(
    db: Session = Depends(get_db)
):
    return fetch_all_attendance(db)


@attendance_router.get("/{attendance_id}")
def get_attendance(
    attendance_id: int,
    db: Session = Depends(get_db)
):
    return fetch_attendance(attendance_id, db)


@attendance_router.put("/{attendance_id}")
def update_attendance(
    attendance_id: int,
    attendance: AttendanceUpdate,
    db: Session = Depends(get_db)
):
    return modify_attendance(attendance_id, attendance, db)


@attendance_router.delete("/{attendance_id}")
def delete_attendance(
    attendance_id: int,
    db: Session = Depends(get_db)
):
    return remove_attendance(attendance_id, db)