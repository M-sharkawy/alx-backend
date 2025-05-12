#!/usr/bin/env python3
"""
module to Implement a method named get_page
in the provided class for pagination
"""


import csv
import math
from typing import List, Dict, Any


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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
        Return a dict containing the page data
        and hypermedia pagination metadata:
        - page_size: number of items on this page
        - page: current page number
        - data: list of rows for this page
        - next_page: next page number or None
        - prev_page: previous page number or None
        - total_pages: total number of pages
        Implements HATEOAS link semantics for
        pagination.
        """
        assert isinstance(page, int) and page > 0, \
            "page must be a positive integer"
        assert isinstance(page_size, int) and page_size > 0, \
            "page_size must be a positive integer"

        full_data = self.dataset()
        total_items = len(full_data)
        total_pages = math.ceil(total_items / page_size)

        page_data = self.get_page(page, page_size)
        current_size = len(page_data)

        prev_page = page - 1 if page > 1 else None
        next_page = page + 1 if page < total_pages else None

        return {
            "page_size": current_size,
            "page": page,
            "data": page_data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages,
        }
