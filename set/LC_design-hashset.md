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
