"""
logger_config.py
----------------
Application logging configuration.
"""

import logging
import sys


def configure_logger() -> None:
    """
    Configure application logging.
    """

    logging.basicConfig(
        level=logging.WARNING,
        format="[%(levelname)s] %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout)
        ],
        force=True,
    )