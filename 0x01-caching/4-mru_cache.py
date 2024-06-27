#!/usr/bin/python3
"""_summary_
"""

from collections import OrderedDict
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """_summary_

    Args:
        BaseCaching (_type_): _description_
    """
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """_summary_

        Args:
            key (_type_): _description_
            item (_type_): _description_
        """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discard = self.cache_data.popitem()
            print(f"DISCARD: {discard[0]}")

        self.cache_data[key] = item

    def get(self, key):
        """_summary_

        Args:
            key (_type_): _description_

        Returns:
            _type_: _description_
        """
        if key not in self.cache_data or key is None:
            return None
        self.cache_data.move_to_end(key)
        return self.cache_data[key]
