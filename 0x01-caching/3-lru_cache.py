#!/usr/bin/env python3
""" LRU Caching """

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ FIFOCache defines a FIFO caching system """

    def __init__(self):
        """ Initialize the class with the parent's init method """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Cache a key-value pair """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.order:
                self.order.append(key)
        else:
            self.order.append(
                self.order.pop(self.order.index(key)))
        length = len(self.order)
        if length >= BaseCaching.MAX_ITEMS:
            discarded_key = self.order.pop(0)
            del self.cache_data[discarded_key]
            print('DISCARD: {}'.format(discarded_key))

    def get(self, key):
        """ Return the value linked to a given key, or Non """
        if key is not None and key in self.cache_data.keys():
            self.order.append(self.order.pop(self.order.index(key)))
            return self.cache_data.get(key)
        return None
