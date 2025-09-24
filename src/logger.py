import os
import logging
from datetime import datetime


LOG_DIR = os.path.join(os.getcwd(), "logs")
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE)

logger = logging.getLogger()  
logger.setLevel(logging.INFO)

if logger.hasHandlers():
    logger.handlers.clear()


file_handler = logging.FileHandler(LOG_FILE_PATH)
file_handler.setLevel(logging.INFO)
file_formatter = logging.Formatter("[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(file_formatter)
logger.addHandler(console_handler)


logger.info(f"Logging initialized. Log file created at: {LOG_FILE_PATH}")

