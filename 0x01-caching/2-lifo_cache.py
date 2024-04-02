#!/usr/bin/env python3
""" LIFO Caching """

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ FIFOCache defines a FIFO caching system """
    def __init__(self):
        """ Initialize the class with the parent's init method """
        super().__init__()

    def put(self, key, item):
        """ Cache a key-value pair """
        if key is None or item is None:
            pass
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS \
                    and key not in self.cache_data.keys():
                last_key = self.cache_data.popitem()
                print('DISCARD: {}'.format(last_key))
        self.cache_data[key] = item

    def get(self, key):
        """ Return the value linked to a given key, or None """
        if key is None or key not in self.cache_data(keys):
            return None
        return self.cache_data.get(key)
