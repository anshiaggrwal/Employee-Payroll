"""
==========================================================
File        : project_router.py
Project     : Enterprise Employee Project and Payroll
              Management System
Description : Project FastAPI Router
==========================================================
"""

from fastapi import (
    APIRouter,
    HTTPException,
    status
)

from schemas.project_schema import (
    ProjectCreate,
    ProjectUpdate
)

from services.project_api_service import (
    add_project_api,
    search_project_api,
    update_project_api,
    delete_project_api,
    display_all_projects_api
)

from exceptions.custom_exception import (
    ValidationException,
    RecordNotFoundException,
    DatabaseException
)

router = APIRouter(
    prefix="/projects",
    tags=["Projects"]
)


# =====================================================
# Add Project
# =====================================================

@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    summary="Add Project"
)
def add_project(project: ProjectCreate):

    try:

        result = add_project_api(

            project.project_name,

            project.project_budget,

            project.start_date,

            project.end_date,

            project.status

        )

        return {

            "success": True,

            "message":
                "Project Added Successfully.",

            "data":
                result

        }

    except ValidationException as e:

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

    except DatabaseException as e:

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )


# =====================================================
# Search Project
# =====================================================

@router.get(
    "/{project_id}",
    summary="Search Project"
)
def search_project(project_id: int):

    try:

        project = search_project_api(project_id)

        return {

            "success": True,

            "data":
                project

        }

    except RecordNotFoundException as e:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )

    except DatabaseException as e:

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )


# =====================================================
# Display All Projects
# =====================================================

@router.get(
    "/",
    summary="Display All Projects"
)
def display_all_projects():

    try:

        projects = display_all_projects_api()

        return {

            "success": True,

            "count": len(projects),

            "data":
                projects

        }

    except DatabaseException as e:

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )


# =====================================================
# Update Project
# =====================================================

@router.put(
    "/{project_id}",
    summary="Update Project"
)
def update_project(

    project_id: int,

    project: ProjectUpdate

):

    try:

        result = update_project_api(

            project_id,

            project.project_name,

            project.project_budget,

            project.status

        )

        return {

            "success": True,

            "message":
                "Project Updated Successfully.",

            "data":
                result

        }

    except ValidationException as e:

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

    except RecordNotFoundException as e:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )

    except DatabaseException as e:

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )


# =====================================================
# Delete Project
# =====================================================

@router.delete(
    "/{project_id}",
    summary="Delete Project"
)
def delete_project(project_id: int):

    try:

        delete_project_api(project_id)

        return {

            "success": True,

            "message":
                "Project Deleted Successfully."

        }

    except RecordNotFoundException as e:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )

    except DatabaseException as e:

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )