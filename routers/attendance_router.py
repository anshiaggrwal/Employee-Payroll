"""
==========================================================
File        : attendance_router.py
Project     : Enterprise Employee Project and Payroll
              Management System
Description : Attendance FastAPI Router
==========================================================
"""

from fastapi import (
    APIRouter,
    HTTPException,
    status
)

from schemas.attendance_schema import (
    AttendanceCreate,
    AttendanceUpdate
)

from services.attendance_api_service import (
    mark_attendance_api,
    search_attendance_api,
    update_attendance_api,
    delete_attendance_api,
    display_all_attendance_api
)

from exceptions.custom_exception import (
    ValidationException,
    RecordNotFoundException,
    DatabaseException
)

router = APIRouter(
    prefix="/attendance",
    tags=["Attendance"]
)


# =====================================================
# Mark Attendance
# =====================================================

@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    summary="Mark Attendance"
)
def mark_attendance(attendance: AttendanceCreate):

    try:

        result = mark_attendance_api(

            attendance.employee_id,

            attendance.attendance_date,

            attendance.status

        )

        return {

            "success": True,

            "message":
                "Attendance Marked Successfully.",

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
# Search Attendance By Employee ID
# =====================================================

@router.get(
    "/{employee_id}",
    summary="Search Attendance"
)
def search_attendance(employee_id: int):

    try:

        attendance = search_attendance_api(
            employee_id
        )

        return {

            "success": True,

            "count": len(attendance),

            "data": attendance

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
# Display All Attendance
# =====================================================

@router.get(
    "/",
    summary="Display All Attendance"
)
def display_all_attendance():

    try:

        attendance = display_all_attendance_api()

        return {

            "success": True,

            "count": len(attendance),

            "data": attendance

        }

    except DatabaseException as e:

        raise HTTPException(

            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,

            detail=str(e)

        )


# =====================================================
# Update Attendance
# =====================================================

@router.put(
    "/{attendance_id}",
    summary="Update Attendance"
)
def update_attendance(

        attendance_id: int,

        attendance: AttendanceUpdate

):

    try:

        result = update_attendance_api(

            attendance_id,

            attendance.status

        )

        return {

            "success": True,

            "message":
                "Attendance Updated Successfully.",

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
# Delete Attendance
# =====================================================

@router.delete(
    "/{attendance_id}",
    summary="Delete Attendance"
)
def delete_attendance(attendance_id: int):

    try:

        delete_attendance_api(
            attendance_id
        )

        return {

            "success": True,

            "message":
                "Attendance Deleted Successfully."

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