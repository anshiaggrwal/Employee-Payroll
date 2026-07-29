import os
import logging
from datetime import datetime

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

today = datetime.now().strftime("%Y-%m-%d")

application_log = os.path.join(LOG_DIR, f"application_{today}.log")
exception_log = os.path.join(LOG_DIR, f"exception_{today}.log")


def application(message):

    logger = logging.getLogger("application_logger")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        file_handler = logging.FileHandler(application_log)
        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(message)s"
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    logger.info(message)

def exception(message):

    logger = logging.getLogger("exception_logger")
    logger.setLevel(logging.ERROR)

    if not logger.handlers:
        file_handler = logging.FileHandler(exception_log)
        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(message)s"
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    logger.error(message)