"""
==========================================================
File        : leave_api_service.py
Project     : Enterprise Employee Project and Payroll
              Management System
Description : Leave API Service Module
==========================================================
"""

from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError

from database import get_session

from models.leave_model import LeaveRequest
from models.employee_model import Employee

from validations.validation import (
    validate_leave_days,
    validate_date
)

from utilities.logger_config import application, exception

from exceptions.custom_exception import (
    ValidationException,
    RecordNotFoundException,
    DatabaseException
)


# =====================================================
# Apply Leave
# =====================================================

def apply_leave_api(
        employee_id,
        leave_date,
        leave_days,
        reason
):

    session = get_session()

    try:

        employee = session.get(
            Employee,
            employee_id
        )

        if employee is None:

            raise RecordNotFoundException(
                "Employee Not Found."
            )

        leave_date = validate_date(
            leave_date
        )

        leave_days = validate_leave_days(
            leave_days
        )

        leave = LeaveRequest(

            employee_id=employee_id,

            leave_date=leave_date,

            leave_days=leave_days,

            reason=reason,

            status="Pending"

        )

        session.add(leave)

        session.commit()

        session.refresh(leave)

        application(
            "Leave Applied Successfully."
        )

        return leave

    except ValidationException:

        session.rollback()

        raise

    except SQLAlchemyError as e:

        session.rollback()

        exception(str(e))

        raise DatabaseException(
            "Database Error."
        )

    finally:

        session.close()


# =====================================================
# Search Leave
# =====================================================

def search_leave_api(employee_id):

    session = get_session()

    try:

        leaves = session.scalars(

            select(LeaveRequest).where(

                LeaveRequest.employee_id == employee_id

            )

        ).all()

        if not leaves:

            raise RecordNotFoundException(
                "Leave Record Not Found."
            )

        return leaves

    except SQLAlchemyError as e:

        exception(str(e))

        raise DatabaseException(
            "Database Error."
        )

    finally:

        session.close()


# =====================================================
# Update Leave Status
# =====================================================

def update_leave_status_api(
        leave_id,
        status
):

    session = get_session()

    try:

        leave = session.get(
            LeaveRequest,
            leave_id
        )

        if leave is None:

            raise RecordNotFoundException(
                "Leave Record Not Found."
            )

        leave.status = status.title()

        session.commit()

        session.refresh(leave)

        application(
            "Leave Status Updated Successfully."
        )

        return leave

    except SQLAlchemyError as e:

        session.rollback()

        exception(str(e))

        raise DatabaseException(
            "Database Error."
        )

    finally:

        session.close()


# =====================================================
# Delete Leave
# =====================================================

def delete_leave_api(leave_id):

    session = get_session()

    try:

        leave = session.get(
            LeaveRequest,
            leave_id
        )

        if leave is None:

            raise RecordNotFoundException(
                "Leave Record Not Found."
            )

        session.delete(leave)

        session.commit()

        application(
            "Leave Deleted Successfully."
        )

        return {

            "message":
                "Leave Deleted Successfully."

        }

    except SQLAlchemyError as e:

        session.rollback()

        exception(str(e))

        raise DatabaseException(
            "Database Error."
        )

    finally:

        session.close()


# =====================================================
# Display All Leaves
# =====================================================

def display_all_leaves_api():

    session = get_session()

    try:

        leaves = session.scalars(

            select(LeaveRequest)

        ).all()

        return leaves

    except SQLAlchemyError as e:

        exception(str(e))

        raise DatabaseException(
            "Database Error."
        )

    finally:

        session.close()