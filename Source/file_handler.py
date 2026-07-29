"""
file_handler.py
---------------
Handles reading and writing IP address files.
"""

from pathlib import Path


def read_ip_file(file_path: Path) -> list[str]:
    """
    Read IP addresses from a text file.

    Args:
        file_path: Path to the input file.

    Returns:
        List of IP addresses.
    """

    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    with file_path.open("r", encoding="utf-8") as file:
        return file.read().splitlines()


def write_ip_file(file_path: Path, ip_addresses: list[str]) -> None:
    """
    Write IP addresses to a text file.

    Args:
        file_path: Destination file.
        ip_addresses: List of IP addresses.
    """

    with file_path.open("w", encoding="utf-8") as file:
        file.write("\n".join(ip_addresses))