from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.orm import relationship
from models import attendance_model, department_model, payroll_model

from database import Base


class Employee(Base):

    __tablename__ = "employees"

    employee_id = Column(
        Integer,
        primary_key=True
    )

    employee_name = Column(
        String(100),
        nullable=False
    )

    email = Column(
        String(100),
        unique=True,
        nullable=False
    )

    department_id = Column(
        Integer,
        ForeignKey("departments.department_id"),
        nullable=False
    )

    designation = Column(
        String(100),
        nullable=False
    )

    date_of_joining = Column(
        Date,
        nullable=False
    )

    basic_salary = Column(
        Float,
        nullable=False
    )

    employment_status = Column(
        String(20),
        default="Active"
    )

    department = relationship(
        "Department",
        back_populates="employees"
    )

    attendance = relationship(
        "Attendance",
        back_populates="employee",
        cascade="all, delete-orphan"
    )

    payroll = relationship(
        "Payroll",
        back_populates="employee",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Employee {self.employee_name}>"