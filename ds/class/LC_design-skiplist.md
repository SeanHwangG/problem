# [LC_design-skiplist](https://leetcode.com/problems/design-skiplist)

```en
Design a Skiplist without using any built-in libraries
  O(log(n)) time to add, erase and search
```

```txt
Skiplist skiplist = new Skiplist();

skiplist.add(1);
skiplist.add(2);
skiplist.add(3);
skiplist.search(0);   // return false.
skiplist.add(4);
skiplist.search(1);   // return true.
skiplist.erase(0);    // return false, 0 is not in skiplist.
skiplist.erase(1);    // return true.
skiplist.search(1);   // return false, 1 has already been erased.
```

## Solution

* py

  ```py
  class Node:
    def __init__(self, val, levels):
      self.val = val
      self.levels = [None] * levels

  class Skiplist(object):
    def __init__(self):
      self.head = Node(-1, 16)

    def _iter(self, num):
      cur = self.head
      for level in range(15, -1, -1):
        while True:
          future = cur.levels[level]
          if future and future.val < num:
            cur = future
          else:
            break
        yield cur, level

    def search(self, target):
      for prev, level in self._iter(target):
        pass
      cur = prev.levels[0]
      return cur and cur.val == target

    def add(self, num):
      nodelvls = min(16, 1 + int(math.log2(1.0 / random.random())))
      node = Node(num, nodelvls)
      for cur, level in self._iter(num):
        if level < nodelvls:
          future = cur.levels[level]
          cur.levels[level] = node
          node.levels[level] = future

    def erase(self, num):
      ans = False
      for cur, level in self._iter(num):
        future = cur.levels[level]
        if future and future.val == num:
          ans = True
          cur.levels[level] = future.levels[level]
      return ans
  ```
