"""
allowlist_manager.py
--------------------
Business logic for managing IP allow lists.
"""

from pathlib import Path


def remove_unauthorized_ips(
    allow_list: list[str],
    remove_list: list[str],
) -> tuple[list[str], int]:
    """
    Remove unauthorized IP addresses.

    Args:
        allow_list: Current allow list.
        remove_list: IPs to remove.

    Returns:
        (updated_allow_list, removed_count)
    """

    remove_set = set(remove_list)

    updated = [
        ip
        for ip in allow_list
        if ip not in remove_set
    ]

    removed_count = len(allow_list) - len(updated)

    return updated, removed_count


def generate_summary(
    *,
    original_count: int,
    remove_count: int,
    removed_count: int,
    invalid_count: int,
    remaining_count: int,
    output_path: Path,
) -> str:
    """
    Generate execution summary.
    """

    return f"""
============================================================
                EXECUTION SUMMARY
============================================================

Original Allow List : {original_count}

Remove List Entries : {remove_count}

Removed             : {removed_count}

Invalid IPs         : {invalid_count}

Remaining           : {remaining_count}

Updated File

{output_path}

============================================================
Application completed successfully.
============================================================
""".strip()