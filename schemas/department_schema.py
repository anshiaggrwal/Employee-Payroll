from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    field_validator
)


class DepartmentCreate(BaseModel):

    department_name: str = Field(
        ...,
        min_length=2,
        max_length=100,
        description="Department name must contain 2 to 100 characters."
    )

    @field_validator("department_name")
    @classmethod
    def validate_department_name(cls, value: str):

        value = value.strip()

        if not value:
            raise ValueError(
                "Department name cannot be empty."
            )

        if not value.replace(" ", "").isalpha():
            raise ValueError(
                "Department name should contain only alphabets."
            )

        return value.title()


class DepartmentUpdate(BaseModel):

    department_name: str = Field(
        ...,
        min_length=2,
        max_length=100
    )

    @field_validator("department_name")
    @classmethod
    def validate_department_name(cls, value: str):

        value = value.strip()

        if not value:
            raise ValueError(
                "Department name cannot be empty."
            )

        if not value.replace(" ", "").isalpha():
            raise ValueError(
                "Department name should contain only alphabets."
            )

        return value.title()


class DepartmentResponse(BaseModel):

    department_id: int

    department_name: str

    model_config = ConfigDict(
        from_attributes=True
    )