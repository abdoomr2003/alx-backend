#!/usr/bin/env python3

"""
Index Range Calculation

This script provides a function to calculate the start and end indices for
pagination based on the given page number and page size.
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end indices for a given page number and page size.

    Args:
        page (int): The page number, 1-indexed.
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start index (inclusive) and
        end index (exclusive) for the given page.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size

    return (start_index, end_index)
