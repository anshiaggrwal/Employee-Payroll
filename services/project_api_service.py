"""
==========================================================
File        : project_api_service.py
Project     : Enterprise Employee Project and Payroll
              Management System
Description : Project API Service Module
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


# =====================================================
# Add Project
# =====================================================

def add_project_api(
    project_name,
    project_budget,
    start_date,
    end_date,
    status
):

    session = get_session()

    try:

        project = Project(

            project_name=validate_project_name(
                project_name
            ),

            project_budget=validate_project_budget(
                project_budget
            ),

            start_date=validate_date(
                start_date
            ),

            end_date=validate_date(
                end_date
            ),

            status=status.title()

        )

        session.add(project)

        session.commit()

        session.refresh(project)

        application(
            "Project Added Successfully."
        )

        return project

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
# Search Project
# =====================================================

def search_project_api(project_id):

    session = get_session()

    try:

        project = session.get(
            Project,
            project_id
        )

        if project is None:

            raise RecordNotFoundException(
                "Project Not Found."
            )

        return project

    except SQLAlchemyError as e:

        exception(str(e))

        raise DatabaseException(
            "Database Error."
        )

    finally:

        session.close()


# =====================================================
# Update Project
# =====================================================

def update_project_api(
    project_id,
    project_name,
    project_budget,
    status
):

    session = get_session()

    try:

        project = session.get(
            Project,
            project_id
        )

        if project is None:

            raise RecordNotFoundException(
                "Project Not Found."
            )

        project.project_name = validate_project_name(
            project_name
        )

        project.project_budget = validate_project_budget(
            project_budget
        )

        project.status = status.title()

        session.commit()

        session.refresh(project)

        application(
            "Project Updated Successfully."
        )

        return project

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
# Delete Project
# =====================================================

def delete_project_api(project_id):

    session = get_session()

    try:

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

        application(
            "Project Deleted Successfully."
        )

        return {
            "message":
            "Project Deleted Successfully."
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
# Display All Projects
# =====================================================

def display_all_projects_api():

    session = get_session()

    try:

        projects = session.scalars(
            select(Project)
        ).all()

        return projects

    except SQLAlchemyError as e:

        exception(str(e))

        raise DatabaseException(
            "Database Error."
        )

    finally:

        session.close()