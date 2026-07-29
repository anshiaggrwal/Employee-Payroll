from pydantic import BaseModel


class PayrollCreate(BaseModel):

    employee_id: int
    basic_salary: float
    bonus: float
    deduction: float


class PayrollUpdate(BaseModel):

    basic_salary: float
    bonus: float
    deduction: float