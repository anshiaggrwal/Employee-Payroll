"""
==========================================================
File        : report_router.py
Project     : Enterprise Employee Project and Payroll
              Management System
Description : Report FastAPI Router
==========================================================
"""

from fastapi import (
    APIRouter,
    HTTPException,
    status
)

from services.report_api_service import (
    employee_report_api,
    department_report_api,
    project_report_api,
    payroll_report_api,
    dashboard_report_api
)

from exceptions.custom_exception import (
    DatabaseException
)

router = APIRouter(
    prefix="/reports",
    tags=["Reports"]
)


# =====================================================
# Employee Report
# =====================================================

@router.get(
    "/employees",
    summary="Employee Report"
)
def employee_report():

    try:

        employees = employee_report_api()

        return {

            "success": True,

            "count": len(employees),

            "data": employees

        }

    except DatabaseException as e:

        raise HTTPException(

            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,

            detail=str(e)

        )


# =====================================================
# Department Report
# =====================================================

@router.get(
    "/departments",
    summary="Department Report"
)
def department_report():

    try:

        departments = department_report_api()

        return {

            "success": True,

            "count": len(departments),

            "data": departments

        }

    except DatabaseException as e:

        raise HTTPException(

            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,

            detail=str(e)

        )


# =====================================================
# Project Report
# =====================================================

@router.get(
    "/projects",
    summary="Project Report"
)
def project_report():

    try:

        projects = project_report_api()

        return {

            "success": True,

            "count": len(projects),

            "data": projects

        }

    except DatabaseException as e:

        raise HTTPException(

            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,

            detail=str(e)

        )


# =====================================================
# Payroll Report
# =====================================================

@router.get(
    "/payrolls",
    summary="Payroll Report"
)
def payroll_report():

    try:

        payrolls = payroll_report_api()

        return {

            "success": True,

            "count": len(payrolls),

            "data": payrolls

        }

    except DatabaseException as e:

        raise HTTPException(

            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,

            detail=str(e)

        )


# =====================================================
# Dashboard Report
# =====================================================

@router.get(
    "/dashboard",
    summary="Dashboard Report"
)
def dashboard_report():

    try:

        dashboard = dashboard_report_api()

        return {

            "success": True,

            "data": dashboard

        }

    except DatabaseException as e:

        raise HTTPException(

            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,

            detail=str(e)

        )
    