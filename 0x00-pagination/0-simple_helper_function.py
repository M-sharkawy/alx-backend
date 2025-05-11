#!/usr/bin/env python3
"""
module return a tuple of size two
containing a start index and an end index
"""


def index_range(page: int, page_size: int):
    """
    function that return the start index and an end index
    page : int number of page
    page_size : int page size content
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
