#!/usr/bin/python3
"""Module with a python script"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Class with a basic caching system"""
    def __init__(self):
        """Method that initializes the class"""
        super().__init__()

    def put(self, key, item):
        """Method that puts to dict"""
        if key is not None or item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Method that gets from dict"""
        if key not in self.cache_data.keys() or key is None:
            return None
        return self.cache_data[key]
