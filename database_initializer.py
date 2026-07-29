from sqlalchemy.exc import SQLAlchemyError
from database import (
    Base,
    engine
)
from utilities.logger_config import (
    application_logger,
    exception_logger
)
from models.department_model import Department
from models.employee_model import Employee
from models.attendance_model import Attendance
from models.payroll_model import Payroll


def create_tables():

    try:

        application_logger.info("Creating database tables...")

        print("\n" + "=" * 70)
        print("CREATING DATABASE TABLES")
        print("=" * 70)

        Base.metadata.create_all(bind=engine)

        application_logger.info("All database tables created successfully.")

        print("\nAll Database Tables Created Successfully.")

    except SQLAlchemyError as error:

        exception_logger.exception(error)

        print("\nUnable to Create Database Tables.")
        print(f"Database Error : {error}")

        raise

    except Exception as error:

        exception_logger.exception(error)

        print("\nUnexpected Error While Creating Tables.")
        print(error)

        raise

    finally:

        application_logger.info("Database initialization completed.")

        print("\nDatabase Initialization Completed.")


def drop_tables():
    try:

        application_logger.info("Dropping database tables...")

        print("\n" + "=" * 70)
        print("DROPPING DATABASE TABLES")
        print("=" * 70)

        Base.metadata.drop_all(bind=engine)

        application_logger.info("All database tables dropped successfully.")

        print("\nAll Database Tables Dropped Successfully.")

    except SQLAlchemyError as error:

        exception_logger.exception(error)

        print("\nUnable to Drop Tables.")
        print(error)

        raise

    except Exception as error:

        exception_logger.exception(error)

        print("\nUnexpected Error.")
        print(error)

        raise

    finally:

        application_logger.info("Drop table operation completed.")

        print("\nDrop Table Operation Completed.")


def recreate_tables():
    """
    Drops all existing tables and recreates them.
    """

    try:

        application_logger.info("Recreating database tables...")

        drop_tables()
        create_tables()

        application_logger.info("Database recreated successfully.")

        print("\nDatabase Recreated Successfully.")

    except Exception as error:

        exception_logger.exception(error)

        print("\nDatabase Recreation Failed.")
        print(error)

        raise


if __name__ == "__main__":

    create_tables()