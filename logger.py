"""
Logging configuration for gh-wrapper application
"""

import logging
import sys
from typing import Optional


class Logger:
    """
    Centralized logging configuration for the application
    """

    def __init__(
        self,
        name: str = "gh-wrapper",
        level: str = "INFO",
        log_file: Optional[str] = None,
    ):
        """
        Initialize logger with configurable settings

        Args:
            name: Logger name (default: gh-wrapper)
            level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
            log_file: Optional file path to write logs to
        """
        self.logger = logging.getLogger(name)
        self.logger.setLevel(getattr(logging, level.upper(), logging.INFO))

        # Avoid duplicate handlers
        if not self.logger.handlers:
            self._setup_handlers(log_file)

    def _setup_handlers(self, log_file: Optional[str] = None):
        """Configure console and optional file handlers"""

        # Console handler
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.DEBUG)
        console_formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        console_handler.setFormatter(console_formatter)
        self.logger.addHandler(console_handler)

        # File handler (optional)
        if log_file:
            file_handler = logging.FileHandler(log_file)
            file_handler.setLevel(logging.DEBUG)
            file_formatter = logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s"
            )
            file_handler.setFormatter(file_formatter)
            self.logger.addHandler(file_handler)

    def get_logger(self):
        """Return configured logger instance"""
        return self.logger


# Convenience function to get logger instance
def get_logger(
    name: str = "gh-wrapper", level: str = "INFO", log_file: Optional[str] = None
):
    """
    Get a configured logger instance

    Args:
        name: Logger name
        level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        log_file: Optional file path for logging

    Returns:
        logging.Logger instance
    """
    return Logger(name=name, level=level, log_file=log_file).get_logger()
