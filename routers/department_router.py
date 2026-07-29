from fastapi import APIRouter, HTTPException, status

from schemas.department_schema import (
    DepartmentCreate,
    DepartmentUpdate
)

from services.department_api_service import (
    add_department_api,
    search_department_api,
    update_department_api,
    delete_department_api,
    display_all_departments_api
)

from exceptions.custom_exception import (
    ValidationException,
    RecordNotFoundException,
    DatabaseException
)

router = APIRouter(
    prefix="/departments",
    tags=["Department"]
)


# ==========================================
# Add Department
# ==========================================

@router.post(
    "/",
    status_code=status.HTTP_201_CREATED
)
def add_department(
    department: DepartmentCreate
):

    try:

        result = add_department_api(
            department.department_name
        )

        return {
            "message": "Department Added Successfully.",
            "department": result
        }

    except ValidationException as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )

    except DatabaseException as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# ==========================================
# Search Department
# ==========================================

@router.get("/{department_id}")
def search_department(
    department_id: int
):

    try:

        department = search_department_api(
            department_id
        )

        return department

    except RecordNotFoundException as e:

        raise HTTPException(
            status_code=404,
            detail=str(e)
        )


# ==========================================
# Display All Departments
# ==========================================

@router.get("/")
def display_all_departments():

    return display_all_departments_api()


# ==========================================
# Update Department
# ==========================================

@router.put("/{department_id}")
def update_department(

    department_id: int,

    department: DepartmentUpdate

):

    try:

        result = update_department_api(

            department_id,

            department.department_name

        )

        return {

            "message":
                "Department Updated Successfully.",

            "department":
                result

        }

    except ValidationException as e:

        raise HTTPException(

            status_code=400,

            detail=str(e)

        )

    except RecordNotFoundException as e:

        raise HTTPException(

            status_code=404,

            detail=str(e)

        )


# ==========================================
# Delete Department
# ==========================================

@router.delete("/{department_id}")
def delete_department(
    department_id: int
):

    try:

        delete_department_api(
            department_id
        )

        return {

            "message":
                "Department Deleted Successfully."

        }

    except RecordNotFoundException as e:

        raise HTTPException(

            status_code=404,

            detail=str(e)

        )