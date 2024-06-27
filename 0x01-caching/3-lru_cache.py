#!/usr/bin/python3
"""
LRU caching system
"""

from collections import OrderedDict
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache class that inherits from BaseCaching and is an LRU caching system.
    """

    def __init__(self):
        """ Initialize the class """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Add an item in the cache. If the number of items in the cache exceeds
        the limit (MAX_ITEMS), remove the least recently used item (LRU).

        Args:
            key: The key under which the item is stored.
            item: The item to store in the cache.
        """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            popped = self.cache_data.popitem(last=False)
            print("DISCARD: {}".format(popped[0]))
        self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key.

        Args:
            key: The key to retrieve from the cache.

        Returns:
            The value associated with the key,
            or None if the key does not exist.
        """
        if key is None or key not in self.cache_data:
            return None
        self.cache_data.move_to_end(key)
        return self.cache_data.get(key)