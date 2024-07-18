from src.logger import logging_config
logger = logging_config.configure_logging()
logger.info("This is a test message")