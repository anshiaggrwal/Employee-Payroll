"""
==========================================================
File        : employee_router.py
Project     : Enterprise Employee Project and Payroll
              Management System
Description : Employee FastAPI Router
==========================================================
"""

from fastapi import (
    APIRouter,
    HTTPException,
    status
)

from schemas.employee_schema import (
    EmployeeCreate,
    EmployeeUpdate
)

from services.employee_api_service import (
    add_employee_api,
    search_employee_api,
    update_employee_api,
    delete_employee_api,
    display_all_employees_api
)

from exceptions.custom_exception import (
    ValidationException,
    RecordNotFoundException,
    DatabaseException
)

router = APIRouter(
    prefix="/employees",
    tags=["Employees"]
)


# =====================================================
# Add Employee
# =====================================================

@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    summary="Add Employee"
)
def add_employee(employee: EmployeeCreate):

    try:

        result = add_employee_api(
            employee.employee_name,
            employee.age,
            employee.email,
            employee.phone
        )

        return {
            "success": True,
            "message": "Employee Added Successfully.",
            "data": result
        }

    except ValidationException as e:

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

    except DatabaseException as e:

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )


# =====================================================
# Search Employee
# =====================================================

@router.get(
    "/{employee_id}",
    summary="Search Employee"
)
def search_employee(employee_id: int):

    try:

        employee = search_employee_api(
            employee_id
        )

        return {
            "success": True,
            "data": employee
        }

    except RecordNotFoundException as e:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )

    except DatabaseException as e:

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )


# =====================================================
# Display All Employees
# =====================================================

@router.get(
    "/",
    summary="Display All Employees"
)
def display_all_employees():

    try:

        employees = display_all_employees_api()

        return {
            "success": True,
            "count": len(employees),
            "data": employees
        }

    except DatabaseException as e:

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )


# =====================================================
# Update Employee
# =====================================================

@router.put(
    "/{employee_id}",
    summary="Update Employee"
)
def update_employee(
        employee_id: int,
        employee: EmployeeUpdate
):

    try:

        result = update_employee_api(

            employee_id,

            employee.employee_name,

            employee.age,

            employee.email,

            employee.phone

        )

        return {

            "success": True,

            "message":
                "Employee Updated Successfully.",

            "data":
                result

        }

    except ValidationException as e:

        raise HTTPException(

            status_code=status.HTTP_400_BAD_REQUEST,

            detail=str(e)

        )

    except RecordNotFoundException as e:

        raise HTTPException(

            status_code=status.HTTP_404_NOT_FOUND,

            detail=str(e)

        )

    except DatabaseException as e:

        raise HTTPException(

            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,

            detail=str(e)

        )


# =====================================================
# Delete Employee
# =====================================================

@router.delete(
    "/{employee_id}",
    summary="Delete Employee"
)
def delete_employee(employee_id: int):

    try:

        delete_employee_api(employee_id)

        return {

            "success": True,

            "message":
                "Employee Deleted Successfully."

        }

    except RecordNotFoundException as e:

        raise HTTPException(

            status_code=status.HTTP_404_NOT_FOUND,

            detail=str(e)

        )

    except DatabaseException as e:

        raise HTTPException(

            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,

            detail=str(e)

        )