from datetime import date
from typing import Literal

from pydantic import (
    BaseModel,
    ConfigDict,
    EmailStr,
    Field,
    field_validator
)


class EmployeeCreate(BaseModel):

    employee_id: int = Field(
        ...,
        gt=0,
        description="Employee ID must be greater than 0."
    )

    employee_name: str = Field(
        ...,
        min_length=3,
        max_length=100,
        description="Employee name should contain 3 to 100 characters."
    )

    email: EmailStr

    department_id: int = Field(
        ...,
        gt=0,
        description="Department ID must be greater than 0."
    )

    designation: str = Field(
        ...,
        min_length=2,
        max_length=100
    )

    date_of_joining: date

    basic_salary: float = Field(
        ...,
        gt=0,
        le=10000000,
        description="Salary must be greater than 0."
    )

    employment_status: Literal[
        "Active",
        "Inactive"
    ]

    @field_validator("employee_name")
    @classmethod
    def validate_employee_name(cls, value: str):

        value = value.strip()

        if not value.replace(" ", "").isalpha():
            raise ValueError(
                "Employee name should contain only alphabets."
            )

        return value.title()

    @field_validator("designation")
    @classmethod
    def validate_designation(cls, value: str):

        value = value.strip()

        if len(value) < 2:
            raise ValueError(
                "Designation is too short."
            )

        return value.title()


class EmployeeUpdate(BaseModel):

    employee_name: str = Field(
        ...,
        min_length=3,
        max_length=100
    )

    email: EmailStr

    department_id: int = Field(
        ...,
        gt=0
    )

    designation: str = Field(
        ...,
        min_length=2,
        max_length=100
    )

    date_of_joining: date

    basic_salary: float = Field(
        ...,
        gt=0,
        le=10000000
    )

    employment_status: Literal[
        "Active",
        "Inactive"
    ]

    @field_validator("employee_name")
    @classmethod
    def validate_employee_name(cls, value: str):

        value = value.strip()

        if not value.replace(" ", "").isalpha():
            raise ValueError(
                "Employee name should contain only alphabets."
            )

        return value.title()

    @field_validator("designation")
    @classmethod
    def validate_designation(cls, value: str):

        return value.strip().title()


class EmployeeResponse(BaseModel):

    employee_id: int

    employee_name: str

    email: EmailStr

    department_id: int

    designation: str

    date_of_joining: date

    basic_salary: float

    employment_status: str

    model_config = ConfigDict(
        from_attributes=True
    )