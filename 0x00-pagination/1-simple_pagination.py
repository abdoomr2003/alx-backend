#!/usr/bin/env python3

"""
Server Pagination

This script provides a Server class to paginate a dataset of popular baby names
from a CSV file. It includes a function to calculate the start and end indices
for pagination.
"""

import csv
import math
from typing import List, Tuple


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


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset.

        Reads the CSV file and caches the dataset.

        Returns:
            List[List]: The cached dataset, excluding the header.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip the header

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get a page of the dataset.

        Args:
            page (int, optional): The page number to retrieve. Defaults to 1.
            page_size (int, optional): The number of items per page.
                Defaults to 10.

        Returns:
            List[List]: A list of rows for the specified page.
        """
        assert (type(page) == int) and (page > 0)
        assert (type(page_size) == int) and (page_size > 0)

        start_index, end_index = index_range(page, page_size)
        data_set = self.dataset()

        return data_set[start_index:end_index]
