# [LC_flatten-2d-vector](https://leetcode.com/problems/flatten-2d-vector)

Design flattened 2D Vector

```txt
Input: [ [1,2],
  [3],
  [4,5,6]]

Output: [1,2,3,4,5,6]
```

## Solution

* py

```py
class Vector2D:
  def __init__(self, lis):
    def it():
      for li in lis:
        for el in li:
          self.size -= 1
          yield el
    self.it = it()
    self.size = sum(len(li) for li in lis)

  def next(self) -> int:
    return next(self.it)

  def hasNext(self) -> bool:
    return self.size
```
