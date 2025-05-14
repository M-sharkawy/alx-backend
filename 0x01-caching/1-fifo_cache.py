#!/usr/bin/env python3
"""
model inherets from caching class
FIFO caching
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFO caching class"""
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Add an key and item in the cache"""
        if (key is not None or item is not None):
            self.cache_data[key] = item
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discard = sorted(self.cache_data)[0]
            self.cache_data.pop(discard)
            print("DISCARD: {}".format(discard))

    def get(self, key):
        """Get an item by key"""
        if (key is None or not key):
            return None
        value = self.cache_data.get(key)
        return value
