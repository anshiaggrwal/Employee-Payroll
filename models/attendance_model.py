from sqlalchemy import Column, Integer, Date, String, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Attendance(Base):

    __tablename__ = "attendance"

    attendance_id = Column(Integer, primary_key=True, autoincrement=True)

    employee_id = Column(
        Integer,
        ForeignKey("employees.employee_id")
    )

    attendance_date = Column(Date)

    status = Column(String(10))

    employee = relationship(
        "Employee",
        back_populates="attendance"
    )