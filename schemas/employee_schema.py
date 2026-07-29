from pydantic import BaseModel, EmailStr


class EmployeeCreate(BaseModel):

    employee_name: str
    age: int
    email: EmailStr
    phone: str


class EmployeeUpdate(BaseModel):

    employee_name: str
    age: int