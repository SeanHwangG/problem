# [LC_lru-cache](https://leetcode.com/problems/lru-cache)

```en
Implement the LRUCache class
LRUCache(int capacity) Initialize the LRU cache with positive size capacity
  int get(int key) Return the value of the key if the key exists, otherwise return -1
  void put(int key, int value) Update value of key if key exists. Otherwise, add key-value pair to cache
    If number of keys exceeds capacity from this operation, evict least recently used key
```

```txt
Input:
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]

Output: [null, null, null, 1, null, -1, null, -1, 3, 4]
```

## Solution

* py

  ```py
  class LRUCache:
    def __init__(self, Capacity):
      self.size = Capacity
      self.cache = OrderedDict()

    def get(self, key):
      if key not in self.cache: return -1
      val = self.cache[key]
      self.cache.move_to_end(key)
      return val

    def put(self, key, val):
      self.cache.pop(key, None)
      self.cache[key] = val
      if len(self.cache) > self.size:
        self.cache.popitem(last=False)
  ```
