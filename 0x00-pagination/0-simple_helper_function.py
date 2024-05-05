#!/usr/bin/env python3
"""Module with a python script"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Function that returns a tuple"""
    first_item = (page - 1) * page_size
    last_item = page * page_size
    return (first_item, last_item)
