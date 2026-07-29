from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Payroll(Base):

    __tablename__ = "payroll"

    payroll_id = Column(Integer, primary_key=True, autoincrement=True)

    employee_id = Column(
        Integer,
        ForeignKey("employees.employee_id")
    )

    basic_salary = Column(Float)

    bonus = Column(Float)

    deduction = Column(Float)

    net_salary = Column(Float)

    employee = relationship(
        "Employee",
        back_populates="payrolls"
    )