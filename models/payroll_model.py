from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from models import attendance_model, department_model, employee_model

from database import Base


class Payroll(Base):

    __tablename__ = "payroll"

    payroll_id = Column(
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

    basic_salary = Column(
        Float,
        nullable=False
    )

    bonus_amount = Column(
        Float,
        default=0
    )

    deductions = Column(
        Float,
        default=0
    )

    net_salary = Column(
        Float,
        nullable=False
    )

    employee = relationship(
        "Employee",
        back_populates="payroll"
    )

    def __repr__(self):
        return f"<Payroll Employee ID : {self.employee_id}>"