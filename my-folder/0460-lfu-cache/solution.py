from collections import defaultdict, OrderedDict


class LFUCache:
    def __init__(self, capacity):
        self.cache = {}  # stores key to (freq, value)
        self.frequencies = defaultdict(OrderedDict)  # stores freq to keys in order of their usage
        self.min_freq = 0
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache:
            return -1

        freq, value = self.cache[key]
        # Remove the key from the current frequency list
        del self.frequencies[freq][key]
        if not self.frequencies[freq]:
            del self.frequencies[freq]
            if self.min_freq == freq:
                self.min_freq += 1

        # Increase the frequency of the key
        self.cache[key] = (freq + 1, value)
        self.frequencies[freq + 1][key] = None  # None is just a placeholder

        return value

    def put(self, key, value):
        if self.capacity <= 0:
            return

        if key in self.cache:
            # Update the value and increase the frequency
            freq, _ = self.cache[key]
            self.cache[key] = (freq, value)
            self.get(key)  # This will handle frequency increase
            return

        if len(self.cache) >= self.capacity:
            # Find the least frequently used key and remove it
            key_to_delete, _ = next(iter(self.frequencies[self.min_freq].items()))
            del self.cache[key_to_delete]
            del self.frequencies[self.min_freq][key_to_delete]
            if not self.frequencies[self.min_freq]:
                del self.frequencies[self.min_freq]

        # Insert the new key
        self.min_freq = 1
        self.cache[key] = (1, value)
        self.frequencies[1][key] = None


# Example usage:
lfu_cache = LFUCache(2)
lfu_cache.put(1, 1)
lfu_cache.put(2, 2)
print(lfu_cache.get(1))  # returns 1
lfu_cache.put(3, 3)  # evicts key 2
print(lfu_cache.get(2))  # returns -1 (not found)
print(lfu_cache.get(3))  # returns 3

