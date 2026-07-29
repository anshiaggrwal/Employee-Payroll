from fastapi import FastAPI

from routers.department_router import department_router
from routers.employee_router import employee_router
from routers.attendance_router import attendance_router
from routers.payroll_router import payroll_router

app = FastAPI(
    title="Employee Payroll Management System"
)

app.include_router(department_router)
app.include_router(employee_router)
app.include_router(attendance_router)
app.include_router(payroll_router)


@app.get("/")
def home():
    return {
        "message": "Welcome to Employee Payroll Management System API"
    }