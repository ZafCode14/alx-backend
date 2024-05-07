#!/usr/bin/python3
"""Module with a python script"""
from base_caching import BaseCaching
from collections import Counter


class LFUCache(BaseCaching):
    """Class with a LFU caching system"""
    def __init__(self):
        """Method that initializes the class"""
        super().__init__()
        self.lfu = []

    def put(self, key, item):
        """Method that puts to dict"""
        if key is not None or item is not None:
            self.lfu.append(key)

            if key in self.cache_data.keys():
                del self.cache_data[key]
                self.cache_data[key] = item

            if len(self.cache_data) >= self.MAX_ITEMS \
                    and key not in self.cache_data.keys():
                counter = Counter(self.lfu[0:-1])
                lfu_key = min(counter, key=counter.get)

                del self.cache_data[lfu_key]
                self.lfu = [x for x in self.lfu if x != lfu_key]
                print("DISCARD: {}".format(lfu_key))
            self.cache_data[key] = item

    def get(self, key):
        """Method that gets from dict"""
        if key not in self.cache_data or key is None:
            return None

        self.lfu.append(key)

        return self.cache_data[key]
