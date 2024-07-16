import logging
import os

from datetime import datetime

def configure_logging(msg):
    """
    Configure logging to a file with a timestamped filename.

    Returns:
        None
    """
    LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
    log_path = os.path.join(os.getcwd(), "Logs")
    os.makedirs(log_path, exist_ok=True)
    LOG_FILE_PATH = os.path.join(log_path, LOG_FILE)

    logging.basicConfig(
        filename=LOG_FILE_PATH,
        format="[%(asctime)s] %(name)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.DEBUG
    )
    return logging.info(msg)

    """
Module for configuring logging to a file with a timestamped filename.

The log file is created in a "Logs" directory in the current working directory.
The filename is in the format "MM_DD_YYYY_HH_MM_SS.log".

Example:
    >>> import logging_config
    >>> logging_config
    # This will create a log file with the current timestamp and configure logging to it.
"""

if __name__ == "__main__":
