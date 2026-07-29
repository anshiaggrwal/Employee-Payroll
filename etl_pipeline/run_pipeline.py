from etl_pipeline.employee_pipeline import run_employee_pipeline
from etl_pipeline.attendance_pipeline import run_attendance_pipeline

from utilities.logger_config import (
    application_logger,
    exception_logger
)


def run_etl_pipeline():

    try:
        application_logger.info("ETL Pipeline Started")
        run_employee_pipeline()
        run_attendance_pipeline()
        application_logger.info("ETL Pipeline Completed Successfully")

    except Exception as error:
        exception_logger.exception(error)
        raise

if __name__ == "__main__":
    run_etl_pipeline()