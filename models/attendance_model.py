from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from models import employee_model, department_model, payroll_model

from database import Base


class Attendance(Base):

    __tablename__ = "attendance"

    attendance_id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    employee_id = Column(
        Integer,
        ForeignKey("employees.employee_id"),
        nullable=False
    )

    payroll_month = Column(
        String(20),
        nullable=False
    )

    total_working_days = Column(
        Integer,
        nullable=False
    )

    present_days = Column(
        Integer,
        nullable=False
    )

    leave_days = Column(
        Integer,
        nullable=False
    )

    overtime_hours = Column(
        Float,
        default=0
    )

    bonus_amount = Column(
        Float,
        default=0
    )

    employee = relationship(
        "Employee",
        back_populates="attendance"
    )

    def __repr__(self):
        return f"<Attendance Employee ID : {self.employee_id}>"