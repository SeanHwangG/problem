# [LC_lfu-cache](https://leetcode.com/problems/lfu-cache)

* en

  ```en
  Deisng LFU Cache
  ```

* tc

  ```tc
  Input:
  ["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
  [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]

  Output:
  [null, null, null, 1, null, -1, 3, null, -1, 3, 4]
  ```

## Solution

* py

  ```py
  from collections import defaultdict, OrderedDict

  class Node:
    def __init__(self, key, val, count):
      self.key = key
      self.val = val
      self.count = count

  class LFUCache(object):
    def __init__(self, capacity):
      self.cap = capacity
      self.key2node = {}
      self.count2node = defaultdict(OrderedDict)
      self.minCount = None

    def get(self, key):
      if key not in self.key2node:
        return -1

      node = self.key2node[key]
      del self.count2node[node.count][key]

      if not self.count2node[node.count]:
        del self.count2node[node.count]

      node.count += 1
      self.count2node[node.count][key] = node

      if not self.count2node[self.minCount]:
        self.minCount += 1

      return node.val

    def put(self, key, value):
      if not self.cap:
        return

      if key in self.key2node:
        self.key2node[key].val = value
        self.get(key) # NOTICE, put makes count+1 too
        return

      if len(self.key2node) == self.cap:
        # popitem(last=False) is FIFO, like queue
        k, n = self.count2node[self.minCount].popitem(last=False)
        del self.key2node[k]

      self.count2node[1][key] = self.key2node[key] = Node(key, value, 1)
      self.minCount = 1
  ```
