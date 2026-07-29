
import matplotlib.pyplot as plt
from sqlalchemy import func
from sqlalchemy.orm import Session

from models.employee_model import Employee
from models.department_model import Department


def employees_by_department_graph(db: Session):

    result = (
        db.query(
            Department.department_name,
            func.count(Employee.employee_id)
        )
        .join(
            Employee,
            Employee.department_id == Department.department_id
        )
        .group_by(
            Department.department_name
        )
        .all()
    )

    departments = [row[0] for row in result]
    counts = [row[1] for row in result]

    plt.figure(figsize=(8,5))
    plt.bar(
        departments,
        counts,
        color="skyblue",
        edgecolor="black"
    )

    plt.title("Employees by Department")
    plt.xlabel("Department")
    plt.ylabel("Number of Employees")

    plt.tight_layout()

    file_path = "employees_by_department.png"

    plt.savefig(file_path)

    plt.close()

    return file_path