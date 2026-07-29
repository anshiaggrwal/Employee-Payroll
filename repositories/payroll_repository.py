from sqlalchemy.orm import Session

from models.payroll_model import Payroll


def create_payroll(
    payroll: Payroll,
    db: Session
):
    db.add(payroll)
    db.commit()
    db.refresh(payroll)

    return payroll


def get_all_payrolls(
    db: Session
):
    return db.query(Payroll).all()


def get_payroll_by_id(
    payroll_id: int,
    db: Session
):
    return db.query(Payroll).filter(
        Payroll.payroll_id == payroll_id
    ).first()


def get_payroll_by_employee_and_month(
    employee_id: int,
    payroll_month: str,
    db: Session
):
    return db.query(Payroll).filter(
        Payroll.employee_id == employee_id,
        Payroll.payroll_month == payroll_month
    ).first()


def update_payroll(
    db: Session
):
    db.commit()


def delete_payroll(
    payroll: Payroll,
    db: Session
):
    db.delete(payroll)
    db.commit()