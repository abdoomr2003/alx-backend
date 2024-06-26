#!/usr/bin/env python3
from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discard = self.cache_data.popitem(False)
            print(f"DISCARD: {discard[0]}")
        if key == None or item == None:
            pass
        self.cache_data[key] = item


    def get(self, key):
        if key == None or self.cache_data[key] == None:
            return None
        return self.cache_data[key]
