# [LC_design-hashset](https://leetcode.com/problems/design-hashset)

Design Hashset

```txt
Input:
["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
[[], [1], [2], [1], [3], [2], [2], [2], [2]]

Output: [null, null, null, true, false, null, true, null, false]
```

## Solution

* py

```py
class MyHashSet:
  def __init__(self):
    self.set = [False] * 197431

  def add(self, key: int) -> None:
    self.set[key % 197431] = True

  def remove(self, key: int) -> None:
    self.set[key % 197431] = False

  def contains(self, key: int) -> bool:
    return self.set[key % 197431]
```
