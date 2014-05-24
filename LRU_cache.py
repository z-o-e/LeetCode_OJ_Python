import collections
class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        # OrderedDict like dictionary, but remembers the order keys are inserted
        self.bag = collections.OrderedDict()
        self.count = 0
        self.lookup = {}

    # @return an integer
    def get(self, key):
        try:
            value = self.bag[key]
            return value
        except:
            return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        try:
            del self.bag[key]
            self.bag[key] = value
        except:
            if self.count == self.capacity:
                self.bag.popitem(last = False)
            self.bag[key] = value
            self.count += 1