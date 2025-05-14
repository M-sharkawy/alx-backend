#!/usr/bin/env python3
"""MRU Caching"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRUCache class that uses MRU caching system"""

    def __init__(self):
        """Initialize"""
        super().__init__()
        self.usage_order = []

    def put(self, key, item):
        """Add item to cache using MRU eviction policy"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.usage_order.remove(key)

        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            mru_key = self.usage_order.pop()
            del self.cache_data[mru_key]
            print("DISCARD:", mru_key)

        self.cache_data[key] = item
        self.usage_order.append(key)

    def get(self, key):
        """Get an item by key"""
        if (key is None or not key):
            return None
        value = self.cache_data.get(key)
        return value
