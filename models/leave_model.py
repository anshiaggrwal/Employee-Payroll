from sqlalchemy import Column, Integer, Date, String, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class LeaveRequest(Base):

    __tablename__ = "leave_requests"

    leave_id = Column(Integer, primary_key=True, autoincrement=True)

    employee_id = Column(
        Integer,
        ForeignKey("employees.employee_id")
    )

    leave_date = Column(Date)

    leave_days = Column(Integer)

    reason = Column(String(255))

    status = Column(String(20))

    employee = relationship(
        "Employee",
        back_populates="leaves"
    )