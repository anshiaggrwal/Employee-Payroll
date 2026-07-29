from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from database import SessionLocal
from models.employee_model import Employee
from models.department_model import Department
from datetime import datetime

from utilities.logger_config import (
    application_logger,
    exception_logger
)


spark = (
    SparkSession.builder
    .appName("Employee ETL Pipeline")
    .getOrCreate()
)

def extract_employee():

    try:

        application_logger.info("Reading employee CSV file.")

        employee_df = spark.read.csv(
            "etl_pipeline/data/employees.csv",
            header=True,
            inferSchema=True
        )

        application_logger.info(
            f"Employee CSV loaded successfully. Total Records : {employee_df.count()}"
        )

        return employee_df

    except Exception as error:

        exception_logger.exception(error)
        raise

def transform_employee(employee_df):

    try:

        application_logger.info("Transforming employee data.")

        # Remove duplicate employee records
        employee_df = employee_df.dropDuplicates(["employee_id"])

        # Remove leading & trailing spaces
        employee_df = employee_df.withColumn(
            "employee_name",
            trim(col("employee_name"))
        )

        employee_df = employee_df.withColumn(
            "email",
            lower(trim(col("email")))
        )

        employee_df = employee_df.withColumn(
            "department",
            trim(col("department"))
        )

        employee_df = employee_df.withColumn(
            "designation",
            trim(col("designation"))
        )

        employee_df = employee_df.withColumn(
            "employment_status",
            trim(col("employment_status"))
        )

        # Fill missing employee names
        employee_df = employee_df.withColumn(
            "employee_name",
            when(
                col("employee_name").isNull(),
                "Unknown Employee"
            ).otherwise(col("employee_name"))
        )

        # Format employee name
        employee_df = employee_df.withColumn(
            "employee_name",
            initcap(col("employee_name"))
        )

        application_logger.info(
            "Employee transformation completed."
        )

        return employee_df

    except Exception as error:

        exception_logger.exception(error)
        raise


def validate_employee(employee_df):

    try:

        application_logger.info(
            "Validating employee records."
        )

        valid_employee = employee_df.filter(
            col("basic_salary") > 0
        )

        rejected_employee = employee_df.filter(
            col("basic_salary") <= 0
        )

        application_logger.info(
            f"Valid Records : {valid_employee.count()}"
        )

        application_logger.info(
            f"Rejected Records : {rejected_employee.count()}"
        )

        return valid_employee, rejected_employee

    except Exception as error:

        exception_logger.exception(error)
        raise

def load_employee(valid_employee):

    db = SessionLocal()

    try:

        application_logger.info("Loading Employee Data into Database.")

        employees = valid_employee.collect()

        for row in employees:

            # Find Department
            department = db.query(Department).filter(
                Department.department_name == row.department
            ).first()

            # Create Department if not exists
            if department is None:

                department = Department(
                    department_name=row.department
                )

                db.add(department)
                db.commit()
                db.refresh(department)

            employee = Employee(

                employee_id=row.employee_id,

                employee_name=row.employee_name,

                email=row.email,

                department_id=department.department_id,

                designation=row.designation,

                date_of_joining=datetime.strptime(
                    row.date_of_joining,
                    "%d-%m-%Y"
                ).date(),

                basic_salary=row.basic_salary,

                employment_status=row.employment_status

            )

            db.merge(employee)

        db.commit()

        application_logger.info(
            "Employee Data Loaded Successfully."
        )

    except Exception as error:

        db.rollback()

        exception_logger.exception(error)

        raise

    finally:

        db.close()


def run_employee_pipeline():

    try:

        application_logger.info(
            "Employee ETL Pipeline Started."
        )

        employee_df = extract_employee()

        employee_df = transform_employee(employee_df)

        valid_employee, rejected_employee = validate_employee(
            employee_df
        )

        load_employee(valid_employee)

        application_logger.info(
            "Employee ETL Pipeline Completed."
        )

    except Exception as error:

        exception_logger.exception(error)
        raise

if __name__ == "__main__":

    try:

        run_employee_pipeline()

    finally:

        spark.stop()

        application_logger.info(
            "Spark Session Closed."
        )