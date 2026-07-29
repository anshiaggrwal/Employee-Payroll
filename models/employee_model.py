from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Employee(Base):

    __tablename__ = "employees"

    employee_id = Column(Integer, primary_key=True, autoincrement=True)

    employee_name = Column(String(100), nullable=False)

    age = Column(Integer)

    email = Column(String(100), unique=True)

    phone = Column(String(15), unique=True)

    status = Column(String(20), default="ACTIVE")

    department_id = Column(
        Integer,
        ForeignKey("departments.department_id")
    )

    role_id = Column(
        Integer,
        ForeignKey("roles.role_id")
    )

    department = relationship(
        "Department",
        back_populates="employees"
    )

    role = relationship(
        "Role",
        back_populates="employees"
    )

    attendance = relationship(
        "Attendance",
        back_populates="employee"
    )

    leaves = relationship(
        "LeaveRequest",
        back_populates="employee"
    )

    payrolls = relationship(
        "Payroll",
        back_populates="employee"
    )

    tasks = relationship(
        "Task",
        back_populates="employee"
    )

    projects = relationship(
        "EmployeeProject",
        back_populates="employee"
    )

    def __repr__(self):

        return f"<Employee {self.employee_name}>"