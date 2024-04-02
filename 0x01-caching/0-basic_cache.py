#!/usr/bin/env python3
""" Task-0 Basic dictionary """

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ caching system """
    def __init__(self):
        """ """
        BaseCaching.__init__(self)

    def put(self, key, item):
        """Store a key-value pair
        Args:
            Key
            Item
        """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """ return the value in self.cache_data linked to key """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
