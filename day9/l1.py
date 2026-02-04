import time
from collections import OrderedDict

class L1Cache:
    def __init__(self, capacity=3, ttl=5):
        self.cache = OrderedDict()
        self.capacity = capacity
        self.ttl = ttl

    def get(self, key):
        if key not in self.cache:
            print("❌ L1 MISS")
            return None

        value, timestamp = self.cache.pop(key)

        if time.time() - timestamp > self.ttl:
            print("⏰ L1 EXPIRED")
            return None

        self.cache[key] = (value, timestamp)
        print("✅ L1 HIT")
        return value

    def set(self, key, value):
        if key in self.cache:
            self.cache.pop(key)
        elif len(self.cache) >= self.capacity:
            evicted, _ = self.cache.popitem(last=False)
            print(f"🔥 L1 EVICTED: {evicted}")

        self.cache[key] = (value, time.time())

if __name__ == "__main__":
    cache = L1Cache()

    cache.set("a", 1)
    cache.set("b", 2)
    cache.set("c", 3)

    print(cache.get("a"))
    cache.set("d", 4)
    print(cache.get("b"))
