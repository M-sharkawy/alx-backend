#!/usr/bin/env python3

"""module containing LRUCache class"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRUCache class that LRU Caching"""
    def __init__(self):
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """put item and key to cache accordin to LRU"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(list(self.cache_data.keys())) > self.MAX_ITEMS:
                least_recently_used_key = list(self.cache_data.keys())[0]
                del self.cache_data[least_recently_used_key]
                print(f"DISCARD: {least_recently_used_key}")

    def get(self, key):
        """Get an item by key"""
        if (key is None or not key):
            return None
        value = self.cache_data.get(key)
        return value
