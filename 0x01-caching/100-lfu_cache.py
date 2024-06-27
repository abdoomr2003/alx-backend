#!/usr/bin/env python3
"""
LFUCache module implements a caching system using
the Least Frequently Used (LFU) algorithm.
"""

from collections import OrderedDict, defaultdict
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache class implements a caching system with LFU eviction policy.

    Args:
        BaseCaching (class): Base class with cache system interface.
    """
    def __init__(self):
        """
        Initialize the cache.

        Attributes:
            cache_data (OrderedDict): Dictionary to store the cache items.
            frequency (defaultdict): Dictionary to store the frequency
            count of items.
            lru (defaultdict): Dictionary to store the order of insertion for
            LRU policy within the same frequency count.
            lru_counter (int): Counter to maintain the order of insertion.
        """
        super().__init__()
        self.cache_data = OrderedDict()
        self.frequency = defaultdict(int)
        self.lru = defaultdict(OrderedDict)
        self.lru_counter = 0

    def put(self, key, item):
        """
        Add an item to the cache. If the cache exceeds its maximum size,
        remove the least frequently used item, and if there's a tie,
        remove the least recently used item within the same frequency.

        Args:
            key (str): The key under which the item should be stored.
            item (any): The item to be stored in the cache.

        Returns:
            None
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.get(key)
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            min_freq = min(self.frequency.values())
            lru_key = next(iter(self.lru[min_freq]))
            self.cache_data.pop(lru_key)
            self.frequency.pop(lru_key)
            self.lru[min_freq].pop(lru_key)
            if not self.lru[min_freq]:
                self.lru.pop(min_freq)
            print(f"DISCARD: {lru_key}")

        self.cache_data[key] = item
        self.frequency[key] = 1
        self.lru[1][key] = self.lru_counter
        self.lru_counter += 1

    def get(self, key):
        """
        Retrieve an item from the cache by key.

        Args:
            key (str): The key of the item to be retrieved.

        Returns:
            any: The value associated with the key,
            or None if the key is not found.
        """
        if key is None or key not in self.cache_data:
            return None

        value = self.cache_data[key]

        freq = self.frequency[key]
        self.frequency[key] += 1
        self.lru[freq].pop(key)
        if not self.lru[freq]:
            self.lru.pop(freq)
        self.lru[freq + 1][key] = self.lru_counter
        self.lru_counter += 1

        return value
