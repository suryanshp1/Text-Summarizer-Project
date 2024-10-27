import os
import sys
import logging

logging_str = "[%(asctime)s][%(levelname)s][%(module)s]: %(message)s"

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE_PATH = os.path.join(LOG_DIR, "running_logs.log")

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[logging.FileHandler(LOG_FILE_PATH), logging.StreamHandler(sys.stdout)],
)

logger = logging.getLogger(__name__)