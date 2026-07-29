from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from schemas.payroll_schema import PayrollCreate, PayrollUpdate
from services.payroll_service import (
    add_payroll,
    fetch_all_payrolls,
    fetch_payroll,
    modify_payroll,
    remove_payroll
)

payroll_router = APIRouter(
    prefix="/payroll",
    tags=["Payroll"]
)


@payroll_router.post("/")
def create_payroll(
    payroll: PayrollCreate,
    db: Session = Depends(get_db)
):
    return add_payroll(payroll, db)


@payroll_router.get("/")
def get_all_payrolls(
    db: Session = Depends(get_db)
):
    return fetch_all_payrolls(db)


@payroll_router.get("/{payroll_id}")
def get_payroll(
    payroll_id: int,
    db: Session = Depends(get_db)
):
    return fetch_payroll(payroll_id, db)


@payroll_router.put("/{payroll_id}")
def update_payroll(
    payroll_id: int,
    payroll: PayrollUpdate,
    db: Session = Depends(get_db)
):
    return modify_payroll(payroll_id, payroll, db)


@payroll_router.delete("/{payroll_id}")
def delete_payroll(
    payroll_id: int,
    db: Session = Depends(get_db)
):
    return remove_payroll(payroll_id, db)