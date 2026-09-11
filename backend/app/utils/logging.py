import os
import logging
from logging.handlers import RotatingFileHandler
from app.config.config import settings

def setup_logger(name: str, log_file: str, level=logging.INFO) -> logging.Logger:
    """Configures a logger with both console and rotating file output."""
    os.makedirs(settings.LOGS_DIR, exist_ok=True)
    file_path = os.path.join(settings.LOGS_DIR, log_file)
    
    formatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] [%(name)s]: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Avoid duplicate handlers if setup_logger is called multiple times
    if not logger.handlers:
        # File handler (10MB max, 3 backups)
        file_handler = RotatingFileHandler(file_path, maxBytes=10*1024*1024, backupCount=3)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger

# Dedicated loggers as specified in project structure
ingestion_logger = setup_logger("ingestion", "ingestion.log")
indexing_logger = setup_logger("indexing", "indexing.log")
query_logger = setup_logger("query", "query.log")
error_logger = setup_logger("error", "error.log", level=logging.ERROR)
