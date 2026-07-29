
import re
from datetime import datetime

from exceptions.custom_exception import ValidationException

def validate_required(value, field_name):
    """
    Validates empty input.
    """

    if value is None or str(value).strip() == "":

        raise ValidationException(
            f"{field_name} cannot be empty."
        )

    return True

def validate_employee_id(employee_id):
    """
    Employee ID should be a positive integer.
    """

    try:

        employee_id = int(employee_id)

        if employee_id <= 0:

            raise ValidationException(
                "Employee ID must be greater than zero."
            )

        return employee_id

    except ValueError:

        raise ValidationException(
            "Employee ID must be numeric."
        )


def validate_employee_name(name):

    validate_required(name, "Employee Name")

    if not re.fullmatch(r"[A-Za-z ]{3,50}", name):

        raise ValidationException(
            "Employee name should contain only alphabets "
            "and must be between 3 and 50 characters."
        )

    return name.title()


def validate_age(age):

    try:

        age = int(age)

        if age < 18 or age > 60:

            raise ValidationException(
                "Employee age should be between 18 and 60."
            )

        return age

    except ValueError:

        raise ValidationException(
            "Age must be numeric."
        )


def validate_email(email):

    validate_required(email, "Email")

    pattern = (
        r"^[A-Za-z0-9._%+-]+"
        r"@[A-Za-z0-9.-]+"
        r"\.[A-Za-z]{2,}$"
    )

    if not re.fullmatch(pattern, email):

        raise ValidationException(
            "Invalid email address."
        )

    return email.lower()


def validate_phone(phone):

    phone = str(phone)

    if not re.fullmatch(r"[6-9]\d{9}", phone):

        raise ValidationException(
            "Phone number must contain "
            "10 digits starting from 6-9."
        )

    return phone

def validate_department_name(name):

    validate_required(name, "Department Name")

    if len(name) < 2:

        raise ValidationException(
            "Department name is too short."
        )

    return name.title()

def validate_role_name(role):

    validate_required(role, "Role")

    return role.title()


def validate_salary_grade(grade):

    try:

        grade = float(grade)

        if grade <= 0:

            raise ValidationException(
                "Salary grade must be positive."
            )

        return grade

    except ValueError:

        raise ValidationException(
            "Salary grade must be numeric."
        )

def validate_attendance_status(status):

    status = status.upper()

    valid_status = [

        "P",
        "A",
        "L"

    ]

    if status not in valid_status:

        raise ValidationException(
            "Attendance status must be "
            "P, A or L."
        )

    return status

def validate_leave_days(days):

    try:

        days = int(days)

        if days <= 0:

            raise ValidationException(
                "Leave days must be greater than zero."
            )

        return days

    except ValueError:

        raise ValidationException(
            "Leave days must be numeric."
        )

def validate_project_name(project_name):

    validate_required(
        project_name,
        "Project Name"
    )

    if len(project_name) < 3:

        raise ValidationException(
            "Project name is too short."
        )

    return project_name.title()


def validate_project_budget(budget):

    try:

        budget = float(budget)

        if budget <= 0:

            raise ValidationException(
                "Budget should be greater than zero."
            )

        return budget

    except ValueError:

        raise ValidationException(
            "Budget should be numeric."
        )

def validate_salary(amount):

    try:

        amount = float(amount)

        if amount <= 0:

            raise ValidationException(
                "Salary should be greater than zero."
            )

        return amount

    except ValueError:

        raise ValidationException(
            "Salary must be numeric."
        )


def validate_percentage(value):

    try:

        value = float(value)

        if value < 0 or value > 100:

            raise ValidationException(
                "Percentage should be "
                "between 0 and 100."
            )

        return value

    except ValueError:

        raise ValidationException(
            "Percentage must be numeric."
        )

def validate_date(date_string):

    try:

        return datetime.strptime(
            date_string,
            "%Y-%m-%d"
        )

    except ValueError:

        raise ValidationException(
            "Date should be in "
            "YYYY-MM-DD format."
        )

def validate_yes_no(choice):

    choice = choice.upper()

    if choice not in ["Y", "N"]:

        raise ValidationException(
            "Enter only Y or N."
        )

    return choice

def validate_menu_choice(choice, minimum, maximum):

    try:

        choice = int(choice)

        if choice < minimum or choice > maximum:

            raise ValidationException(
                f"Choice must be between "
                f"{minimum} and {maximum}."
            )

        return choice

    except ValueError:

        raise ValidationException(
            "Menu choice should be numeric."
        )