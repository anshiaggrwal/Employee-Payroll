"""
==========================================================
File        : project_schema.py
Project     : Enterprise Employee Project and Payroll
              Management System
Description : Project Pydantic Schemas
==========================================================
"""

from datetime import date

from pydantic import (
    BaseModel,
    Field
)


class ProjectCreate(BaseModel):

    project_name: str = Field(...)

    project_budget: float = Field(...)

    start_date: date

    end_date: date

    status: str


class ProjectUpdate(BaseModel):

    project_name: str = Field(...)

    project_budget: float = Field(...)

    status: str