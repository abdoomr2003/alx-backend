#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
    Retrieve a deletion-resilient page of the dataset.

    This method returns a dictionary containing the current page of the dataset
    based on the given start index and page size. It ensures that if rows have
    been deleted from the dataset, the user does not miss any items when
    paginating.

    Args:
        index (int, optional): The start index of the return page.
                               Must be within the valid range of dataset
                               indices.
                               Defaults to None.
        page_size (int, optional): The number of items to include in
                                the returned
                                   page. Defaults to 10.

    Returns:
        Dict: A dictionary containing:
            - 'index' (int): The current start index of the return page.
            - 'data' (List[List]): The actual page of the dataset.
            - 'page_size' (int): The current page size.
            - 'next_index' (int): The next index to query with.

    Raises:
        AssertionError: If the provided index is out of the valid range.
    """
        assert 1 <= index <= len(self.dataset())
        # if self.__indexed_dataset is None:
        #     dataset = self.dataset()
        # next_index = index + page_size
        # data = (self.dataset())[index: next_index]
        indexed_data = self.indexed_dataset()

        data = []
        next_index = index
        while len(data) < page_size and next_index < len(self.dataset()):
            if next_index in indexed_data:
                data.append(indexed_data[next_index])
            next_index += 1
        my_dict = {
            'index': index,
            'data': data,
            'page_size': page_size,
            'next_index': next_index
        }
        return my_dict
