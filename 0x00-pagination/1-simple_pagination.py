#!/usr/bin/env python3
"""
module to Implement a method named get_page
in the provided class for pagination
"""


import csv
import math
from typing import List


def index_range(page: int, page_size: int):
    """
    function that return the start index and an end index
    page : int number of page
    page_size : int page size content
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """pagination methods of pages"""
        assert isinstance(page, int) and page > 0, \
            "page must be greater than 0"
        assert isinstance(page_size, int) and page_size > 0, \
            "page_size must be greater than 0"

        data = self.__dataset
        [start, end] = index_range(page, page_size)
        return data[start:end]
