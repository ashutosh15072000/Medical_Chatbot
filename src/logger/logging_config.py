import logging
import os
import sys

from datetime import datetime

def configure_logging():
    """
    Configure logging to a file with a timestamped filename.

    This function sets up a logger that writes logs to a file with a timestamped filename
    and also prints logs to the console.

    Parameters:
    None

    Returns:
        logger: A logger object

    Example:
        >>> logger = configure_logging()
        >>> logger.info("This is a test message")
        This will create a log file with a timestamped filename in the "Logs" directory
        and write the log message to the file and print it to the console.
    """
    LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
    log_path = os.path.join(os.getcwd(), "Logs")
    os.makedirs(log_path, exist_ok=True)
    LOG_FILE_PATH = os.path.join(log_path, LOG_FILE)

    logger = logging.getLogger("MedicalChatbot")
    logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler(LOG_FILE_PATH)
    file_handler.setLevel(logging.INFO)
    formatter = logging.Formatter("[%(asctime)s] %(name)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger

# if __name__ == "__main__":
#     logger = configure_logging()
#     logger.info("This is a test message")