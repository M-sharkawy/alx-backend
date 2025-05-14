#!/usr/bin/env python3
"""
model inherets from caching class
LIFO caching
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFO caching class"""
    def __init__(self):
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """ Add item in the cache"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.stack.remove(key)

        self.cache_data[key] = item
        self.stack.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last_key = self.stack.pop(-2)
            del self.cache_data[last_key]
            print("DISCARD:", last_key)

    def get(self, key):
        """Get an item by key"""
        if (key is None or not key):
            return None
        value = self.cache_data.get(key)
        return value
