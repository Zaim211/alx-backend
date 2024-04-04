#!/usr/bin/env python3
""" """

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ """

    def __init__(self):
        """ """
        super().__init__()
        self.order = []
        self.freq = {}

    def put(self, key, item):
        """ """
        if key is None or item is None:
            pass
        else:
            length = len(self.cache_data)
            if length >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                lfucache = min(self.freq.values())
                lfucache_keys = []
                for keys, value in self.freq.items():
                    if value == lfucache:
                        lfucache_keys.append(keys)
                if len(lfucache_keys) > 1:
                    count = {}
                    for keys in lfucache_keys:
                        count[keys] = self.order.index(keys)
                    discarded_keys = min(count.values())
                    discarded_keys = self.order[discarded_keys]
                else:
                    discarded_keys = lfucache_keys[0]

                print("DISCARD: {}".format(discarded_keys))
                del self.cache_data[discarded_keys]
                del self.order[self.order.index(discarded_keys)]
                del self.freq[discarded_keys]

            if key in self.freq:
                self.freq[key] += 1
            else:
                self.freq[key] = 1
            if key in self.order:
                del self.order[self.order.index(key)]
            self.order.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """ """
        if key is not None and key in self.cache_data.keys():
            del self.order[self.order.index(key)]
            self.order.append(key)
            self.freq[key] += 1
            return self.cache_data[key]
        return None
