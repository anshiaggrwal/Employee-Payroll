from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Salary(Base):

    __tablename__ = "salary_details"

    salary_id = Column(Integer, primary_key=True, autoincrement=True)

    employee_id = Column(
        Integer,
        ForeignKey("employees.employee_id")
    )

    basic_salary = Column(Float)

    hra = Column(Float)

    da = Column(Float)

    tax = Column(Float)

    employee = relationship("Employee")