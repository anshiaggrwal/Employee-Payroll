from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship

from database import Base


class Role(Base):

    __tablename__ = "roles"

    role_id = Column(Integer, primary_key=True, autoincrement=True)

    role_name = Column(String(100), nullable=False)

    basic_salary = Column(Float, nullable=False)

    employees = relationship(
        "Employee",
        back_populates="role"
    )

    def __repr__(self):

        return f"<Role {self.role_name}>"