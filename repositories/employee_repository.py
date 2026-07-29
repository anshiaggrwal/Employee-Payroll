from sqlalchemy.orm import Session

from models.employee_model import Employee


def create_employee(
    employee: Employee,
    db: Session
):
    db.add(employee)
    db.commit()
    db.refresh(employee)

    return employee


def get_all_employees(
    db: Session
):
    return db.query(Employee).all()


def get_employee_by_id(
    employee_id: int,
    db: Session
):
    return db.query(Employee).filter(
        Employee.employee_id == employee_id
    ).first()


def get_employee_by_email(
    email: str,
    db: Session
):
    return db.query(Employee).filter(
        Employee.email == email
    ).first()


def update_employee(
    db: Session
):
    db.commit()


def delete_employee(
    employee: Employee,
    db: Session
):
    db.delete(employee)
    db.commit()