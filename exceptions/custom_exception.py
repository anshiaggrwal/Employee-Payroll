"""
==========================================================
File        : custom_exception.py
Project     : Enterprise Employee Project and Payroll
              Management System
Description : Custom Exception Classes
==========================================================
"""

class EmployeePayrollException(Exception):
    """
    Base Exception Class
    """

    def __init__(self, message):

        super().__init__(message)

        self.message = message

    def __str__(self):

        return self.message

class ValidationException(EmployeePayrollException):
    """
    Raised when validation fails.
    """

    pass

class DatabaseException(EmployeePayrollException):
    """
    Raised when database operation fails.
    """

    pass

class EmployeeException(EmployeePayrollException):
    """
    Raised for Employee related errors.
    """

    pass

class DepartmentException(EmployeePayrollException):
    """
    Raised for Department related errors.
    """

    pass

class RoleException(EmployeePayrollException):
    """
    Raised for Role related errors.
    """

    pass

class AttendanceException(EmployeePayrollException):
    """
    Raised for Attendance related errors.
    """

    pass

class LeaveException(EmployeePayrollException):
    """
    Raised for Leave related errors.
    """

    pass

class ProjectException(EmployeePayrollException):
    """
    Raised for Project related errors.
    """

    pass

class TaskException(EmployeePayrollException):
    """
    Raised for Task related errors.
    """

    pass

class SalaryException(EmployeePayrollException):
    """
    Raised for Salary related errors.
    """

    pass

class PayrollException(EmployeePayrollException):
    """
    Raised for Payroll related errors.
    """

    pass

class ReportException(EmployeePayrollException):
    """
    Raised for Report generation errors.
    """

    pass

class DuplicateRecordException(EmployeePayrollException):
    """
    Raised when duplicate records are found.
    """

    pass

class RecordNotFoundException(EmployeePayrollException):
    """
    Raised when a record is not found.
    """

    pass

class AuthenticationException(EmployeePayrollException):
    """
    Raised for authentication failures.
    """

    pass

class AuthorizationException(EmployeePayrollException):
    """
    Raised for authorization failures.
    """

    pass