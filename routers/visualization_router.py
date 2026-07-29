from fastapi import APIRouter, Depends
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from database import get_db

from services.visualization_service import (
    employees_by_department_graph
)

visualization_router = APIRouter(
    prefix="/visualization",
    tags=["Visualization"]
)


@visualization_router.get("/employees-by-department")
def employee_department_graph(
    db: Session = Depends(get_db)
):

    file_path = employees_by_department_graph(db)

    return FileResponse(
        file_path,
        media_type="image/png",
        filename="employees_by_department.png"
    )