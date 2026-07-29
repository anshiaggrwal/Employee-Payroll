from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Department(Base):

    __tablename__ = "departments"

    department_id = Column(Integer, primary_key=True, autoincrement=True)

    department_name = Column(String(100), unique=True, nullable=False)

    employees = relationship(
        "Employee",
        back_populates="department"
    )

    def __repr__(self):

        return f"<Department {self.department_name}>"