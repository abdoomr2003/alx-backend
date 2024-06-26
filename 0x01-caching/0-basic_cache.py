#!/usr/bin/env python3
"""
This module implements a basic caching system.
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache class that inherits from BaseCaching and provides a basic cache
    implementation.

    Attributes:
        cache_data (dict): The dictionary where cached data is stored.
    """
    def __init__(self):
        """
        Initialize the cache.
        """
        super().__init__()

    def put(self, key, item):
        """
        Add an item to the cache.

        Args:
            key (str): The key under which the item should be stored.
            item (any): The item to be stored in the cache.

        Returns:
            None
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache.

        Args:
            key (str): The key of the item to retrieve.

        Returns:
            any: The item stored in the cache, or None if the key is not found.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
