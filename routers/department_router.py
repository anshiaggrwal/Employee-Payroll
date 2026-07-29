from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db

from schemas.department_schema import (
    DepartmentCreate,
    DepartmentUpdate
)

from services.department_service import (
    add_department,
    fetch_all_departments,
    fetch_department,
    modify_department,
    remove_department
)

department_router = APIRouter(
    prefix="/departments",
    tags=["Department"]
)


@department_router.post("/")
def create_department(
    department: DepartmentCreate,
    db: Session = Depends(get_db)
):
    return add_department(department, db)


@department_router.get("/")
def get_all_departments(
    db: Session = Depends(get_db)
):
    return fetch_all_departments(db)


@department_router.get("/{department_id}")
def get_department(
    department_id: int,
    db: Session = Depends(get_db)
):
    return fetch_department(department_id, db)


@department_router.put("/{department_id}")
def update_department(
    department_id: int,
    department: DepartmentUpdate,
    db: Session = Depends(get_db)
):
    return modify_department(department_id, department, db)


@department_router.delete("/{department_id}")
def delete_department(
    department_id: int,
    db: Session = Depends(get_db)
):
    return remove_department(department_id, db)