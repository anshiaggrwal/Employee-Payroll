from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from schemas.employee_schema import EmployeeCreate, EmployeeUpdate
from services.employee_service import (
    add_employee,
    fetch_all_employees,
    fetch_employee,
    modify_employee,
    remove_employee
)

employee_router = APIRouter(
    prefix="/employees",
    tags=["Employee"]
)


@employee_router.post("/")
def create_employee(
    employee: EmployeeCreate,
    db: Session = Depends(get_db)
):
    return add_employee(employee, db)


@employee_router.get("/")
def get_all_employees(
    db: Session = Depends(get_db)
):
    return fetch_all_employees(db)


@employee_router.get("/{employee_id}")
def get_employee(
    employee_id: int,
    db: Session = Depends(get_db)
):
    return fetch_employee(employee_id, db)


@employee_router.put("/{employee_id}")
def update_employee(
    employee_id: int,
    employee: EmployeeUpdate,
    db: Session = Depends(get_db)
):
    return modify_employee(employee_id, employee, db)


@employee_router.delete("/{employee_id}")
def delete_employee(
    employee_id: int,
    db: Session = Depends(get_db)
):
    return remove_employee(employee_id, db)