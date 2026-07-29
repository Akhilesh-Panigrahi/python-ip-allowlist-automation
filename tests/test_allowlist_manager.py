"""
Unit tests for allowlist_manager.py
"""

from pathlib import Path

from src.allowlist_manager import (
    remove_unauthorized_ips,
    generate_summary,
)


def test_remove_unauthorized_ips():
    """
    Ensure IP addresses present in the remove list
    are removed correctly.
    """

    allow_list = [
        "192.168.1.10",
        "192.168.1.20",
        "10.0.0.5",
        "172.16.0.8",
    ]

    remove_list = [
        "10.0.0.5",
        "172.16.0.8",
    ]

    updated, removed = remove_unauthorized_ips(
        allow_list,
        remove_list,
    )

    assert updated == [
        "192.168.1.10",
        "192.168.1.20",
    ]

    assert removed == 2


def test_remove_empty_list():
    """
    Removing nothing should leave the allow list unchanged.
    """

    allow_list = [
        "192.168.1.10",
        "192.168.1.20",
    ]

    remove_list = []

    updated, removed = remove_unauthorized_ips(
        allow_list,
        remove_list,
    )

    assert updated == allow_list

    assert removed == 0


def test_remove_everything():
    """
    Removing every IP should return an empty list.
    """

    allow_list = [
        "192.168.1.10",
        "192.168.1.20",
    ]

    remove_list = [
        "192.168.1.10",
        "192.168.1.20",
    ]

    updated, removed = remove_unauthorized_ips(
        allow_list,
        remove_list,
    )

    assert updated == []

    assert removed == 2


def test_summary_generation():
    """
    Verify execution summary formatting.
    """

    summary = generate_summary(
        original_count=15,
        remove_count=4,
        removed_count=4,
        invalid_count=0,
        remaining_count=11,
        output_path=Path("data/updated_allow_list.txt"),
    )

    assert "EXECUTION SUMMARY" in summary
    assert "15" in summary
    assert "11" in summary
    assert "updated_allow_list.txt" in summary