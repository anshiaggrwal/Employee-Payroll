"""
==========================================================
File        : payroll_router.py
Project     : Enterprise Employee Project and Payroll
              Management System
Description : Payroll FastAPI Router
==========================================================
"""

from fastapi import (
    APIRouter,
    HTTPException,
    status
)

from schemas.payroll_schema import (
    PayrollCreate,
    PayrollUpdate
)

from services.payroll_api_service import (
    generate_payroll_api,
    search_payroll_api,
    update_payroll_api,
    delete_payroll_api,
    display_all_payrolls_api
)

from exceptions.custom_exception import (
    ValidationException,
    RecordNotFoundException,
    DatabaseException
)

router = APIRouter(
    prefix="/payrolls",
    tags=["Payroll"]
)


# =====================================================
# Generate Payroll
# =====================================================

@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    summary="Generate Payroll"
)
def generate_payroll(payroll: PayrollCreate):

    try:

        result = generate_payroll_api(

            payroll.employee_id,

            payroll.basic_salary,

            payroll.bonus,

            payroll.deduction

        )

        return {

            "success": True,

            "message":
                "Payroll Generated Successfully.",

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
# Search Payroll
# =====================================================

@router.get(
    "/{employee_id}",
    summary="Search Payroll"
)
def search_payroll(employee_id: int):

    try:

        payroll = search_payroll_api(employee_id)

        return {

            "success": True,

            "data":
                payroll

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
# Display All Payrolls
# =====================================================

@router.get(
    "/",
    summary="Display All Payrolls"
)
def display_all_payrolls():

    try:

        payrolls = display_all_payrolls_api()

        return {

            "success": True,

            "count": len(payrolls),

            "data":
                payrolls

        }

    except DatabaseException as e:

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )


# =====================================================
# Update Payroll
# =====================================================

@router.put(
    "/{payroll_id}",
    summary="Update Payroll"
)
def update_payroll(

        payroll_id: int,

        payroll: PayrollUpdate

):

    try:

        result = update_payroll_api(

            payroll_id,

            payroll.basic_salary,

            payroll.bonus,

            payroll.deduction

        )

        return {

            "success": True,

            "message":
                "Payroll Updated Successfully.",

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
# Delete Payroll
# =====================================================

@router.delete(
    "/{payroll_id}",
    summary="Delete Payroll"
)
def delete_payroll(payroll_id: int):

    try:

        delete_payroll_api(payroll_id)

        return {

            "success": True,

            "message":
                "Payroll Deleted Successfully."

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