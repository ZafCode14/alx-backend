#!/usr/bin/python3
"""Module with a python script"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """Class with a MRU caching system"""
    def __init__(self):
        """Method that initializes the class"""
        super().__init__()
        self.mru = []

    def put(self, key, item):
        """Method that puts to dict"""
        if key is not None or item is not None:
            if key in self.mru:
                self.mru.remove(key)
            self.mru.append(key)

            if key in self.cache_data.keys():
                del self.cache_data[key]
                self.cache_data[key] = item

            if len(self.cache_data) >= self.MAX_ITEMS \
                    and key not in self.cache_data.keys():
                mru_key = self.mru[-2]
                del self.cache_data[mru_key]
                self.mru.remove(mru_key)
                print("DISCARD: {}".format(mru_key))

            self.cache_data[key] = item

    def get(self, key):
        """Method that gets from dict"""
        if key not in self.cache_data or key is None:
            return None

        if key in self.mru:
            self.mru.remove(key)
        self.mru.append(key)

        return self.cache_data[key]
