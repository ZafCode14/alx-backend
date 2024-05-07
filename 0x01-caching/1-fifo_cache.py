#!/usr/bin/python3
"""Module with a python script"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Class with a FIFO caching system"""
    def __init__(self):
        """Method that initializes the class"""
        super().__init__()

    def put(self, key, item):
        """Method that puts to dict"""
        if key is not None or item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS \
                    and key not in self.cache_data.keys():
                first_key = list(self.cache_data.keys())[0]
                del self.cache_data[first_key]
                print("DISCARD: {}".format(first_key))
            self.cache_data[key] = item

    def get(self, key):
        """Method that gets from dict"""
        if key not in self.cache_data.keys() or key is None:
            return None
        return self.cache_data[key]
