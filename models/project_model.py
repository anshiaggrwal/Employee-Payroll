from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.orm import relationship

from database import Base


class Project(Base):

    __tablename__ = "projects"

    project_id = Column(Integer, primary_key=True, autoincrement=True)

    project_name = Column(String(100))

    project_budget = Column(Float)

    start_date = Column(Date)

    end_date = Column(Date)

    status = Column(String(30))

    employees = relationship(
        "EmployeeProject",
        back_populates="project"
    )

    tasks = relationship(
        "Task",
        back_populates="project"
    )