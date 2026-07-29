from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    field_validator,
    model_validator
)


class PayrollCreate(BaseModel):

    employee_id: int = Field(
        ...,
        gt=0,
        description="Employee ID must be greater than 0."
    )

    payroll_month: str = Field(
        ...,
        min_length=3,
        max_length=20,
        description="Example: July-2026"
    )


    bonus_amount: float = Field(
        default=0,
        ge=0,
        le=1000000
    )

    deductions: float = Field(
        default=0,
        ge=0,
        le=1000000
    )

    @field_validator("payroll_month")
    @classmethod
    def validate_payroll_month(cls, value: str):

        value = value.strip()

        if not value:
            raise ValueError(
                "Payroll month cannot be empty."
            )

        return value.title()


class PayrollUpdate(BaseModel):

    payroll_month: str = Field(
        ...,
        min_length=3,
        max_length=20
    )

    bonus_amount: float = Field(
        default=0,
        ge=0,
        le=1000000
    )

    deductions: float = Field(
        default=0,
        ge=0,
        le=1000000
    )

    @field_validator("payroll_month")
    @classmethod
    def validate_payroll_month(cls, value: str):

        return value.strip().title()


class PayrollResponse(BaseModel):

    payroll_id: int

    employee_id: int

    payroll_month: str

    basic_salary: float

    bonus_amount: float

    deductions: float

    net_salary: float

    model_config = ConfigDict(
        from_attributes=True
    )