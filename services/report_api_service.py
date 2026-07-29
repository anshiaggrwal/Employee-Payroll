"""
==========================================================
File        : report_api_service.py
Project     : Enterprise Employee Project and Payroll
              Management System
Description : Report API Service Module
==========================================================
"""

from sqlalchemy import select, func
from sqlalchemy.exc import SQLAlchemyError

from database import get_session

from models.employee_model import Employee
from models.department_model import Department
from models.project_model import Project
from models.payroll_model import Payroll

from utilities.logger_config import application, exception

from exceptions.custom_exception import (
    DatabaseException
)


# =====================================================
# Employee Report
# =====================================================

def employee_report_api():

    session = get_session()

    try:

        employees = session.scalars(

            select(Employee)

        ).all()

        return employees

    except SQLAlchemyError as e:

        exception(str(e))

        raise DatabaseException(
            "Unable to Generate Employee Report."
        )

    finally:

        session.close()


# =====================================================
# Department Report
# =====================================================

def department_report_api():

    session = get_session()

    try:

        departments = session.scalars(

            select(Department)

        ).all()

        return departments

    except SQLAlchemyError as e:

        exception(str(e))

        raise DatabaseException(
            "Unable to Generate Department Report."
        )

    finally:

        session.close()


# =====================================================
# Project Report
# =====================================================

def project_report_api():

    session = get_session()

    try:

        projects = session.scalars(

            select(Project)

        ).all()

        return projects

    except SQLAlchemyError as e:

        exception(str(e))

        raise DatabaseException(
            "Unable to Generate Project Report."
        )

    finally:

        session.close()


# =====================================================
# Payroll Report
# =====================================================

def payroll_report_api():

    session = get_session()

    try:

        payrolls = session.scalars(

            select(Payroll)

        ).all()

        return payrolls

    except SQLAlchemyError as e:

        exception(str(e))

        raise DatabaseException(
            "Unable to Generate Payroll Report."
        )

    finally:

        session.close()


# =====================================================
# Dashboard Report
# =====================================================

def dashboard_report_api():

    session = get_session()

    try:

        total_employees = session.scalar(

            select(
                func.count(
                    Employee.employee_id
                )
            )

        )

        total_departments = session.scalar(

            select(
                func.count(
                    Department.department_id
                )
            )

        )

        total_projects = session.scalar(

            select(
                func.count(
                    Project.project_id
                )
            )

        )

        total_payrolls = session.scalar(

            select(
                func.count(
                    Payroll.payroll_id
                )
            )

        )

        application(
            "Dashboard Report Generated."
        )

        return {

            "total_employees": total_employees,

            "total_departments": total_departments,

            "total_projects": total_projects,

            "total_payrolls": total_payrolls

        }

    except SQLAlchemyError as e:

        exception(str(e))

        raise DatabaseException(
            "Unable to Generate Dashboard Report."
        )

    finally:

        session.close()