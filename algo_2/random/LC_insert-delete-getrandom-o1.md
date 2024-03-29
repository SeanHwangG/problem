# [LC_insert-delete-getrandom-o1](https://leetcode.com/problems/insert-delete-getrandom-o1)

* en

  ```en
  Implement the RandomizedSet class:
    RandomizedSet() Initializes the RandomizedSet object
    bool insert(int val) Inserts an item val into the set if not present. Returns if the item was not present
    bool remove(int val) Removes an item val from set if present. Returns if the item was present
    int getRandom() Return random element from current set of elements (guaranteed element exists when method is called)
      Each element must have the same probability of being returned
  ```

* tc

  ```tc
  Input:
  ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
  [[], [1], [2], [2], [], [1], [2], []]

  Output: [null, true, false, true, 2, true, false, 2]
  ```

## Solution

* py

  ```py
  import random

  class RandomizedSet(object):
    def __init__(self):
      self.nums, self.pos = [], {}

    def insert(self, val):
      if val not in self.pos:
        self.nums.append(val)
        self.pos[val] = len(self.nums) - 1
        return True
      return False

    def remove(self, val):
      if val in self.pos:
        idx, last = self.pos[val], self.nums[-1]
        self.nums[idx], self.pos[last] = last, idx
        self.nums.pop(); self.pos.pop(val, 0)
        return True
      return False

    def getRandom(self):
      return self.nums[random.randint(0, len(self.nums) - 1)]
  ```
