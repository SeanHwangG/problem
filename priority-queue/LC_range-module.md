```py
from bisect import bisect_left, bisect_right

class RangeModule:

  def __init__(self):
    self._X = []

  def addRange(self, left, right):
    i, j = bisect_left(self._X, left), bisect_right(self._X, right)
    self._X[i:j] = [left] * (i % 2 == 0) + [right] * (j % 2 == 0)

  def queryRange(self, left, right):
    i, j = bisect_right(self._X, left), bisect_left(self._X, right)
    return i == j and i%2 == 1

  def removeRange(self, left, right):
    i, j = bisect_left(self._X, left), bisect_right(self._X, right)
    self._X[i:j] = [left]*(i % 2 == 1) + [right] * (j % 2 == 1)
```
