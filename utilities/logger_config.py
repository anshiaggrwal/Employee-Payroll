import logging
import os
from datetime import datetime


PROJECT_NAME = "Payroll-FastAPI"

current_date = datetime.now().strftime("%Y-%m-%d")

daily_log_folder = os.path.join(
    "logs",
    current_date
)

os.makedirs(
    daily_log_folder,
    exist_ok=True
)

log_file_name = (
    f"{PROJECT_NAME}-log-{current_date}.txt"
)

exception_file_name = (
    f"{PROJECT_NAME}-exception-{current_date}.txt"
)

log_file_path = os.path.join(
    daily_log_folder,
    log_file_name
)

exception_file_path = os.path.join(
    daily_log_folder,
    exception_file_name
)


application_logger = logging.getLogger(
    "application_logger"
)

application_logger.setLevel(logging.INFO)


exception_logger = logging.getLogger(
    "exception_logger"
)

exception_logger.setLevel(logging.ERROR)


log_formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(message)s"
)


application_file_handler = logging.FileHandler(
    log_file_path,
    mode="a",
    encoding="utf-8"
)

application_file_handler.setLevel(logging.INFO)
application_file_handler.setFormatter(log_formatter)


exception_file_handler = logging.FileHandler(
    exception_file_path,
    mode="a",
    encoding="utf-8"
)

exception_file_handler.setLevel(logging.ERROR)
exception_file_handler.setFormatter(log_formatter)


if not application_logger.handlers:
    application_logger.addHandler(
        application_file_handler
    )


if not exception_logger.handlers:
    exception_logger.addHandler(
        exception_file_handler
    )