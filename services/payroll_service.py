from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from utilities.logger_config import (
    application_logger,
    exception_logger
)

from models.payroll_model import Payroll

from schemas.payroll_schema import (
    PayrollCreate,
    PayrollUpdate
)

from repositories.payroll_repository import (
    create_payroll,
    get_all_payrolls,
    get_payroll_by_id,
    get_payroll_by_employee_and_month,
    update_payroll,
    delete_payroll
)

from repositories.employee_repository import (
    get_employee_by_id
)


def add_payroll(
    payroll: PayrollCreate,
    db: Session
):
    try:

        employee = get_employee_by_id(
            payroll.employee_id,
            db
        )

        if employee is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Employee not found."
            )

        existing_payroll = get_payroll_by_employee_and_month(
            payroll.employee_id,
            payroll.payroll_month,
            db
        )

        if existing_payroll:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Payroll already exists for this payroll month."
            )

        basic_salary = employee.basic_salary

        net_salary = (
            basic_salary
            + payroll.bonus_amount
            - payroll.deductions
        )

        new_payroll = Payroll(
            employee_id=payroll.employee_id,
            payroll_month=payroll.payroll_month,
            basic_salary=basic_salary,
            bonus_amount=payroll.bonus_amount,
            deductions=payroll.deductions,
            net_salary=net_salary
        )

        create_payroll(
            new_payroll,
            db
        )

        application_logger.info(
            f"Payroll created for Employee ID {payroll.employee_id}."
        )

        return new_payroll

    except HTTPException:
        raise

    except Exception as error:

        exception_logger.exception(error)

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Unable to create payroll."
        )


def fetch_all_payrolls(
    db: Session
):
    try:

        return get_all_payrolls(db)

    except Exception as error:

        exception_logger.exception(error)

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Unable to fetch payrolls."
        )


def fetch_payroll(
    payroll_id: int,
    db: Session
):
    try:

        payroll = get_payroll_by_id(
            payroll_id,
            db
        )

        if payroll is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Payroll not found."
            )

        return payroll

    except HTTPException:
        raise

    except Exception as error:

        exception_logger.exception(error)

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Unable to fetch payroll."
        )


def modify_payroll(
    payroll_id: int,
    payroll: PayrollUpdate,
    db: Session
):
    try:

        existing_payroll = get_payroll_by_id(
            payroll_id,
            db
        )

        if existing_payroll is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Payroll not found."
            )

        duplicate = get_payroll_by_employee_and_month(
            existing_payroll.employee_id,
            payroll.payroll_month,
            db
        )

        if (
            duplicate
            and
            duplicate.payroll_id != payroll_id
        ):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Payroll already exists for this payroll month."
            )

        employee = get_employee_by_id(
            existing_payroll.employee_id,
            db
        )

        basic_salary = employee.basic_salary

        net_salary = (
            basic_salary
            + payroll.bonus_amount
            - payroll.deductions
        )

        existing_payroll.payroll_month = payroll.payroll_month
        existing_payroll.basic_salary = basic_salary
        existing_payroll.bonus_amount = payroll.bonus_amount
        existing_payroll.deductions = payroll.deductions
        existing_payroll.net_salary = net_salary

        update_payroll(db)

        application_logger.info(
            f"Payroll ID {payroll_id} updated successfully."
        )

        return existing_payroll

    except HTTPException:
        raise

    except Exception as error:

        exception_logger.exception(error)

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Unable to update payroll."
        )


def remove_payroll(
    payroll_id: int,
    db: Session
):
    try:

        payroll = get_payroll_by_id(
            payroll_id,
            db
        )

        if payroll is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Payroll not found."
            )

        delete_payroll(
            payroll,
            db
        )

        application_logger.info(
            f"Payroll ID {payroll_id} deleted successfully."
        )

        return {
            "message": "Payroll deleted successfully."
        }

    except HTTPException:
        raise

    except Exception as error:

        exception_logger.exception(error)

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Unable to delete payroll."
        )