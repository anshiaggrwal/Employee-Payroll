from datetime import date

from pydantic import BaseModel


class AttendanceCreate(BaseModel):

    employee_id: int
    attendance_date: date
    status: str


class AttendanceUpdate(BaseModel):

    status: str