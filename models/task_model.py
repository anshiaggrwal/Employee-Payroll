from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Task(Base):

    __tablename__ = "tasks"

    task_id = Column(Integer, primary_key=True, autoincrement=True)

    task_name = Column(String(100))

    status = Column(String(30))

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
        back_populates="tasks"
    )

    project = relationship(
        "Project",
        back_populates="tasks"
    )