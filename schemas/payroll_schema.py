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

    basic_salary: float = Field(
        ...,
        gt=0,
        le=10000000,
        description="Basic salary must be greater than 0."
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

    net_salary: float = Field(
        ...,
        ge=0,
        le=10000000
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

    @model_validator(mode="after")
    def validate_salary(self):

        calculated_salary = (
            self.basic_salary
            + self.bonus_amount
            - self.deductions
        )

        if self.net_salary != calculated_salary:
            raise ValueError(
                "Net salary must be equal to "
                "Basic Salary + Bonus - Deductions."
            )

        return self


class PayrollUpdate(BaseModel):

    payroll_month: str = Field(
        ...,
        min_length=3,
        max_length=20
    )

    basic_salary: float = Field(
        ...,
        gt=0,
        le=10000000
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

    net_salary: float = Field(
        ...,
        ge=0,
        le=10000000
    )

    @field_validator("payroll_month")
    @classmethod
    def validate_payroll_month(cls, value: str):

        return value.strip().title()

    @model_validator(mode="after")
    def validate_salary(self):

        calculated_salary = (
            self.basic_salary
            + self.bonus_amount
            - self.deductions
        )

        if self.net_salary != calculated_salary:
            raise ValueError(
                "Net salary must be equal to "
                "Basic Salary + Bonus - Deductions."
            )

        return self


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