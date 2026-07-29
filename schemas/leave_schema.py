from datetime import date
from pydantic import BaseModel


class LeaveCreate(BaseModel):

    employee_id: int

    leave_date: date

    leave_days: int

    reason: str


class LeaveUpdate(BaseModel):

    status: str