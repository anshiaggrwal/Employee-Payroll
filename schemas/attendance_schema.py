from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    field_validator,
    model_validator
)


class AttendanceCreate(BaseModel):

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

    total_working_days: int = Field(
        ...,
        gt=0,
        le=31,
        description="Working days must be between 1 and 31."
    )

    present_days: int = Field(
        ...,
        ge=0,
        le=31
    )

    leave_days: int = Field(
        ...,
        ge=0,
        le=31
    )

    overtime_hours: float = Field(
        ...,
        ge=0,
        le=300
    )

    bonus_amount: float = Field(
        ...,
        ge=0
    )

    @field_validator("payroll_month")
    @classmethod
    def validate_payroll_month(cls, value: str):

        value = value.strip()

        if len(value) < 3:
            raise ValueError(
                "Payroll month is invalid."
            )

        return value.title()

    @model_validator(mode="after")
    def validate_attendance(self):

        if self.present_days > self.total_working_days:
            raise ValueError(
                "Present days cannot be greater than total working days."
            )

        if self.leave_days > self.total_working_days:
            raise ValueError(
                "Leave days cannot be greater than total working days."
            )

        if (self.present_days + self.leave_days) > self.total_working_days:
            raise ValueError(
                "Present days and leave days exceed total working days."
            )

        return self


class AttendanceUpdate(BaseModel):

    payroll_month: str = Field(
        ...,
        min_length=3,
        max_length=20
    )

    total_working_days: int = Field(
        ...,
        gt=0,
        le=31
    )

    present_days: int = Field(
        ...,
        ge=0,
        le=31
    )

    leave_days: int = Field(
        ...,
        ge=0,
        le=31
    )

    overtime_hours: float = Field(
        ...,
        ge=0,
        le=300
    )

    bonus_amount: float = Field(
        ...,
        ge=0
    )

    @field_validator("payroll_month")
    @classmethod
    def validate_payroll_month(cls, value: str):

        return value.strip().title()

    @model_validator(mode="after")
    def validate_attendance(self):

        if self.present_days > self.total_working_days:
            raise ValueError(
                "Present days cannot be greater than total working days."
            )

        if self.leave_days > self.total_working_days:
            raise ValueError(
                "Leave days cannot be greater than total working days."
            )

        if (self.present_days + self.leave_days) > self.total_working_days:
            raise ValueError(
                "Present days and leave days exceed total working days."
            )

        return self


class AttendanceResponse(BaseModel):

    attendance_id: int

    employee_id: int

    payroll_month: str

    total_working_days: int

    present_days: int

    leave_days: int

    overtime_hours: float

    bonus_amount: float

    model_config = ConfigDict(
        from_attributes=True
    )