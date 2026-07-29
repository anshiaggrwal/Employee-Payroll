"""
==========================================================
File        : database.py
Project     : Enterprise Employee Project and Payroll
              Management System
Description : Database configuration using SQLAlchemy ORM
==========================================================
"""

from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

USERNAME = "root"
PASSWORD = ""          
HOST = "localhost"
PORT = "3006"
DATABASE = "employee_payroll_db"

DATABASE_URL = ("mysql+pymysql://root:Revanth%40123@localhost:3006/employee_payroll_db"
)

Base = declarative_base()

try:

    engine = create_engine(

        DATABASE_URL,

        echo=True,

        future=True

    )

    print("\n" + "=" * 60)
    print("Database Engine Created Successfully")
    print("=" * 60)

except SQLAlchemyError as error:

    print("\nUnable to create database engine.")

    print(f"Database Error : {error}")

    raise

except Exception as error:

    print("\nUnexpected Error While Creating Engine.")

    print(f"Error : {error}")

    raise

finally:

    print("\nDatabase Engine Initialization Completed.")

try:

    SessionLocal = sessionmaker(

        bind=engine,

        autoflush=False,

        autocommit=False,

        expire_on_commit=False

    )

    print("\nSession Factory Created Successfully.")

except SQLAlchemyError as error:

    print("\nUnable to Create Session Factory.")

    print(f"Database Error : {error}")

    raise

except Exception as error:

    print("\nUnexpected Error.")

    print(error)

    raise

finally:

    print("\nSession Factory Initialization Completed.")


def get_session():
    """
    Returns a SQLAlchemy session object.
    """

    session = None

    try:

        session = SessionLocal()

        return session

    except SQLAlchemyError as error:

        print("\nUnable to Create Database Session.")

        print(error)

        raise

    except Exception as error:

        print("\nUnexpected Error.")

        print(error)

        raise