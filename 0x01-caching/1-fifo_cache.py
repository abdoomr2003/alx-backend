#!/usr/bin/env python3
"""
This module contains the FIFOCache class that implements a caching system using
the First In, First Out (FIFO) algorithm.
"""

from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """
    FIFOCache class implements a caching system with FIFO eviction policy.

    Args:
        BaseCaching (class): Base class with cache system interface.
    """

    def __init__(self):
        """
        Initialize the cache.

        Attributes:
            cache_data (OrderedDict): Dictionary to store the cache items while
            maintaining their insertion order.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Add an item to the cache. If the cache exceeds its maximum size,
        remove the first added item.

        Args:
            key (str): The key under which the item should be stored.
            item (any): The item to be stored in the cache.

        Returns:
            None
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discard = self.cache_data.popitem(False)
            print(f"DISCARD: {discard[0]}")
        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache by key.

        Args:
            key (str): The key of the item to be retrieved.

        Returns:
            any: The value associated with the key, or None if the key is not
            found.
        """
        if key is None:
            return None
        return self.cache_data.get(key)
