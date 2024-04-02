#!/usr/bin/env python3
""" Task-1 FIFO caching """

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache defines a FIFO caching system """
    def __init__(self):
        """Initialize the class with the parent's init method"""
        super().__init__()

    def put(self, key, item):
        """Cache a key-value pair"""
        if key is None or item is None:
            pass
        else:
            length = len(self.cache_data)
            if length > BaseCaching.MAX_ITEMS \
                    and key not in self.cache_data.keys():
                first_in = next(iter(self.cache_data.keys()))
                del self.cache_data[first_in]
                print('DISCARD: {}'.format(first_in))
            self.cache_data[key] = item

    def get(self, key):
        """Return the value linked to a given key, or None"""
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
