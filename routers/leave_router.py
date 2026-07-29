"""
==========================================================
File        : leave_router.py
Project     : Enterprise Employee Project and Payroll
              Management System
Description : Leave FastAPI Router
==========================================================
"""

from fastapi import (
    APIRouter,
    HTTPException,
    status
)

from schemas.leave_schema import (
    LeaveCreate,
    LeaveUpdate
)

from services.leave_api_service import (
    apply_leave_api,
    search_leave_api,
    update_leave_status_api,
    delete_leave_api,
    display_all_leaves_api
)

from exceptions.custom_exception import (
    ValidationException,
    RecordNotFoundException,
    DatabaseException
)

router = APIRouter(
    prefix="/leaves",
    tags=["Leaves"]
)


# =====================================================
# Apply Leave
# =====================================================

@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    summary="Apply Leave"
)
def apply_leave(leave: LeaveCreate):

    try:

        result = apply_leave_api(

            leave.employee_id,

            leave.leave_date,

            leave.leave_days,

            leave.reason

        )

        return {

            "success": True,

            "message":
                "Leave Applied Successfully.",

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
# Search Leave
# =====================================================

@router.get(
    "/{employee_id}",
    summary="Search Leave"
)
def search_leave(employee_id: int):

    try:

        leaves = search_leave_api(employee_id)

        return {

            "success": True,

            "count": len(leaves),

            "data": leaves

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
# Display All Leaves
# =====================================================

@router.get(
    "/",
    summary="Display All Leaves"
)
def display_all_leaves():

    try:

        leaves = display_all_leaves_api()

        return {

            "success": True,

            "count": len(leaves),

            "data": leaves

        }

    except DatabaseException as e:

        raise HTTPException(

            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,

            detail=str(e)

        )


# =====================================================
# Update Leave Status
# =====================================================

@router.put(
    "/{leave_id}",
    summary="Update Leave Status"
)
def update_leave_status(

        leave_id: int,

        leave: LeaveUpdate

):

    try:

        result = update_leave_status_api(

            leave_id,

            leave.status

        )

        return {

            "success": True,

            "message":
                "Leave Status Updated Successfully.",

            "data":
                result

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
# Delete Leave
# =====================================================

@router.delete(
    "/{leave_id}",
    summary="Delete Leave"
)
def delete_leave(leave_id: int):

    try:

        delete_leave_api(leave_id)

        return {

            "success": True,

            "message":
                "Leave Deleted Successfully."

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