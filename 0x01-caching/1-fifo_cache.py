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
        """ Add item in the cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(list(self.cache_data.keys())) > self.MAX_ITEMS:
                first_key = list(self.cache_data.keys())[0]
                del self.cache_data[first_key]
                print(f"DISCARD: {first_key}")

    def get(self, key):
        """Get an item by key"""
        if (key is None or not key):
            return None
        value = self.cache_data.get(key)
        return value
