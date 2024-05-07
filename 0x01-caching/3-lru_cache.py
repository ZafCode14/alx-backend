#!/usr/bin/python3
"""Module with a python script"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """Class with a LRU caching system"""
    def __init__(self):
        """Method that initializes the class"""
        super().__init__()
        self.lru = []

    def put(self, key, item):
        """Method that puts to dict"""
        if key is not None or item is not None:
            if key in self.lru:
                self.lru.remove(key)
            self.lru.append(key)

            if key in self.cache_data.keys():
                del self.cache_data[key]
                self.cache_data[key] = item

            if len(self.cache_data) >= self.MAX_ITEMS \
                    and key not in self.cache_data.keys():
                lru_key = self.lru[0]
                del self.cache_data[lru_key]
                self.lru.remove(lru_key)
                print("DISCARD: {}".format(lru_key))
            self.cache_data[key] = item

    def get(self, key):
        """Method that gets from dict"""
        if key not in self.cache_data or key is None:
            return None

        if key in self.lru:
            self.lru.remove(key)
        self.lru.append(key)

        return self.cache_data[key]
