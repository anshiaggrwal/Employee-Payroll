from fastapi import FastAPI

from routers.employee_router import router as employee_router
from routers.department_router import router as department_router
from routers.attendance_router import router as attendance_router
from routers.leave_router import router as leave_router
from routers.project_router import router as project_router
from routers.payroll_router import router as payroll_router
from routers.report_router import router as report_router

app = FastAPI(
    title="Enterprise Employee Payroll Management System",
    version="1.0.0",
    description="Employee Payroll Management REST API"
)

app.include_router(employee_router)
app.include_router(department_router)
app.include_router(attendance_router)
app.include_router(leave_router)
app.include_router(project_router)
app.include_router(payroll_router)
app.include_router(report_router)


@app.get("/")
def home():
    return {
        "message": "Welcome to Enterprise Employee Payroll Management API"
    }