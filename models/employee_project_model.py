from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class EmployeeProject(Base):

    __tablename__ = "employee_projects"

    id = Column(Integer, primary_key=True, autoincrement=True)

    employee_id = Column(
        Integer,
        ForeignKey("employees.employee_id")
    )

    project_id = Column(
        Integer,
        ForeignKey("projects.project_id")
    )

    employee = relationship(
        "Employee",
        back_populates="projects"
    )

    project = relationship(
        "Project",
        back_populates="employees"
    )