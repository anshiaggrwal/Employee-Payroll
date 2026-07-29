"""
==========================================================
File        : project_service.py
Project     : Enterprise Employee Project and Payroll
              Management System
Description : Project Service Module
==========================================================
"""

from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError

from database import get_session
from models.project_model import Project

from validations.validation import (
    validate_project_name,
    validate_project_budget,
    validate_date
)

from utilities.logger_config import application, exception

from exceptions.custom_exception import (
    ValidationException,
    RecordNotFoundException,
    DatabaseException
)

def add_project():

    session = get_session()

    try:

        project = Project(

            project_name=validate_project_name(

                input("Enter Project Name : ")

            ),

            project_budget=validate_project_budget(

                input("Enter Project Budget : ")

            ),

            start_date=validate_date(

                input("Enter Start Date (YYYY-MM-DD) : ")

            ),

            end_date=validate_date(

                input("Enter End Date (YYYY-MM-DD) : ")

            ),

            status=input(

                "Enter Project Status : "

            ).title()

        )

        session.add(project)

        session.commit()

        application("Project Added Successfully.")

        print("\nProject Added Successfully.")

    except ValidationException as e:

        session.rollback()

        print(e)

    except SQLAlchemyError as e:

        session.rollback()

        exception(str(e))

        raise DatabaseException(
            "Database Error."
        )

    finally:

        session.close()

def search_project():

    session = get_session()

    try:

        project_id = int(

            input("Enter Project ID : ")

        )

        project = session.get(

            Project,
            project_id

        )

        if project is None:

            raise RecordNotFoundException(
                "Project Not Found."
            )

        print("\nProject Details")
        print("-" * 50)

        print(f"Project ID     : {project.project_id}")
        print(f"Project Name   : {project.project_name}")
        print(f"Budget         : {project.project_budget}")
        print(f"Start Date     : {project.start_date}")
        print(f"End Date       : {project.end_date}")
        print(f"Status         : {project.status}")

    except Exception as e:

        print(e)

    finally:

        session.close()

def update_project():

    session = get_session()

    try:

        project_id = int(

            input("Enter Project ID : ")

        )

        project = session.get(

            Project,
            project_id

        )

        if project is None:

            raise RecordNotFoundException(
                "Project Not Found."
            )

        project.project_name = validate_project_name(

            input("Enter New Project Name : ")

        )

        project.project_budget = validate_project_budget(

            input("Enter New Budget : ")

        )

        project.status = input(

            "Enter New Status : "

        ).title()

        session.commit()

        application("Project Updated Successfully.")

        print("\nProject Updated Successfully.")

    except ValidationException as e:

        session.rollback()

        print(e)

    except SQLAlchemyError as e:

        session.rollback()

        exception(str(e))

        raise DatabaseException(
            "Database Error."
        )

    finally:

        session.close()

def delete_project():

    session = get_session()

    try:

        project_id = int(

            input("Enter Project ID : ")

        )

        project = session.get(

            Project,
            project_id

        )

        if project is None:

            raise RecordNotFoundException(
                "Project Not Found."
            )

        session.delete(project)

        session.commit()

        application("Project Deleted Successfully.")

        print("\nProject Deleted Successfully.")

    except Exception as e:

        session.rollback()

        print(e)

    finally:

        session.close()

def display_all_projects():

    session = get_session()

    try:

        projects = session.scalars(

            select(Project)

        ).all()

        if not projects:

            print("\nNo Projects Found.")

            return

        print("\nProject Records")
        print("-" * 100)

        print(
            "{:<5} {:<20} {:<12} {:<12} {:<12} {:<12}".format(
                "ID",
                "Project Name",
                "Budget",
                "Start Date",
                "End Date",
                "Status"
            )
        )

        print("-" * 100)

        for project in projects:

            print(
                "{:<5} {:<20} {:<12} {:<12} {:<12} {:<12}".format(
                    project.project_id,
                    project.project_name,
                    project.project_budget,
                    str(project.start_date),
                    str(project.end_date),
                    project.status
                )
            )

    except SQLAlchemyError as e:

        exception(str(e))

        raise DatabaseException(
            "Database Error."
        )

    finally:

        session.close()