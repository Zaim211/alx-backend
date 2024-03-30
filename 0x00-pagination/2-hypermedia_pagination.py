#!/usr/bin/env python3
""" Hypermedia pagination """
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Function that return a tuple of size two containing
    a start index and an end index corresponding
    to the range of indexes to return in a list for
    those particular pagination parameters.
    """
    return ((page-1) * page_size, page * page_size)


class Server:
    """Server class to paginate a database of popular baby names.
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
        """ find the correct indexes to paginate the dataset correctly
        and return the appropriate page of the dataset """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        try:
            index = index_range(page, page_size)
            return self.dataset()[index[0]:index[1]]
        except Exception:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ returns a dictionary containing the following key-value pairs:
        """
        total_pages = len(self.dataset()) // page_size + 1
        data = self.get_page(page, page_size)
        return {'page_size': page_size,
                'page': page,
                'data': data,
                'total_pages': total_pages,
                'prev_page': page - 1 if page > 1 else None,
                'next_page': page + 1 if page + 1 <= total_pages else None
                }
