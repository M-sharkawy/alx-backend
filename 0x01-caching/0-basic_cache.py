#!/usr/bin/env python3
"""
model inherets from caching class
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache
    """

    def put(self, key, item):
        """Add an key and item in the cache"""
        if (key is None or item is None):
            return
        self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        if (key is None or not key):
            return None
        value = self.cache_data.get(key)
        return value
