"""
validator.py
------------
Validates and cleans IP address data.
"""

import ipaddress


def validate_ip(ip: str) -> bool:
    """
    Validate an IPv4 or IPv6 address.

    Args:
        ip: IP address string.

    Returns:
        True if valid.
    """

    try:
        ipaddress.ip_address(ip)
        return True

    except ValueError:
        return False


def clean_ip_list(ip_list: list[str]) -> tuple[list[str], int]:
    """
    Remove blank lines, duplicate entries,
    and invalid IP addresses.

    Args:
        ip_list: Raw IP list.

    Returns:
        (cleaned_list, invalid_count)
    """

    cleaned = []
    seen = set()
    invalid = 0

    for ip in ip_list:

        ip = ip.strip()

        if not ip:
            continue

        if not validate_ip(ip):
            invalid += 1
            continue

        if ip in seen:
            continue

        seen.add(ip)
        cleaned.append(ip)

    return cleaned, invalid