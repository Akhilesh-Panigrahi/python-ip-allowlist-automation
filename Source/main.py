"""
Python IP Allow List Automation
--------------------------------
Main application entry point.

This application automates the maintenance of an IP allow list by
removing unauthorized IP addresses listed in a separate remove list.

Author: Akhilesh Panigrahi
Project: Python IP Allow List Automation
Repository:
https://github.com/<your-username>/python-ip-allowlist-automation
"""

from pathlib import Path
import logging

from file_handler import read_ip_file, write_ip_file
from validator import clean_ip_list
from allowlist_manager import (
    remove_unauthorized_ips,
    generate_summary,
)
from logger_config import configure_logger


# -------------------------------------------------------------------
# Configuration
# -------------------------------------------------------------------

DATA_DIRECTORY = Path(__file__).resolve().parent.parent / "data"

ALLOW_LIST_FILE = DATA_DIRECTORY / "allow_list.txt"
REMOVE_LIST_FILE = DATA_DIRECTORY / "remove_list.txt"
OUTPUT_FILE = DATA_DIRECTORY / "updated_allow_list.txt"


# -------------------------------------------------------------------
# Main Application
# -------------------------------------------------------------------

def main() -> None:
    """
    Execute the IP allow list automation workflow.
    """

    configure_logger()
    logger = logging.getLogger(__name__)

    logger.info("=" * 60)
    logger.info("Python IP Allow List Automation")
    logger.info("=" * 60)

    try:

        # ----------------------------------------------------------
        # Load Files
        # ----------------------------------------------------------

        logger.info("Loading allow list...")

        allow_list = read_ip_file(ALLOW_LIST_FILE)

        logger.info("Loading remove list...")

        remove_list = read_ip_file(REMOVE_LIST_FILE)

        # ----------------------------------------------------------
        # Validate & Clean
        # ----------------------------------------------------------

        logger.info("Validating allow list...")

        allow_list, invalid_allow = clean_ip_list(allow_list)

        logger.info("Validating remove list...")

        remove_list, invalid_remove = clean_ip_list(remove_list)

        # ----------------------------------------------------------
        # Process Allow List
        # ----------------------------------------------------------

        logger.info("Removing unauthorized IP addresses...")

        updated_allow_list, removed_count = remove_unauthorized_ips(
            allow_list,
            remove_list,
        )

        # ----------------------------------------------------------
        # Save Results
        # ----------------------------------------------------------

        logger.info("Writing updated allow list...")

        write_ip_file(
            OUTPUT_FILE,
            updated_allow_list,
        )

        # ----------------------------------------------------------
        # Display Summary
        # ----------------------------------------------------------

        summary = generate_summary(
            original_count=len(allow_list),
            remove_count=len(remove_list),
            removed_count=removed_count,
            invalid_count=invalid_allow + invalid_remove,
            remaining_count=len(updated_allow_list),
            output_path=OUTPUT_FILE,
        )

        print(summary)

        logger.info("Application completed successfully.")

    except FileNotFoundError as error:

        logger.error(error)

    except PermissionError as error:

        logger.error("Permission denied: %s", error)

    except Exception as error:
        logger.exception(
            "Unexpected error occurred: %s",
            error,
        )


# -------------------------------------------------------------------
# Entry Point
# -------------------------------------------------------------------

if __name__ == "__main__":
    main()