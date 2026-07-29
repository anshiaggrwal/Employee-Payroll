from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from database import SessionLocal
from models.attendance_model import Attendance

from utilities.logger_config import (
    application_logger,
    exception_logger
)

spark = (
    SparkSession.builder
    .appName("Attendance ETL Pipeline")
    .getOrCreate()
)

def extract_attendance():
    try:
        application_logger.info("Reading attendance CSV file.")

        attendance_df = spark.read.csv(
            "etl_pipeline/data/attendance.csv",
            header=True,
            inferSchema=True
        )
        application_logger.info(
            f"Attendance CSV Loaded Successfully. Total Records : {attendance_df.count()}"
        )
        return attendance_df

    except Exception as error:
        exception_logger.exception(error)
        raise

def transform_attendance(attendance_df):

    try:

        application_logger.info("Transforming attendance data.")

        # Remove duplicate employee records
        attendance_df = attendance_df.dropDuplicates(["employee_id"])

        # Remove extra spaces
        attendance_df = attendance_df.withColumn(
            "payroll_month",
            trim(col("payroll_month"))
        )

        application_logger.info("Attendance transformation completed.")

        return attendance_df

    except Exception as error:

        exception_logger.exception(error)
        raise
def validate_attendance(attendance_df):

    try:

        application_logger.info("Validating attendance records.")

        valid_attendance = attendance_df.filter(
            (col("present_days") >= 0) &
            (col("present_days") <= col("total_working_days")) &
            (col("leave_days") >= 0) &
            (col("overtime_hours") >= 0) &
            (col("bonus_amount") >= 0)
        )

        rejected_attendance = attendance_df.filter(
            (col("present_days") < 0) |
            (col("present_days") > col("total_working_days")) |
            (col("leave_days") < 0) |
            (col("overtime_hours") < 0) |
            (col("bonus_amount") < 0)
        )

        application_logger.info(
            f"Valid Records : {valid_attendance.count()}"
        )

        application_logger.info(
            f"Rejected Records : {rejected_attendance.count()}"
        )

        return valid_attendance, rejected_attendance

    except Exception as error:

        exception_logger.exception(error)
        raise

def load_attendance(valid_attendance):

    db = SessionLocal()

    try:

        application_logger.info(
            "Loading Attendance Data into Database."
        )

        attendance = valid_attendance.collect()

        for row in attendance:

            record = Attendance(

                employee_id=row.employee_id,

                payroll_month=row.payroll_month,

                total_working_days=row.total_working_days,

                present_days=row.present_days,

                leave_days=row.leave_days,

                overtime_hours=row.overtime_hours,

                bonus_amount=row.bonus_amount

            )

            db.add(record)

        db.commit()

        application_logger.info(
            "Attendance Loaded Successfully."
        )

    except Exception as error:

        db.rollback()

        exception_logger.exception(error)

        raise

    finally:

        db.close()

def run_attendance_pipeline():
    try:
        application_logger.info("Attendance ETL Pipeline Started.")

        attendance_df = extract_attendance()

        attendance_df = transform_attendance(attendance_df)

        valid_attendance, rejected_attendance = validate_attendance(attendance_df)

        load_attendance(valid_attendance)

        application_logger.info("Attendance ETL Pipeline Completed.")

    except Exception as error:
        exception_logger.exception(error)
        raise

    finally:
        spark.stop()
        application_logger.info("Spark Session Closed.")


if __name__ == "__main__":
    run_attendance_pipeline()