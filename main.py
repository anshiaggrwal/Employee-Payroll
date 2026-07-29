from database_initializer import create_tables

from services.employee_repository import (
    add_employee,
    search_employee,
    update_employee,
    delete_employee,
    display_all_employees
)

from services.department_repository import (
    add_department,
    search_department,
    update_department,
    delete_department,
    display_all_departments
)

from services.report_repository import (
    employee_report,
    department_report,
    project_report,
    payroll_report,
    dashboard_report
)

from services.attendance_repository import (
    mark_attendance,
    search_attendance,
    update_attendance,
    delete_attendance,
    display_all_attendance
)

from services.leave_repository import (
    apply_leave,
    search_leave,
    update_leave_status,
    delete_leave,
    display_all_leaves
)

from services.project_repository import (
    add_project,
    search_project,
    update_project,
    delete_project,
    display_all_projects
)

from services.payroll_repository import (
    generate_payroll,
    search_payroll,
    update_payroll,
    delete_payroll,
    display_all_payrolls
)

def employee_menu():

    while True:

        print("\n")
        print("=" * 50)
        print("EMPLOYEE MANAGEMENT")
        print("=" * 50)

        print("1. Add Employee")
        print("2. Search Employee")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Display All Employees")
        print("6. Back")

        choice = input("\nEnter Choice : ")

        if choice == "1":

            add_employee()

        elif choice == "2":

            search_employee()

        elif choice == "3":

            update_employee()

        elif choice == "4":

            delete_employee()

        elif choice == "5":

            display_all_employees()

        elif choice == "6":

            break

        else:

            print("Invalid Choice.")

def department_menu():

    while True:

        print("\n")
        print("=" * 50)
        print("DEPARTMENT MANAGEMENT")
        print("=" * 50)

        print("1. Add Department")
        print("2. Search Department")
        print("3. Update Department")
        print("4. Delete Department")
        print("5. Display All Departments")
        print("6. Back")

        choice = input("\nEnter Choice : ")

        if choice == "1":

            add_department()

        elif choice == "2":

            search_department()

        elif choice == "3":

            update_department()

        elif choice == "4":

            delete_department()

        elif choice == "5":

            display_all_departments()

        elif choice == "6":

            break

        else:

            print("Invalid Choice.")

create_tables()

def attendance_menu():

    while True:

        print("\n")
        print("=" * 50)
        print("ATTENDANCE MANAGEMENT")
        print("=" * 50)

        print("1. Mark Attendance")
        print("2. Search Attendance")
        print("3. Update Attendance")
        print("4. Delete Attendance")
        print("5. Display All Attendance")
        print("6. Back")

        choice = input("\nEnter Choice : ")

        if choice == "1":

            mark_attendance()

        elif choice == "2":

            search_attendance()

        elif choice == "3":

            update_attendance()

        elif choice == "4":

            delete_attendance()

        elif choice == "5":

            display_all_attendance()

        elif choice == "6":

            break

        else:

            print("Invalid Choice.")

def leave_menu():

    while True:

        print("\n")
        print("=" * 50)
        print("LEAVE MANAGEMENT")
        print("=" * 50)

        print("1. Apply Leave")
        print("2. Search Leave")
        print("3. Update Leave Status")
        print("4. Delete Leave")
        print("5. Display All Leaves")
        print("6. Back")

        choice = input("\nEnter Choice : ")

        if choice == "1":

            apply_leave()

        elif choice == "2":

            search_leave()

        elif choice == "3":

            update_leave_status()

        elif choice == "4":

            delete_leave()

        elif choice == "5":

            display_all_leaves()

        elif choice == "6":

            break

        else:

            print("Invalid Choice.")

def project_menu():

    while True:

        print("\n")
        print("=" * 50)
        print("PROJECT MANAGEMENT")
        print("=" * 50)

        print("1. Add Project")
        print("2. Search Project")
        print("3. Update Project")
        print("4. Delete Project")
        print("5. Display All Projects")
        print("6. Back")

        choice = input("\nEnter Choice : ")

        if choice == "1":

            add_project()

        elif choice == "2":

            search_project()

        elif choice == "3":

            update_project()

        elif choice == "4":

            delete_project()

        elif choice == "5":

            display_all_projects()

        elif choice == "6":

            break

        else:

            print("Invalid Choice.")

def payroll_menu():

    while True:

        print("\n")
        print("=" * 50)
        print("PAYROLL MANAGEMENT")
        print("=" * 50)

        print("1. Generate Payroll")
        print("2. Search Payroll")
        print("3. Update Payroll")
        print("4. Delete Payroll")
        print("5. Display All Payrolls")
        print("6. Back")

        choice = input("\nEnter Choice : ")

        if choice == "1":

            generate_payroll()

        elif choice == "2":

            search_payroll()

        elif choice == "3":

            update_payroll()

        elif choice == "4":

            delete_payroll()

        elif choice == "5":

            display_all_payrolls()

        elif choice == "6":

            break

        else:

            print("Invalid Choice.")

def report_menu():

    while True:

        print("\n")
        print("=" * 50)
        print("REPORT MANAGEMENT")
        print("=" * 50)

        print("1. Employee Report")
        print("2. Department Report")
        print("3. Project Report")
        print("4. Payroll Report")
        print("5. Dashboard Report")
        print("6. Back")

        choice = input("\nEnter Choice : ")

        if choice == "1":

            employee_report()

        elif choice == "2":

            department_report()

        elif choice == "3":

            project_report()

        elif choice == "4":

            payroll_report()

        elif choice == "5":

            dashboard_report()

        elif choice == "6":

            break

        else:

            print("Invalid Choice.")

def main():

    while True:

        print("\n")
        print("=" * 60)
        print("EMPLOYEE PROJECT AND PAYROLL MANAGEMENT SYSTEM")
        print("=" * 60)

        print("1. Employee Management")
        print("2. Department Management")
        print("3. Attendance Management")
        print("4. Leave Management")
        print("5. Project Management")
        print("6. Payroll Management")
        print("7. Reports")
        print("8. Exit")

        choice = input("\nEnter Choice : ")

        if choice == "1":

            employee_menu()

        elif choice == "2":

            department_menu()

        elif choice == "3":

            attendance_menu()

        elif choice == "4":

            leave_menu()

        elif choice == "5":

            project_menu()

        elif choice == "6":

            payroll_menu()

        elif choice == "7":

            report_menu()

        elif choice == "8":

            print("\nThank You For Using The System.")
            break

        else:

            print("Invalid Choice. Please Try Again.")

if __name__ == "__main__":

    create_tables()

    main()
