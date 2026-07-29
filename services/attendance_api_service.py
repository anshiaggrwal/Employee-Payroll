from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError

from database import get_session

from models.attendance_model import Attendance
from models.employee_model import Employee

from validations.validation import (
    validate_attendance_status,
    validate_date
)

from utilities.logger_config import application, exception

from exceptions.custom_exception import (
    RecordNotFoundException,
    DatabaseException,
    ValidationException
)


# ==========================================
# Mark Attendance
# ==========================================

def mark_attendance_api(
        employee_id,
        attendance_date,
        status
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

        attendance_date = validate_date(
            attendance_date
        )

        status = validate_attendance_status(
            status
        )

        attendance = Attendance(

            employee_id=employee_id,

            attendance_date=attendance_date,

            status=status

        )

        session.add(attendance)

        session.commit()

        session.refresh(attendance)

        application(
            "Attendance Marked Successfully."
        )

        return attendance

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


# ==========================================
# Search Attendance
# ==========================================

def search_attendance_api(employee_id):

    session = get_session()

    try:

        records = session.scalars(

            select(Attendance).where(

                Attendance.employee_id == employee_id

            )

        ).all()

        if not records:

            raise RecordNotFoundException(
                "Attendance Record Not Found."
            )

        return records

    except SQLAlchemyError as e:

        exception(str(e))

        raise DatabaseException(
            "Database Error."
        )

    finally:

        session.close()


# ==========================================
# Update Attendance
# ==========================================

def update_attendance_api(
        attendance_id,
        status
):

    session = get_session()

    try:

        attendance = session.get(

            Attendance,

            attendance_id

        )

        if attendance is None:

            raise RecordNotFoundException(
                "Attendance Record Not Found."
            )

        attendance.status = validate_attendance_status(
            status
        )

        session.commit()

        session.refresh(attendance)

        application(
            "Attendance Updated Successfully."
        )

        return attendance

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


# ==========================================
# Delete Attendance
# ==========================================

def delete_attendance_api(
        attendance_id
):

    session = get_session()

    try:

        attendance = session.get(

            Attendance,

            attendance_id

        )

        if attendance is None:

            raise RecordNotFoundException(
                "Attendance Record Not Found."
            )

        session.delete(attendance)

        session.commit()

        application(
            "Attendance Deleted Successfully."
        )

        return {

            "message":
                "Attendance Deleted Successfully."

        }

    except SQLAlchemyError as e:

        session.rollback()

        exception(str(e))

        raise DatabaseException(
            "Database Error."
        )

    finally:

        session.close()


# ==========================================
# Display All Attendance
# ==========================================

def display_all_attendance_api():

    session = get_session()

    try:

        attendance = session.scalars(

            select(Attendance)

        ).all()

        return attendance

    except SQLAlchemyError as e:

        exception(str(e))

        raise DatabaseException(
            "Database Error."
        )

    finally:

        session.close()