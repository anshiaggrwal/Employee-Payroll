from sqlalchemy.orm import Session

from models.department_model import Department


def create_department(
    department: Department,
    db: Session
):
    db.add(department)
    db.commit()
    db.refresh(department)

    return department


def get_all_departments(db: Session):

    return db.query(Department).all()


def get_department_by_id(
    department_id: int,
    db: Session
):

    return db.query(Department).filter(
        Department.department_id == department_id
    ).first()


def get_department_by_name(
    department_name: str,
    db: Session
):

    return db.query(Department).filter(
        Department.department_name == department_name
    ).first()


def update_department(db: Session):

    db.commit()


def delete_department(
    department: Department,
    db: Session
):

    db.delete(department)
    db.commit()